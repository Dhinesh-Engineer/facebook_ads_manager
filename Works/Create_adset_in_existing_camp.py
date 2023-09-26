from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

# Set up your Facebook App credentials
app_id = input("Enter your app id: ")
app_secret = input("Enter your app secret id: ")
access_token = input("Enter your Facebook access token: ")

# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)
ad_account_id = input("Enter your Facebook Ad Account ID: ")

# Initialize your Ad Account with the user-provided Ad Account ID
my_adaccount = AdAccount(ad_account_id)

def create_ad_set(name, campaign_id, optimization_goal, status, daily_budget, billing_event, targeting, bid_strategy):
    params = {
        'name': name,
        'campaign_id': campaign_id,
        'optimization_goal': optimization_goal,
        'status': status,
        'daily_budget': daily_budget,
        'billing_event': billing_event,
        'targeting': targeting,
        'bid_strategy': bid_strategy
    }
    try:
        response = my_adaccount.create_ad_set(params=params)
        print("Ad Set created successfully. ID:", response['id'])
    except Exception as e:
        print("Error:", e)

# Prompt the user for the campaign ID
campaign_id = input("Enter the Campaign ID: ")

# Add input validation for the campaign ID
while not campaign_id.isdigit():
    print("Campaign ID must be a numeric value.")
    campaign_id = input("Enter the Campaign ID: ")

targeting = {
    'geo_locations': {
        'countries': ['IN'],  # 'IN' for india
    },
}

#  create_ad_set function  
create_ad_set(
    name='Ad Set 2',
    campaign_id=campaign_id,
    optimization_goal='LINK_CLICKS',  
    status='ACTIVE',                 
    daily_budget=10000,               
    billing_event='IMPRESSIONS',     
    targeting=targeting,                    
    bid_strategy='LOWEST_COST_WITHOUT_CAP'  
)
