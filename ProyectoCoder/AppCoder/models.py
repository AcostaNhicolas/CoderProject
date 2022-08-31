from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    año_nacimiento = models.DateField()

class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()