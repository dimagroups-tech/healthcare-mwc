# reasoning/priority_explainer.py

def explain_priority(hospital: dict) -> list:
    """
    Explain why a hospital received its priority score.

    This function is:
    - Deterministic
    - Rule-based
    - Explainable
    - Audit-safe (no AI reasoning)

    Input:
        hospital (dict)

    Output:
        list of human-readable reasons (strings)
    """

    reasons = []

    if hospital.get("emergency"):
        reasons.append("24x7 emergency department available")

    if hospital.get("ambulance"):
        reasons.append("Ambulance support available")

    trauma_level = hospital.get("trauma_level")
    if trauma_level == 1:
        reasons.append("Trauma Level 1 facility (highest emergency care)")
    elif trauma_level == 2:
        reasons.append("Trauma Level 2 facility")

    if not reasons:
        reasons.append("No emergency or trauma capabilities detected")

    return reasons
