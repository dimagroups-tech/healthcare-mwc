# reasoning/priority_engine.py

"""
Priority Engine
----------------
Calculates a transparent, explainable priority score
for hospitals based on emergency relevance.

This is deterministic, auditable, and government-safe.
"""

def calculate_priority(hospital: dict, context: dict) -> int:
    """
    Returns an integer priority score (0–100).

    Inputs:
    - hospital: hospital metadata
    - context: session context (symptoms, intent, urgency)

    No AI, no randomness.
    """

    score = 0

    # 1. Emergency relevance
    if context.get("is_emergency"):
        if hospital.get("emergency"):
            score += 60
        else:
            score -= 20

    # 2. Trauma capability
    trauma_level = hospital.get("trauma_level")
    if trauma_level == 1:
        score += 30
    elif trauma_level == 2:
        score += 15

    # 3. Ambulance support
    if hospital.get("ambulance"):
        score += 10

    # 4. Safety floor
    if score < 0:
        score = 0

    return score
