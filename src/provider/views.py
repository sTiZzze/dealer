
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.provider.serializers import ProviderSerializer, CarSerializer, SaleSerializer
from src.provider.models import Provider, Car, ProviderSale
from src.provider.services import buy_car_provider


class ProviderView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CarView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SaleView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = SaleSerializer
    queryset = ProviderSale.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



