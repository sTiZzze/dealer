from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

from src.addition.abstract_model import UpdatedAt, Delete
from src.core.enums.ProviderEnum import Color


class Car(UpdatedAt, Delete):
    model = models.TextField(max_length=50)
    description = models.TextField(blank=True, max_length=200)
    color = models.CharField(choices=Color.choices, default=Color.BLACK)
    price = MoneyField(decimal_places=2, default_currency='USD', max_digits=10)
    engine_volume = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    mileage = models.PositiveIntegerField(null=True, blank=True)
    is_from_the_factory = models.BooleanField()
    year = models.PositiveIntegerField(blank=True)
    amount_of_owners = models.PositiveIntegerField(default=1)
    vin_number = models.CharField(
        max_length=17,
        unique=True,
        validators=[
            RegexValidator(regex="^[A-HJ-NPR-Za-hj-npr-z\d]{8}[\dX][A-HJ-NPR-Za-hj-npr-z\d]{2}\d{6}$")
        ]
    )

    def __str__(self):
        return self.name


class Provider(UpdatedAt, Delete):
    name = models.CharField(max_length=40)
    description = models.CharField(blank=True, max_length=200)
    list_cars = models.ManyToManyField(Car, through='EditorCar')
    balance = MoneyField(decimal_places=2, default_currency='USD', max_digits=100)

    def __str__(self):
        return self.name


class EditorCar(UpdatedAt, Delete):
    car = models.ForeignKey(Car, to_field='number_of_car', on_delete=models.SET_NULL, related_name='buy_car', null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider')
    is_sale = models.BooleanField(default=False)


class ProviderSale(UpdatedAt, Delete):
    car = models.ForeignKey(Car, to_field='number_of_car', on_delete=models.SET_NULL, related_name='car_sale', null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider_sale')
    sale = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    end_date = models.DateField()






