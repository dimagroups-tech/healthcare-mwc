# runtime/cli.py

import sys
import os

# --- FIX: Add project root to PYTHON PATH ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from orchestration_core.reasoning.simple_decision_engine import decide


def main():
    print("\n🚑 Healthcare Emergency Checker (Karnataka – V1)")
    print("Type your problem in simple words (type 'exit' to quit)\n")

    while True:
        text = input("👉 Enter situation: ").strip()

        if text.lower() in {"exit", "quit"}:
            print("Goodbye 👋")
            break

        result = decide(text)

        print("\n🧾 RESULT")
        print("Location    :", result["location_detected"])
        print("Situation   :", result["status"])

        if result["status"] == "EMERGENCY":
            print("🚨 ACTION: Go to nearest emergency hospital immediately")
        elif result["status"] == "NON_EMERGENCY":
            print("⚠️ ACTION: Visit doctor / clinic")
        else:
            print("ℹ️ ACTION: No urgent medical risk detected")

        print("-" * 40)


if __name__ == "__main__":
    main()