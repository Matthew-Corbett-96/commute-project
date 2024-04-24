import json

from geo.main import get_dist_dur, pull_start_end

if __name__ == "__main__":
    homes, works = pull_start_end()
    results: dict[str, dict[str, str]] = {}

    for work in works:
        temp = {}
        for home in homes:
            distance, duration = get_dist_dur(work, home)
            if distance and duration:
                temp[home] = {"distance": distance, "duration": duration}
        results[work] = temp

    with open("results-afternoon.json", "w") as file:
        json.dump(results, file, indent=4)
