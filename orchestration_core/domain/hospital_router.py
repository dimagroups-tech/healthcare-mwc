# orchestration_core/domain/hospital_router.py

from domain.hospital_store import HOSPITALS


def route_hospital(city: str, emergency: bool):
    if not city:
        return None

    hospitals = HOSPITALS.get(city)
    if not hospitals:
        return None

    if emergency:
        emergency_hospitals = [
            h for h in hospitals if h.get("emergency") is True
        ]
        if emergency_hospitals:
            return sorted(emergency_hospitals, key=lambda x: x["priority"])[0]

    return sorted(hospitals, key=lambda x: x["priority"])[0]