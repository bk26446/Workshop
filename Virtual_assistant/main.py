# main.py is the starting point of your virtual assistant.

from chatbot.engine import ChatbotEngine


def main():
    """
    Runs the chatbot conversation loop.
    """

    bot = ChatbotEngine()
    # ⚠️ KEY LINE: Creating an instance of the chatbot engine

    print("🤖 Virtual Assistant is running. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        response = bot.process_message(user_input)
        print(f"Bot: {response}")

        # Exit condition
        if user_input.lower().strip() in ("exit", "quit", "bye"):
            break
            # ⚠️ KEY LINE: Cleanly exits the infinite loop


if __name__ == "__main__":
    main()
    # ⚠️ KEY LINE: Ensures this file runs only when executed directly
