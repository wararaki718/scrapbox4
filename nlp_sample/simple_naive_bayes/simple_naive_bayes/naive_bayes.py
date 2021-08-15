from collections import Counter, defaultdict
import math
from typing import List

class NaiveBayes:
    def train(self, D: List[str], C: List[int]) -> None:
        N_doc = len(D)
        N_c = Counter(C)

        self.log_piror = {
            c: math.log(n_c/N_doc) for c, n_c in N_c.items()
        }

        self.V = set()
        for d in D:
            self.V |= set(d.split())

        bigdoc = defaultdict(list)
        for d, c in zip(D, C):
            bigdoc[c] += d.split()
        
        self.loglikelihood = defaultdict(dict)
        for c in N_c:
            for w in self.V:
                count_w_c = bigdoc[c].count(w)
                self.loglikelihood[w][c] = math.log(
                    (count_w_c+1) / sum(map(lambda w_: bigdoc[c].count(w_)+1, self.V))
                )

    def test(self, testdoc: str, C: List[int]) -> int:
        sum_ = dict()
        for c in C:
            sum_[c] = self.log_piror[c]
            for word in testdoc.split():
                if word in self.V:
                    sum_[c] += self.loglikelihood[word][c]

        best_c = C[0]
        for c in C:
            if sum_[best_c] < sum_[c]:
                best_c = c        
        return best_c
