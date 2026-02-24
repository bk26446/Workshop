# This file controls how the chatbot processes messages.

from chatbot.responses import get_response


class ChatbotEngine:
    """
    The ChatbotEngine manages the conversation logic.
    """

    def process_message(self, message: str) -> str:
        """
        Processes user input and returns a response.
        """

        # Delegate response generation to the response module
        response = get_response(message)
        # ⚠️ KEY LINE: Separating logic like this makes your code modular

        return response
