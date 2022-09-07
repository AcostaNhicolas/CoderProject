from django import forms

class CampañasForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    cantidad_empleados = forms.IntegerField()

class SupervisoresForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    grupo = forms.IntegerField()

class AgentesForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    grupo = forms.IntegerField()