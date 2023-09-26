from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

# Set up your Facebook App credentials
app_id = input("Enter your app id: ")
app_secret = input("Enter your app secret id: ")
access_token = input("Enter your Facebook access token: ")

# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)

# Specify the ad account ID you want to work with
ad_account_id = input("Enter your ad_account_id: ")
campaign_id = input("Enter the campaign ID: ")  # Specify the campaign ID

try:
    # Create a Campaign object
    campaign = Campaign(campaign_id)

    # Retrieve a list of ad sets in the campaign
    ad_sets = campaign.get_ad_sets(fields=['id', 'name', 'status'])

    # Print the ad set details
    print(f"Ad Sets in Campaign {campaign_id}:")
    for ad_set in ad_sets:
        print(f"ID: {ad_set['id']}")
        print(f"Name: {ad_set['name']}")
        print(f"Status: {ad_set['status']}")
        print()  # Add a line break between ad sets

except Exception as e:
    print(f"An error occurred: {e}")
