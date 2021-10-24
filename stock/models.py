from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Poste_CHOICES = [
    ('Chef de département', 'Chef de département'),
    ('Chef de rayon', 'Chef de rayon'),
    ('Assistante de département', 'Assistante de département'),
    ('Responsable réception marchandise', 'Responsable réception marchandise'),

]

Dep_CHOICES = [
    ('PGC', 'PGC'),
    ('PF', 'PF'),
    ('APLS', 'APLS'),
]


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='Profile', primary_key=True)
    name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)
    poste = models.CharField(max_length=50, choices=Poste_CHOICES)
    departement = models.CharField(max_length=15, choices=Dep_CHOICES)


Rayon_CHOICES = [
    ('Rayon Epiceries', 'Rayon Epiceries'),
    ('Rayon Confiserie Biscuterie', 'Rayon Confiserie Biscuterie'),
    ('Rayon Liquide', 'Rayon Liquide'),
    ('Rayon Droguerie Parfumerie Hygiène', 'Rayon Droguerie Parfumerie Hygiène'),
    ('Rayon Crémerie/Charcuterie', 'Rayon Crémerie/Charcuterie'),
    ('Rayon Surgelé', 'Rayon Surgelé'),
    ('Rayon Boulangerie/Patiserie', 'Rayon Boulangerie/Patiserie'),
    ('Rayon Fruit légume', 'Rayon Fruit légume'),
    ('Rayon Volaille/Boulangerie', 'Rayon Volaille/Boulangerie'),
    ('Rayon Poissonerie', 'Rayon Poissonerie'),
    ('Rayon Epices/Olives', 'Rayon Boulangerie/Patiserie'),

]


class Stock(models.Model):
    departement = models.CharField(
        max_length=50, blank=True, null=True, choices=Dep_CHOICES)
    rayon = models.CharField(max_length=50, blank=True,
                             null=True, choices=(Rayon_CHOICES))
    code_fournisseur = models.CharField(max_length=14, blank=True, null=True)
    libelle = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=False, null=True)
    expire_date = models.DateTimeField()
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.libelle
