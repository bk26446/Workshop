# main.py is the starting point of your virtual assistant.

from chatbot.engine import ChatbotEngine
from chatbot.ml_model import IntentClassifier


def main():
    """
    Runs the chatbot conversation loop.
    """

    bot = ChatbotEngine()
    classifier = IntentClassifier()
    
    
    # ⚠️ KEY LINE: Creating an instance of the chatbot engine

    print("🤖 ML-Powered Virtual Assistant is running. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        
        intent = classifier.predict_intent(user_input)
        response = bot.process_message(user_input)
        
        print(f"Bot: {response}")

        # Exit condition
# %%
        if  intent == "exit":

            break
            # ⚠️ KEY LINE: Cleanly exits the infinite loop


if __name__ == "__main__":
    main()
    # ⚠️ KEY LINE: Ensures this file runs only when executed directly
