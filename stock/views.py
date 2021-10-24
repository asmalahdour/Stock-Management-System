from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.http import HttpResponse
import csv
# Create your views here.


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully ')

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('list_item')
        else:
            messages.info(request, 'Username or Password is incorrrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def fprofile(request):
    form = ProfilForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_item')

    context = {"form": form}
    return render(request, 'profile.html', context)


def view_profile(request):
    pf = Profile.objects.get(user=request.user)
    context = {'pf': pf}
    return render(request, 'view_profile.html', context)


def update_profile(request, pk):
    queryset = Profile.objects.get(user=pk)
    form = ProfilUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ProfilUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)


def home(request):
    return render(request, "dashboard.html")


def list_item(request):
    header = 'List of Items'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all().order_by('expire_date')
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }

    if request.method == 'POST':
        queryset = Stock.objects.filter(departement__icontains=form['departement'].value(),
                                        code_fournisseur__icontains=form['code_fournisseur'].value(
        )
        )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['Code Fournisseur', 'Libellé', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow(
                    [stock.code_fournisseur, stock.libelle, stock.quantity])
            return response
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "list_item.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_item')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)


def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_item')
    return render(request, 'delete_items.html')
