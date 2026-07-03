"""
Rule-Based Email Classification Engine
"""

from ai.keywords import KEYWORDS


def classify_email(subject, snippet, sender):
    """
    Classify email using keyword matching.

    Returns:
    {
        category,
        confidence,
        matched_keywords
    }
    """

    text = f"{subject} {snippet} {sender}".lower()

    best_category = "Others"
    highest_score = 0
    matched_keywords = []

    for category, keywords in KEYWORDS.items():

        current_matches = []

        for keyword in keywords:

            if keyword.lower() in text:
                current_matches.append(keyword)

        if len(current_matches) > highest_score:
            highest_score = len(current_matches)
            best_category = category
            matched_keywords = current_matches

    confidence = min(highest_score * 25, 100)

    return {
        "category": best_category,
        "confidence": confidence,
        "matched_keywords": matched_keywords
    }