"""GET_linkedin_id
    inputs:
        oauth_token: you can generate your oauth token usuing the linkedin developer api
        trigger: a boolean toggle
    outputs:
        api_response: prints the entire api response 
        linkedin_id: prints only the id from the api response"""

# requirements: requests

import requests

def get_linkedin_response(oauth_token, trigger):
    if not trigger:
        return "Waiting for trigger...", None

    url = "https://api.linkedin.com/v2/userinfo"
    headers = {
        "Authorization": "Bearer " + oauth_token # authentication
    }

    response = requests.get(url, headers=headers)
    
    # get api response
    api_response = response.text
    
    # extract linkedin id (sub)
    response_data = response.json()
    linkedin_id = response_data.get("sub", "No ID found")
    
    return api_response, linkedin_id # return response and id

# outputs
api_response, linkedin_id = get_linkedin_response(oauth_token, trigger)
