# orchestration_core/reasoning/audit_log.py

import time

# Simple in-memory audit store (Phase 1)
AUDIT_LOGS = []


def log_event(event_type: str, session_id: str, metadata: dict = None):
    """
    Central audit logger.
    This MUST NEVER fail silently.
    """

    record = {
        "timestamp": time.time(),
        "event_type": event_type,
        "session_id": session_id,
        "metadata": metadata or {}
    }

    AUDIT_LOGS.append(record)

    return record