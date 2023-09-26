import requests

# Replace with your access token and Page ID
access_token = ''
page_id = '132025263323078'

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
        for post in posts:
            post_id = post.get('id')
            message = post.get('message', 'No message')
            created_time = post.get('created_time')
            likes_count = post['likes']['summary']['total_count']
            comments_count = post['comments']['summary']['total_count']
            shares_count = post.get('shares', {}).get('count', 0)

            print(f"Post ID: {post_id}")
            print(f"Message: {message}")
            print(f"Created Time: {created_time}")
            print(f"Likes Count: {likes_count}")
            print(f"Comments Count: {comments_count}")
            print(f"Shares Count: {shares_count}")
            print("\n")

    else:
        print("No posts found.")

except Exception as e:
    print(f"An error occurred: {e}")
