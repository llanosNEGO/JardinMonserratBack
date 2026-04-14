from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]