from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    model = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=200)
    price = MoneyField(decimal_places=2, default_currency='USD', max_digits=10)
    engine_volume = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    mileage = models.PositiveIntegerField(null=True, blank=True)
    from_the_factory = models.BooleanField()
    year = models.PositiveIntegerField(blank=True)
    number_of_owners = models.PositiveIntegerField(default=1)
    number_of_car = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(blank=True, max_length=200)
    list_cars = models.ManyToManyField(Car, through='EditorCar')
    balance = MoneyField(decimal_places=2, default_currency='USD', max_digits=100)

    def __str__(self):
        return self.name


class EditorCar(models.Model):
    car = models.ForeignKey(Car, to_field='number_of_car', on_delete=models.SET_NULL, related_name='buy_car', null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider')
    sale = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])


class ProviderSale(models.Model):
    car = models.ForeignKey(Car, to_field='number_of_car', on_delete=models.SET_NULL, related_name='car_sale', null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='provider_sale')
    sale = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    end_date = models.DateField()






