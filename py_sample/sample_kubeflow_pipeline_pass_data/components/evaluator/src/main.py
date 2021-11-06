from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd


def parse() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--inputpath", type=Path, default="data.csv")
    parser.add_argument("--outputpath", type=Path, default="data.csv")

    return parser.parse_args()


def main():
    parser = parse()
    df = pd.read_csv(parser.inputpath)
    df.loc[df.name == "evaluator", "status"] = True
    print(df)

    if not parser.outputpath.parents[0].exists():
        parser.outputpath.parents[0].mkdir(parents=True)

    df.to_csv(parser.outputpath, index=False)
    print("DONE")


if __name__ == "__main__":
    main()
