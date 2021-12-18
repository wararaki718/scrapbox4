from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder


def main():
    X = [
        ["test", "sample"],
        ["hello", "world"],
        ["text", "test"],
        ["hello", "hello"],
    ]

    print("one-hot:")
    encoder = OneHotEncoder()
    encoder.fit(X)

    print(encoder.get_feature_names_out())
    print(encoder.transform(X).toarray())
    print()

    print("multi-label binarizer:")
    encoder = MultiLabelBinarizer(sparse_output=True)
    encoder.fit(X)
    
    print(encoder.classes_)
    print(encoder.transform(X).toarray())
    print()

    print("DONE")


if __name__ == "__main__":
    main()
