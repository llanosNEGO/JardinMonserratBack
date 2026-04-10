from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("API Reportes - Servicio disponible")

urlpatterns = [
    path('', index, name='reportes-index'),
]
