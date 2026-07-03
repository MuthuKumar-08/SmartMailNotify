from database.repository import email_exists, save_email
from gmail.reader import get_messages
from gmail.parser import parse_email
from ai.classifier import classify_email
from ai.priority import calculate_priority
from ai.extractor import extract_information
from utils.formatter import print_email
from ai.gemini_client import generate_summary
from ai.decision import should_notify
from whatsapp.sender import send_whatsapp_message

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
        classification = classify_email(
        email["subject"],
        email["snippet"],
        email["sender"]
        )
        category = classification["category"]
        priority = calculate_priority(
    email["subject"],
    email["snippet"],
    category
)
        info = extract_information(
    email["subject"],
    email["snippet"]
)
        summary = generate_summary(
    email["subject"],
    email["snippet"]
)
        decision = should_notify(
    category,
    priority["priority"]
)

        print_email(
    email=email,
    classification=classification,
    priority=priority,
    info=info
)
        print(f"🧠 AI Summary : {summary}")
        print(f"📲 Notify    : {'✅ YES' if decision['notify'] else '❌ NO'}")
        print(f"📝 Reason    : {decision['reason']}")
        
        if decision["notify"]:

            whatsapp_email = {
                "sender": email["sender"],
                "subject": email["subject"],
                "category": category,
                "priority": priority["priority"]
            }

            send_whatsapp_message(
                "+919442872844",
                whatsapp_email,
                summary
            )

        print(
            f"🔍 Matched   : "
            f"{', '.join(classification['matched_keywords']) if classification['matched_keywords'] else 'None'}"
        )
        
        save_email(
        gmail_id=email["gmail_id"],
        sender=email["sender"],
        subject=email["subject"],
        received_time=email["received_time"],
        category=category
        )