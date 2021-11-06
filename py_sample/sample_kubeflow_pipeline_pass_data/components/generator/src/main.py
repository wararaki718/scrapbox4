from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd


def parse() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--outputpath", type=Path, default="data.csv")
    return parser.parse_args()


def main():
    parser = parse()
    df = pd.DataFrame([
        ["generater", True],
        ["preprocessor", False],
        ["trainer", False],
        ["evaluator", False]
    ], columns=["name", "status"])
    print(df)

    if not parser.outputpath.parents[0].exists():
        parser.outputpath.parents[0].mkdir(parents=True)

    df.to_csv(parser.outputpath, index=False)
    print("DONE")


if __name__ == "__main__":
    main()
