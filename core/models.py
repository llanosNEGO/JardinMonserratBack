from django.db import models


class Grado(models.Model):
    NIVEL_CHOICES = [
        ('Inicial', 'Inicial'),
        ('Primaria', 'Primaria'),
    ]
    
    nombre = models.CharField(max_length=50, unique=True)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    orden = models.IntegerField()  # 1=1ro, 2=2do, etc.
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['orden']
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
    
    def __str__(self):
        return f"{self.nombre} ({self.nivel})"


class Seccion(models.Model):
    nombre = models.CharField(max_length=10, unique=True)  # A, B, C, Única
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'
    
    def __str__(self):
        return f"Sección {self.nombre}"


class Alumno(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Retirado', 'Retirado'),
        ('Egresado', 'Egresado'),
    ]
    
    nro_matricula = models.CharField(max_length=20, unique=True)  # Formato: AÑO-0001
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email_apoderado = models.EmailField(blank=True, null=True)
    nombre_apoderado = models.CharField(max_length=100)
    telefono_apoderado = models.CharField(max_length=15)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['apellidos', 'nombres']
        indexes = [
            models.Index(fields=['dni']),
            models.Index(fields=['nro_matricula']),
            models.Index(fields=['estado']),
        ]
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
    
    def __str__(self):
        return f"{self.apellidos}, {self.nombres} ({self.dni})"
    
    def get_full_name(self):
        return f"{self.nombres} {self.apellidos}"
