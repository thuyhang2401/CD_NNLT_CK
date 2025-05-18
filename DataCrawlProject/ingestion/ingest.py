import json, requests
import os
import time


def ingest_data(filePath):
    with open(filePath) as f:
        data = json.load(f)
    res = requests.post("http://localhost:8000/import-glasses", json=data)
    print(res.status_code)
    print(res.json())


def watch_file(filePath, interval=1):
    last_time = None
    while True:
        try:
            current_time = os.path.getmtime(filePath)
            if last_time is None:
                last_time = current_time

            if current_time != last_time:
                print(f"Detected change in {filePath}, ingesting data...")
                ingest_data(filePath)
                last_time = current_time
            else:
                print("No changes detected.")
        except FileNotFoundError:
            print(f"File {filePath} not found. Waiting for it to be created...")

        time.sleep(interval)


watch_file("data_crawl/data.json", interval=1)
