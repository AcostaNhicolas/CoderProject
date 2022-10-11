from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class Emisor(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_user.username

class Receptor(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_user.username

class Mensaje(models.Model):
    mensaje = RichTextField(blank=True, null=True)
    emisor = models.ForeignKey(Emisor,null=True,  on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'De: ' + self.emisor.id_user.username + ' | Para: ' + self.receptor.id_user.username

    # def get_absolute_url(self):
    #     return reverse('verMensajes.html', args=(str(self.id)))