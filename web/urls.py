from django.conf.urls import url, include
from rest_framework import routers
from .APIviews import *


router = routers.SimpleRouter()
router.register(r'carrousel', CarrouselModelViewSet)

app_name = "web"

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'perros/$', PerroAPIView.as_view()),

]
