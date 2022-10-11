from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Emisor, Receptor, Mensaje
# Create your views here.

class enviarMensaje(CreateView):
    model = Mensaje
    template_name = 'appMensaje/enviarMensaje.html'
    fields = '__all__'  
