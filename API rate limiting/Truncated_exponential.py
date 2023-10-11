import requests
import time

app_id = input("Enter the App Id: ")
app_secret = input("Enter the App_secret: ")
access_token = input("Enter the Access token: ")

user_id = 'me'  
graph_api_url = f'https://graph.facebook.com/v18.0/{user_id}'

fields = 'id,name,email'

params = {
    'fields': fields,
    'access_token': access_token
}

max_attempts = 5
initial_delay = 1  
max_delay = 5  

try:
    consecutive_failures = 0  # Track consecutive failures

    for attempt in range(1, max_attempts + 1):
        response = requests.get(graph_api_url, params=params)

        if response.status_code == 200:
            user_data = response.json()
            print("User Details:")
            print(f"Name: {user_data['name']}")
            print(f"ID: {user_data['id']}")
            if 'email' in user_data:
                print(f"Email: {user_data['email']}")
            break 

        else:
            
            consecutive_failures += 1
            print(f"Attempt {attempt}: API request failed with status code {response.status_code}.")

            if attempt < max_attempts:
                if consecutive_failures >= 4:
                    delay = max_delay
                else:
                    delay = initial_delay * (2 ** (consecutive_failures - 1))

                print(f"Attempt {attempt}: Waiting for {delay} seconds before retry...")
                time.sleep(delay)

except Exception as e:
    print(f"Error: {str(e)}")




















# Truncated exponential backoff limits the maximum waiting time between retries. After a certain number of consecutive failures, the waiting time no longer doubles but remains constant.
# This approach balances the desire to wait for a longer time to reduce server load with the need for timely retries.
# For example:
# Attempt 1: Wait for 1 second
# Attempt 2: Wait for 2 seconds
# Attempt 3: Wait for 4 seconds
# Attempt 4 and beyond: Wait for 5 seconds (constant waiting time)