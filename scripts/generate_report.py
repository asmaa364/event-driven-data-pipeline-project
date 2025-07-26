import os
import json
from datetime import datetime

INPUT_FILE = "sample-input/input.jsonl"
REPORT_FILE = "reports/daily_report.txt"

def create_sample_input():
    os.makedirs(os.path.dirname(INPUT_FILE), exist_ok=True)
    if not os.path.exists(INPUT_FILE):
        print("Creating sample input.jsonl file...")
        with open(INPUT_FILE, "w") as f:
            f.write('{"event_id": "evt1", "message": "User signed up"}\n')
            f.write('{"event_id": "evt2", "message": "File uploaded"}\n')
            f.write('{"event_id": "evt3", "message": "Report generated"}\n')

def generate_report():
    create_sample_input()
    summary = []

    with open(INPUT_FILE, "r") as infile:
        for line in infile:
            try:
                data = json.loads(line.strip())
                event_id = data.get("event_id", "N/A")
                message = data.get("message", "No message")
                summary.append(f"{event_id}: {message}")
            except json.JSONDecodeError:
                continue

    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)

    with open(REPORT_FILE, "w") as outfile:
        outfile.write(f"Daily Report - {datetime.now()}\n")
        outfile.write("\n".join(summary))

if __name__ == "__main__":
    generate_report()
