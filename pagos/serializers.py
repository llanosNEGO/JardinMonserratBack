from rest_framework import serializers
from .models import Pago, ConceptoPago
from matriculas.models import Estudiante


class ConceptoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptoPago
        fields = [
            'id', 'nombre', 'descripcion', 'monto', 'es_mensualidad', 'activo',
            'fecha_creacion', 'fecha_actualizacion'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']


class PagoSerializer(serializers.ModelSerializer):
    concepto_detail = ConceptoPagoSerializer(source='concepto', read_only=True)
    estudiante_nombre = serializers.CharField(source='estudiante.get_full_name', read_only=True)
    
    class Meta:
        model = Pago
        fields = [
            'id', 'estudiante', 'estudiante_nombre', 'concepto', 'concepto_detail', 'monto',
            'fecha_pago', 'metodo_pago', 'estado', 'comprobante', 'referencia', 'observaciones',
            'fecha_creacion', 'fecha_actualizacion'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']
