# api/hospital_registry.py

"""
Static hospital registry for MVP.
Later this will be replaced by:
- database
- government registry
- real-time availability APIs
"""

_HOSPITALS = {
    "Manipal": [
        {
            "name": "Kasturba Hospital",
            "type": "Multi-specialty",
            "emergency": True,
            "ambulance": True,
            "trauma_level": 1,
        },
        {
            "name": "Dr TMA Pai Hospital",
            "type": "General",
            "emergency": False,
            "ambulance": False,
            "trauma_level": None,
        },
    ],
    "Udupi": [
        {
            "name": "District Government Hospital",
            "type": "Government",
            "emergency": True,
            "ambulance": True,
            "trauma_level": 2,
        }
    ],
}


def get_hospitals_for_city(city: str) -> list:
    """
    Returns hospitals for a given city.
    City match is case-insensitive.
    """

    if not city:
        return []

    city_key = city.strip().title()
    return _HOSPITALS.get(city_key, [])
