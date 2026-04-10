from rest_framework import serializers
from .models import Grado, Seccion, Alumno


class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = [
            'id', 'nombre', 'nivel', 'orden', 'activo',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = [
            'id', 'nombre', 'activo',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AlumnoSerializer(serializers.ModelSerializer):
    edad = serializers.SerializerMethodField()
    
    class Meta:
        model = Alumno
        fields = [
            'id', 'nro_matricula', 'nombres', 'apellidos', 'dni',
            'fecha_nacimiento', 'edad', 'direccion', 'telefono',
            'email_apoderado', 'nombre_apoderado', 'telefono_apoderado',
            'estado', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_edad(self, obj):
        from datetime import date
        today = date.today()
        return today.year - obj.fecha_nacimiento.year - (
            (today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day)
        )
