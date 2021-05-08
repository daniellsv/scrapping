from datetime import datetime
from time import sleep

from scrapping.celery import app as celery_app


@celery_app.task()
def tasks_test_diarioAS():
    print(datetime.now())
