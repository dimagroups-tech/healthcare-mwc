# reasoning/city_extractor.py

import re


KNOWN_CITIES = [
    "Manipal",
    "Udupi",
    "Bangalore",
    "Bengaluru",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad",
    "Pune"
]


def extract_city(text: str):
    """
    Extracts city name from user input if present.
    Returns city string or None.
    """

    if not text:
        return None

    text_lower = text.lower()

    for city in KNOWN_CITIES:
        if city.lower() in text_lower:
            return city

    return None