import spacy


def main():
    nlp = spacy.load("en_core_web_sm")

    text = "The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."

    result = nlp(text)
    for ent in result.ents:
        print(f"{ent.text}: {ent.label_}")
    print("DONE")


if __name__ == "__main__":
    main()
