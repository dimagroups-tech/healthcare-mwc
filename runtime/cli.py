from orchestration_core.reasoning.simple_decision_engine import decide

print("🚑 Healthcare Emergency Checker (India – V1)")
print("Type your problem in simple words (type 'exit' to quit)\n")

while True:
    user_input = input("👉 Enter situation: ")
    if user_input.lower() == "exit":
        break

    result = decide(user_input)

    print("\n🧾 RESULT")
    print(f"Location    : {result['location']['city']}, {result['location']['state']}, {result['location']['country']}")
    print(f"Situation   : {result['situation']}")
    print(f"{result['action']}")
    print("-" * 40)


if __name__ == "__main__":
    main()