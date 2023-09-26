from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adset import AdSet

#Set up your Facebook App credentials
app_id = '630290889236631'
app_secret = 'b2a408908120a8ce6ca57801c448991b'
access_token = ''
# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)

# Specify the sandbox account ID
sandbox_account_id = '709905554489858'  

# Define ad set parameters
ad_set_params = {
    AdSet.Field.name: 'My Ad Set',
    AdSet.Field.campaign_id: 'CAMPAIGN_ID',  
    AdSet.Field.daily_budget: 1000,  
    AdSet.Field.bid_strategy: 'LOWEST_COST_WITHOUT_CAP',
    # Add other ad set parameters as needed
} 


# Create the ad set within the specified campaign
ad_set = AdSet(f'act_{sandbox_account_id}').create(params=ad_set_params)

print(f"Created Ad Set ID: {ad_set['id']}")



