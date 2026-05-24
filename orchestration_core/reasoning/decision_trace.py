# orchestration_core/reasoning/decision_trace.py

_TRACE_LOG = {}

def log_trace(session_id: str, step: str, detail: str):
    if session_id not in _TRACE_LOG:
        _TRACE_LOG[session_id] = []
    _TRACE_LOG[session_id].append({
        "step": step,
        "detail": detail
    })

def get_trace(session_id: str):
    return _TRACE_LOG.get(session_id, [])

def clear_traces():
    _TRACE_LOG.clear()