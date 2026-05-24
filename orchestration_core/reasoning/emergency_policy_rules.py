# orchestration_core/reasoning/emergency_policy_rules.py

EMERGENCY_KEYWORDS = [
    "emergency",
    "chest pain",
    "heart attack",
    "breathing",
    "unconscious",
    "accident"
]

def check_emergency(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in EMERGENCY_KEYWORDS)