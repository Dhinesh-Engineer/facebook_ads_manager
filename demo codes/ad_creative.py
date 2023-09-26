from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

# Prompt for Facebook App credentials
app_id = input("Enter your app id: ")
app_secret = input("Enter your app secret id: ")
access_token = input("Enter your Facebook access token: ")
ad_account_id = input("Enter your ad account id: ")

# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)

# Define the Ad Creative fields and parameters
fields = []
params = {
    'name': 'Sample Promoted Post',
    'object_story_id': '132025263323078_122112781838031597',  # Replace with your Page ID and Post ID
}

# Create the Ad Creative within the Ad Set
ad_creative = AdAccount(ad_account_id).create_ad_creative(
    fields=fields,
    params=params,
)

# Print the created Ad Creative's ID
print("Ad Creative ID:", ad_creative.get_id())
