from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("API Jardín Monserrat - Servidor activo")

urlpatterns = [
    path('', home, name='core-home'),
]
