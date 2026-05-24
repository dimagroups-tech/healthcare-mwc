# orchestration_core/reasoning/audit_logger.py

from datetime import datetime
from typing import List, Dict

_AUDIT_LOG: List[Dict] = []


def log_event(event_type: str, message: str, session_id: str):
    _AUDIT_LOG.append({
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "event_type": event_type,
        "message": message,
    })


def get_audit_log():
    return list(_AUDIT_LOG)


def clear_audit_log():
    _AUDIT_LOG.clear()