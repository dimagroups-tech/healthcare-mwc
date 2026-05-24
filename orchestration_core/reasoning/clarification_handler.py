# reasoning/clarification_handler.py

def handle_clarification(intent_data: dict):
    intent = intent_data.get("intent")

    # Unknown or empty intent
    if intent in (None, "unknown"):
        return {
            "status": "clarification_required",
            "message": "Please provide more details so I can help you.",
            "data": {
                "expected": "medical issue, hospital visit, emergency, etc."
            }
        }

    # Hospital visit needs location or purpose
    if intent == "hospital_visit":
        return {
            "status": "clarification_required",
            "message": "Which city or area are you looking for hospitals in?",
            "data": {
                "expected": "city or locality (e.g., Udupi)"
            }
        }

    return None