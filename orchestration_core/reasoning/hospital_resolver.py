# orchestration_core/reasoning/hospital_resolver.py

from orchestration_core.reasoning.decision_trace import trace_step
from orchestration_core.reasoning.audit_logger import log_event


def resolve_hospital(text: str, session: dict):
    if "hospital" not in text.lower():
        return False

    session["hospital"] = text

    trace_step(
        session["session_id"],
        "HOSPITAL_SELECTED",
        text
    )

    log_event(
        "HOSPITAL_SELECTED",
        f"Hospital selected: {text}",
        session["session_id"]
    )

    return True