"""
Extract useful information from emails.
"""

import re

COMPANIES = [
    "Cisco",
    "Google",
    "Microsoft",
    "Amazon",
    "TCS",
    "Infosys",
    "Zoho",
    "Wipro",
    "Accenture",
    "Cognizant",
    "Capgemini"
]


def extract_information(subject, snippet):
    """
    Extract company, links, OTP and deadline.
    """

    text = f"{subject} {snippet}"

    company = None

    for name in COMPANIES:
        if name.lower() in text.lower():
            company = name
            break

    otp = None

    otp_match = re.search(r"\b\d{4,8}\b", text)

    if otp_match:
        otp = otp_match.group()

    deadline = None

    deadline_match = re.search(
        r"\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|June|July|August|September|October|November|December)\b",
        text,
        re.IGNORECASE
    )

    if deadline_match:
        deadline = deadline_match.group()

    links = re.findall(r"https?://\S+", text)

    return {
        "company": company,
        "deadline": deadline,
        "otp": otp,
        "links": links
    }