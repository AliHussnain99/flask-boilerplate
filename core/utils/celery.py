# CELERY CONFIGURATIONS
from celery import Celery, schedules
from redis import Redis

from core.settings import app
from core.utils.helpers import get_env_variable

REDIS_HOST = get_env_variable('REDIS_HOST')
REDIS_PORT = get_env_variable('REDIS_PORT')
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

# Configure Celery
celery = Celery(
    app.name,
    broker=f'redis://{REDIS_HOST}:{REDIS_PORT}/0',
    backend=f'redis://{REDIS_HOST}:{REDIS_PORT}/0',
)
celery.conf.update(app.config)

# SCHEDULING TASKS
# celery.conf.beat_schedule = {
#     'task-long': {
#         'task': 'user.tasks.task_long',
#         'schedule': schedules.schedule(run_every=10),  # Run the task every 1 second
#     },
# }
