from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet

# Set up your Facebook App credentials
app_id = input("Enter your app id: ")
app_secret = input("Enter your app secret id: ")
access_token = input("Enter your Facebook access token: ")

# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)

# Specify the ad account ID you want to work with
ad_account_id = input("Enter your ad_account_id: ")
ad_set_id = input("Enter the ad set ID: ")  # Specify the ad set ID

try:
    # Create an AdSet object
    ad_set = AdSet(ad_set_id)

    # Retrieve a list of ads in the ad set
    ads = ad_set.get_ads(fields=['id', 'name', 'status'])

    # Print the ad IDs
    print(f"Ads in Ad Set {ad_set_id}:")
    for ad in ads:
        print(f"ID: {ad['id']}")
        print(f"Name: {ad['name']}")
        print(f"Status: {ad['status']}")
        print()  

except Exception as e:
    print(f"An error occurred: {e}")
