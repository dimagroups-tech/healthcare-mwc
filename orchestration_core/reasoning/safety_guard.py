# reasoning/safety_guard.py

"""
Safety guard to block diagnosis / medical advice requests.
Allows emergency intent but blocks diagnosis intent.
"""

DIAGNOSIS_KEYWORDS = [
    "diagnose",
    "diagnosis",
    "what disease",
    "what condition",
    "what illness",
    "do i have",
    "is this",
    "can you tell me what",
    "what problem do i have",
]

EMERGENCY_KEYWORDS = [
    "emergency",
    "urgent",
    "help now",
    "severe pain",
    "chest pain",
    "breathing problem",
    "unconscious",
    "bleeding",
]


def is_diagnosis_request(text: str) -> bool:
    """
    Returns True ONLY if user is asking for diagnosis or medical advice.
    Emergency expressions alone should NOT trigger this.
    """

    text_lower = text.lower()

    # If explicit diagnosis language → block
    for keyword in DIAGNOSIS_KEYWORDS:
        if keyword in text_lower:
            return True

    return False