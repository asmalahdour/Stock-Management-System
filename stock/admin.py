from django.contrib import admin
from .models import *
from .forms import StockCreateForm


# Register your models here.

class StockCreateForm(admin.ModelAdmin):
    list_display = ['departement', 'code_fournisseur', 'quantity']
    form = StockCreateForm
    list_filter = ['departement']
    search_fields = ['departement', 'code_fournisseur']


admin.site.register(Stock, StockCreateForm)

admin.site.register(Profile)
