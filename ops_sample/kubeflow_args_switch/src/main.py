from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--flag", type=str, default="test")

    return parser.parse_args()


def main():
    args = parse_args()
    
    print(f"args: {args.flag}")

    print("DONE")


if __name__ == "__main__":
    main()
