def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your name":
        return "I'm a simple chatbot."
    else:
        return "Sorry, I don't understand that."


def main():
    print("🤖 Chatbot started! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break


if __name__ == "__main__":
    main()
