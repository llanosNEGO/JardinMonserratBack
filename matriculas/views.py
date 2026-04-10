from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Estudiante, Matricula
from .serializers import EstudianteSerializer, MatriculaSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombres', 'apellidos', 'numero_documento', 'email']
    ordering_fields = ['apellidos', 'nombres', 'fecha_creacion']
    ordering = ['apellidos', 'nombres']
    
    @action(detail=False, methods=['get'])
    def activos(self, request):
        """Obtener solo estudiantes activos"""
        estudiantes = Estudiante.objects.filter(activo=True)
        serializer = self.get_serializer(estudiantes, many=True)
        return Response(serializer.data)


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['estudiante__nombres', 'estudiante__apellidos', 'año_lectivo']
    ordering_fields = ['año_lectivo', 'fecha_matricula', 'estado']
    ordering = ['-año_lectivo']
