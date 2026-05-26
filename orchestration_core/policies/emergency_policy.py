# orchestration_core/policies/emergency_policy.py

EMERGENCY_KEYWORDS = [

    # 🔴 BLEEDING / INJURY
    "bleeding",
    "severe bleeding",
    "heavy bleeding",
    "blood loss",
    "cut badly",
    "injured badly",
    "deep wound",
    "accident",
    "road accident",
    "fall",
    "fracture",
    "broken bone",
    "hit by vehicle",

    # 🔴 HEART / CHEST
    "heart attack",
    "chest pain",
    "severe chest pain",
    "heart pain",
    "cardiac arrest",
    "pulse stopped",

    # 🔴 BREATHING
    "not breathing",
    "breathing problem",
    "shortness of breath",
    "cannot breathe",
    "breathless",
    "asthma attack",
    "choking",

    # 🔴 BRAIN / NERVOUS
    "stroke",
    "paralysis",
    "unconscious",
    "fainted",
    "collapsed",
    "seizure",
    "fits",
    "convulsions",
    "head injury",

    # 🔴 PREGNANCY / WOMEN
    "pregnant bleeding",
    "labor pain",
    "delivery pain",
    "pregnancy emergency",
    "miscarriage",

    # 🔴 POISON / BURNS
    "poison",
    "poisoned",
    "snake bite",
    "dog bite",
    "burn",
    "burn injury",
    "acid attack",
    "electric shock",

    # 🔴 GENERAL DANGER WORDS (VERY IMPORTANT)
    "critical",
    "serious condition",
    "life threatening",
    "emergency",
    "very serious",
    "dying",
    "danger",
    "immediate help",
    "help fast",
    "urgent"
]


def evaluate(text: str, session: dict) -> dict:
    """
    Emergency policy evaluation.
    Detects emergencies using strong keyword matching.
    """

    text = text.lower()

    is_emergency = any(keyword in text for keyword in EMERGENCY_KEYWORDS)

    session["emergency"] = is_emergency
    session["emergency_details"] = {
        "is_emergency": is_emergency,
        "policy_id": "emergency_policy",
        "policy_version": "v1"
    }

    return {
        "session": session,
        "message": "🚨 Emergency detected. Immediate action required."
        if is_emergency
        else "No emergency detected."
    }