# This file stores the chatbot's response logic.
# Keeping responses separate makes the system easier to expand later.


from chatbot.ml_model import IntentClassifier

classifier = IntentClassifier()


def get_response(user_input: str) -> str:
    
    intent = classifier.predict_intent(user_input)
    # ⚠️ KEY LINE: Machine learning replaces rules here
    
    """
    Generates response using ML-based intent detection.
    """
    if intent == "greeting":
        return "Hello! How can I help you today?"
    
    elif intent == "name":
        return "I'm your virtual assistant, powered by machine learning."
    
    elif intent == "help":
        return "I can chat, answer questions, and grow smarter over time."
    
    elif intent == "exit":
        return "Goodbye! It was nice talking to you."
    
    else:
        return "I'm not sure I understood that."
            

