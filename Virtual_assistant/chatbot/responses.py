# This file stores the chatbot's response logic.
# Keeping responses separate makes the system easier to expand later.

from chatbot.ml_model import IntentClassifier

classifier = IntentClassifier()


def get_response(user_input: str, memory) -> str:
    
    intent = classifier.predict_intent(user_input)
    # ⚠️ KEY LINE: Machine learning replaces rules here
    
    """
    Remember's user name.
    """
    if intent == "name" and "name is" in user_input.lower():
        name = user_input.lower().split("name is")[-1].strip().capitalize()
        memory.remember("user_name", name)
        return f"Nice to meet you, {name}!"
    
    if memory.has("user_name"):
        user_name = memory.recall("user_name")
    else:
        user_name = None
       
    
    if intent == "greeting":
        if user_name:
            return f"hello, {user_name}! How can I help you today?"
        return "Hello! How can I help you today?"
    
    elif intent == "help":
        return "I can chat with you, remember things, and understand intent."
    
    elif intent == "exit":
        return "Goodbye! I’ll remember our conversation."
    
    else:
        return "Tell me more"
            


