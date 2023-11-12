from django import forms

from apps.movimiento.models import Movimiento


class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ('tipo_movimiento',)