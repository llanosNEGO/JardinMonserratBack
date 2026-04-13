from django.db import models

class Aula(models.Model):
    nombre = models.CharField(max_length=50)  # 2 años, 3 años...
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Apoderado(models.Model):
    nombres = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombres


class Estudiante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"