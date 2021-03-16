<<<<<<< HEAD
from django.conf.urls import url, include
from rest_framework import routers
from .APIviews import *


router = routers.SimpleRouter()
router.register(r'carrousel', CarrouselModelViewSet)

app_name = "web"

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'perros/$', PerroAPIView.as_view()),

=======
from rest_framework import routers
from django.conf.urls import url, include
from .API_views import *


router = routers.SimpleRouter()
router.register(r'carrousel', CarrouselViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
>>>>>>> 8ae5c0cb5707e71855e617ee997038ab04c67230
]
