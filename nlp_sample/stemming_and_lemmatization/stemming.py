from nltk import PorterStemmer
from nltk.tokenize import word_tokenize


class NLTKStemmer:
    def __init__(self):
        self._stemmer = PorterStemmer()

    def stemming(self, text: str) -> list:
        tokens = word_tokenize(text)
        return [self._stemmer.stem(token) for token in tokens]
