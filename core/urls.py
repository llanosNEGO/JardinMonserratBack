from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GradoViewSet, SeccionViewSet, AlumnoViewSet

router = DefaultRouter()
router.register(r'grados', GradoViewSet, basename='grado')
router.register(r'secciones', SeccionViewSet, basename='seccion')
router.register(r'alumnos', AlumnoViewSet, basename='alumno')

urlpatterns = [
    path('', include(router.urls)),
]
