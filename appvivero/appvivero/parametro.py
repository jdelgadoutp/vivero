from django import forms

class LaborForm(forms.ModelForm):
    class Meta:
        model = ModeloLaborVivero
        fields = [
            'codigoLabor',
            'nombreLabor',
            'fechaLabor',
            'descripcionLabor',
        ]