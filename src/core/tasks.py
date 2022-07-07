from __future__ import absolute_import, unicode_literals
from celery import shared_task


from config.celery import app
from src.provider.services import buy_car_provider, create_random_car


@shared_task
def create_car():
    create_random_car.delay()
    buy_car_provider.delay()










