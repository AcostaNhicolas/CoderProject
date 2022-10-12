from django import forms
from ckeditor.fields import RichTextField, RichTextFormField
from django.views.generic import CreateView, DetailView, ListView
from .models import Mensaje, Emisor, Receptor

class MensajeForm(forms.Form):
    emisor = forms.CharField(widget=forms.Select())
    receptor = forms.CharField(widget=forms.Select())
    mensaje = RichTextFormField()
