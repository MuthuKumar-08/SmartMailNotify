from gmail.auth import authenticate
from gmail.gmail_reader import get_unread_emails
from database.db import create_database


def main():

    print("\n🚀 Starting SmartMail Notify...\n")

    create_database()

    creds = authenticate()

    print("✅ Gmail Authentication Successful!")

    get_unread_emails(creds)


if __name__ == "__main__":
    main()