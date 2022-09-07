from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agentes/', views.agentes, name='agentes'),
    path('campañas/', views.campañas, name='campañas'),
    path('supervisores/', views.supervisores, name='supervisores'),
    path('busquedaGrupo/', views.busquedaGrupo, name='busquedaGrupo'),
    path('buscar/', views.buscar, name='buscar'),
]