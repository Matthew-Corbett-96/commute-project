import json
import requests
from requests.models import Response

api_key = "AIzaSyCBsjUxCwkwDA8XUkb_aO3x0J0VewR4z_A"


def get_dist_dur(start, end):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        "origins": start,
        "destinations": end,
        "key": "AIzaSyCBsjUxCwkwDA8XUkb_aO3x0J0VewR4z_A",
    }

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
    starts: list[str] = []
    ends: list[str] = []
    # open file and parse Json
    with open("locations.json", "r") as file:
        data = json.load(file)
        for item in data["start-locations"]:
            starts.append(item)
        for item in data["end-locations"]:
            ends.append(item)
    return starts, ends
