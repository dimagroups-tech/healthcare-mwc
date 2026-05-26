# runtime/core/intent_parser.py

def parse_intent(text: str) -> dict:
    text_lower = text.lower()

    emergency_keywords = [
        "emergency",
        "chest pain",
        "heart attack",
        "breathing",
        "unconscious",
        "severe pain"
    ]

    is_emergency = any(k in text_lower for k in emergency_keywords)

    return {
        "user_text": text,
        "type": "emergency" if is_emergency else "general",
        "confidence": 1.0 if is_emergency else 0.4
    }