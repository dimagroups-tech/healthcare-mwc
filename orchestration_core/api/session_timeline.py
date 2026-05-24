from datetime import datetime
from api.session_store import get_session, update_session


def log_event(
    session_id: str,
    trace_id: str,
    event: str,
    data: dict = None
):
    """
    Append an event to the session timeline.
    This function is SELF-HEALING:
    - Creates session if missing
    - Creates timeline if missing
    - Never crashes due to bad state
    """

    if data is None:
        data = {}

    # Load existing session
    session = get_session(session_id)

    # 🛠️ FIX 1: Create session if it does not exist
    if session is None:
        session = {
            "session_id": session_id,
            "timeline": []
        }

    # 🛠️ FIX 2: Heal missing or corrupted timeline
    if "timeline" not in session or not isinstance(session["timeline"], list):
        session["timeline"] = []

    # Append event
    session["timeline"].append({
        "timestamp": datetime.utcnow().isoformat(),
        "trace_id": trace_id,
        "event": event,
        "data": data
    })

    # Persist session
    update_session(session_id, session)