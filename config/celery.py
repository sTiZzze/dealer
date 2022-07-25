from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add_provider_car': {
        'task': 'src.core.tasks.create_car',
        'schedule': 600.0
    },
    'add-dealer_car': {
        'task': 'src.core.tasks.create_dealer',
        'schedule': 600.0
    },
    'add-customer_car': {
        'task': 'src.core.tasks.create_customer',
        'schedule': 10.0
    },
}
app.conf.timezone = 'UTC'
