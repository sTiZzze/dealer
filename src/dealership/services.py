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
            model = query.get('model')
            price = query.get('price')
            engine = query.get('engine')
            color = query.get('color')
            cars = Car.objects.filter(Q(model=model) &
                                      Q(price__lte=price) &
                                      Q(engine_volume__lte=engine) &
                                      Q(color=color))
            car = cars.exclude(buy_car__provider__isnull=True).order_by('price').first()
            editor = EditorCar.objects.filter(car=car).first()
            ProviderCars.objects.create(dealership=dealership, provider=editor.provider, cars=editor.car)
            dealership.balance -= car.price
            dealership.save()
        except:
            continue
