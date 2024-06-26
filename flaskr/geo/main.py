import json
from datetime import datetime
from os import environ

import requests
from requests.models import Response


def get_dist_dur(start, end):
    base_url: str = environ.get("BASE_URL", "")

    params = {"origins": start, "destinations": end, "key": environ.get("API_KEY")}

    response: Response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            distance = data["rows"][0]["elements"][0]["distance"]["text"]
            duration = data["rows"][0]["elements"][0]["duration"]["text"]
            return distance, duration
        else:
            print("Request failed.")
            return None, None
    else:
        print("Failed to make the request.")
        return None, None


def pull_start_end() -> tuple[list[str], list[str]]:
    homes: list[str] = []
    works: list[str] = []
    # open file and parse Json
    with open("flaskr/geo/locations.json", "r") as file:
        data = json.load(file)
        for item in data["homes"]:
            homes.append(item)
        for item in data["works"]:
            works.append(item)
    return homes, works


def morning_commute() -> None:
    homes, works = pull_start_end()
    results: dict[str, dict[str, str]] = {}

    for home in homes:
        temp = {}
        for work in works:
            distance, duration = get_dist_dur(home, work)
            if distance and duration:
                temp[work] = {"distance": distance, "duration": duration}
        results[home] = temp

    with open(f"results-morning{datetime.now()}.json", "w") as file:
        json.dump(results, file, indent=4)


def afternoon_commute() -> None:
    homes, works = pull_start_end()
    results: dict[str, dict[str, str]] = {}

    for work in works:
        temp = {}
        for home in homes:
            distance, duration = get_dist_dur(work, home)
            if distance and duration:
                temp[home] = {"distance": distance, "duration": duration}
        results[work] = temp

    with open(f"results-afternoon{datetime.now()}.json", "w") as file:
        json.dump(results, file, indent=4)
