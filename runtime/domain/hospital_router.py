# runtime/domain/hospital_router.py

from runtime.domain.hospital_store import find_hospitals


def route_hospital_request(intent: dict) -> dict:
    """
    Routes hospital-related requests safely.
    """

    location = intent.get("location")

    # 🔒 SAFETY: location is REQUIRED
    if not location:
        return {
            "status": "clarification_required",
            "message": "To find nearby hospitals, I need your location.",
            "data": {
                "expected": "city, area, or pin code"
            }
        }

    hospitals = find_hospitals(location)

    return {
        "status": "ok",
        "message": "Here are hospitals you can consider",
        "data": {
            "hospitals": hospitals
        }
    }