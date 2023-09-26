from facebook_business.exceptions import FacebookRequestError
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adimage import AdImage

# Set your Facebook App credentials and access token here
app_id = '630290889236631'
app_secret = 'b2a408908120a8ce6ca57801c448991b'
access_token = ''
ad_account_id = ''
page_id = '132025263323078'

# Initialize the Facebook API client
from facebook_business.api import FacebookAdsApi
FacebookAdsApi.init(app_id, app_secret, access_token)

try:
    # Upload an image for the Ad
    image = AdImage(parent_id=ad_account_id)
    image[AdImage.Field.filename] = 'image.jpg'  # Replace with the actual image path
    image.remote_create()
    image_hash = image[AdImage.Field.hash]

    # Create an Ad Creative
    fields = []
    params = {
        'name': 'cAMERA',
        'object_story_spec': {
            'page_id': page_id,
            'link_data': {
                'image_hash': image_hash,
                'link': 'https://www.facebook.com/',  # Replace with your page URL
                'message': 'sALE'
            }
        }
    }
    adcreative = AdAccount(ad_account_id).create_ad_creative(fields=fields, params=params)

    # Create the Facebook Ad
    fields = []
    params = {
        'name': 'Bag sale',
        'adset_id': '120330000399227914',  # Replace with your ad set ID
        'creative': {'creative_id': adcreative['creative_id']},
        'status': 'ACTIVE'
    }
    AdAccount(ad_account_id).create_ad(fields=fields, params=params)

    print("Your ad has been successfully created!")

except FacebookRequestError as e:
    print(f"Facebook API Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
