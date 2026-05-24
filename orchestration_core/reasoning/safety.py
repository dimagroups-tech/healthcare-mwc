# reasoning/safety.py

"""
Safety & Medical Guard
-----------------------
Prevents diagnosis, treatment, or medical advice.
Allows emergency navigation and hospital discovery.
"""

DIAGNOSIS_KEYWORDS = [
    "diagnose",
    "diagnosis",
    "what do i have",
    "what disease",
    "is this",
    "what condition",
    "treatment",
    "medicine",
    "drug",
    "tablet",
    "dose",
    "dosage",
    "cure",
    "therapy"
]


def is_diagnosis_request(text: str) -> bool:
    """
    Returns True if the user is asking for diagnosis or medical advice.
    """
    if not text:
        return False

    text = text.lower()

    for keyword in DIAGNOSIS_KEYWORDS:
        if keyword in text:
            return True

    return False
