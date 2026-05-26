def adapt_response(decision: dict) -> dict:
    """
    Converts internal decision output into a user-facing response.
    This is intentionally minimal for Phase 1.
    """

    status = decision.get("status")

    if status == "refused":
        return {
            "status": "refused",
            "message": decision.get("reason", "Action refused by system policy."),
            "data": {}
        }

    if status == "ok":
        return {
            "status": "ok",
            "message": "Here is a safe path you can follow.",
            "data": {
                "steps": decision.get("steps", [])
            }
        }

    return {
        "status": "unknown",
        "message": "System could not determine a safe response.",
        "data": {}
    }