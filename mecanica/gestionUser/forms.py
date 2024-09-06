from django import forms
from .models import Cliente, Genero, Vehiculo

from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"

