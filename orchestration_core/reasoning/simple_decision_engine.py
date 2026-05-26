# orchestration_core/reasoning/simple_decision_engine.py

from orchestration_core.reasoning.emergency_policy_rules import classify_emergency
from orchestration_core.reasoning.india_location_resolver import detect_location

def decide(text: str):
    status = classify_emergency(text)
    location = detect_location(text)

    return {
        "input": text,
        "location_detected": location,
        "status": status
    }