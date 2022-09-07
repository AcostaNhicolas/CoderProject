from django.http import HttpResponse
from django.shortcuts import render
from .models import Campañas, Supervisores, Agentes
from AppCoder.forms import CampañasForm, SupervisoresForm, AgentesForm

# Create your views here.

#------------------------------INICIO------------------------------------------
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
#------------------------------CAMPAÑAS------------------------------------------

def campañas(request):
    if request.method == 'POST':
        form = CampañasForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            cantidad_empleados = info['cantidad_empleados']
            campaña = Campañas(nombre=nombre,cantidad_empleados=cantidad_empleados)
            campaña.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario = CampañasForm()
        return render(request, 'AppCoder/campañas.html', {'formulario':formulario})

#--------------------------------SUPERVISORES----------------------------------

def supervisores(request):
    if request.method == 'POST':
        form = SupervisoresForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            grupo = info['grupo']
            campaña = Supervisores(nombre=nombre,apellido=apellido,grupo=grupo)
            campaña.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario = SupervisoresForm()
        return render(request, 'AppCoder/supervisores.html', {'formulario':formulario})

#------------------------------AGENTES------------------------------------------

def agentes(request):
    if request.method == 'POST':
        form = AgentesForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            grupo = info['grupo']
            agentes = Agentes(nombre=nombre,apellido=apellido,grupo=grupo)
            agentes.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario = AgentesForm()
        return render(request, 'AppCoder/agentes.html', {'formulario':formulario})


#---------------------BUSQUEDA POR GRUPO-----------------------


def busquedaGrupo(request):
    return render(request, 'AppCoder/busquedaGrupo.html')

def buscar(request):
    if request.GET['grupo']:
        grupo = request.GET['grupo']
        agentes = Agentes.objects.filter(grupo=grupo)
        return render(request, 'AppCoder/resultadosBusqueda.html',{'agentes':agentes})
    else:
        return render(request, 'AppCoder/busquedaGrupo.html', {'mensaje':'Ingrese un grupo'})

