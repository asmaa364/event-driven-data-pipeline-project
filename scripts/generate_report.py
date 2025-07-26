import json
import sys

input_file = sys.argv[1]
template_file = sys.argv[2]

with open(input_file) as f:
    events = json.load(f)

with open(template_file) as f:
    template = f.read()

output = template.replace("{{ event_count }}", str(len(events)))

print(output)
