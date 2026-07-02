from googleapiclient.discovery import build
from config.settings import EMAIL_QUERY, MAX_EMAILS


def get_messages(creds):
    """
    Fetch unread email references from Gmail.
    """

    service = build("gmail", "v1", credentials=creds)

    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            labelIds=["INBOX"],
            q=EMAIL_QUERY,
            maxResults=MAX_EMAILS,
        )
        .execute()
    )

    return service, results.get("messages", [])