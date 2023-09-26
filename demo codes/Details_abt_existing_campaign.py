from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.exceptions import FacebookRequestError

# Set up your Facebook App credentials
app_id = '630290889236631'
app_secret = 'b2a408908120a8ce6ca57801c448991b'
access_token = ''

# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)

# Specify your sandbox account ID
sandbox_account_id = '709905554489858'
# Specify the Campaign ID of the campaign you want to retrieve details for
campaign_id = input("Campaign ID")

try:
    # Fetch the campaign details
    campaign = Campaign(campaign_id)
    campaign.api_get(fields=[
        Campaign.Field.id,
        Campaign.Field.name,
        Campaign.Field.status,
        Campaign.Field.daily_budget,
        Campaign.Field.start_time,
        Campaign.Field.bid_strategy,
        # Add other campaign fields you want to display here
    ])
    
    # Print campaign details
    print("Campaign Details:")
    print(f"ID: {campaign[Campaign.Field.id]}")
    print(f"Name: {campaign[Campaign.Field.name]}")
    print(f"Status: {campaign[Campaign.Field.status]}")
    print(f"Daily Budget: {campaign[Campaign.Field.daily_budget]}")
    print(f"Start Date: {campaign[Campaign.Field.start_time]}")
    print(f"Bid Strategy: {campaign[Campaign.Field.bid_strategy]}")
    # Print other campaign fields as needed
    
except FacebookRequestError as e:
    print(f"Error: {e}")
