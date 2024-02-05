from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qr.settings')

app = Celery('qr')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-outdated-events-every-day-at-22-00': {
        'task': 'back.tasks.delete_expired_data',
        'schedule': crontab(hour=17),  # Run every day at 22:00
    },
}

app.conf.timezone = 'UTC'
