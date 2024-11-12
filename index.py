import json

# Read the input JSON file
with open('/Users/codelight/Downloads/candidates_202411111436.json', 'r') as f:
    data = json.load(f)

# Write to JSONL format
output_path = '/Users/codelight/Downloads/candidates_202411111436.jsonl'
with open(output_path, 'w') as f:
    for item in data:
        json_line = json.dumps(item)
        f.write(json_line + '\n')