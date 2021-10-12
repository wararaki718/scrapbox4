import numpy as np

from metrics import precision_at_k, recall_at_k, ndcg_at_k, entropy_at_k, gini_at_k, map_at_k, mrr_at_k


def main():
    print("## model evaluation:")
    interaction = np.random.randint(2, size=20)
    score = np.random.rand(20)
    print(f"interaction: {interaction}")
    print(f"score       : {score}")
    print("")

    print("evaluate (iteractions):")
    precision = precision_at_k(interaction, score)
    recall = recall_at_k(interaction, score)
    ndcg = ndcg_at_k(interaction, score)

    print(f"precision: {precision}")
    print(f"recall   : {recall}")
    print(f"ndcg     : {ndcg}")
    print("")

    print("## item evaluation")
    all_items = np.arange(1, 11)
    recommends = np.array([1, 2, 3, 1, 2, 3, 6, 2, 1, 1])
    print(f"all items: {all_items}")
    print(f"recommend: {recommends}")
    print("")

    print("evaluate (appeared items):")
    entropy = entropy_at_k(all_items, recommends, k=5)
    gini = gini_at_k(all_items, recommends, k=5)
    print(f"entropy: {entropy}")
    print(f"gini   : {gini}")
    print("")

    print("## users evaluation")
    interactions = np.random.randint(2, size=400).reshape(-1, 20)
    scores = np.random.rand(400).reshape(-1, 20)
    print(f"interactions : {interactions.shape}")
    print(f"scores       : {scores.shape}")
    print("")
    
    print("evaluate (users x items):")
    map_ = map_at_k(interactions, scores, k=10)
    mrr = mrr_at_k(interactions, scores, k=10)
    print(f"map : {map_}")
    print(f"mrr : {mrr}")
    print("")

    print("DONE")


if __name__ == "__main__":
    main()
