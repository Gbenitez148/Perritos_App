from django.conf.urls import url, include
from rest_framework import routers
from .APIviews import *


router = routers.SimpleRouter()
router.register(r'carrousel', CarrouselModelViewSet)

app_name = "web"

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'perros/$', PerroAPIView.as_view()),
    url(r'contacto/(?P<pk>\d+)/$', ContactoAPIView.as_view()),
    url(r'entrega/(?P<pk>\d+)/$', EntregaAPIView.as_view()),
]
