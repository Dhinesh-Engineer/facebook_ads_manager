import json
import logging


logging.basicConfig(filename='validation_failures.log', level=logging.INFO)


with open('facebook_posts.json', 'r') as json_file:
    data = json.load(json_file)


def validate_json_object(obj):
    required_fields = ["Post ID", "Message", "Created Time", "Likes Count", "Comments Count", "Shares Count"]
    for field in required_fields:
        if field not in obj:
            logging.error(f"Missing required field '{field}' in JSON object:\n{obj}")
            return False

    #numeric fields
    numeric_fields = ["Likes Count", "Comments Count", "Shares Count"]
    for field in numeric_fields:
        if not isinstance(obj[field], (int, float)):
            logging.error(f"Invalid numeric value in field '{field}' in JSON object:\n{obj}")
            return False
    
    logging.info(f"Validation successful for JSON object:\n{obj}")    
    return True

for obj in data:
    if not validate_json_object(obj):
        pass
