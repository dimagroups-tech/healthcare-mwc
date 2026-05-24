# orchestration_core/domain/hospital_store.py

HOSPITALS = {
    "Manipal": [
        {
            "id": "kmc_manipal",
            "name": "KMC Manipal",
            "city": "Manipal",
            "emergency": True,
            "specialties": ["cardiac", "trauma", "general"],
            "priority": 1
        },
        {
            "id": "castello_clinic",
            "name": "Castello Clinic",
            "city": "Manipal",
            "emergency": False,
            "specialties": ["general"],
            "priority": 2
        }
    ],
    "Bangalore": [
        {
            "id": "narayana",
            "name": "Narayana Health",
            "city": "Bangalore",
            "emergency": True,
            "specialties": ["cardiac", "neuro"],
            "priority": 1
        }
    ]
}