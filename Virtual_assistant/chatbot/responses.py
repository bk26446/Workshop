# This file stores the chatbot's response logic.
# Keeping responses separate makes the system easier to expand later.

def get_response(user_input: str) -> str:
    """
    Determines the chatbot's response based on user input.
    """

    # Normalize input to make matching easier
    user_input = user_input.lower().strip()
    # ⚠️ KEY LINE: Normalizing text avoids bugs caused by capitalization or spaces

    # --- Rule-based responses ---
    if user_input in ("hi", "hello", "hey"):
        return "Hello! How can I help you today?"

    elif "your name" in user_input:
        return "I'm your virtual assistant. You can name me if you like!"

    elif "help" in user_input:
        return "I can chat with you for now. Soon I'll be able to do much more."

    elif user_input in ("bye", "exit", "quit"):
        return "Goodbye! Have a great day."

    else:
        return "I'm not sure how to respond to that yet."
