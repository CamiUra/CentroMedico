# Generated by Django 4.2 on 2024-12-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichamedica',
            name='nombre_paciente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
