from typing import List, Optional

from .analyzer import Analyzer
from .spell_checker import SpellChecker
from .spell_corrector import SpellCorrector


# Noisy Channel Model
class NCM:
    def __init__(self,
                 analyzer: Optional[Analyzer]=None,
                 n: int=3,
                 tp: int=0,
                 ts: int=-2,
                 n_candidate_char: int=300,
                 n_candidate_word: int=5):
        self._checker = SpellChecker(n, tp, ts, n_candidate_char, n_candidate_word)
        self._corrector = SpellCorrector(analyzer, n)
    
    def fit(self, sentences: List[str]):
        self._checker.fit(sentences)
        self._corrector.fit(sentences)
    
    def correct(self, sentence: str) -> list:
        candidates = self._checker.check(sentence)
        results = self._corrector.correct(sentence, candidates)
        return results
