# Generated by Django 3.0.7 on 2020-07-01 06:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postulacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulantes',
            name='rut',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\d{1,2}\\.?\\d{3}\\.?\\d{3}[-]?[0-9kK]{1}$', message='Ingrese un RUT Valido')]),
        ),
    ]
