from naive_bayes import NaiveBayes


def main():
    D = [
        "just plain boring",
        "entirely predictable and lacks energy",
        "no surprises and very few laughs",
        "very powerful",
        "the most fun film of the summer"
    ]
    C = [0, 0, 0, 1, 1]
    testdoc = "predicable with no fun"
    model = NaiveBayes()
    model.train(D, C)
    result = model.test(testdoc, list(set(C)))
    print(f"testdoc: {result}")
    print("DONE")


if __name__ == "__main__":
    main()
