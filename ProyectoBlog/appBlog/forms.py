from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subtitulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    autor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cuerpo = forms.Textarea(attrs={'class':'form-control'})
    imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        helps_texts = {k:'' for k in fields}
    
class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Nombre', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Apellido', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        helps_texts = {k:'' for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label='Imagen')