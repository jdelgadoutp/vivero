from django import forms
import models

class LaborForm(forms.ModelForm):
    class Meta:
        model = models
        fields = [
            'nombreProducto',
            'FrecuenAplicacion',
            'fechaLabor',
            'ValorProcducto ',
        ]