"""
Decision Engine
"""


def should_notify(category, priority):
    """
    Decide whether an email should be sent to WhatsApp.
    """

    if priority == "🔴 High":
        return {
            "notify": True,
            "reason": "High priority email"
        }

    if category in ["OTP", "Banking"]:
        return {
            "notify": True,
            "reason": "Important security email"
        }

    return {
        "notify": False,
        "reason": "Low priority email"
    }