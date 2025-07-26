import datetime
import json
import os

def generate_report():
    today = datetime.date.today().isoformat()
    input_dir = "sample-input"
    output_file = f"reports/summary-{today}.txt"

    if not os.path.exists("reports"):
        os.makedirs("reports")

    summary = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            with open(os.path.join(input_dir, filename)) as f:
                data = json.load(f)
                summary.append(f"{data['event_id']}: {data['message']}")

    with open(output_file, "w") as f:
        f.write("\n".join(summary))

    print(f"✅ Report generated: {output_file}")

if __name__ == "__main__":
    generate_report()
