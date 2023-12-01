from celery import Celery
from celery.utils.log import get_task_logger
from dotenv import load_dotenv
import os


load_dotenv('.env')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
clr = Celery(
    "tasks", broker=f"redis://{REDIS_HOST}:{REDIS_PORT}/0", include=["mail.sending"]
)
