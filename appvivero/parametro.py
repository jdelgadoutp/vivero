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
    class productor:
        model = models
        fields = [
            'identificacion',
            'nombre',
            'apellido',
        ]
    