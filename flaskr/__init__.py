import os
from flask import Flask
from flaskr.utils import celery_init_app


def create_app():
   app = Flask(__name__)
   app.config["CELERY_CONFIG"] = {
        "broker_url": os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"),
        "result_backend": os.environ.get(
            "CELERY_RESULT_BACKEND", "redis://localhost:6379/0"
        ),
        "beat_schedule": {
            "name-here": {
                "task": "flaskr.tasks.task-name",
                "schedule": 30.0,
                "args": (16, 16),
            }
        },
    }
   celery = celery_init_app(app)
   celery.set_default()
   return app, celery