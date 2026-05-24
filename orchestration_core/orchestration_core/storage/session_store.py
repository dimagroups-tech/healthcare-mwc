# orchestration_core/storage/session_store.py

_sessions = {}


def get_session(session_id: str) -> dict:
    """
    Retrieve or create a session.
    """
    if session_id not in _sessions:
        _sessions[session_id] = {
            "session_id": session_id,
            "emergency": False,
            "city": None,
            "hospital": None
        }

    return _sessions[session_id]


def save_session(session: dict) -> None:
    """
    Persist session in memory (noop for now).
    """
    _sessions[session["session_id"]] = session