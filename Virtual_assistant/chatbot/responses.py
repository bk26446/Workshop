# This file stores the chatbot's response logic.
# Keeping responses separate makes the system easier to expand later.

from chatbot.nlp_utils import preprocess_text


# Define intents and keywords
INTENTS = {
    "greeting": {"hello", "hi", "hey", "wagwan", "wassup", "whatsup", "bho"},
    "name": {"name", "who"},
    "help": {"help", "support", "assist"},
    "exit": {"bye", "exit", "quit"},

    }

def detect)intent(tokens: list) -> str:
  """
    Determines the user's intent based on keywords.
    """

  for intent, keywords in INTENTS.items():
      if any(token in keywords for token in tokens):
          return intent
        # ⚠️ KEY LINE: Keyword-based intent detection
    return "unknown"

    

def get_response(user_input: str) -> str:
    """
    Determines the chatbot's response based on user input.
    """

    tokens = preprocess_text(user_input)
    intent - detect_intent(tokens)

    if intent == "greeting":
        return "Hello! How can I help you today?"
    
    elif intent == "name":
        return "I'm your virtual assistant. You can customize me anytime."

    elif intent == "help":
        return "I can chat, answer questions, and soon perform tasks."

    elif intent == "exit":
        return "Goodbye! See you next time."

    else:
        return "I'm still learning. Could you rephrase that?"
