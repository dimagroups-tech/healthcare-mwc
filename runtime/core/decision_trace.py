from datetime import datetime, timezone


class DecisionTrace:
    def __init__(self, request_id: str):
        self.request_id = request_id
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.intent = None
        self.policies_checked = []
        self.domain_rules_applied = []
        self.final_decision = None

    def to_dict(self) -> dict:
        return {
            "request_id": self.request_id,
            "timestamp": self.timestamp,
            "intent": self.intent,
            "policies_checked": self.policies_checked,
            "domain_rules_applied": self.domain_rules_applied,
            "final_decision": self.final_decision,
        }
