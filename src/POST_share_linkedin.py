"""POST_share_linkedin
    inputs:
        linkedin_id: the id output from the previous get request
        oauth_token: same token as the get request
        post_content: whatever you want to post (should be a string)
        trigger: a boolean toggle
    outputs:
        api_response: prints the entire api response"""

# requirements: requests

import requests
import json

def post_linkedin_update(linkedin_id, oauth_token, post_content, trigger):
    if not trigger:
        return "Waiting for trigger..."

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": "Bearer " + oauth_token,
        "Content-Type": "application/json"
    }

    # Ensure the linkedin_id is correctly formatted as a URN
    linkedin_id = "urn:li:person:" + linkedin_id

    # Create the JSON payload
    payload = {
        "author": linkedin_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": post_content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Return the response text
    return response.text

# Outputs
api_response = post_linkedin_update(linkedin_id, oauth_token, post_content, trigger)
