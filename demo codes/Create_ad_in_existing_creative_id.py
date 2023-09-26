from facebook_business.exceptions import FacebookRequestError
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad

# Set your Facebook App credentials and access token here
app_id = '630290889236631'
app_secret = 'b2a408908120a8ce6ca57801c448991b'
access_token = ''
ad_account_id = ''

# Initialize the Facebook API client
from facebook_business.api import FacebookAdsApi
FacebookAdsApi.init(app_id, app_secret, access_token)

try:
    # Assuming you have an existing ad creative or post ID
    existing_ad_creative_id = '132025263323078'

    fields = []
    params = {
        'name': 'sale',
        'adset_id': '120330000399227914',
        'creative': {'creative_id': existing_ad_creative_id},
        'status': 'ACTIVE'
    }

    # Create the ad using the existing creative or post
    AdAccount(ad_account_id).create_ad(fields=fields, params=params)

    print("Your ad has been successfully created!")

except FacebookRequestError as e:
    print(f"Facebook API Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
