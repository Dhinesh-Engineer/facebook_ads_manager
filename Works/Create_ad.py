from facebook_business.adobjects.adimage import AdImage
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi

# Set your Facebook App credentials and access token here
app_id = '630290889236631'
app_secret = 'b2a408908120a8ce6ca57801c448991b'
access_token = ''
ad_account_id = ''
page_id = '132025263323078'
# Initialize the Facebook API client
FacebookAdsApi.init(app_id, app_secret, access_token)

try:
    # Upload the image and obtain the image_hash
    image = AdImage(parent_id=ad_account_id)
    image[AdImage.Field.filename] = 'image.jpg'  # Corrected image path
    image.remote_create()
    image_hash = image[AdImage.Field.hash]

    print(f"Image Hash: {image_hash}")

    # Create an ad creative using the obtained image_hash
    ad_creative = AdCreative(parent_id=ad_account_id)
    ad_creative[AdCreative.Field.name] = 'Name'
    ad_creative[AdCreative.Field.object_story_spec] = {
        'page_id': page_id,
        'link_data': {
            'image_hash': image_hash,
            'link': 'https://www.facebook.com/',
            'message': 'welcome to sale'
        }
    }
    ad_creative.remote_create()

    # Get the creative ID
    creative_id = ad_creative.get_id()

    # Create an ad using the created creative
    fields = []
    params = {
        'name': 'bag Ad',
        'adset_id': '120330000399227914',
        'creative': {'creative_id': creative_id},
        'status': 'ACTIVE'
    }

    AdAccount(ad_account_id).create_ad(fields=fields, params=params)

    print("Your ad has been successfully created!")

except Exception as e:
    print(f"An error occurred: {e}")
