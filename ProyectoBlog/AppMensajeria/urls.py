from unicodedata import name
from django.urls import path
from .views import EnviarMensaje
from AppMensajeria import views
urlpatterns = [
    path('enviarMensaje/', EnviarMensaje.as_view(), name='enviarMensaje'),
    path('buzonEntrada/<id>', views.buzonEntrada, name='buzonEntrada'),
    path('buzonSalida/<id>', views.buzonSalida, name='buzonSalida'),
    path('mensajeCompleto/<id>', views.mensajeCompleto, name='mensajeCompleto'),
    path('responder/<id>', views.responder, name='responder'),
]
