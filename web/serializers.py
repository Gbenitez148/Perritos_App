<<<<<<< HEAD
from rest_framework import serializers
from .models import *
=======
from .models import Carrousel
from rest_framework import serializers
>>>>>>> 8ae5c0cb5707e71855e617ee997038ab04c67230


class CarrouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrousel
<<<<<<< HEAD
        fields = ['id','foto', 'titulo', 'texto', 'pie_de_pagina']


class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
=======
>>>>>>> 8ae5c0cb5707e71855e617ee997038ab04c67230
        fields = '__all__'
