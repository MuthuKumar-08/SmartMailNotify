"""
Application configuration.
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ----------------------------
# Gmail API
# ----------------------------

GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

EMAIL_QUERY = "is:unread"
MAX_EMAILS = 10

# ----------------------------
# Database
# ----------------------------

DATABASE_NAME = "database/smartmail.db"

# ----------------------------
# Gemini AI
# ----------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")