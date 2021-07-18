import itertools
from typing import Dict, List, Optional

from nltk.lm import Vocabulary
from nltk.lm.models import MLE
from nltk.util import ngrams

from .analyzer import Analyzer


class SpellCorrector:
    def __init__(self,
                 analyzer: Optional[Analyzer]=None,
                 n: int=3):
        self._n_gram = n

        if analyzer is None:
            self._analyzer = Analyzer()
        else:
            self._analyzer = analyzer

    def fit(self, sentences: List[str]):
        tokenized_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) == 0:
                continue
            tokenized_sentence = [token for token in self._analyzer.analyze(sentence)]
            tokenized_sentence = ["__BOS__"] + tokenized_sentence + ["__EOS__"]
            tokenized_sentences.append(tokenized_sentence)
        
        word_vocabulary = Vocabulary(itertools.chain.from_iterable(tokenized_sentences))
        word_ngram = [ngrams(sentence, self._n_gram) for sentence in tokenized_sentences]

        self._wlm = MLE(order=self._n_gram, vocabulary=word_vocabulary)
        self._wlm.fit(word_ngram)

    def correct(self,
               sentence: str,
               candidates: dict) -> list:
        results = []
        for i, words in candidates.items():
            for word in words:
                l = sentence[:i] + word + sentence[i+len(word):]
                tokens = [token for token in self._analyzer.analyze(l)]

                pl = 1.0
                is_calc = False
                for context in ngrams(tokens, self._n_gram):
                    pl *= self._wlm.score(context[-1], context[:-1])
                    is_calc = True
                
                if is_calc and pl > 0:
                    results.append([l, pl])
        return results
