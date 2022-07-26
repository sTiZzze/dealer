import pytest

from src.dealership.models import Location
from src.dealership.models import Dealership


def create_location():
    Location.objects.create(country='Bel', city='Brest', street='Gs', home=18)


@pytest.mark.django_db
def test_location_create():
    create_location()
    assert Location.objects.count() == 1


@pytest.mark.django_db
def test_dealership_create():
    create_location()
    location = Location.objects.all().first()
    Dealership.objects.create(name='Test', location=location, balance=2000, query='gi')
    assert Dealership.objects.count() == 1





