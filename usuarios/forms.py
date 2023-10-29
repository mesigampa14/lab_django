from django import forms
from django.contrib.auth.forms import AuthenticationForm

class DNIAuthenticationForm(AuthenticationForm):
    dni = forms.CharField(max_length=10)
