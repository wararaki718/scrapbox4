from itertools import count
from tempfile import NamedTemporaryFile

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from loader import DataLoader


def main():
    texts =  {
        "text": [
            "just plain boring",
            "entirely predictable and lacks energy",
            "no surprises and very few laughs",
            "very powerful",
            "the most fun film of the summer",
            "just plain boring",
            "entirely predictable and lacks energy",
            "no surprises and very few laughs",
            "very powerful",
            "the most fun film of the summer"
        ]
    }
    df = pd.DataFrame(texts)

    tfidf_vectorizer = TfidfVectorizer()
    count_vectorizer = CountVectorizer()

    print("chunking:")
    with NamedTemporaryFile(mode="wt") as f:
        df.to_csv(f, index=False)
        f.seek(0)

        loader = DataLoader(f.name, chunksize=5, batchsize=1)
        tfidf_vectorizer.fit(map(lambda x: x.text.iloc[0], loader))
        count_vectorizer.fit(map(lambda x: x.text.iloc[0], loader))
        print(tfidf_vectorizer.get_feature_names_out())
        print(count_vectorizer.get_feature_names_out())
    print()

    print("DONE")


if __name__ == "__main__":
    main()
