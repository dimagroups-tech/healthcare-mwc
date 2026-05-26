# runtime/api/server.py

import uuid
from datetime import datetime, timezone

from runtime.core.intent_classifier import classify_intent
from runtime.core.reasoning_engine import reason


def handle_request(user_text: str) -> dict:
    request_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()

    try:
        # 1️⃣ Always classify first
        intent = classify_intent(user_text)

        # 2️⃣ ALWAYS pass request_id to reason()
        decision = reason(intent, request_id)

        return {
            "request_id": request_id,
            "timestamp": timestamp,
            "status": decision.get("status", "ok"),
            "message": decision.get("message", ""),
            "data": decision.get("data", {}),
            "source": "internal"
        }

    except Exception as e:
        return {
            "request_id": request_id,
            "timestamp": timestamp,
            "status": "error",
            "message": "Internal system error",
            "data": {
                "error_type": type(e).__name__,
                "error_message": str(e)
            },
            "source": "internal"
        }