from rest_framework import routers
from django.urls import path, include

from src.dealership.views import LocationView, DealershipView

router = routers.DefaultRouter()
router.register('list', DealershipView, "dealerships")
router.register('locations', LocationView, "locations")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
