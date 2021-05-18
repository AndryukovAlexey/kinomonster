import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kinomonster.settings')

app = Celery('kinomonster')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_prem': {
        'task': 'users.tasks.check_prem',
        'schedule': crontab(minute=1, hour=0)
    },
}
