# runtime/core/policy_guard.py

class PolicyViolation(Exception):
    pass


class PolicyGuard:
    EMERGENCY_KEYWORDS = [
        "emergency",
        "chest pain",
        "heart attack",
        "breathing",
        "unconscious",
        "severe pain"
    ]

    def check(self, intent: dict):
        if not isinstance(intent, dict):
            raise PolicyViolation("Invalid intent structure")

        confidence = intent.get("confidence", 1.0)
        text = intent.get("user_text", "").lower()

        # 🚑 NEVER block emergencies
        if any(word in text for word in self.EMERGENCY_KEYWORDS):
            return

        if confidence < 0.3:
            raise PolicyViolation("Intent confidence too low")