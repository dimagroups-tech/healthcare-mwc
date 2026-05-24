# domain/hospital_ranker.py

from reasoning.explanation_engine import explain_hospital
from reasoning.priority_scorer import sort_by_priority


def rank_hospitals(hospitals: list) -> list:
    """
    Explain, score, and rank hospitals by priority
    """

    explained = []

    for hospital in hospitals:
        explained.append(explain_hospital(hospital))

    # Sort hospitals by priority score
    ranked = sort_by_priority(explained)

    return ranked