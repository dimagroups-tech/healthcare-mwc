# reasoning/hospital_router.py

HOSPITALS = [
    {
        "id": "kmc_manipal",
        "name": "KMC Manipal",
        "city": "Manipal",
        "emergency": True,
        "specialties": ["cardiac", "trauma", "general"],
        "priority": 1
    },
    {
        "id": "aj_hospital",
        "name": "AJ Hospital",
        "city": "Mangalore",
        "emergency": True,
        "specialties": ["cardiac", "neuro"],
        "priority": 2
    },
    {
        "id": "district_hospital_udupi",
        "name": "District Hospital Udupi",
        "city": "Udupi",
        "emergency": True,
        "specialties": ["general"],
        "priority": 3
    }
]


def route_hospital(city: str, emergency: bool = False):
    if not city:
        return None

    city = city.lower()

    candidates = [
        h for h in HOSPITALS
        if h["city"].lower() == city
        and (h["emergency"] if emergency else True)
    ]

    if not candidates:
        return None

    # lowest priority number = highest priority
    candidates.sort(key=lambda x: x["priority"])
    return candidates[0]