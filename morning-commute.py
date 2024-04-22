import json
from geo.main import get_dist_dur, pull_start_end

if __name__ == "__main__":
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
