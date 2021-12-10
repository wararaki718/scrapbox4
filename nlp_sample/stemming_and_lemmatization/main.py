import nltk

from lemmatize import NLTKLemmatizer, SpacyLemmatizer
from stemming import NLTKStemmer


nltk.download('wordnet')


def main():
    text = "I have a pen. I had some pens. I am writing research papers."

    print("nltk stemming:")
    nltk_stemmer = NLTKStemmer()
    results = nltk_stemmer.stemming(text)
    print(results)
    print()

    print("nltk lemmatize:")
    nltk_lemmatizer = NLTKLemmatizer()
    results = nltk_lemmatizer.lemmatize(text)
    print(results)
    print()

    print("spacy lemmatize:")
    spacy_lemmatizer = SpacyLemmatizer()
    results = spacy_lemmatizer.lemmatize(text)
    print(results)
    print()
    print("DONE")


if __name__ == "__main__":
    main()
