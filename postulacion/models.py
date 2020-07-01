from django.db import models
from django.core.validators import *


# Create your models here.

class postulantes(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=20, validators=[RegexValidator('^\d{1,2}\.?\d{3}\.?\d{3}[-]?[0-9kK]{1}$')])
    email = models.EmailField(max_length=50)

