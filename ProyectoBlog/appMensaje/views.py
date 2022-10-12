from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Emisor, Receptor, Mensaje
from .forms import MensajeForm
# Create your views here.


def enviarMensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            emisor = info['emisor']
            receptor = info['receptor']
            mensaje = info['mensaje']
            mensajeCompleto = Mensaje(emisor=emisor,receptor=receptor,mensaje=mensaje)
            mensajeCompleto.save()
            mensajes = Mensaje.objects.all()
            return render(request, 'verMensajes.html', {'mensajes':mensajes})
        else:
            return render(request, 'enviarMensaje.html',{'adv':'Formulario Invalido'})
    else:
        form = MensajeForm()
        return render(request, 'enviarMensaje.html', {'form':form})
