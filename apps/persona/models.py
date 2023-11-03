from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Persona(models.Model):
    GENERO_OPCIONES = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )
    dni = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    mail = models.EmailField(max_length=254, blank=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=9, choices=GENERO_OPCIONES)
    domicilio = models.CharField(max_length=250)

    class Meta:
        ordering = ('apellido',)

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)


class Estudiante(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return '{} - {}'.format(self.matricula, self.persona)


class Docente(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    cuil = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return '{} - {}'.format(self.cuil, self.persona)
