from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative

# Set up your Facebook App credentials
app_id = input("Enter your app id: ")
app_secret = input("Enter your app secret id: ")
access_token = input("Enter your Facebook access token: ")

# Initialize the Facebook Ads API
FacebookAdsApi.init(app_id, app_secret, access_token)

# Specify the ad account ID you want to work with
ad_account_id = input("Enter your ad_account_id: ")

try:
    # Create an AdAccount object
    ad_account = AdAccount(ad_account_id)

    # Create a new campaign with an objective
    campaign = Campaign(parent_id=ad_account_id)
    campaign[Campaign.Field.name] = "My Campaign"
    campaign[Campaign.Field.status] = Campaign.Status.active
    campaign[Campaign.Field.special_ad_categories] = []  
    campaign[Campaign.Field.objective] = "OUTCOME_TRAFFIC"  
    campaign.remote_create()  

    # Create an AdSet
    ad_set = AdSet(parent_id=ad_account_id)
    ad_set[AdSet.Field.name] = "My AdSet"
    ad_set[AdSet.Field.campaign_id] = campaign.get_id()
    ad_set[AdSet.Field.daily_budget] = 10000
    ad_set[AdSet.Field.billing_event] = AdSet.BillingEvent.impressions
    ad_set[AdSet.Field.optimization_goal] = AdSet.OptimizationGoal.impressions
    ad_set[AdSet.Field.bid_strategy] = AdSet.BidStrategy.lowest_cost_with_bid_cap
    ad_set[AdSet.Field.bid_amount] = 10
    ad_set[AdSet.Field.targeting] = {
        'geo_locations': {'countries': ['IN']},
        'age_min': 18,
        'age_max': 65,
        # Add more targeting options as needed
    }
    ad_set.remote_create(params={'status': 'ACTIVE'})

    
    # Print campaign details
    print("Campaign Details:")
    print(f"ID: {campaign.get_id()}")
    print(f"Name: {campaign.get(Campaign.Field.name)}")
    print(f"Status: {campaign.get(Campaign.Field.status)}")
    print(f"Objective: {campaign.get(Campaign.Field.objective)}")
    
    # Print other campaign fields as needed


    print("Campaign, AdSet created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
