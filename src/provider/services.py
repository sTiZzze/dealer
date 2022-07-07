from __future__ import absolute_import, unicode_literals

import random

from celery import shared_task
from src.provider.models import Car, Provider, EditorCar


@shared_task
def buy_car_provider():
    car = Car.objects.order_by('?').first()
    provider = Provider.objects.order_by('?').first()
    EditorCar.objects.create(provider=provider, car=car)
    provider.save()
    car.save()


@shared_task
def create_random_car():
    model = random.choice(['BMW', 'Audi', 'Lada', 'Mercedes'])
    color = random.choice(['RED', 'BLUE', 'GREEN', 'WHITE', 'BLACK', 'SILVER'])
    price = random.randint(1000, 10000)
    engine = random.randint(1, 10)
    mileage = random.randint(1, 10)
    is_factory = random.choice(['True', 'False'])
    year = random.randint(1990, 2022)
    amount_of_owners = random.randint(1,8)
    vin_number = random.randint(1000000, 9999999)

    Car.objects.create(
        model=model,
        color=color,
        price=price,
        engine_volume=engine,
        mileage=mileage,
        is_from_the_factory=is_factory,
        year=year,
        amount_of_owners=amount_of_owners,
        vin_number='JN8AZ2NE5C' + str(vin_number)
    )


try:
    from celery.utils.log import get_task_logger
    logger = get_task_logger(__name__)
except ImportError:
    logger = buy_car_provider.get_logger()

