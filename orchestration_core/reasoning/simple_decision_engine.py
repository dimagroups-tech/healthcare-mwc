# orchestration_core/reasoning/simple_decision_engine.py

from orchestration_core.reasoning.location_resolver import resolve_location
from orchestration_core.reasoning.emergency_rules import classify_situation


def decide(user_input: str) -> dict:
    location = resolve_location(user_input)
    situation = classify_situation(user_input)

    if situation == "EMERGENCY":
        action = "🚨 IMMEDIATE medical attention required. Call ambulance / visit ER."
    elif situation == "NON_EMERGENCY":
        action = "🩺 Medical attention advised. Visit nearby clinic."
    else:
        action = "ℹ️ No urgent medical risk detected."

    return {
        "location": location,
        "situation": situation,
        "action": action
    }