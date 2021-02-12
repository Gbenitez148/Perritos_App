from rest_framework import viewsets
from .models import Carrousel
from .serializers import CarrouselSerializer


class CarrouselModelViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna el detalle del carrousel
    """

    queryset = Carrousel.objects.filter(habilitado=True)
    serializer_class = CarrouselSerializer
    http_method_names = ['get'] #lo limitamos a que solo pueda usar get
    #permission_classes = (IsAuthenticated,)
