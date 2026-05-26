# runtime/core/clarification_handler.py

def handle_clarification(intent: dict):
    """
    Returns clarification response OR None
    """

    intent_type = intent.get("intent")

    # Unknown intent → ask user
    if intent_type == "unknown":
        return {
            "status": "clarification_required",
            "message": "Please provide more details so I can help you safely.",
            "data": {
                "expected": "medical issue, hospital visit, emergency, checkup, etc."
            }
        }

    # Hospital visit but missing location
    if intent_type == "hospital_visit" and not intent.get("location"):
        return {
            "status": "clarification_required",
            "message": "Which city or area are you looking for hospitals in?",
            "data": {
                "expected": "city or locality (e.g., Udupi)"
            }
        }

    return None