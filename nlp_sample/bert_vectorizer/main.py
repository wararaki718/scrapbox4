import torch
from transformers import AutoTokenizer, AutoModel
from typing import Union


def try_gpu(x: Union[torch.Tensor, AutoModel]) -> Union[torch.Tensor, AutoModel]:
    if torch.cuda.is_available():
        return x.cuda()
    else:
        return x


def main():
    model_name = "roberta-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = try_gpu(AutoModel.from_pretrained(model_name))
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
    print(tokens.keys())
    out = model(
        input_ids=try_gpu(tokens["input_ids"]),
        attention_mask=try_gpu(tokens["attention_mask"])
    )
    print(type(out))

    result = out.last_hidden_state.mean(1).detach().cpu().numpy()
    print(result.shape)

    print("DONE")


if __name__ == "__main__":
    main()
