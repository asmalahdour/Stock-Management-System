from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'mobile_no', 'poste', 'departement']


class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'mobile_no', 'poste', 'departement']


class DateInput(forms.DateInput):
    input_type = 'date'


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['departement', 'rayon',
                  'code_fournisseur', 'libelle', 'quantity', 'expire_date']

        widgets = {
            'expire_date': DateInput(attrs={'id': 'datepicker', 'minDate': 0}),

        }

        def departement(self):
            departement = self.cleaned_data.get('departement')
            if not departement:
                raise forms.ValidationError('This field is required')
            # for instance in Stock.objects.all():
            #     if instance.departement == departement:
                #         raise forms.ValidationError(str(departement) + ' is already created')
            return departement

        def clean_rayon(self):
            rayon = self.cleaned_data.get('rayon')
            if not rayon:
                raise forms.ValidationError('This field is required')
            return rayon


class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Stock
        fields = ['departement', 'code_fournisseur']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['departement', 'rayon',
                  'code_fournisseur', 'libelle', 'quantity', 'expire_date']
