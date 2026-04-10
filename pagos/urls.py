from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PagoViewSet, ConceptoPagoViewSet

router = DefaultRouter()
router.register(r'conceptos', ConceptoPagoViewSet, basename='concepto-pago')
router.register(r'pagos', PagoViewSet, basename='pago')

urlpatterns = [
    path('', include(router.urls)),
]
