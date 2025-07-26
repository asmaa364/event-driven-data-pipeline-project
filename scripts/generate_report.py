import json
import os
from datetime import datetime

def generate_report():
    input_file = 'sample-input/events.json'
    output_dir = 'reports'
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'summary-' + datetime.now().strftime('%Y-%m-%d') + '.txt')

    with open(input_file, 'r') as f:
        data_list = json.load(f)

    summary = []
    for data in data_list:
        event_id = data.get('event_id', 'N/A')
        message = data.get('message', 'No message')
        summary.append(f"{event_id}: {message}")

    with open(output_file, 'w') as f:
        f.write("\n".join(summary))

    print(f"✅ Report generated: {output_file}")

if __name__ == "__main__":
    generate_report()
