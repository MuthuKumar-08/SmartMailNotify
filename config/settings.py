"""
Application configuration.

All project settings should live here.
"""

# Gmail API
GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

# Gmail Search
EMAIL_QUERY = "is:unread"

# Number of emails to fetch
MAX_EMAILS = 10

# SQLite Database
DATABASE_NAME = "database/smartmail.db"