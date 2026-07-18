def get_response(user_input: str) -> str:
    message = user_input.lower().strip()

    greetings = {
        "hi": "Hello!",
        "hello": "Hello!",
        "hey": "Hey there!",
    }

    if message in greetings:
        return greetings[message]

    if any(phrase in message for phrase in ["how are you", "how're you"]):
        return "I'm doing well. How can I help?"

    if "your name" in message:
        return "I'm a simple rule-based chatbot."

    if "help" in message:
        return "Try saying hello, asking my name, or typing 'bye' to exit."

    if "weather" in message:
        return "I cannot check live weather, but I can chat with you."

    if "time" in message:
        return "I do not have access to the current time in this basic version."

    if message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye!"

    return "I'm not sure how to respond to that."


def main() -> None:
    print("Chatbot: Hello. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
