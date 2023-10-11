import requests
import time

app_id = input("ENter the App Id: ")
app_secret = input("Enter the App_secret: ")
access_token = input("ENter the Access token: ")


user_id = 'me'  # You can use "me" or a user_id
graph_api_url = f'https://graph.facebook.com/v18.0/{user_id}'

fields = 'id,name,email'

params = {
    'fields': fields,
    'access_token': access_token
}

# Define the rate limit and time interval (requests per minute)
rate_limit = 10
time_interval = 3  # 60 seconds

try:
    for _ in range(rate_limit):
        response = requests.get(graph_api_url, params=params)

        if response.status_code == 200:
            user_data = response.json()
            print("User Details:")
            print(f"Name: {user_data['name']}")
            print(f"ID: {user_data['id']}")
            if 'email' in user_data:
                print(f"Email: {user_data['email']}")
        else:
            print(f"Error: Unable to fetch user data. Status code: {response.status_code}")

        # Introduce a delay to respect the rate limit
        time.sleep(time_interval)
except Exception as e:
    print(f"Error: {str(e)}")
