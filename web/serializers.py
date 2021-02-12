from rest_framework import serializers
from .models import Carrousel


class CarrouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrousel
        fields = ['id','foto', 'titulo', 'texto', 'pie_de_pagina']
