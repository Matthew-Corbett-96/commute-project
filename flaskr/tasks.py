import json

from celery import shared_task
from celery.utils.log import get_task_logger

from flaskr.geo.main import afternoon_commute, morning_commute


@shared_task(bind=True)
def morning_commute_task(self) -> None:
    morning_commute()


@shared_task(bind=True)
def afternoon_commute_task(self) -> None:
    afternoon_commute()
