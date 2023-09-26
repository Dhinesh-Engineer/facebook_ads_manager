from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.exceptions import FacebookRequestError

app_id = '630290889236631'
app_secret = 'b2a408908120a8ce6ca57801c448991b'
access_token = ''

# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)

# Specify your sandbox account ID
sandbox_account_id = '709905554489858'

# Define the special ad category 
special_ad_category = 'HOUSING'

# Define the campaign objective
campaign_objective = 'OUTCOME_LEADS'  

# Define campaign budget and schedule
campaign_budget = 10000  
campaign_start_date = '2023-10-01'  # Start date in YYYY-MM-DD format
campaign_end_date = '2023-10-31'  # End date in YYYY-MM-DD format

# Define bid strategy
bid_strategy = 'LOWEST_COST_WITHOUT_CAP'  

# Create a campaign in the sandbox account
try:
    ad_account = AdAccount(f'act_{sandbox_account_id}')
    campaign = ad_account.create_campaign(
        fields=[
            Campaign.Field.id,
            Campaign.Field.name,
            Campaign.Field.status,
            Campaign.Field.daily_budget,
            Campaign.Field.start_time,
            Campaign.Field.bid_strategy,
            # Add other campaign fields you want to retrieve here
        ],
        params={
            Campaign.Field.name: 'My Sandbox Campaign',
            Campaign.Field.status: Campaign.Status.paused,
            'special_ad_categories': [special_ad_category],
            'objective': campaign_objective,
            'daily_budget': campaign_budget,
            'start_time': campaign_start_date,
            'bid_strategy': bid_strategy,
        },
    )
    
    # Fetch and print campaign details
    campaign.api_get(fields=[
        Campaign.Field.id,
        Campaign.Field.name,
        Campaign.Field.status,
        Campaign.Field.daily_budget,
        Campaign.Field.start_time,
        Campaign.Field.bid_strategy,
    ])
    
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
