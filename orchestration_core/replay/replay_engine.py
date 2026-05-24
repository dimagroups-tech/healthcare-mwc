from orchestration_core.policy.registry import POLICIES


def replay_decision(trace_entry: dict, original_text: str) -> bool:
    policy_id = trace_entry["data"]["policy_id"]
    policy_version = trace_entry["data"]["policy_version"]

    if policy_id not in POLICIES:
        raise Exception("Policy not found")

    if policy_version not in POLICIES[policy_id]:
        raise Exception("Policy version not found")

    rules = POLICIES[policy_id][policy_version]["rules"]
    return any(r in original_text.lower() for r in rules)