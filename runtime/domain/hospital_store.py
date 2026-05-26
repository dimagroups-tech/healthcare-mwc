# runtime/domain/hospital_store.py

def find_hospitals(location: str) -> list:
    """
    Temporary in-memory hospital lookup.
    Later this will be replaced by DB / API / GIS.
    """

    # Normalize input
    location = location.lower()

    # Dummy data (safe stub)
    return [
        {
            "name": "City General Hospital",
            "type": "Government",
            "distance_km": 2.5,
            "emergency": True,
            "location": location
        },
        {
            "name": "CarePlus Clinic",
            "type": "Private",
            "distance_km": 1.2,
            "emergency": False,
            "location": location
        }
    ]