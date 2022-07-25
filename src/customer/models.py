from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from djmoney.models.fields import MoneyField

from src.addition.abstract_model import CreatedAt, UpdatedAt, Delete
from src.provider.models import Car
from src.dealership.models import Dealership


class Location(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.TextField(max_length=10)
    flat = models.TextField(max_length=10, blank=True)


class Customer(CreatedAt, UpdatedAt, Delete):
    name = models.CharField(max_length=30)
    age = models.IntegerField(
        blank=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(14)
        ])
    query = models.JSONField(blank=True)
    location = models.ForeignKey(Location,  on_delete=models.CASCADE, related_name='location')
    balance = MoneyField(decimal_places=2, default_currency='USD', max_digits=10)
    phone = models.CharField(
        max_length=40,
        validators=(
            RegexValidator(regex="^(\+375|80)(17|29|33|44)[0-9]{3}[0-9]{2}[0-9]{2}$"),
        )
    )
    cars = models.ManyToManyField(Car, through='Buy')

    def __str__(self):
        return self.name


class Buy(CreatedAt, UpdatedAt, Delete):
    count = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, to_field='vin_number', on_delete=models.SET_NULL,
                            related_name='cars',
                            null=True, blank=True)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, related_name='car_dealership')


