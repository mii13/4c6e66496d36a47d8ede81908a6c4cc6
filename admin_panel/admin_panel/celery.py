import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_panel.settings')

broker = os.environ.get('AMQP_CELERY_URL', "amqp://user1:mypass@rabbit/host0")
result_backend = os.environ.get('REDIS_CELERY_URL', 'redis://redis:6379/0')

app = Celery('admin_panel', broker=broker, backend=result_backend)
# app.conf.result_backend = result_backend

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings',  namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
