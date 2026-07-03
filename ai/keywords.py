"""
Keyword database for email classification.
"""

KEYWORDS = {

    "Placement": [
        "internship",
        "career",
        "job",
        "hiring",
        "campus",
        "placement",
        "recruitment",
        "interview",
        "cisco",
        "tcs",
        "infosys",
        "zoho",
        "microsoft",
        "google",
        "amazon"
    ],

    "College": [
        "assignment",
        "exam",
        "semester",
        "attendance",
        "faculty",
        "ssn",
        "department",
        "class",
        "course",
        "project"
    ],

    "OTP": [
        "otp",
        "verification code",
        "one time password",
        "login code",
        "security code"
    ],

    "Banking": [
        "bank",
        "transaction",
        "credited",
        "debited",
        "upi",
        "account",
        "statement"
    ],

    "Shopping": [
        "order",
        "amazon",
        "flipkart",
        "delivery",
        "shipment",
        "discount",
        "sale",
        "offer"
    ],

    "Learning": [
        "coursera",
        "edx",
        "udemy",
        "leetcode",
        "nptel",
        "course"
    ],

    "Promotions": [
        "unsubscribe",
        "offer",
        "sale",
        "discount",
        "limited time",
        "newsletter"
    ]
}
PRIORITY_RULES = {

    "High": [
        "internship",
        "placement",
        "interview",
        "deadline",
        "urgent",
        "otp",
        "verification",
        "security code",
        "exam",
        "payment due"
    ],

    "Medium": [
        "assignment",
        "course",
        "project",
        "meeting",
        "class",
        "attendance",
        "submission",
        "bank"
    ],

    "Low": [
        "offer",
        "sale",
        "discount",
        "newsletter",
        "promotion",
        "subscribe"
    ]
}