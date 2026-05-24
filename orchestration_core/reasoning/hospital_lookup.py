# reasoning/hospital_lookup.py

"""
Hospital Lookup Engine
----------------------
Returns hospitals for a given city.
This is NOT diagnosis.
This is discovery + prioritization only.
"""

HOSPITAL_DATABASE = {
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


def get_hospitals_for_city(city: str):
    """
    Returns list of hospitals for the city.
    """
    if not city:
        return []

    return HOSPITAL_DATABASE.get(city, [])
