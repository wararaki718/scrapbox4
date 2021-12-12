import nltk
import spacy
from nltk import pos_tag, word_tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')


class NLTKPosAnalyzer:
    def __init__(self):
        pass

    def analyze(self, text: str) -> list:
        tokens = pos_tag(word_tokenize(text))
        return [token[1] for token in tokens]


class SpacyPosAnalyzer:
    def __init__(self):
        self._model = spacy.load("en_core_web_sm")

    def analyze(self, text: str) -> list:
        doc = self._model(text)
        return [token.pos_ for token in doc]
