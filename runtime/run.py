import uuid
from orchestration_core.reasoning.engine import process_input


def main():
    print("Healthcare MWC — Phase 1")
    print("Type your situation and press Enter:\n")

    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue

        request_id = str(uuid.uuid4())

        session = {
            "session_id": request_id,
            "history": []
        }

        try:
            result = process_input(
                text=user_input,
                session=session
            )

            print("\n--- SYSTEM RESPONSE ---")
            for k, v in result.items():
                print(f"{k}: {v}")

        except Exception as e:
            print("\n--- SYSTEM RESPONSE ---")
            print("status: error")
            print("message: Internal system error")
            print("data:", {
                "error_type": type(e).__name__,
                "error_message": str(e)
            })
            print("source: internal")


if __name__ == "__main__":
    main()