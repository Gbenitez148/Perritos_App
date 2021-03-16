from rest_framework import routers
from django.conf.urls import url, include
from .API_views import *


router = routers.SimpleRouter()
router.register(r'carrousel', CarrouselViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
