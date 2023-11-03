from django.db import models
from django.utils import timezone

from apps.persona.models import Estudiante, Docente


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_presentacion = models.DateTimeField(default=timezone.now)
    estudiantes = models.ManyToManyField(Estudiante, related_name='proyectos')
    docentes = models.ManyToManyField(Docente, related_name='proyectos')

    def __str__(self):
        return self.titulo

# Create your models here.
