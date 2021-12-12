from sklearn.feature_extraction.text import TfidfVectorizer

from analyzer import NLTKPosAnalyzer, SpacyPosAnalyzer


def main():
    text = "I have a pen. I eat an apple!"
    nltk_analyzer = NLTKPosAnalyzer()
    spacy_analyzer = SpacyPosAnalyzer()

    print("NLTK:")
    print(nltk_analyzer.analyze(text))
    print()
    print("spaCy:")
    print(spacy_analyzer.analyze(text))
    print()

    nltk_vectorizer = TfidfVectorizer(analyzer=nltk_analyzer.analyze)
    spacy_vectorizer = TfidfVectorizer(analyzer=spacy_analyzer.analyze)
    nltk_vectorizer.fit([text])
    spacy_vectorizer.fit([text])
    print(nltk_vectorizer.get_feature_names_out())
    print(spacy_vectorizer.get_feature_names_out())
    print("DONE")


if __name__ == "__main__":
    main()
