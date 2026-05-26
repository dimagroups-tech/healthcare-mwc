# orchestration_core/reasoning/emergency_rules.py

EMERGENCY_KEYWORDS = {
    # HEART / BREATHING
    "heart",
    "heart pain",
    "heart problem",
    "heart patient",
    "heart attack",
    "cardiac",
    "cardiac arrest",
    "chest pain",
    "severe chest pain",
    "breathing problem",
    "breath problem",
    "breathless",
    "not breathing",
    "shortness of breath",

    # NEURO
    "stroke",
    "brain stroke",
    "paralysis",
    "seizure",
    "fits",
    "unconscious",
    "fainted",
    "collapse",

    # BLEEDING / ACCIDENT
    "bleed",
    "bleeding",
    "blood loss",
    "heavy bleeding",
    "accident",
    "road accident",
    "bike accident",
    "car accident",
    "fall",
    "fracture",
    "head injury",

    # TOXIC / OTHER
    "burn",
    "fire burn",
    "electric shock",
    "poison",
    "poisoning",
    "snake bite",
    "dog bite",
    "overdose",
    "suicide"
}

NON_EMERGENCY_KEYWORDS = {
    "fever",
    "cold",
    "cough",
    "headache",
    "body pain",
    "stomach pain",
    "vomiting",
    "loose motion",
    "diarrhea",
    "weakness",
    "checkup",
    "consultation"
}


def classify_situation(text: str) -> str:
    text = text.lower()

    for word in EMERGENCY_KEYWORDS:
        if word in text:
            return "EMERGENCY"

    for word in NON_EMERGENCY_KEYWORDS:
        if word in text:
            return "NON_EMERGENCY"

    return "NORMAL"