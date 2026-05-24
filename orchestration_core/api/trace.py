from orchestration_core.reasoning.decision_trace import get_trace


def get_decision_trace(session_id: str):
    """
    Read-only API to inspect how a decision was made.
    """

    trace = get_trace(session_id)

    return {
        "session_id": session_id,
        "steps": trace,
        "total_steps": len(trace)
    }