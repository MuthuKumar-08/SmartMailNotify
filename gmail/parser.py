from datetime import datetime
from zoneinfo import ZoneInfo


def parse_email(message, gmail_id):
    """
    Convert Gmail API response into a Python dictionary.
    """

    headers = message.get("payload", {}).get("headers", [])

    sender = "Unknown"
    subject = "No Subject"

    for header in headers:

        name = header["name"].lower()

        if name == "from":
            sender = header["value"]

        elif name == "subject":
            subject = header["value"]

    try:

        timestamp = int(message["internalDate"]) / 1000

        india_time = datetime.fromtimestamp(
            timestamp,
            tz=ZoneInfo("Asia/Kolkata")
        )

        received_time = india_time.strftime("%d-%m-%Y %I:%M:%S %p")

    except Exception:

        received_time = "Unknown"

    snippet = message.get("snippet", "No Preview Available")

    return {
        "gmail_id": gmail_id,
        "sender": sender,
        "subject": subject,
        "received_time": received_time,
        "snippet": snippet
    }