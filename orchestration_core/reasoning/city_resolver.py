# orchestration_core/reasoning/city_resolver.py

KARNATAKA_CITIES = {
    # Major
    "bengaluru", "bangalore", "mysuru", "mysore", "mangaluru", "mangalore",
    "hubballi", "hubli", "dharwad", "belagavi", "belgaum", "kalaburagi",
    "gulbarga", "ballari", "bellary", "vijayapura", "bijapur",
    "shivamogga", "shimoga", "tumakuru", "tumkur", "udupi", "chitradurga",
    "davangere", "raichur", "kolar", "hassan", "mandya", "chikkamagaluru",
    "chikmagalur", "bagalkot", "gadag", "haveri", "yadgir", "bidar",
    "ramanagara", "chamarajanagar", "kodagu", "madikeri",

    # Small towns (important)
    "kr puram", "whitefield", "electronic city", "yelahanka",
    "kanakapura", "hosur", "doddaballapur", "nelamangala",
    "sira", "gubbi", "tarikere", "koppa", "sringeri",
    "kundapura", "karkala", "puttur", "sullia", "bantwal",
    "sirsi", "karwar", "ankola", "bhatkal", "honnavar",
    "channapatna", "malavalli", "pandavapura"
}

def extract_city(text: str):
    text = text.lower()
    for city in KARNATAKA_CITIES:
        if city in text:
            return city
    return None