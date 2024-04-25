import os

from celery.schedules import crontab
from flask import Flask

from flaskr.tasks import afternoon_commute, morning_commute
from flaskr.utils import celery_init_app


def create_app():
    app = Flask(__name__)
    app.config["CELERY_CONFIG"] = {
        "broker_url": os.environ.get("CELERY_BROKER_URL"),
        "result_backend": os.environ.get("CELERY_RESULT_BACKEND"),
        "beat_schedule": {
            "morning-commute-matthew": {
                "task": "flaskr.tasks.morning_commute_task",
                "schedule": crontab(hour="10", minute="30"),
            },
            "afternoon-commute-matthew": {
                "task": "flaskr.tasks.afternoon_commute_task",
                "schedule": crontab(hour="21", minute="0"),
            },
            "morning-commute-patience": {
                "task": "flaskr.tasks.morning_commute_task",
                "schedule": crontab(hour="11", minute="30"),
            },
            "afternoon-commute-patience": {
                "task": "flaskr.tasks.afternoon_commute_task",
                "schedule": crontab(hour="22", minute="30"),
            },
        },
    }
    celery = celery_init_app(app)
    celery.set_default()
    return app, celery
