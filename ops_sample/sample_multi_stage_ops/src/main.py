import pandas as pd

from sample import plus


def main():
    df = pd.DataFrame([
        [1, 2],
        [2, 3]
    ], columns=["a", "b"])

    print(df)
    df["c"] = df.apply(lambda row: plus(row.a, row.b), axis=1)
    print(df)
    print("DONE")


if __name__ == "__main__":
    main()
