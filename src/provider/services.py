from __future__ import absolute_import, unicode_literals
from celery import shared_task
from src.provider.models import Car, Provider, EditorCar


@shared_task
def buy_car_provider():
    cars = Car.objects.all()
    providers = Provider.objects.all()
    for provider in providers:
        for car in cars:
            if provider.balance > car.price:
                provider.balance -= car.price
                EditorCar.objects.create(provider=provider, car=car)
                provider.save()
                car.save()
            else:
                continue
    return True


try:
    from celery.utils.log import get_task_logger
    logger = get_task_logger(__name__)
except ImportError:
    logger = buy_car_provider.get_logger()

