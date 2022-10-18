from django import template
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Mensaje
from django.contrib.auth.models import User


# Create your views here.

class EnviarMensaje(CreateView):
    model = Mensaje
    template_name = 'enviarMensaje.html'
    fields = '__all__'


def buzonEntrada(request,id):
    mensajes = Mensaje.objects.filter(receptor=id)
    return render(request, 'buzonEntrada.html',{'mensajes':mensajes})

def buzonSalida(request,id):
    mensajes = Mensaje.objects.filter(emisor=id)
    return render(request, 'buzonEntrada.html',{'mensajes':mensajes})

def mensajeCompleto(request, id):
    mensaje = Mensaje.objects.get(id=id)
    return render(request, 'mensajeCompleto.html',{'mensaje':mensaje})

def responder(request, id):
    mensaje = Mensaje.objects.get()
    


# class BuzonEntrada(ListView):
#     model = Mensaje
#     template_name = 'buzonEntrada.html'

# class MensajeCompleto(DetailView):
#     model = Mensaje
#     template_name = 'mensajeCompleto.html'

