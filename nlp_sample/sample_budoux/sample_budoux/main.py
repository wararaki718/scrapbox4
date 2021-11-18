import budoux

def main():
    parser = budoux.load_default_japanese_parser()
    text = "今日は東京タワーでご飯を食べます。"
    tokens = parser.parse(text)
    print(tokens)
    print("DONE")


if __name__ == "__main__":
    main()
