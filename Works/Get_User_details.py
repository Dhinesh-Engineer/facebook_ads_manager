#required Modules
import requests

app_id = '630290889236631'
app_secret = 'b2a408908120a8ce6ca57801c448991b'
access_token = ''


user_id = 'me' #can use "me" or user_id
graph_api_url = f'https://graph.facebook.com/v18.0/{user_id}'


fields = 'id,name,email'

params = {
    'fields': fields,
    'access_token': access_token
}

try:
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
except Exception as e:
    print(f"Error: {str(e)}")
