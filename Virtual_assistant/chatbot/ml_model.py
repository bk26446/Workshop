from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


from chatbot.training_data import TRAINING_DATA


class IntentClassifier:
     """
    Machine learning model for intent classification.
    """

     def __init__(self):
         self.vectorizer = TfidfVectorizer()

        #⚠️ This line converts text into numerical features


         self.model = LogisticRegression()

         # Simple, fast, and effective classifier


         self._train()

     def _train(self):
        
              """
            Trains the intent classification model.
            """
              texts = [text for text, intent in TRAINING_DATA]
              labels = [intent for text, intent in TRAINING_DATA]

              X = self.vectorizer.fit_transform(texts)
              #⚠️ KEY LINE: Learns vocabulary and vectorizes text

              self.model.fit(X, labels)
              # ⚠️ KEY LINE: Model learns patterns between text and intent
              
     def predict_intent(self, text: str) -> str:
                
                """
                Predicts intent from user input.
                """
                vector = self.vectorizer.transform([text])
                prediction = self.model.predict(vector)[0]
                
                return prediction
        
              
 
    
        

              
  

            

         

    
