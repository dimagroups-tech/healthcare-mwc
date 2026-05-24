from orchestration_core.policy.emergency import evaluate as emergency_policy
from orchestration_core.reasoning.trace import add_trace


def process_input(text: str, session: dict) -> dict:
    session_id = session["session_id"]

    add_trace(session_id, "ENGINE_INPUT", {"text": text})

    decision = emergency_policy(text)

    # 🔒 POLICY TRACE (versioned)
    add_trace(
        session_id,
        "EMERGENCY_POLICY",
        {
            "is_emergency": decision["is_emergency"],
            "policy_id": decision["policy_id"],
            "policy_version": decision["policy_version"],
        },
    )

    # ✅ REQUIRED SESSION STATE (for tests + replay)
    session["emergency"] = decision["is_emergency"]
    session["emergency_details"] = {
        "is_emergency": decision["is_emergency"],
        "policy_id": decision["policy_id"],
        "policy_version": decision["policy_version"],
    }

    session["policy"] = {
        "id": decision["policy_id"],
        "version": decision["policy_version"],
    }

    message = (
        "Emergency detected. Routing to nearest hospital."
        if decision["is_emergency"]
        else "No emergency detected."
    )

    add_trace(session_id, "ENGINE_OUTPUT", {"message": message})

    return {
        "session": session,
        "message": message,
    }