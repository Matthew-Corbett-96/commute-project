from celery import shared_task
from celery.utils.log import get_task_logger

@shared_task(bind=True)
def heartbeat(self) -> None:
    get_task_logger().info("heartbeat!...")

@shared_task(bind=True)
def send_day_before_message(self) -> None:
    get_task_logger().info("Test")
