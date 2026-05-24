from orchestration_core.reasoning.engine import process_input
from orchestration_core.reasoning.trace import add_trace


def receive_input(text: str, session_id: str) -> dict:
    add_trace(session_id, "INPUT", {"text": text})

    session = {
        "session_id": session_id,
        "emergency": False,
        "city": None,
        "hospital": None,
    }

    result = process_input(text, session)

    return {
        "status": "OK",
        "input": text,
        "session": result["session"],
        "message": result["message"],
    }