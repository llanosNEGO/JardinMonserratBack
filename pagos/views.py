from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Pago, ConceptoPago
from .serializers import PagoSerializer, ConceptoPagoSerializer


class ConceptoPagoViewSet(viewsets.ModelViewSet):
    queryset = ConceptoPago.objects.filter(activo=True)
    serializer_class = ConceptoPagoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['nombre', 'monto']
    ordering = ['nombre']


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['estudiante__numero_documento', 'estudiante__nombres', 'estado']
    ordering_fields = ['fecha_pago', 'monto', 'estado']
    ordering = ['-fecha_pago']
