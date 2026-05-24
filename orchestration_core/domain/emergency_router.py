# domain/emergency_router.py

from domain.hospital_ranker import rank_hospitals


def route_emergency_hospitals(city: str):
    """
    Emergency-only routing.
    Ignores all non-emergency filters.
    """

    hospitals = rank_hospitals(
        city=city,
        filters={"emergency": True}
    )

    # Emergency always returns highest priority first
    return hospitals
