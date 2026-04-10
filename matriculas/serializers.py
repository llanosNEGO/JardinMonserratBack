from rest_framework import serializers
from .models import Estudiante, Matricula


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = [
            'id', 'tipo_documento', 'numero_documento', 'nombres', 'apellidos',
            'fecha_nacimiento', 'grado', 'direccion', 'telefono', 'email', 'activo',
            'nombre_acudiente', 'telefono_acudiente', 'email_acudiente',
            'fecha_creacion', 'fecha_actualizacion'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']


class MatriculaSerializer(serializers.ModelSerializer):
    estudiante_detail = EstudianteSerializer(source='estudiante', read_only=True)
    
    class Meta:
        model = Matricula
        fields = [
            'id', 'estudiante', 'estudiante_detail', 'fecha_matricula', 'año_lectivo',
            'estado', 'observaciones', 'fecha_creacion', 'fecha_actualizacion'
        ]
        read_only_fields = ['id', 'fecha_matricula', 'fecha_creacion', 'fecha_actualizacion']
