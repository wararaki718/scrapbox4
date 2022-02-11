import numpy as np
import pandas as pd
import scipy.sparse as sps
from lightfm import LightFM


def main():
    interactions = pd.DataFrame([
        ["user0", "item0"],
        ["user0", "item1"],
        ["user0", "item3"],
        ["user1", "item2"],
        ["user2", "item0"],
        ["user2", "item3"]
    ], columns=["user_id", "item_id"])

    user2idx = {user_id: idx for idx, user_id in enumerate(sorted(interactions.user_id.unique()))}
    item2idx = {item_id: idx for idx, item_id in enumerate(sorted(interactions.item_id.unique()))}

    interactions["user_id"] = interactions.user_id.map(user2idx)
    interactions["item_id"] = interactions.item_id.map(item2idx)

    X = sps.coo_matrix((np.ones(interactions.shape[0]), (interactions.user_id.values, interactions.item_id.values)))

    model = LightFM(no_components=2)
    model.fit(X)

    results = model.predict(interactions.user_id.values, interactions.item_id.values)
    print("interaction:")
    print(X.toarray())
    print()

    print("predict:")
    print(results)
    print("DONE")


if __name__ == "__main__":
    main()
    