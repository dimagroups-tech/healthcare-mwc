from orchestration_core.policy.registry import POLICIES

POLICY_ID = "emergency_policy"
POLICY_VERSION = "v1"


def evaluate(text: str) -> dict:
    rules = POLICIES[POLICY_ID][POLICY_VERSION]["rules"]
    is_emergency = any(rule in text.lower() for rule in rules)

    return {
        "is_emergency": is_emergency,
        "policy_id": POLICY_ID,
        "policy_version": POLICY_VERSION,
    }