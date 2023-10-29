from django.contrib import admin
from .models import Persona, Estudiante, Docente

# Register your models here.
admin.site.register(Persona)
admin.site.register(Estudiante)
admin.site.register(Docente)