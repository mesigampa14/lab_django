from django.db import models
from django.utils import timezone

from apps.persona.models import Estudiante, Docente
from proyecto.models import Proyecto


class Estado(models.Model):
    ESTADO_OPCIONES = (
        ('aceptado', 'Aceptado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado'),
    )
    MOVIMIENTO_OPCIONES = (
        ('presenta_PTF', 'Presentación PTF'),
        ('pase_a_CSTF', 'pase a la CSTF'),
        ('dictamen_a_CSTF', 'dictamen de la CSTF sobre el formato del PTF'),
        ('pase_a_TE', 'Pase al TE'),
        ('dictamen_TE', 'Dictamen tribunal evaluador sobre evaluación PT'),
        ('presenta_IF', 'Presentación borrador Informe final'),
        ('dictamen_Borrador', 'Dictamen tribunal evaluador sobre borrador'),
    )
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_movimiento = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=100, blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=20, choices=MOVIMIENTO_OPCIONES, default='presenta_PTF', blank=True, null=True)
    archivos_relacionados = models.FileField(upload_to='archivos_estado/', blank=True, null=True)

    def __str__(self):
        return f"Estado del Proyecto: {self.proyecto}, Tipo: {self.tipo_movimiento}"