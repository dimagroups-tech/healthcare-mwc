# orchestration_core/reasoning/location_resolver.py

INDIAN_CITIES = {
    "bangalore": "Karnataka",
    "mysuru": "Karnataka",
    "mangalore": "Karnataka",
    "pune": "Maharashtra",
    "mumbai": "Maharashtra",
    "delhi": "Delhi",
    "chennai": "Tamil Nadu",
    "hyderabad": "Telangana",
    "kolkata": "West Bengal",
}

def resolve_location(text: str) -> dict:
    text = text.lower()

    for city, state in INDIAN_CITIES.items():
        if city in text:
            return {
                "city": city.title(),
                "state": state,
                "country": "India"
            }

    return {
        "city": "Unknown",
        "state": "Unknown",
        "country": "India"
    }