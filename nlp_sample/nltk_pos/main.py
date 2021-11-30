import nltk
from nltk import pos_tag, word_tokenize

# download tagger
nltk.download('averaged_perceptron_tagger')

# download tokenizer
nltk.download('punkt')


def main():
    text = "I have a pen. I eat an apple."

    print(pos_tag(word_tokenize(text)))
    print("DONE")


if __name__ == "__main__":
    main()
