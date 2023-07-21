from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

import core.tasks


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mails.settings')

app = Celery('mails')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.enable_utc = False

app.conf.update(timezone='Africa/Nairobi')


# celery beat settings
app.conf.beat_schedule = {
    'send-mail-daily': {
        'task': 'core.tasks.send_periodic_mails',
        'schedule': crontab(hour='14', minute='30'),
        'args': ('Omo, Do de ting!! Just do it.',)
    }
}

app.autodiscover_tasks()
