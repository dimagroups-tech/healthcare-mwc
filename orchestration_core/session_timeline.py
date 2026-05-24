# session_timeline.py
"""
Timeline Engine (Event Ledger)

Purpose:
- Maintain an ordered list of events per session
- Attach trace_id for observability
- Enable explainability, audits, and replay
"""

from typing import Dict, List
from datetime import datetime


# In-memory timeline store
_TIMELINES: Dict[str, List[dict]] = {}


def record_event(
    session_id: str,
    trace_id: str,
    event_type: str,
    payload: dict
) -> None:
    """
    Record an event in the session timeline.

    Args:
        session_id: Logical conversation/session ID
        trace_id: Unique trace ID for this orchestration cycle
        event_type: Type of event (input, intent, filter, decision, output)
        payload: Event-specific data
    """

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "trace_id": trace_id,
        "event_type": event_type,
        "payload": payload
    }

    if session_id not in _TIMELINES:
        _TIMELINES[session_id] = []

    _TIMELINES[session_id].append(event)


def get_timeline(session_id: str) -> List[dict]:
    """
    Retrieve full timeline for a session.
    """
    return _TIMELINES.get(session_id, [])
