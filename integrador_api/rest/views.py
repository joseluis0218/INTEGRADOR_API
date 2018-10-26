from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario,Captura,Rostro
from .serializers import UsuarioSerializer,CapturaSerializer,RostroSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id_usuario')
    serializer_class = UsuarioSerializer

class CapturaViewSet(viewsets.ModelViewSet):
    queryset = Captura.objects.all().order_by('fecha')
    serializer_class = CapturaSerializer

class RostroViewSet(viewsets.ModelViewSet):
    queryset = Rostro.objects.all().order_by('id_rostro')
    serializer_class = RostroSerializer