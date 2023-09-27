import requests

page_id = input("Enter the Page Id: ")
page_access_token = input("Enter the access token: ")
message = input("Enter the Message to be posted: ")

# image file path
image_path = input("Enter the path to the image file: ")

# API url
url = f"https://graph.facebook.com/{page_id}/photos"

# POST request
params = {
    "message": message,
    "access_token": page_access_token,
}


with open(image_path, "rb") as image_file:
    files = {
        "source": image_file,
    }

    # POST request 
    response = requests.post(url, data=params, files=files)


if response.status_code == 200:
    print("Image posted successfully to Page")
else:
    print("Error posting image to Page:", response.text)
