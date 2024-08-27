# GH_PostToLinkedin
**Make a post on LinkedIn only using Grasshopper**

![](assets/script.png)

## Requirements ##
  - Rhinoceros 8
  - A LinkedIn Developer account to obtain OAuth tokens

## LinkedIn API Prerequisites ##
Before you can use this script, you'll need to set up a LinkedIn Developer application to obtain your OAuth token. Follow these steps:
  1. Create a LinkedIn Developer Account: Go to [LinkedIn Developers](https://www.linkedin.com/developers/) and create an account.
  2. Create a New App: Register a new application under your LinkedIn Developer account.
  3. Set Up OAuth: Using OAuth 2.0 Tools, configure a new access token, and ensure that you have the `openid`, `profile`, `w_member_social` and `email` scope enabled to allow posting on behalf of the user.
