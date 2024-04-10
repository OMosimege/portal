import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

messenger = Celery('app')
messenger.config_from_object('django.conf:settings', namespace='CELERY')
messenger.autodiscover_tasks()