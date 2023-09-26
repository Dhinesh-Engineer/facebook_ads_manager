import requests
import json
import logging

# Configure logging
logging.basicConfig(filename='data_fetching.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Get user input for the search query and access token
    search_query = input("Enter the search query (e.g., fitness): ")
    access_token = input("Enter your Facebook access token: ")

    # Define the URL with user input
    url = f'https://graph.facebook.com/search?type=adinterest&q=[{search_query}]&limit=100&access_token={access_token}'

    # Make an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Print the JSON data (optional)
        print(json.dumps(data, indent=4))

        # Store the JSON data in a file
        with open('facebook_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print("Data stored in 'facebook_data.json'")

    else:
        # Log the error
        logging.error(f"Failed to fetch data. Status code: {response.status_code}")

except Exception as e:
    # Handle and log any exceptions that occur
    logging.error(f"An error occurred: {str(e)}")

