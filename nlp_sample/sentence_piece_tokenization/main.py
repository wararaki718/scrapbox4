from io import BytesIO

import sentencepiece as spm

from loader import load_text


def main():
    url = "https://raw.githubusercontent.com/google/sentencepiece/master/data/botchan.txt"
    text = load_text(url)

    print("start: train")
    model = BytesIO()
    spm.SentencePieceTrainer.train(
        sentence_iterator=text,
        model_writer=model,
        vocab_size=1000
    )
    print("end: train")

    spp = spm.SentencePieceProcessor(model_proto=model.getvalue())
    print(spp.encode("this is test"))
    print("DONE")


if __name__ == "__main__":
    main()
