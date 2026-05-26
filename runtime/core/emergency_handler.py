# runtime/core/emergency_handler.py

def handle_emergency(intent: dict) -> dict:
    return {
        "status": "ok",
        "message": "Here is a safe path you can follow.",
        "data": {
            "steps": [
                "This appears to be a medical emergency",
                "Immediately call local emergency services or ambulance number",
                "If possible, go to the nearest emergency department",
                "Do NOT delay seeking professional medical help"
            ]
        }
    }