import requests

page_id = input("Enter the Page Id :") 
page_access_token = input("Enter the access token :")  

message = input("Enter the Message to be posted:")

# API URL
url = f"https://graph.facebook.com/{page_id}/feed"

# Define the parameters for the POST request
params = {
    "message": message,
    "access_token": page_access_token,
}

# POST request 
response = requests.post(url, params=params)

# Check the response status code and handle errors
if response.status_code == 200:
    print("Message posted successfully to Page")
else:
    print("Error posting message to Page:", response.json())
