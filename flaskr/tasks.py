import json

from celery import shared_task
from celery.utils.log import get_task_logger
from geo.main import get_dist_dur, pull_start_end


@shared_task(bind=True)
def morningCommute(self) -> None:
    homes, works = pull_start_end()
    results: dict[str, dict[str, str]] = {}

    for home in homes:
        temp = {}
        for work in works:
            distance, duration = get_dist_dur(home, work)
            if distance and duration:
                temp[work] = {"distance": distance, "duration": duration}
        results[home] = temp

    with open("results-morning.json", "w") as file:
        json.dump(results, file, indent=4)


@shared_task(bind=True)
def afternoonCommute(self) -> None:
    get_task_logger("Test").info("Test")
