# Generated by Django 4.1.1 on 2022-11-18 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0001_initial"),
        ("core", "0006_alter_usuario_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="media.image",
            ),
        ),
    ]
