from gmail.auth import authenticate
from gmail.service import process_emails
from database.db import create_database


def main():

    print("\n🚀 Starting SmartMail Notify...\n")

    create_database()

    creds = authenticate()

    print("✅ Gmail Authentication Successful!")

    process_emails(creds)


if __name__ == "__main__":
    main()