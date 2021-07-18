from ncm import Analyzer, NCM


def main():
    filename = "text/peachy/peachy-4304732.txt"
    sentences = []
    with open(filename, "r") as f:
        for line in f.readlines()[2:]:
            s = line.strip()
            if len(s) == 0:
                continue
            sentences.append(s)
    print(f"the number of sentences: {len(sentences)}")

    analyzer = Analyzer()
    ncm = NCM(analyzer=analyzer)
    ncm.fit(sentences)

    sentence = "アミノアミノクレンジング"
    results = ncm.correct(sentence)
    for result in results:
        print(result)
    print("DONE")


if __name__ == "__main__":
    main()
