from transformers import AutoTokenizer, AutoModel


def main():
    model_name = "roberta-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    max_legnth = 128

    texts = [
        "hello, world!",
        "i have a pen",
        "this is an apple"
    ]
    tokens = tokenizer.batch_encode_plus(
        texts,
        truncation=True,
        add_special_tokens=True,
        max_length=max_legnth,
        padding="max_length",
        return_tensors="pt"
    )
    out = model(**tokens)
    print(type(out))

    result = out.last_hidden_state.mean(1).detach().cpu().numpy()
    print(result.shape)

    print("DONE")


if __name__ == "__main__":
    main()
