from typing import Optional
from runtime.core.decision_trace import DecisionTrace


def healthcare_rules(intent: dict, trace: Optional[DecisionTrace] = None) -> dict:
    if trace is None:
        trace = DecisionTrace(request_id="internal")

    text = intent.get("user_text", "").lower()

    # Emergency detection (must refuse)
    if "emergency" in text or "chest pain" in text or "unconscious" in text:
        trace.domain_rules_applied.append("emergency_detection")
        return {
            "status": "refused",
            "reason": "This appears to be an emergency. Please contact local emergency services immediately."
        }

    # Default safe navigation steps
    trace.domain_rules_applied.append("default_navigation")

    steps = [
        "Identify the nearest appropriate healthcare facility",
        "Check OPD/visiting hours or appointment requirements",
        "Prepare required documents (ID, insurance, prior reports if any)",
        "Visit the facility or book an appointment manually"
    ]

    return {
        "status": "ok",
        "steps": steps
    }