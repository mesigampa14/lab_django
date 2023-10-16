from django.db import models

# Create your models here.
class Persona(models.Model):
    GENERO_OPCIONES = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
    )
    dni = models.CharField(max_length=8, unique=True)
    nombre_completo = models.CharField(max_length=200)
    mail = models.EmailField(max_length=254, blank=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=9, choices=GENERO_OPCIONES)
    domicilio = models.CharField(max_length=250)

    class Meta:
        ordering = ('nombre_completo',)

    def __str__(self):
        return '{}'.format(self.nombre_completo)

class Estudiante(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return '{}'.format(self.matricula)