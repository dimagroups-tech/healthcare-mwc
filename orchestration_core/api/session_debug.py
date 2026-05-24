# api/session_debug.py

from api.session_store import SESSION_STORE


def get_session_state(session_id: str) -> dict:
    """
    Inspect current session memory including reasoning timeline.
    """

    session = SESSION_STORE.get(session_id)

    if not session:
        return {
            "status": "not_found",
            "message": f"No session found for id '{session_id}'"
        }

    return {
        "status": "ok",
        "session_id": session_id,
        "state": dict(session)
    }