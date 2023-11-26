from celery import Celery
from celery.utils.log import get_task_logger


clr = Celery('tasks', broker='redis://localhost:6379/0', include=['mail.sending'])
log = get_task_logger('logs/mailings.log')
