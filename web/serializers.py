from rest_framework import serializers
from .models import *


class CarrouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrousel
        fields = ['id', 'foto', 'titulo', 'texto', 'pie_de_pagina']


class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
        fields = '__all__'


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'


class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'
