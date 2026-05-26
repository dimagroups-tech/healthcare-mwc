# orchestration_core/reasoning/location_resolver.py

INDIAN_CITIES = {

    # =======================
    # KARNATAKA
    # =======================
    "bangalore": "Karnataka",
    "bengaluru": "Karnataka",
    "mysuru": "Karnataka",
    "mysore": "Karnataka",
    "mangaluru": "Karnataka",
    "mangalore": "Karnataka",
    "hubli": "Karnataka",
    "dharwad": "Karnataka",
    "belagavi": "Karnataka",
    "ballari": "Karnataka",
    "bellary": "Karnataka",
    "tumkur": "Karnataka",
    "davangere": "Karnataka",
    "shivamogga": "Karnataka",
    "hassan": "Karnataka",
    "chitradurga": "Karnataka",
    "udupi": "Karnataka",
    "raichur": "Karnataka",
    "bidar": "Karnataka",
    "kalaburagi": "Karnataka",
    "gulbarga": "Karnataka",
    "kolar": "Karnataka",
    "chikkamagaluru": "Karnataka",

    # =======================
    # MAHARASHTRA
    # =======================
    "mumbai": "Maharashtra",
    "pune": "Maharashtra",
    "nagpur": "Maharashtra",
    "nashik": "Maharashtra",
    "aurangabad": "Maharashtra",
    "kolhapur": "Maharashtra",
    "solapur": "Maharashtra",
    "sangli": "Maharashtra",

    # =======================
    # TAMIL NADU
    # =======================
    "chennai": "Tamil Nadu",
    "coimbatore": "Tamil Nadu",
    "madurai": "Tamil Nadu",
    "salem": "Tamil Nadu",

    # =======================
    # TELANGANA
    # =======================
    "hyderabad": "Telangana",
    "warangal": "Telangana",

    # =======================
    # DELHI
    # =======================
    "delhi": "Delhi",
    "new delhi": "Delhi",

    # =======================
    # WEST BENGAL
    # =======================
    "kolkata": "West Bengal",

    # =======================
    # KERALA
    # =======================
    "kochi": "Kerala",
    "trivandrum": "Kerala",
    "thiruvananthapuram": "Kerala",
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