import requests
import time

app_id = input("ENter the App Id: ")
app_secret = input("Enter the App_secret: ")
access_token = input("ENter the Access token: ")

user_id = 'me'  # can use "me" or user_id
graph_api_url = f'https://graph.facebook.com/v18.0/{user_id}'

fields = 'id,name,email'

params = {
    'fields': fields,
    'access_token': access_token
}

# Define the maximum number of retry attempts and initial delay
max_attempts = 5
initial_delay = 1  # 1 second

try:
    for attempt in range(1, max_attempts + 1):
        response = requests.get(graph_api_url, params=params)

        if response.status_code == 200:
            user_data = response.json()
            print("User Details:")
            print(f"Name: {user_data['name']}")
            print(f"ID: {user_data['id']}")
            if 'email' in user_data:
                print(f"Email: {user_data['email']}")
            break  # Successful request, exit the loop

        else:
            print(f"Attempt {attempt}: API request failed with status code {response.status_code}.")

            if attempt < max_attempts:
                # Calculate the next delay (exponential backoff)
                delay = initial_delay * (2 ** (attempt - 1))
                print(f"Attempt {attempt}: Waiting for {delay} seconds before retry...")
                time.sleep(delay)

except Exception as e:
    print(f"Error: {str(e)}")





# Basic Exponential Backoff:

# In the basic exponential backoff strategy, when a request or operation fails, the client waits for a fixed amount of time before retrying. If the second attempt also fails, the client waits for a longer fixed time, and so on.
# The waiting time between retries doubles with each consecutive failure, leading to an exponential increase in waiting time.
# For example:
# Attempt 1: Wait for 1 second
# Attempt 2: Wait for 2 seconds
# Attempt 3: Wait for 4 seconds
# And so on...