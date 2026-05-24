# reasoning/explanation_engine.py

def explain_hospital(hospital: dict) -> dict:
    reasons = []

    if hospital.get("emergency"):
        reasons.append("Supports emergency care")

    if hospital.get("type") == "Multi-specialty":
        reasons.append("Multi-specialty hospital")
    elif hospital.get("type") == "General":
        reasons.append("General hospital")

    hospital["reason"] = ", ".join(reasons)
    return hospital
