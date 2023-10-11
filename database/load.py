import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['fb_manager']  
collection = db['post']  

json_file_path = 'facebook_posts.json'  

with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

result = collection.insert_many(data)

print(f"Inserted {len(result.inserted_ids)} documents")
