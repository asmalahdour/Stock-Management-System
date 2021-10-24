# Generated by Django 3.2.7 on 2021-09-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_alter_stock_rayon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='rayon',
            field=models.CharField(blank=True, choices=[('Rayon Epiceries', 'Rayon Epiceries'), ('Rayon Confiserie Biscuterie', 'Rayon Confiserie Biscuterie'), ('Rayon Liquide', 'Rayon Liquide'), ('Rayon Droguerie Parfumerie Hygiène', 'Rayon Droguerie Parfumerie Hygiène'), ('Rayon Crémerie/Charcuterie', 'Rayon Crémerie/Charcuterie'), ('Rayon Surgelé', 'Rayon Surgelé'), ('Rayon Boulangerie/Patiserie', 'Rayon Boulangerie/Patiserie'), ('Rayon Fruit légume', 'Rayon Fruit légume'), ('Rayon Volaille/Boulangerie', 'Rayon Volaille/Boulangerie'), ('Rayon Poissonerie', 'Rayon Poissonerie'), ('Rayon Epices/Olives', 'Rayon Boulangerie/Patiserie')], max_length=50, null=True),
        ),
    ]
