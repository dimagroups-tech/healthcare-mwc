# reasoning/emergency_escalation.py

EMERGENCY_KEYWORDS = [
    "emergency",
    "urgent",
    "immediately",
    "severe",
    "unconscious",
    "bleeding",
    "heart attack",
    "chest pain",
    "stroke",
    "accident",
    "not breathing",
]


def should_escalate(text: str, filters=None) -> bool:
    """
    Decide whether this request requires emergency escalation.
    Works only for routing priority — NOT diagnosis.
    """

    text_lower = text.lower()

    # Explicit emergency keyword
    for word in EMERGENCY_KEYWORDS:
        if word in text_lower:
            return True

    # Emergency filter already applied
    if filters and filters.get("emergency"):
        return True

    return False