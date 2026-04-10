from rest_framework import serializers
from .models import Matricula
from core.models import Alumno, Grado, Seccion
from core.serializers import AlumnoSerializer, GradoSerializer, SeccionSerializer


class MatriculaSerializer(serializers.ModelSerializer):
    alumno_detail = AlumnoSerializer(source='alumno', read_only=True)
    grado_detail = GradoSerializer(source='grado', read_only=True)
    seccion_detail = SeccionSerializer(source='seccion', read_only=True)
    
    class Meta:
        model = Matricula
        fields = [
            'id', 'alumno', 'alumno_detail', 'grado', 'grado_detail',
            'seccion', 'seccion_detail', 'anio', 'fecha_matricula',
            'estado', 'observaciones', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'fecha_matricula', 'created_at', 'updated_at']
