# Generated by Django 4.1.1 on 2022-10-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_cachorro_altura_cachorro_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachorro',
            name='altura',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cachorro',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
