from rest_framework import serializers
from .models import Usuario,Captura,Rostro

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario','email','nombres','token')

class CapturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Captura
        fields = ('id_captura','fecha','intensidad_pix','cantidad_pix','id_usuario')

class RostroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rostro
        fields = ('id_rostro', 'cantidad_rostros', 'estado', 'id_captura', 'id_usuario')


