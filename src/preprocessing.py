import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

class Preprocessing:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        # Tokenize the text
        words = word_tokenize(text)
        # Remove stopwords
        filtered_words = [w for w in words if w.lower() not in self.stop_words]
        return ' '.join(filtered_words)
