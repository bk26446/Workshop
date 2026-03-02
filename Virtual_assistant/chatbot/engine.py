# This file controls how the chatbot processes messages.

from chatbot.responses import get_response
from chatbot.memory import ConversationMemory


class ChatbotEngine:
    def __init__(self):
       self.memory = ConversationMemory()

       
       
       self.memory.decays_memory()
       self.memory.forget_low_priority()

    def process_message(self, message: str) -> str:
        
        return get_response(message, self.memory)

