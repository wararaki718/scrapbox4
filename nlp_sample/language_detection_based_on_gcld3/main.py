import gcld3


def show_result(text: str, results: list):
    print(text)
    for result in results:
        print(f"-> {result.language}")
    print()


def main():
    detector = gcld3.NNetLanguageIdentifier(min_num_bytes=10, max_num_bytes=1000)
    sentences = [
        "je mange de la nourriture",
        "i have something in this box.",
        "こんにちわ",
        "i have something in this box. こんにちわ"
    ]
    for sentence in sentences:
        results = detector.FindTopNMostFreqLangs(text=sentence, num_langs=2)
        show_result(sentence, results)
    print("DONE")


if __name__ == "__main__":
    main()
