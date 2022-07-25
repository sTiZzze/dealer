from __future__ import absolute_import, unicode_literals
from django.db.models import Q
from celery import shared_task

from src.provider.models import Car, Provider, EditorCar
from src.dealership.models import Dealership, ProviderCars


@shared_task
def dealer_buy_car():
    Dealerships = Dealership.objects.all()

    for dealership in Dealerships:
        query = dealership.query
        try:
            cars = Car.objects.filter(Q(model=query.get('model')) &
                                      Q(price__lte=query.get('price')) &
                                      Q(engine_volume__lte=query.get('engine')) &
                                      Q(color=query.get('color')))
            car = cars.exclude(buy_car__provider__isnull=True).order_by('price').first()
            editor = EditorCar.objects.filter(car=car).first()
            ProviderCars.objects.create(dealership=dealership, provider=editor.provider, cars=editor.car)
            dealership.balance -= car.price
            editor.provider.balance += car.price
            dealership.save()
            editor.provider.save()
        except:
            continue
