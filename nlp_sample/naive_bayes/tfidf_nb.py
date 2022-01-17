from typing import Tuple

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_nb(X_train: np.ndarray, X_test: np.ndarray, y_train: np.ndarray, y_test: np.ndarray) -> Tuple[float, float]:
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(X_train)

    model = MultinomialNB()
    model.fit(X_train, y_train)
    train_score = model.score(X_train, y_train)

    X_test = vectorizer.transform(X_test)
    test_score = model.score(X_test, y_test)
    
    return train_score, test_score
