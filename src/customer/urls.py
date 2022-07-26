from rest_framework import routers
from django.urls import path, include

from src.customer.views import LocationView, CustomerView

router = routers.DefaultRouter()
router.register('list', CustomerView, "customers")
router.register('locations', LocationView, "locations")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
