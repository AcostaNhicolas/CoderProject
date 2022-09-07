from django.db import models

# Create your models here.
class Campañas(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad_empleados = models.IntegerField()
    def __str__(self):
        return self.nombre

class Supervisores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    grupo = models.IntegerField()
    def __str__(self):
        return self.nombre+' '+self.apellido

class Agentes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    grupo = models.IntegerField()
    def __str__(self):
        return self.nombre+' '+self.apellido
