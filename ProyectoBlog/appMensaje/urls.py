from django import views
from django.urls import path
from . import views
from .views import enviarMensaje

urlpatterns = [
    path('enviarMensaje/', enviarMensaje.as_view(), name='enviarMensaje'),
]
