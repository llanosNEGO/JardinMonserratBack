from django.db import models
from core.models import Alumno, Grado, Seccion


class Matricula(models.Model):
    ESTADO_CHOICES = [
        ('Activa', 'Activa'),
        ('Trasladado', 'Trasladado'),
        ('Retirado', 'Retirado'),
    ]
    
    alumno = models.ForeignKey(Alumno, on_delete=models.RESTRICT, related_name='matriculas')
    grado = models.ForeignKey(Grado, on_delete=models.RESTRICT, related_name='matriculas')
    seccion = models.ForeignKey(Seccion, on_delete=models.RESTRICT, related_name='matriculas')
    anio = models.IntegerField()  # Año lectivo
    fecha_matricula = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activa')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-anio', '-fecha_matricula']
        indexes = [
            models.Index(fields=['anio']),
            models.Index(fields=['estado']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['alumno', 'anio'],
                name='unique_matricula_anio',
                violation_error_message='El alumno ya está matriculado en este año'
            )
        ]
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
    
    def __str__(self):
        return f"{self.alumno.get_full_name()} - Grado {self.grado.nombre} - {self.anio}"
