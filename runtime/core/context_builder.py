# runtime/core/context_builder.py

from datetime import datetime, timezone
from typing import Dict, Optional


def _extract_city(user_text: str) -> Optional[str]:
    """
    Very conservative city extraction.
    No guessing. No ML. No hallucination.
    """

    known_cities = {
        "udupi": "Udupi",
        "bangalore": "Bangalore",
        "bengaluru": "Bangalore",
        "mumbai": "Mumbai",
        "delhi": "Delhi",
        "chennai": "Chennai",
	"mysore":"Mysore",
        "hyderabad": "Hyderabad",
    }

    for key, value in known_cities.items():
        if key in user_text:
            return value

    return None


def build_context(intent: Dict) -> Dict:
    """
    Builds execution context from intent.

    IMPORTANT RULES:
    - This layer does NOT decide
    - This layer does NOT block
    - This layer does NOT override policy
    - This layer only observes reality
    """

    user_text = intent.get("user_text", "").lower()
    intent_type = intent.get("type")

    # --- Emergency awareness (never inferred here)
    is_emergency = intent_type == "emergency"

    # --- Location (safe extraction only)
    city = _extract_city(user_text)

    # --- Time (UTC, immutable reference)
    timestamp = datetime.now(timezone.utc).isoformat()

    # --- Context object (expandable later)
    context = {
        "city": city,
        "timestamp": timestamp,
        "is_emergency": is_emergency,
        "intent_type": intent_type,
    }

    return context