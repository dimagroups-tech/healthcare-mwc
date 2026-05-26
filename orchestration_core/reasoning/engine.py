"""
Healthcare MWC — Core Reasoning Engine (V1)

This is the SINGLE entry point for all reasoning.
DO NOT add multiple engines.
DO NOT bypass this file.
"""

from orchestration_core.policy.emergency import evaluate as emergency_policy
from orchestration_core.reasoning.trace import add_trace
from datetime import datetime
import uuid


def reason(text: str, session: dict | None = None) -> dict:
    """
    Main reasoning function used by CLI and APIs.

    Parameters:
        text (str): User input (example: "bleeding", "headache")
        session (dict): Session state (auto-created if missing)

    Returns:
        dict: System response
    """

    # -----------------------------
    # SESSION INITIALIZATION
    # -----------------------------
    if session is None:
        session = {
            "session_id": str(uuid.uuid4()),
            "history": [],
        }

    session_id = session["session_id"]

    # -----------------------------
    # INPUT TRACE
    # -----------------------------
    add_trace(
        session_id,
        "ENGINE_INPUT",
        {
            "text": text,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        },
    )

    # -----------------------------
    # POLICY EVALUATION
    # -----------------------------
    decision = emergency_policy(text)

    # -----------------------------
    # POLICY TRACE
    # -----------------------------
    add_trace(
        session_id,
        "EMERGENCY_POLICY",
        {
            "is_emergency": decision["is_emergency"],
            "policy_id": decision["policy_id"],
            "policy_version": decision["policy_version"],
        },
    )

    # -----------------------------
    # SESSION STATE UPDATE
    # -----------------------------
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

    # -----------------------------
    # HUMAN-READABLE MESSAGE
    # -----------------------------
    if decision["is_emergency"]:
        message = "🚨 Emergency detected. Routing to nearest hospital."
    else:
        message = "No emergency detected."

    # -----------------------------
    # OUTPUT TRACE
    # -----------------------------
    add_trace(
        session_id,
        "ENGINE_OUTPUT",
        {
            "message": message,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        },
    )

    # -----------------------------
    # FINAL RESPONSE
    # -----------------------------
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "session": session,
        "message": message,
    }