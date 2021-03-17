from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *


class CarrouselModelViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna el detalle del carrousel
    """

    queryset = Carrousel.objects.filter(habilitado=True)
    serializer_class = CarrouselSerializer
    http_method_names = ['get'] #lo limitamos a que solo pueda usar get
    #permission_classes = (IsAuthenticated,)


class PerroAPIView(ListAPIView):
	"""
    retrieve:
        Se proporciona toda la info correspondiente a los perros
    """

	queryset = Perro.objects.all()
	serializer_class = PerroSerializer

class ContactoAPIView(RetrieveAPIView):
    """
    retrieve:
        Se proporciona toda la info correspondiente al contacto
    """

    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
