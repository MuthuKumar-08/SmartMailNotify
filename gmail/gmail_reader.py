from datetime import datetime
from zoneinfo import ZoneInfo

from googleapiclient.discovery import build


def get_unread_emails(creds):
    """
    Fetch unread emails from Gmail and display
    Sender, Subject, Received Time and Snippet.
    """

    # Build Gmail service
    service = build("gmail", "v1", credentials=creds)

    # Fetch only unread emails
    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            labelIds=["INBOX"],
            q="is:unread",
            maxResults=10,
        )
        .execute()
    )

    messages = results.get("messages", [])

    if not messages:
        print("\n✅ No unread emails found.")
        return

    print("\n" + "=" * 80)
    print("📬 SMARTMAIL NOTIFY - UNREAD EMAILS")
    print("=" * 80)

    for index, message in enumerate(messages, start=1):

        # Get complete email details
        msg = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=message["id"],
                format="full",
            )
            .execute()
        )
        

        headers = msg.get("payload", {}).get("headers", [])

        sender = "Unknown"
        subject = "No Subject"

        # Extract required headers
        for header in headers:

            name = header["name"].lower()

            if name == "from":
                sender = header["value"]

            elif name == "subject":
                subject = header["value"]

        # Gmail's received timestamp (milliseconds since Unix epoch)
        try:
            
            timestamp = int(msg["internalDate"]) / 1000
            india_time = datetime.fromtimestamp(timestamp,tz=ZoneInfo("Asia/Kolkata"))
            received_time = india_time.strftime("%d-%m-%Y %I:%M:%S %p")

        except Exception as e:
            print(f"Time conversion error: {e}")
            received_time = "Unknown"

        print("\n" + "-" * 80)
        snippet = msg.get("snippet", "No Preview Available")
        print(f"📧 Email #{index}")
        print("-" * 80)
        print(f"👤 From      : {sender}")
        print(f"📌 Subject   : {subject}")
        print(f"🕒 Received  : {received_time}")
        print(f"📄 Snippet   : {snippet}")
        print("-" * 80)