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
campaign_id = input("Enter the ID of the campaign you want to update: ")

try:
    # Create an AdAccount object
    ad_account = AdAccount(ad_account_id)

    # Fetch the existing campaign by its ID
    campaign = Campaign(fbid=campaign_id)

    # Update campaign details
    campaign[Campaign.Field.name] = "Sales"
    campaign[Campaign.Field.status] = Campaign.Status.active  
    campaign.remote_update()  

    # Print updated campaign details
    print("Updated Campaign Details:")
    print(f"ID: {campaign.get_id()}")
    print(f"Name: {campaign.get(Campaign.Field.name)}")
    print(f"Status: {campaign.get(Campaign.Field.status)}")

    print("Campaign updated successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
