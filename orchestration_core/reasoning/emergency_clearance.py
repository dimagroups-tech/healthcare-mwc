# reasoning/emergency_clearance.py

"""
Emergency intent detection.
Emergency intent must override all other reasoning.
"""

EMERGENCY_KEYWORDS = [
    "emergency",
    "urgent",
    "immediately",
    "right now",
    "now",
    "help fast",
    "severe",
    "critical",
    "life threatening"
]


def is_emergency(text: str) -> bool:
    """
    Returns True if the user input signals emergency intent.
    """
    text = text.lower()
    return any(keyword in text for keyword in EMERGENCY_KEYWORDS)