# orchestration_core/reasoning/simple_decision_engine.py

from orchestration_core.reasoning.city_resolver import extract_city
from orchestration_core.reasoning.emergency_policy_rules import classify_emergency

def decide(text: str):
    city = extract_city(text)
    emergency_status = classify_emergency(text)

    return {
        "input": text,
        "city_detected": city if city else "UNKNOWN",
        "status": emergency_status
    }