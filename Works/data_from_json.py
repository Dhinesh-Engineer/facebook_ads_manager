import json

# Load data from the JSON file
with open('facebook_data.json', 'r') as json_file:
    data = json.load(json_file)

# Prompt the user to enter an ID
search_id = input("Enter an ID: ")

# Check if the "data" key exists in the JSON
if 'data' in data:
    found = False
    # Iterate through the list of dictionaries under "data"
    for entry in data['data']:
        if entry['id'] == search_id:
            found = True
            # Print all the data for the matching ID
            print(f"ID: {entry['id']}")
            print(f"Name: {entry['name']}")
            print(f"Audience Size Lower Bound: {entry['audience_size_lower_bound']}")
            print(f"Audience Size Upper Bound: {entry['audience_size_upper_bound']}")
            print(f"Path: {' -> '.join(entry['path'])}")
            print(f"Description: {entry['description']}")
            print(f"Topic: {entry['topic']}")
            break  # Stop searching once a match is found
    
    if not found:
        print(f"No data found for ID: {search_id}")
else:
    print("The 'data' field is not present in the JSON data.")
