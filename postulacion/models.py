from django.db import models
from django.core.validators import *
from django.utils import timezone


# Create your models here.

class postulantes(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=20, validators=[
        RegexValidator('^\d{1,2}\.?\d{3}\.?\d{3}[-]?[0-9kK]{1}$', message='Ingrese un RUT Valido')])
    email = models.EmailField(max_length=50)
    telefono = models.BigIntegerField()
    # comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=75)
    vigente = models.BooleanField(default=True)
    # password = models.CharField(max_length=50)
    f_postulacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f'\nNombres: {self.nombres} \nApellidos: {self.apellidos} \nRUT: {self.rut}'
