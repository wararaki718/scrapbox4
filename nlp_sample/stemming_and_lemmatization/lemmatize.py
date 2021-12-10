import spacy
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


class NLTKLemmatizer:
    def __init__(self):
        self._lemmatizer = WordNetLemmatizer()
    
    def lemmatize(self, text: str) -> list:
        tokens = word_tokenize(text)
        return [self._lemmatizer.lemmatize(token) for token in tokens]


class SpacyLemmatizer:
    def __init__(self, core: str="en_core_web_sm"):
        self._model = spacy.load(core)
    
    def lemmatize(self, text: str) -> list:
        tokens = self._model(text)
        return [token.lemma_ for token in tokens]
