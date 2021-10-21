import numpy as np
from loader import Loader

from metrics import ndcg_at_k, mrr_at_k, map_at_k, recall_at_k, count_appeared_docs_at_k, entropy_at_k, gini_at_k


def main():
    loader = Loader()
    filename = "dataset/MQ2008/S1.txt"
    
    df = loader.load(filename)

    ## predict
    df["pred"] = np.random.rand(df.shape[0])

    print(df.shape)
    print(df.head(3))

    ## evaluation
    ndcg_score = ndcg_at_k(df, k=5)
    map_score = map_at_k(df, k=5)
    mrr_score = mrr_at_k(df, k=5)
    recall_score = recall_at_k(df, k=5)
    appeared_score = count_appeared_docs_at_k(df, k=5)
    entropy_score = entropy_at_k(df, k=5)
    gini_score = gini_at_k(df, k=5)

    print(f"ndcg    : {ndcg_score}")
    print(f"map     : {map_score}")
    print(f"mrr     : {mrr_score}")
    print(f"recall  : {recall_score}")
    print(f"num docs: {appeared_score}")
    print(f"entropy : {entropy_score}")
    print(f"gini    : {gini_score}")
    print("DONE")


if __name__ == "__main__":
    main()
