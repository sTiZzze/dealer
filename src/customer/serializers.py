from rest_framework.serializers import ModelSerializer

from src.customer.models import Location, Customer


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ('__all__')


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = ('__all__')
