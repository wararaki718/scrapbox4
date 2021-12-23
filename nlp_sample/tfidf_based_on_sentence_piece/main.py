import logging
from io import BytesIO, StringIO

import sentencepiece as spm
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    texts = fetch_20newsgroups(
        subset="train",
        categories=["comp.graphics", "sci.med"],
        shuffle=True,
        random_state=42
    )
    X = texts.data
    logger.info(len(X))
    logger.info(type(X))

    logger.info("start: spm train")
    model = BytesIO()
    spm.SentencePieceTrainer.train(
        sentence_iterator=StringIO("\n".join(X)),
        model_writer=model,
    )
    logger.info("end  : spm train")

    logger.info("start: tfidf train")
    spp = spm.SentencePieceProcessor(model_proto=model.getvalue())
    vectorizer = TfidfVectorizer(
        analyzer=lambda x: spp.encode(x)
    )
    vectorizer.fit(X)
    logger.info("end  : tfidf train")

    names = list(vectorizer.get_feature_names_out())
    logger.info(names[:10])
    logger.info(len(names))
    logger.info("DONE")


if __name__ == "__main__":
    main()
