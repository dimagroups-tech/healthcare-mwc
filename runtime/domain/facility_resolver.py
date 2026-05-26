# runtime/domain/facility_resolver.py

def resolve_facility(context: dict) -> dict:
    """
    Determines the most appropriate healthcare facility
    based on context.
    """

    city = context.get("city")
    is_emergency = context.get("is_emergency", False)

    # --- Emergency always routes to ER
    if is_emergency:
        return {
            "facility_type": "Emergency Department",
            "priority": "immediate",
            "instructions": [
                "Call local emergency services immediately",
                "Go to the nearest emergency department",
                "Do not delay medical care"
            ]
        }

    # --- Non-emergency default routing
    return {
        "facility_type": "General Hospital / Clinic",
        "priority": "normal",
        "instructions": [
            "Search for nearby hospitals or clinics",
            "Check OPD timings",
            "Book an appointment if required"
        ]
    }
