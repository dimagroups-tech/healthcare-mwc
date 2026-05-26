from orchestration_core.reasoning.engine import process_input


def receive_input(text: str, session: dict) -> dict:
    """
    Router layer.
    Accepts raw input and forwards it to the reasoning engine.
    """
    return process_input(text, session)