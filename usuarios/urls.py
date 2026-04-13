from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
from .views import RegisterView
from django.urls import path


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatternsj = router.urls


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]