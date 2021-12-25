import fasttext


def main():
    model_path = "/tmp/lid.176.bin"

    model = fasttext.load_model(model_path)

    sentences = [
        "je mange de la nourriture",
        "hello world",
        "こんにちわ",
        "i have something in this box. こんにちわ"
    ]

    labels, _ = model.predict(sentences)
    print(labels)
    print("DONE")


if __name__ == "__main__":
    main()
