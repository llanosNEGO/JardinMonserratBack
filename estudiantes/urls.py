from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, AulaViewSet, ApoderadoViewSet

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'aulas', AulaViewSet)
router.register(r'apoderados', ApoderadoViewSet)

urlpatterns = router.urls