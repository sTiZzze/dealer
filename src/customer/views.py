
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.customer.serializers import LocationSerializer, CustomerSerializer
from src.customer.models import Location, Customer
from src.core.permissions import CustomerPermission


class LocationView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    permission_classes = (CustomerPermission,)
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomerView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    permission_classes = (CustomerPermission,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

