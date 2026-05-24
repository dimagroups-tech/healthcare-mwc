from datetime import datetime
from orchestration_core.audit.ledger import append_audit_event

TRACE_LOG = {}


def add_trace(session_id: str, step: str, data: dict):
    if session_id not in TRACE_LOG:
        TRACE_LOG[session_id] = []

    entry = {
        "ts": datetime.utcnow().isoformat(),
        "step": step,
        "data": data,
    }

    TRACE_LOG[session_id].append(entry)

    append_audit_event(session_id, step, data)


def get_trace(session_id: str):
    return TRACE_LOG.get(session_id, [])


def clear_traces():
    TRACE_LOG.clear()