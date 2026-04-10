from django.db import models
from matriculas.models import Estudiante

class ConceptoPago(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    es_mensualidad = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} - ${self.monto}"


class Pago(models.Model):
    METODOS_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('TRANSFERENCIA', 'Transferencia Bancaria'),
        ('TARJETA', 'Tarjeta Crédito/Débito'),
        ('CHEQUE', 'Cheque'),
    ]
    
    ESTADOS_PAGO = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('REEMBOLSADO', 'Reembolsado'),
    ]
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='pagos')
    concepto = models.ForeignKey(ConceptoPago, on_delete=models.PROTECT, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO, default='EFECTIVO')
    estado = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='PENDIENTE')
    comprobante = models.FileField(upload_to='comprobantes/', blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_pago']
    
    def __str__(self):
        return f"{self.estudiante.numero_documento} - {self.concepto.nombre} - {self.fecha_pago}"
