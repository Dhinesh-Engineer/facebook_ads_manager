import logging
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adimage import AdImage

# Set up logging
logging.basicConfig(filename='facebook_ads.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')

# Set up your Facebook App credentials
app_id = input("Enter your app id: ")
app_secret = input("Enter your app secret id: ")
access_token = input("Enter your Facebook access token: ")

# Initialize the Facebook Ads API
try:
    FacebookAdsApi.init(app_id, app_secret, access_token)
except Exception as e:
    logging.error(f"Error initializing Facebook Ads API: {e}")

# Specify the ad account ID you want to work with
ad_account_id = input("Enter your ad_account_id: ")

# Specify the existing ad set ID where you want to create the ad
ad_set_id = input("Enter the Ad Set ID where you want to create the ad: ")

try:
    # Create an AdAccount object
    ad_account = AdAccount(ad_account_id)

    # Specify the image path (use forward slashes and a raw string)
    image_path = "G:\\OneYes\\First_Training_Task\\image.jpg"


    # Create an AdImage object and upload the image
    image = AdImage(parent_id=ad_account_id)
    with open(image_path, 'rb') as image_file:
        image[AdImage.Field.filename] = image_file
        image.remote_create()

    # Retrieve the image hash
    image_hash = image[AdImage.Field.hash]

    # Create an AdCreative using the retrieved image hash
    creative = AdCreative(parent_id=ad_account_id)
    creative[AdCreative.Field.name] = 'first ad'
    creative[AdCreative.Field.object_story_spec] = {
        'page_id': '132025263323078',
        'link_data': {
            'image_hash': image_hash,
            'link': 'www.google.com',
            'message': 'camera ads'
        }
    }
    creative.remote_create()

    # Create the ad within the existing ad set
    ad = Ad(parent_id=ad_account_id)
    ad[Ad.Field.name] = 'Camera ads'
    ad[Ad.Field.adset_id] = ad_set_id
    ad[Ad.Field.creative] = {'creative_id': creative[AdCreative.Field.id]}
    ad[Ad.Field.status] = 'ACTIVE'
    ad.remote_create()

    print(f"Ad '{ad[Ad.Field.name]}' has been created in Ad Set '{ad_set_id}'.")

except Exception as e:
    logging.error(f"An error occurred: {e}")
