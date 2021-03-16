from rest_framework import serializers
from .models import *


class CarrouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrousel
        fields = ['id','foto', 'titulo', 'texto', 'pie_de_pagina']


class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
        fields = '__all__'
