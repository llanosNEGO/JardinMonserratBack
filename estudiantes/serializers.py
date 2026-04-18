from rest_framework import serializers
from .models import Estudiante, Aula, Apoderado

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'


class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoderado
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    aula_nombre = serializers.CharField(source='aula.nombre', read_only=True)
    apoderado_nombre = serializers.CharField(source='apoderado.nombres', read_only=True)

    apoderado = ApoderadoSerializer()

    class Meta:
        model = Estudiante
        fields = '__all__'

    def create(self, validated_data):
        apoderado_data = validated_data.pop('apoderado')
        apoderado = Apoderado.objects.create(**apoderado_data)
        estudiante = Estudiante.objects.create(apoderado=apoderado, **validated_data)
        return estudiante

    def update(self, instance, validated_data):
        apoderado_data = validated_data.pop('apoderado')

        # actualizar apoderado
        apoderado = instance.apoderado
        for attr, value in apoderado_data.items():
            setattr(apoderado, attr, value)
        apoderado.save()

        # actualizar estudiante
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance