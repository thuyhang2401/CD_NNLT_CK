import json, requests
import os
import time


def ingest_data(filePath):
    with open(filePath) as f:
        data = json.load(f)
    api_host = os.getenv("API_HOST", "localhost")
    api_port = os.getenv("API_PORT", "8000")
    res = requests.post(f"http://{api_host}:{api_port}/import-glasses", json=data)
    print(res.status_code)
    print(res.json())


def watch_file(filePath, interval=1):
    last_time = None
    while True:
        try:
            current_time = os.path.getmtime(filePath)
            print(f"Watching file: {filePath}, last modified: {current_time}")
            if last_time is None:
                last_time = current_time
                print(f"Detected initial file {filePath}, ingesting data...")
                while True:
                    try:
                        ingest_data(filePath)
                        break
                    except Exception as e:
                        print(f"Error ingesting data: {e}. Retrying in 5 seconds...")
                        time.sleep(5)
            elif current_time != last_time:
                print(f"Detected change in {filePath}, ingesting data...")
                while True:
                    try:
                        ingest_data(filePath)
                        break
                    except Exception as e:
                        print(f"Error ingesting data: {e}. Retrying in 5 seconds...")
                        time.sleep(5)
                last_time = current_time
            else:
                print("No changes detected.")
        except FileNotFoundError:
            print(f"File {filePath} not found. Waiting for it to be created...")

        time.sleep(interval)


file_path = os.getenv("DATA_FILE_PATH", "./data_crawl/data.json")
watch_file(file_path, interval=1)
