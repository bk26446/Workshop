# This file controls how the chatbot processes messages.

from chatbot.responses import get_response
from chatbot.memory import ConversationMemory


class ChatbotEngine:
    """
    The ChatbotEngine manages the conversation logic.
    """
    def __init__(self):
       self.memory = ConversationMemory()
       # ⚠️ KEY LINE: Memory persists across turns

    def process_message(self, message: str) -> str:
        """
        Processes user input and returns a response.
        """
        return get_response(message, self.memory)

