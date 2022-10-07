from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agentes/', agentes, name='agentes'),
    path('campañas/', campañas, name='campañas'),
    path('supervisores/', supervisores, name='supervisores'),
    path('busquedaGrupo/', busquedaGrupo, name='busquedaGrupo'),
    path('buscar/', buscar, name='buscar'),
    path('leerAgentes/', leerAgentes, name='leerAgentes'),
    path('eliminarAgente/<id>', eliminarAgente, name='eliminarAgente'),
    path('editarAgente/<id>', editarAgente, name='editarAgente'),
    #cbv
    path('supervisores/list/', SupervisorList.as_view(), name='estudiante_listar')
]