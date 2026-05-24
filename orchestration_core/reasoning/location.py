# reasoning/location.py

"""
Location Extraction Logic
-------------------------
Extracts city names from user input safely.
No external APIs.
No guessing.
"""

KNOWN_CITIES = [
    "Manipal",
    "Udupi",
    "Mangalore",
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
]


def extract_cities(text: str):
    """
    Returns a list of recognized cities mentioned in text.
    """
    if not text:
        return []

    found = []
    text_lower = text.lower()

    for city in KNOWN_CITIES:
        if city.lower() in text_lower:
            found.append(city)

    return found
