"""
Priority Engine
"""

from ai.keywords import PRIORITY_RULES


def calculate_priority(subject, snippet, category):
    """
    Calculate email priority.
    """

    text = f"{subject} {snippet} {category}".lower()

    score = 0
    reasons = []

    # High priority
    for word in PRIORITY_RULES["High"]:
        if word.lower() in text:
            score += 5
            reasons.append(word)

    # Medium priority
    for word in PRIORITY_RULES["Medium"]:
        if word.lower() in text:
            score += 3
            reasons.append(word)

    # Low priority
    for word in PRIORITY_RULES["Low"]:
        if word.lower() in text:
            score -= 2

    if score >= 8:
        priority = "🔴 High"

    elif score >= 3:
        priority = "🟡 Medium"

    else:
        priority = "🟢 Low"

    return {
        "priority": priority,
        "score": score,
        "reasons": reasons
    }