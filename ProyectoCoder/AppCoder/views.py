from django.http import HttpResponse
from django.shortcuts import render
from .models import Campañas, Supervisores, Agentes
from AppCoder.forms import CampañasForm, SupervisoresForm, AgentesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
            supervisores = Supervisores(nombre=nombre,apellido=apellido,grupo=grupo)
            supervisores.save()
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
            agentes = Agentes.objects.all()
            return render(request, 'AppCoder/leerAgentes.html', {'agentes':agentes})
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

#--------------------- MOSTRAR AGENTE -----------------------

def leerAgentes(request):
    agentes = Agentes.objects.all()
    return render(request, 'AppCoder/leerAgentes.html', {'agentes':agentes})

#--------------------- ELIMINAR AGENTE -----------------------


def eliminarAgente(request, id):
    agente = Agentes.objects.get(id=id)
    agente.delete()
    agentes=Agentes.objects.all()
    return render(request, 'AppCoder/leerAgentes.html', {'agentes':agentes})

#--------------------- EDITAR AGENTE -----------------------

def editarAgente(request, id):
    agente = Agentes.objects.get(id=id)
    if request.method == 'POST':
        form = AgentesForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            agente.nombre = info['nombre']
            agente.apellido = info['apellido']
            agente.grupo = info['grupo']
            agente.save()
            agentes = Agentes.objects.all()
            return render(request, 'AppCoder/leerAgentes.html', {'agentes':agentes})
    else:
        formulario = AgentesForm(initial={'nombre':agente.nombre,'apellido':agente.apellido,'grupo':agente.grupo})
        return render(request, 'AppCoder/editarAgente.html', {'formulario':formulario, 'agente':agente})





#--------------------- EDITAR AGENTE -----------------------


class SupervisorList(ListView):
    model = Supervisores
    template_name = 'AppCoder/leerSupervisores.html'




