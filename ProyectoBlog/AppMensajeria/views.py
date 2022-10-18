from django.http import request
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Mensaje
from django.contrib.auth.models import User
from .forms import MensajeForm
from django.urls import reverse
from appBlog.views import getAvatar

# Create your views here.

def enviarMensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            emisor = info['emisor']
            receptor = info['receptor']
            texto = info['texto']
            mensaje = Mensaje(emisor=emisor,receptor=receptor,texto=texto)
            mensaje.save()
            form = MensajeForm()
            return render(request,'enviarMensaje.html',{'form':form,'mensaje':'Mensaje Enviado','avatar':getAvatar(request)})
        else:
            form = MensajeForm()
            return render(request, 'enviarMensaje.html',{'form':form,'mensaje':'Error de envío','avatar':getAvatar(request)})
    else:
        form = MensajeForm()
        return render(request,'enviarMensaje.html',{'form':form,'avatar':getAvatar(request)})

def eliminarMensaje(request,id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()
    form = MensajeForm()
    return render(request,'enviarMensaje.html',{'form':form,'mensaje':'Mensaje Eliminado','avatar':getAvatar(request)})

def buzonEntrada(request,id):
    mensajes = Mensaje.objects.filter(receptor=id)
    return render(request, 'buzonEntrada.html',{'mensajes':mensajes,'avatar':getAvatar(request)})

def buzonSalida(request,id):
    mensajes = Mensaje.objects.filter(emisor=id)
    return render(request, 'buzonSalida.html',{'mensajes':mensajes,'avatar':getAvatar(request)})

def mensajeCompleto(request, id):
    mensaje = Mensaje.objects.get(id=id)
    return render(request, 'mensajeCompleto.html',{'mensaje':mensaje,'avatar':getAvatar(request)})

def responder(request, id):
    mensaje = Mensaje.objects.get()
    
