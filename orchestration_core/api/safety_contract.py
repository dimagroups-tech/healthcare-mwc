# api/safety_contract.py

"""
Safety & decision boundaries for orchestration.
This file defines what the system is NEVER allowed to do.
"""

# Hard safety rules
DISALLOWED_ACTIONS = [
    "diagnose_disease",
    "prescribe_medication",
    "suggest_treatment",
    "replace_doctor",
]

# Emergency must always escalate
EMERGENCY_OVERRIDES = {
    "bypass_filters": True,
    "require_city": True,
    "force_emergency_flag": True,
}


def check_safety(action: str) -> bool:
    """
    Returns False if the action violates safety rules.
    """
    return action not in DISALLOWED_ACTIONS
