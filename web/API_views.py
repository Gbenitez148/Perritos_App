from .models import Carrousel
from .serializers import CarrouselSerializer
from rest_framework import viewsets


class CarrouselViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Carrousel.objects.filter(habilitado=True)
    serializer_class = CarrouselSerializer
