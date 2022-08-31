from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Familiar, Domicilio
import datetime

# Create your views here.

def ingresar_familiar(request):
    año_actual = datetime.datetime.now() #Con la fecha de hoy calcularemos la fecha de nacimiento

    #Se ingresa el primer familiar
    f1 = Familiar(nombre = 'Carlos', apellido = 'Gonzalez', edad = 28, año_nacimiento = año_actual)
    f1.save()
    año_nacimiento1 = año_actual.year - f1.edad #Calculo de la fecha de nacimiento
    #Se ingresa el domicilio del primer familiar ingresado
    d1 = Domicilio(calle = 'Catamarca', ciudad = 'San Marcos', codigo_postal = 4600)
    d1.save()
    #Se ingresa el segundo familiar
    f2 = Familiar(nombre = 'Joaquin', apellido = 'Trival', edad = 52, año_nacimiento = año_actual)
    f2.save()
    año_nacimiento2 = año_actual.year - f2.edad
    #Se ingresa el domicilio del segundo familiar ingresado
    d2 = Domicilio(calle = 'America', ciudad = 'Kenedy', codigo_postal = 2100)
    d2.save()
    #Se ingresa el tercer familiar
    f3 = Familiar(nombre = 'Gissel', apellido = 'Lazarte', edad = 33, año_nacimiento = año_actual)
    f3.save()
    año_nacimiento3 = año_actual.year - f3.edad
    #Se ingresa el domicilio del tercer familiar ingresado
    d3 = Domicilio(calle = 'Juan B. Justo', ciudad = 'Uribe', codigo_postal = 5000)    
    d3.save()

    diccionario = {'n1':f1.nombre,'a1':f1.apellido,'e1':f1.edad,'an1':año_nacimiento1, 
    'ca1':d1.calle, 'ci1':d1.ciudad, 'cp1':d1.codigo_postal, 'n2':f2.nombre,'a2':f2.apellido,'e2':f2.edad,'an2':año_nacimiento2, 
    'ca2':d2.calle, 'ci2':d2.ciudad, 'cp2':d2.codigo_postal, 'n3':f3.nombre,'a3':f3.apellido,'e3':f3.edad,'an3':año_nacimiento3, 
    'ca3':d3.calle, 'ci3':d3.ciudad, 'cp3':d3.codigo_postal}

    

    plantilla = loader.get_template('template.html')
    doc = plantilla.render(diccionario)
    return HttpResponse(doc)

    