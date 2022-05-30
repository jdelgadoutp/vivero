from pyexpat import model
from attr import fields
from django import forms
import models

class LaborForm(forms.ModelForm):
    class Producto:
        model = models
        fields = [
            'nombreProducto',
            'FrecuenAplicacion',
            'ValorProcducto ',
        ]
        labels = {
            'nombreProducto': 'nombreProducto',
            'FrecuenciaAplicacion': 'FrecuenciaAplicacion',
            'ValorProducto': 'ValorProducto',
        }
        widgets = {
            'nombreProducto': forms.TextInput(attrs={'class':'form-control'}),
            'FrecuenciaAplicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'ValorProducto': forms.TextInput(attrs={'class': 'form-control'}),
            }

    class productor:
        model = models
        fields = [
            'identificacion',
            'nombre',
            'apellido',
        ]
    