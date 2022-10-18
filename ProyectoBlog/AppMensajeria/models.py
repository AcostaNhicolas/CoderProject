from django.db import models
from django.forms import forms
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Mensaje(models.Model):
    emisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='emisor',
    )
    receptor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='receptor',
    )
    texto = models.TextField()

    def __str__(self):
        return 'De: ' + str(self.emisor) + ' Para: ' + str(self.receptor)

    def get_absolute(self):
        return reverse('buzonEntrada.html')