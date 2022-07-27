from __future__ import absolute_import, unicode_literals
from celery import shared_task

from src.provider.services import buy_car_provider, create_random_car
from src.dealership.services import dealer_buy_car
from src.customer.services import customer_buy_car


@shared_task
def create_car():
    create_random_car.delay()
    buy_car_provider.delay()


@shared_task
def create_dealer():
    dealer_buy_car.delay()


@shared_task
def create_customer():
    customer_buy_car.delay()
