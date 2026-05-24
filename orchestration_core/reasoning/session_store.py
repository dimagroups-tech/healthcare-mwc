# In-memory session storage
_SESSIONS = {}


def get_session(session_id: str):
    if session_id not in _SESSIONS:
        _SESSIONS[session_id] = {
            "session_id": session_id,
            "emergency": False,
            "city": None,
            "hospital": None
        }
    return _SESSIONS[session_id]


def save_session(session_id: str, session_data: dict):
    _SESSIONS[session_id] = session_data