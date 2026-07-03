from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import json
# Permission to read Gmail
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
def create_secret_files():
    """
    Create credentials.json and token.json from Railway variables
    if they do not already exist.
    """

    credentials = os.getenv("CREDENTIALS_JSON")
    token = os.getenv("TOKEN_JSON")

    if credentials and not os.path.exists("credentials.json"):
        with open("credentials.json", "w") as f:
            f.write(credentials)

    if token and not os.path.exists("token.json"):
        with open("token.json", "w") as f:
            f.write(token)

def authenticate():
    create_secret_files()
    creds = None

    # Load existing token if available
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no valid credentials, let the user log in.
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds