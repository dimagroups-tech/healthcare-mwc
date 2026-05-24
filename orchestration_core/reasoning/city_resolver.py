# orchestration_core/reasoning/city_resolver.py

# Minimal deterministic city resolver
# (No AI, no guessing, safe for healthcare)

KNOWN_CITIES = {
    "manipal": "Manipal",
    "udupi": "Udupi",
    "bangalore": "Bangalore",
    "bengaluru": "Bangalore",
    "mangalore": "Mangalore"
}


def resolve_city(user_input: str):
    """
    Extracts city name from user input if present.
    Returns canonical city name or None.
    """

    if not user_input:
        return None

    text = user_input.lower()

    for key, city in KNOWN_CITIES.items():
        if key in text:
            return city

    return None
