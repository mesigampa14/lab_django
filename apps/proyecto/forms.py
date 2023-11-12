from django import forms
from django.forms import DateInput

from apps.proyecto.models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('titulo', 'descripcion', 'fecha_presentacion', 'estudiantes', 'docentes')

        widgets = {
            'fecha_presentacion': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
