from gmail.auth import authenticate
from gmail.gmail_reader import get_unread_emails


def main():

    print("\n🚀 Starting SmartMail Notify...\n")

    creds = authenticate()

    print("✅ Gmail Authentication Successful!")

    get_unread_emails(creds)


if __name__ == "__main__":
    main()