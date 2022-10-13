# Generated by Django 4.1 on 2022-08-28 22:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_comedouro_hardware_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('cachorro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cachorro')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.comedouro')),
            ],
        ),
    ]
