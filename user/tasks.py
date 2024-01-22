import time

from core.settings import app
from core.utils.celery import celery


@celery.task()
def task_long():
    app.logger.info('IN CELERY TASK')
