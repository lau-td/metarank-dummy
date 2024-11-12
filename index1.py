import json
from datetime import datetime

def convert_to_metarank_format(input_data):
    # Convert timestamp to metarank format
    timestamp = datetime.fromisoformat(input_data['created_at'].replace('Z', '+00:00')).timestamp() * 1000
    
    # Create the base fields list with required fields
    fields = [
        {"name": "first_name", "value": input_data['first_name']},
        {"name": "last_name", "value": input_data['last_name']},
        # {"name": "email", "value": input_data['email']},
        # {"name": "location", "value": input_data['location_id']},
        {"name": "gender", "value": input_data['gender']},
        {"name": "status", "value": input_data['status']},
        {"name": "is_remote", "value": input_data['is_remote']},
        {"name": "data_source", "value": input_data['data_source']},
        {"name": "search_vector", "value": input_data['search_vector']}
    ]
    
    # Add optional fields if they exist and are not None
    optional_fields = {
        'linkedin': 'linkedin',
        'open_to_work': 'open_to_work',
        'profile_created': 'profile_created'
    }
    
    for field_name, json_key in optional_fields.items():
        if json_key in input_data and input_data[json_key] is not None:
            fields.append({"name": field_name, "value": input_data[json_key]})
    
    # Create the metarank format
    metarank_format = {
        "event": "item",
        "id": input_data['id'],
        "timestamp": str(int(timestamp)),
        "item": f"item{hash(input_data['id']) % 1000}", # Generate a simple item ID
        "fields": fields
    }
    
    return metarank_format

# Example usage:
def convert_json_file(input_file, output_file):
    with open(input_file, 'r') as f:
        input_data = json.load(f)
    
    # Handle both single object and list of objects
    if not isinstance(input_data, list):
        input_data = [input_data]
    
    # Convert all items and sort by timestamp
    metarank_items = [convert_to_metarank_format(item) for item in input_data]
    metarank_items.sort(key=lambda x: int(x['timestamp']))
    
    with open(output_file, 'w') as f:
        for item in metarank_items:
            f.write(json.dumps(item) + '\n')

# Usage:
convert_json_file('./codelight/candidates.json', './codelight/candidates.jsonl')