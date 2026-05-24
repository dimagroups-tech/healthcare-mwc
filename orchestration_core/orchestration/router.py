# orchestration/router.py

from reasoning.engine import reason


def orchestrate(input_payload: dict) -> dict:
    """
    Central traffic controller.
    """
    return reason(input_payload)
