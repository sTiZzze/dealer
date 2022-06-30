from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from djmoney.forms import MoneyField

from src.provider.models import Car, Provider
from src.addition.abstract_model import CreatedAt, UpdatedAt, Delete


class Location(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.TextField(max_length=10)
    flat = models.TextField(max_length=10, blank=True)


class Dealership(CreatedAt, UpdatedAt, Delete):
    name = models.TextField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location')
    description = models.TextField(blank=True)
    balance = MoneyField(decimal_places=2, default_currency='USD', max_digits=10)
    cars = models.ManyToManyField(Car, through='ProviderCars')

    def __str__(self):
        return self.name


class ProviderCars(CreatedAt, UpdatedAt, Delete):
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, related_name='dealerships',
                                   null=True, blank=True)
    cars = models.ForeignKey(Car, to_field='vin_number', on_delete=models.SET_NULL, related_name='cars_of_dealership',
                             null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='providers', null=True)


class DealershipSale(CreatedAt, UpdatedAt, Delete):
    car = models.ForeignKey(Car, to_field='vin_number', on_delete=models.SET_NULL,
                            related_name='cars_dealership_sale',
                            null=True)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, related_name='sales_dealership', null=True)
    sale = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    end_date = models.DateField(blank=True)

