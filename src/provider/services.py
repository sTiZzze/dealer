from __future__ import absolute_import, unicode_literals
from celery import shared_task
from config.celery import app

@shared_task
def buy_car_provider():
    from src.provider.models import Car, Provider, EditorCar
    cars = Car.objects.all()
    for car in cars:
        car.is_active = True
        car.save()


                #EditorCar.car = car
                #EditorCar.provider = provider
                #Car.is_active = True
                #EditorCar.save()
                #Car.save()
    return True


try:
    from celery.utils.log import get_task_logger
    logger = get_task_logger(__name__)
except ImportError:
    logger = buy_car_provider.get_logger()

