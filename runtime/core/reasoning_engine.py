# runtime/core/reasoning_engine.py

from runtime.core.clarification_handler import handle_clarification
from runtime.domain.hospital_router import route_hospital_request


def reason(intent: dict, context: dict, request_id: str) -> dict:
    """
    Input: intent dict + context dict
    Output: decision dict
    """

    intent_type = intent.get("intent")

    # 🧠 MERGE CONTEXT INTO INTENT (location memory)
    if "location" not in intent and "location" in context:
        intent["location"] = context["location"]

    # 📍 STEP 3C.5 — LOCATION-ONLY REPLY HANDLING
    if intent_type == "location_only":
        context["location"] = intent["location"]

        if context.get("pending_intent") == "hospital_visit":
            return route_hospital_request({
                "intent": "hospital_visit",
                "location": intent["location"]
            })

        return {
            "status": "ok",
            "message": "Location noted.",
            "data": {},
            "context": {"location": intent["location"]}
        }

    # 🚑 1. MEDICAL EMERGENCY — HIGHEST PRIORITY
    if intent_type == "medical_emergency":
        return {
            "status": "ok",
            "message": "This appears to be a medical emergency",
            "data": {
                "steps": [
                    "Immediately call local emergency services",
                    "Go to the nearest emergency department",
                    "Do NOT delay seeking professional medical help"
                ]
            }
        }

    # 🏥 2. HOSPITAL VISIT
    if intent_type == "hospital_visit":
        location = intent.get("location")

        if not location:
            return {
                "status": "clarification_required",
                "message": "Which city or area are you looking for hospitals in?",
                "data": {"expected": "city or locality (e.g., Udupi)"},
                "context": {"pending_intent": "hospital_visit"}
            }

        return route_hospital_request(intent)

    # 🩺 3. GENERAL CHECKUP
    if intent_type == "general_checkup":
        return {
            "status": "ok",
            "message": "You can safely plan a general checkup",
            "data": {
                "steps": [
                    "Choose a nearby hospital or clinic",
                    "Book an appointment with a general physician",
                    "Carry previous medical records if available"
                ]
            }
        }

    # ❓ 4. CLARIFICATION (LAST)
    clarification = handle_clarification(intent)
    if clarification:
        return clarification

    # 🧩 5. SAFE FALLBACK
    return {
        "status": "ok",
        "message": "I need more information to help you",
        "data": {}
    }