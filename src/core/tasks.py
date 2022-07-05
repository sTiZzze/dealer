from __future__ import absolute_import, unicode_literals
from celery import shared_task


from config.celery import app
from src.provider.services import buy_car_provider


@shared_task
def buy_car():
    buy_car_provider.delay()










