# reasoning/priority_scorer.py

def score_hospital(hospital: dict) -> int:
    score = 0

    # Highest priority: emergency support
    if hospital.get("emergency"):
        score += 100

    # Hospital type priority
    if hospital.get("type") == "Multi-specialty":
        score += 20
    elif hospital.get("type") == "General":
        score += 10

    return score


def sort_by_priority(hospitals: list) -> list:
    """
    Attach priority score and sort hospitals by importance
    """
    for hospital in hospitals:
        hospital["priority_score"] = score_hospital(hospital)

    return sorted(
        hospitals,
        key=lambda h: h["priority_score"],
        reverse=True
    )
