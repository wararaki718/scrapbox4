import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split

from loader import load_news
from count_nb import count_nb
from onehot_nb import one_hot_nb
from tfidf_nb import tfidf_nb


def show(train_score: float, test_score: float):
    print(f"train score: {train_score}")
    print(f"test score : {test_score}")
    print()


def main():
    X, y = load_news()

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, shuffle=True, random_state=42)
    
    print("One-hot encoding + Naive Bayes (Bernoulli)")
    train_score, test_score = one_hot_nb(X_train, X_test, y_train, y_test)
    show(train_score, test_score)

    print("Count vectorizer + Naive Bayes (Multinomial)")
    train_score, test_score = count_nb(X_train, X_test, y_train, y_test)
    show(train_score, test_score)

    print("TF-IDF vectorizer + Naive Bayes (Multinomial)")
    train_score, test_score = tfidf_nb(X_train, X_test, y_train, y_test)
    show(train_score, test_score)

    print("DONE")


if __name__ == "__main__":
    main()
