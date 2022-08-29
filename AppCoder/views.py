from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(request):
    curso = Curso(nombre = 'Desarrollo web', camada = '19881')
    curso.save()
    documento_de_texto = f'---> Curso: {curso.nombre}  Camada: {curso.camada}'
    return HttpResponse(documento_de_texto)
