from database.repository import email_exists, save_email
from gmail.reader import get_messages
from gmail.parser import parse_email


def process_emails(creds):
    """
    Process unread Gmail messages.
    """

    service, messages = get_messages(creds)

    if not messages:
        print("\n✅ No unread emails found.")
        return

    print("\n" + "=" * 80)
    print("📬 SMARTMAIL NOTIFY - UNREAD EMAILS")
    print("=" * 80)

    for index, message in enumerate(messages, start=1):

        gmail_id = message["id"]

        msg = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=gmail_id,
                format="full"
            )
            .execute()
        )

        email = parse_email(msg, gmail_id)

        if email_exists(email["gmail_id"]):
            print(f"⏭ Skipping Email #{index} (Already Processed)")
            continue

        print("\n" + "-" * 80)
        print(f"📧 Email #{index}")
        print("-" * 80)
        print(f"👤 From      : {email['sender']}")
        print(f"📌 Subject   : {email['subject']}")
        print(f"🕒 Received  : {email['received_time']}")
        print(f"📄 Snippet   : {email['snippet']}")
        print("-" * 80)

        save_email(
            gmail_id=email["gmail_id"],
            sender=email["sender"],
            subject=email["subject"],
            received_time=email["received_time"]
        )