from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevoBlog/', views.nuevoBlog, name='nuevoBlog'),
    path('blogCompleto/<id>', views.blogCompleto, name='blogCompleto'),
    path('editarBlog/<id>', views.editarBlog, name='editarBlog'),
    path('eliminarBlog/<id>', views.eliminarBlog, name='eliminarBlog'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('editarPerfil/',views.editarPerfil, name='editarPerfil'),
    path('addAvatar/', views.addAvatar, name='addAvatar'),
    path('about', views.about, name='about'),
]
