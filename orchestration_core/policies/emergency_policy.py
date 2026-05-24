from orchestration_core.reasoning.trace import add_trace


def evaluate(text: str, session: dict) -> dict:
    """
    Emergency policy: keyword-based deterministic rule.
    """

    triggers = ["emergency", "chest pain", "heart attack"]

    is_emergency = any(t in text.lower() for t in triggers)

    if is_emergency:
        session["emergency"] = True
        session["emergency_details"] = {
            "is_emergency": True,
            "trigger": "keyword_match",
            "confidence": 1.0
        }

        add_trace(
            session["session_id"],
            "EMERGENCY_POLICY",
            session["emergency_details"]
        )

    return session