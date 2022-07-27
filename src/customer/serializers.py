from rest_framework.serializers import ModelSerializer

from src.customer.models import Location, Customer


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = ('name', 'location', 'phone', 'balance', 'query', 'age', 'cars',)


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = ('__all__')
