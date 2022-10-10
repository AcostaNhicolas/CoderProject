from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fechaPublicacion = models.DateField(auto_now_add=True)
    cuerpo = RichTextField(blank=True,null=True)
    # cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True,blank=True)
