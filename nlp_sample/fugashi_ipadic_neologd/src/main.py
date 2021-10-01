from fugashi import GenericTagger
import ipadic


def main():
    neologd_path = "/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd"

    tagger = GenericTagger(f"{ipadic.MECAB_ARGS} -d {neologd_path}")

    text = "私は東京タワーでご飯を食べました。"
    for token in tagger(text):
        print(token)
    print("DONE")


if __name__ == "__main__":
    main()
