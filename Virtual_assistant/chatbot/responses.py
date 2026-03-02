# This file stores the chatbot's response logic.
# Keeping responses separate makes the system easier to expand later.

from chatbot.ml_model import IntentClassifier

classifier = IntentClassifier()


def get_response(user_input: str, memory) -> str:
    intent = classifier.predict_intent(user_input)

    # --- Learn user's name with confidence ---
    if "my name is" in user_input.lower():
        name = user_input.lower().split("name is")[-1].strip().capitalize()
        memory.remember(
            key="user_name",
            value=name,
            confidence=0.9,
            priority=5
        )
        return f"Nice to meet you, {name}!"

    # --- Recall name intelligently ---
    user_name = memory.recall("user_name")

    if intent == "greeting":
        if user_name:
            return f"Hello, {user_name}! How can I help you?"
        return "Hello! How can I help you?"

    elif intent == "help":
        return "I can remember important things and forget unimportant ones."

    elif intent == "exit":
        return "Goodbye! I’ll remember what matters."

    return "Tell me more."
            





