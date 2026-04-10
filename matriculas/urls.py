from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, MatriculaViewSet

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet, basename='estudiante')
router.register(r'matriculas', MatriculaViewSet, basename='matricula')

urlpatterns = [
    path('', include(router.urls)),
]
