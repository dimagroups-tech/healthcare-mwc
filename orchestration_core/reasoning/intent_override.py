# reasoning/intent_override.py

EMERGENCY_KEYWORDS = [
    "emergency",
    "urgent",
    "chest pain",
    "heart attack",
    "breathing problem",
    "unconscious",
    "accident",
    "bleeding",
    "severe pain"
]


def detect_intent_override(text: str):
    """
    Force intent override if strong emergency signals are detected.
    """
    text = text.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text:
            return "medical_emergency"

    return None
