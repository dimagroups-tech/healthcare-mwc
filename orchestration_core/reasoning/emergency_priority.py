# reasoning/emergency_priority.py

EMERGENCY_KEYWORDS = [
    "emergency",
    "chest pain",
    "heart attack",
    "breathing problem",
    "unconscious",
    "severe bleeding",
    "stroke",
    "accident",
    "collapse"
]


def is_emergency(text: str) -> bool:
    """
    Detects whether the input indicates a medical emergency.
    Returns True or False.
    """

    if not text:
        return False

    text_lower = text.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text_lower:
            return True

    return False