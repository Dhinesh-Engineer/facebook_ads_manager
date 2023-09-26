# import logging
# import json
# from facebook_business.api import FacebookAdsApi
# from facebook_business.adobjects.adaccount import AdAccount

# # Set up logging
# logging.basicConfig(filename='facebook_ads.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')    

# # Set up your Facebook App credentials
# app_id = input("Enter your app id: ")
# app_secret = input("Enter your app secret id: ")
# access_token = input("Enter your Facebook access token: ")

# # Initialize the Facebook Ads API
# try:
#     FacebookAdsApi.init(app_id, app_secret, access_token)
# except Exception as e:
#     logging.error(f"Error initializing Facebook Ads API: {e}")

# # Specify the ad account ID you want to work with
# ad_account_id = input("Enter your ad_account_id: ")

# # Create an empty list to store campaign details
# campaign_details_list = []

# try:
#     # Create an AdAccount object
#     ad_account = AdAccount(ad_account_id)

#     # Retrieve a list of campaigns in the ad account
#     campaigns = ad_account.get_campaigns(fields=['id', 'name', 'status', 'start_time'])

#     # Loop through campaigns and collect campaign details
#     for campaign in campaigns:
#         campaign_details = {
#             "ID": campaign['id'],
#             "Name": campaign['name'],
#             "Status": campaign['status'],
#             "Start Time": campaign['start_time'],
#             "Ad Sets": []
#         }

#         # Retrieve ad sets within the campaign
#         adsets = campaign.get_ad_sets(fields=['id', 'name'])
#         for adset in adsets:
#             campaign_details["Ad Sets"].append({
#                 "ID": adset['id'],
#                 "Name": adset['name']
#             })

#         campaign_details_list.append(campaign_details)

# except Exception as e:
#     logging.error(f"An error occurred: {e}")

# # Write the campaign details to a JSON file
# with open('campaign_details.json', 'w') as json_file:
#     json.dump(campaign_details_list, json_file, indent=4)

# print("Campaign details have been saved to campaign_details.json.")









import logging
import json
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

# Create an empty list to store campaign details
campaign_details_list = []

try:
    # Create an AdAccount object
    ad_account = AdAccount(ad_account_id)

    # Retrieve a list of campaigns in the ad account
    campaigns = ad_account.get_campaigns(fields=['id', 'name', 'status', 'start_time', 'end_time', 'objective'])

    # Loop through campaigns and collect campaign details
    for campaign in campaigns:
        campaign_details = {
            "ID": campaign['id'],
            "Name": campaign['name'],
            "Status": campaign['status'],
            "Start Time": campaign['start_time'],
            "End Time": campaign.get('end_time', ''),
            "Objective": campaign.get('objective', ''),
            "Ad Sets": []
        }

        # Retrieve ad sets within the campaign
        adsets = campaign.get_ad_sets(fields=['id', 'name', 'status', 'start_time', 'end_time', 'daily_budget'])
        for adset in adsets:
            campaign_details["Ad Sets"].append({
                "ID": adset['id'],
                "Name": adset['name'],
                "Status": adset['status'],
                "Start Time": adset['start_time'],
                "End Time": adset.get('end_time', ''),
                "Daily Budget": adset.get('daily_budget', '')
            })

        campaign_details_list.append(campaign_details)

except Exception as e:
    logging.error(f"An error occurred: {e}")

# Write the campaign details to a JSON file
with open('campaign_details.json', 'w') as json_file:
    json.dump(campaign_details_list, json_file, indent=4)

print("Campaign details have been saved to campaign_details.json.")
