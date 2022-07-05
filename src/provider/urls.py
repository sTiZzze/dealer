from rest_framework import routers
from django.urls import path, include

from src.provider.views import ProviderView, CarView, SaleView

router = routers.DefaultRouter()
router.register('list', ProviderView, "list")
router.register('cars', CarView, "cars")
router.register('sales', SaleView, "sales")


urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
