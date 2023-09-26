import requests
import json

# Replace with your access token and Page ID
access_token = input("Enter the access_token: ")
page_id = input("Enter the page_id: ")

# Define the endpoint URL to fetch posts
url = f'https://graph.facebook.com/v18.0/{page_id}/posts'

# Define query parameters, including the access token
params = {
    'access_token': access_token,
    'fields': 'id,message,created_time,likes.summary(true),comments.summary(true),shares',
    'limit': 100
}

try:
    # GET request to the Facebook Graph API
    response = requests.get(url, params=params)
    data = response.json()

    if 'data' in data:
        posts = data['data']
        
        # Create a list to store post data
        post_data_list = []
        
        for post in posts:
            post_id = post.get('id')
            message = post.get('message', 'No message')
            created_time = post.get('created_time')
            likes_count = post['likes']['summary']['total_count']
            comments_count = post['comments']['summary']['total_count']
            shares_count = post.get('shares', {}).get('count', 0)

            post_data = {
                "Post ID": post_id,
                "Message": message,
                "Created Time": created_time,
                "Likes Count": likes_count,
                "Comments Count": comments_count,
                "Shares Count": shares_count
            }

            post_data_list.append(post_data)

        # Write the post data to a JSON file
        with open('facebook_posts.json', 'w') as json_file:
            json.dump(post_data_list, json_file, indent=4)

        print("Data saved to 'facebook_posts.json' file.")

    else:
        print("No posts found.")

except Exception as e:
    print(f"An error occurred: {e}")
