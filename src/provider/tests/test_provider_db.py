import pytest

from src.provider.models import Car, Provider


@pytest.mark.django_db
def test_car_create():
    Car.objects.create(model='BMW', color='RED', price=1000, engine_volume=5, year=2001, is_from_the_factory=True,
                       vin_number='1G1AK15FX67668379')
    assert Car.objects.count() == 1


@pytest.mark.django_db
def test_provider_create():
    Car.objects.create(model='BMW', color='RED', price=1000, engine_volume=5, year=2001, is_from_the_factory=True,
                       vin_number='1G1AK15FX67668379')
    cars = Car.objects.all()
    provider = Provider.objects.create(name='Test', balance=2000)
    provider.list_cars.set(cars)
    assert Provider.objects.count() == 1
