import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize NLP tools once (efficient & best practice)
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


def preprocess_text(text: str) -> list:
    """
    Cleans and prepares user input for intent detection.
    """

    # Convert to lowercase
    text = text.lower()
    # ⚠️ KEY LINE: Normalization ensures consistency

    # Tokenize text (split into words)
    tokens = word_tokenize(text)
    # ⚠️ KEY LINE: Tokenization is the foundation of NLP

    # Remove stopwords and non-alphabetic tokens
    cleaned_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalpha() and word not in stop_words
    ]
    # ⚠️ KEY LINE: Lemmatization reduces words to base form

    return cleaned_tokens
