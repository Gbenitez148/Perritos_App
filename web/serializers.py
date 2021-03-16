from .models import Carrousel
from rest_framework import serializers


class CarrouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrousel
        fields = '__all__'
