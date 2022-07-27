from rest_framework.serializers import ModelSerializer

from src.provider.models import Provider, Car, EditorCar, ProviderSale


class ProviderSerializer(ModelSerializer):

    class Meta:
        model = Provider
        fields = ('name', 'description', 'list_cars', 'balance', )


class EditorSerializer(ModelSerializer):

    class Meta:
        model = EditorCar
        fields = ('car', 'provider', 'is_sale', )


class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = ('__all__')


class SaleSerializer(ModelSerializer):

    class Meta:
        model = ProviderSale
        fields = ('__all__')
