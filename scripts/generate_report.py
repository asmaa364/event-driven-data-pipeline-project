import json
import os
from datetime import datetime

# File paths
input_file_path = 'sample-input/input.jsonl'
report_output_path = 'daily-report.html'
report_template_path = 'report-template.html'

# Auto-create input file if missing
if not os.path.exists(input_file_path):
    print(f"{input_file_path} not found. Creating sample file.")
    os.makedirs(os.path.dirname(input_file_path), exist_ok=True)
    with open(input_file_path, 'w') as f:
        sample_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": "signup",
            "user_id": "user123"
        }
        f.write(json.dumps(sample_data) + '\n')

# Load input data
events = []
with open(input_file_path, 'r') as f:
    for line in f:
        if line.strip():
            events.append(json.loads(line))

# Generate summary
summary = {}
for event in events:
    event_type = event.get("event_type", "unknown")
    summary[event_type] = summary.get(event_type, 0) + 1

# Load HTML template
with open(report_template_path, 'r') as f:
    html_template = f.read()

# Inject summary into template
report_date = datetime.utcnow().strftime('%Y-%m-%d')
report_body = f"<h2>Summary Report - {report_date}</h2><ul>"
for event_type, count in summary.items():
    report_body += f"<li>{event_type}: {count}</li>"
report_body += "</ul>"

final_report = html_template.replace("{{REPORT_BODY}}", report_body)

# Write report
with open(report_output_path, 'w') as f:
    f.write(final_report)

print(f"✅ Report generated at {report_output_path}")

