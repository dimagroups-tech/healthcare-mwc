# reasoning/entity_extractor.py

KNOWN_CITIES = ["udupi", "mangalore", "bangalore", "chennai", "mumbai"]

def extract_entities(text: str) -> dict:
    text = text.lower()
    entities = {}

    for city in KNOWN_CITIES:
        if city in text:
            entities["location"] = city.title()
            break

    return entities