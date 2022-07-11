
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.dealership.serializers import LocationSerializer, DealershipSerializer
from src.dealership.models import Location, Dealership
from src.core.permissions import DealerPermission


class LocationView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    permission_classes = (DealerPermission,)
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DealershipView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    permission_classes = (DealerPermission,)
    serializer_class = DealershipSerializer
    queryset = Dealership.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
