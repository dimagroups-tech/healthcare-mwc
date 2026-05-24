# reasoning/intent_classifier.py

def classify_intent(text: str, session: dict) -> str:
    text_lower = text.lower()

    # Emergency intent
    emergency_keywords = [
        "emergency",
        "chest pain",
        "heart attack",
        "accident",
        "bleeding",
        "unconscious",
        "breathless",
        "stroke"
    ]

    for keyword in emergency_keywords:
        if keyword in text_lower:
            return "emergency_hospitals"

    # If user previously triggered emergency and now gives location
    if session.get("emergency") and len(text.split()) <= 3:
        return "emergency_city_followup"

    # City only input (non emergency)
    if text.istitle() or len(text.split()) == 1:
        return "city_query"

    return "general_query"