# reasoning/filter_extractor.py

def extract_filters(text: str) -> dict:
    """
    Extract hospital filters from user text.
    Returns a dict like:
    {
        "emergency": True,
        "government": False,
        "private": True
    }
    """

    text = text.lower()

    filters = {
        "emergency": False,
        "government": False,
        "private": False
    }

    # Emergency / ICU signals
    emergency_keywords = [
        "emergency", "icu", "urgent", "trauma", "critical", "accident"
    ]
    if any(word in text for word in emergency_keywords):
        filters["emergency"] = True

    # Government hospital signals
    government_keywords = [
        "government", "govt", "public", "state hospital"
    ]
    if any(word in text for word in government_keywords):
        filters["government"] = True

    # Private hospital signals
    private_keywords = [
        "private", "corporate"
    ]
    if any(word in text for word in private_keywords):
        filters["private"] = True

    return filters