from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('enviarMensaje/', views.enviarMensaje, name='enviarMensaje'),
    path('buzonEntrada/<id>', views.buzonEntrada, name='buzonEntrada'),
    path('buzonSalida/<id>', views.buzonSalida, name='buzonSalida'),
    path('mensajeCompleto/<id>', views.mensajeCompleto, name='mensajeCompleto'),
    path('eliminarMensaje/<id>',views.eliminarMensaje, name='eliminarMensaje'),
]
