from __future__ import absolute_import, unicode_literals
from celery import shared_task
from src.provider.models import Car, Provider, EditorCar
from src.dealership.models import Dealership, ProviderCars


