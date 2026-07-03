"""
Console output formatter for SmartMailNotify.
"""


def print_email(email, classification, priority, info):
    """
    Display formatted email details in the terminal.
    """

    print("\n" + "-" * 80)
    print("📧 New Email")
    print("-" * 80)

    print(f"👤 From       : {email['sender']}")
    print(f"📌 Subject    : {email['subject']}")
    print(f"🤖 Category   : {classification['category']}")
    print(f"🎯 Confidence : {classification['confidence']}%")
    print(f"⭐ Priority   : {priority['priority']}")
    print(f"📊 Score      : {priority['score']}")
    print(f"📝 Reasons    : {', '.join(priority['reasons']) if priority['reasons'] else 'None'}")
    print(f"🏢 Company    : {info['company'] or 'Not Found'}")
    print(f"📅 Deadline   : {info['deadline'] or 'Not Found'}")
    print(f"🔐 OTP        : {info['otp'] or 'Not Found'}")
    print(f"🔗 Links      : {len(info['links'])}")

    if info["links"]:
        print(f"🌐 First Link : {info['links'][0]}")
    print(f"🕒 Received   : {email['received_time']}")
    print(f"📄 Snippet    : {email['snippet']}")

    print("-" * 80)