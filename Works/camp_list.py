import logging
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

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

try:
    # Create an AdAccount object
    ad_account = AdAccount(ad_account_id)

    # Retrieve a list of campaigns in the ad account
    campaigns = ad_account.get_campaigns(fields=['id', 'name', 'status', 'start_time'])

    # Print the campaign details
    print("Campaigns in Ad Account:")
    for campaign in campaigns:
        print(f"ID: {campaign['id']}")
        print(f"Name: {campaign['name']}")
        print(f"Status: {campaign['status']}")
        print(f"Start Time: {campaign['start_time']}")
        
        

        # Retrieve ad sets within the campaign
        adsets = campaign.get_ad_sets(fields=['id', 'name'])
        print("Ad Sets:")
        for adset in adsets:
            print(f"  - ID: {adset['id']}")
            print(f"    Name: {adset['name']}")


        # Print a line break between campaigns
        print()

except Exception as e:
    logging.error(f"An error occurred: {e}")



"""https://graph.facebook.com/v18.0/act_709905554489858/campaigns?fields=id,name,status,start_time,adsets{id,name},ads{id,name}&access_token="""