from AppCoder.models import Familiar, Domicilio
from django.http import HttpResponse
from django.template import loader


def probando(self):
    
    nom = 'Nicolas'
    ap = 'Acosta'
    lista = [2,2,3,7,2,5]

    diccionario = {'nombre':nom, 'apellido':ap, 'notas':lista}


    plantilla = loader.get_template('template.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def familiar(self):
    familiar1 = Familiar(nombre = 'Nicolas', apellido = 'Acosta', edad = '28')
    familiar1.save()
    # texto = f'----> Curso: {curso.nombre} Camada: {curso.apellido}'

    diccionario1 = {'nombre':familiar1.nombre,'apellido':familiar1.apellido,'edad':familiar1.edad}

    plantilla = loader.get_template('template.html')

    documento = plantilla.render(diccionario1)

    return HttpResponse(documento)