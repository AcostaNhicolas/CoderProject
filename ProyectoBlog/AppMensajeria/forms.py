from tkinter.tix import Select
from django.forms import forms, models
from .models import Mensaje
from django import forms

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('emisor','receptor','texto')

        widget = {
            'emisor':forms.Select(attrs={'class':'form-control'}),
            'receptor':forms.Select(attrs={'class':'form-control'}),
            'texto':forms.Textarea(attrs={'class':'form-control'})
        }



