# orchestration_core/reasoning/emergency_policy_rules.py

EMERGENCY_KEYWORDS = {
    "heart attack", "cardiac arrest", "stroke", "unconscious",
    "accident", "road accident", "bleeding", "heavy bleeding",
    "gunshot", "stab", "burn", "fire accident",
    "breathing problem", "cannot breathe", "asthma attack",
    "seizure", "fits", "convulsion",
    "snake bite", "dog bite", "poison", "poisoning",
    "pregnancy pain", "delivery emergency",
    "severe chest pain", "collapsed"
}

NON_EMERGENCY_KEYWORDS = {
    "fever", "cold", "cough", "headache", "stomach pain",
    "vomiting", "diarrhea", "body pain", "back pain",
    "leg pain", "infection", "skin allergy",
    "minor cut", "small wound", "ear pain", "tooth pain"
}

def classify_emergency(text: str):
    text = text.lower()

    for word in EMERGENCY_KEYWORDS:
        if word in text:
            return "EMERGENCY"

    for word in NON_EMERGENCY_KEYWORDS:
        if word in text:
            return "NON_EMERGENCY"

    return "NORMAL"