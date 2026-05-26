# runtime/core/intent_classifier.py

KNOWN_CITIES = [
    "udupi",
    "bangalore",
    "bengaluru",
    "mumbai",
    "delhi",
    "chennai"
]


def classify_intent(user_text: str) -> dict:
    """
    Input: raw user string
    Output: intent dict ONLY
    """

    text = user_text.lower().strip()

    # 🚑 Emergency detection
    if "emergency" in text or "chest pain" in text:
        return {
            "intent": "medical_emergency",
            "confidence": 0.95,
            "requires_clarification": False
        }

    # 🏥 Hospital visit intent
    if "hospital" in text:
        return {
            "intent": "hospital_visit",
            "confidence": 0.85,
            "requires_clarification": True
        }

    # 🩺 General checkup
    if "checkup" in text:
        return {
            "intent": "general_checkup",
            "confidence": 0.80,
            "requires_clarification": False
        }

    # 📍 Location-only reply (e.g., "Udupi")
    if text in KNOWN_CITIES:
        return {
            "intent": "location_only",
            "location": text,
            "confidence": 0.90,
            "requires_clarification": False
        }

    # ❓ Unknown
    return {
        "intent": "unknown",
        "confidence": 0.40,
        "requires_clarification": True
    }