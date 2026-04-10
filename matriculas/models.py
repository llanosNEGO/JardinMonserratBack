from django.db import models

class Estudiante(models.Model):
    TIPOS_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('PP', 'Pasaporte'),
        ('CE', 'Cédula de Extranjería'),
    ]
    
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO)
    numero_documento = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    grado = models.CharField(max_length=20)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    activo = models.BooleanField(default=True)
    nombre_acudiente = models.CharField(max_length=100)
    telefono_acudiente = models.CharField(max_length=20)
    email_acudiente = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['apellidos', 'nombres']
    
    def __str__(self):
        return f"{self.apellidos}, {self.nombres} - {self.numero_documento}"


class Matricula(models.Model):
    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name='matricula')
    fecha_matricula = models.DateField(auto_now_add=True)
    año_lectivo = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVA')
    observaciones = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-año_lectivo', 'estudiante']
    
    def __str__(self):
        return f"{self.estudiante.nombre} - {self.año_lectivo}"
