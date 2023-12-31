from django import forms
from django.forms import DateInput

from apps.persona.models import Persona, Estudiante, Docente


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dni', 'apellido', 'nombre', 'mail', 'fecha_nacimiento', 'sexo', 'domicilio')

        widgets = {
            'fecha_nacimiento': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('matricula',)


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('cuil',)
