import pytest

from src.customer.models import Location
from src.customer.models import Customer


def create_location():
    Location.objects.create(country='Bel', city='Brest', street='Gs', home=18)


@pytest.mark.django_db
def test_location_create():
    create_location()
    assert Location.objects.count() == 1


@pytest.mark.django_db
def test_customer_create():
    create_location()
    location = Location.objects.all().first()
    Customer.objects.create(name='Test', location=location, balance=2000, query='gi', phone='+375333905555', age=15)
    assert Customer.objects.count() == 1





