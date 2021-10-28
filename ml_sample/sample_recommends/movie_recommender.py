from dataclasses import asdict

import numpy as np
import pandas as pd
from scipy import sparse as sps
from irspack.recommenders import AsymmetricCosineKNNRecommender, IALSRecommender
from irspack.utils import IDMappedRecommender

from config import AsymmetricCosineKNNConfig, IALSConfig


class MovieKNNRecommender:
    def __init__(self, config: AsymmetricCosineKNNConfig) -> None:
        self._config = config
    
    def fit(self, interactions: pd.DataFrame, user_ids: pd.Series, item_ids: pd.Series):
        self._userid2index = {
            user_id: i for i, user_id in enumerate(user_ids)
        }
        self._index2itemid = item_ids
        self._itemid2index = {
            item_id: i for i, item_id in enumerate(item_ids)
        }
        user_interactions = interactions.userId.map(self._userid2index)
        item_interactions = interactions.movieId.map(self._itemid2index)

        self._X = sps.csr_matrix(
            (
                np.ones(interactions.shape[0], dtype=np.int32),
                (user_interactions, item_interactions)
            ),
            shape=(user_ids.shape[0], item_ids.shape[0])
        )
        recommender = AsymmetricCosineKNNRecommender(
            self._X,
            **asdict(self._config)
        )
        recommender.learn()
        self._W = recommender.W
    
    def get_recommendations(self, user_id: int, topn: int=5) -> pd.DataFrame:
        user_index = [self._userid2index[user_id]]
        scores = self._X[user_index, :].dot(self._W)

        row = scores.getrow(0)
        indices = np.argsort(row.data)[::-1]
        item_ids = [
            self._index2itemid[row.indices[index]] for index in indices
        ]

        return pd.DataFrame.from_dict(
            {
                "user_id": [user_id]*len(item_ids),
                "movie_id" : item_ids,
                "score": row.data[indices]
            }
        ).head(topn)


class MovieIALSRecommender:
    def __init__(self, config: IALSConfig) -> None:
        self._config = config
    
    def fit(self, interactions: pd.DataFrame, user_ids: pd.Series, item_ids: pd.Series):
        self._userid2index = {
            user_id: i for i, user_id in enumerate(user_ids)
        }
        self._index2itemid = item_ids
        self._itemid2index = {
            item_id: i for i, item_id in enumerate(item_ids)
        }
        user_interactions = interactions.userId.map(self._userid2index)
        item_interactions = interactions.movieId.map(self._itemid2index)

        self._X = sps.csr_matrix(
            (
                np.ones(interactions.shape[0], dtype=np.int32),
                (user_interactions, item_interactions)
            ),
            shape=(user_ids.shape[0], item_ids.shape[0])
        )
        recommender = IALSRecommender(
            self._X,
            **asdict(self._config)
        )
        recommender.learn()
        self._mapped_recommender = IDMappedRecommender(recommender, user_ids, item_ids)
    
    def get_recommendations(self, user_id: int, topn: int=5) -> pd.DataFrame:
        results = self._mapped_recommender.get_recommendation_for_known_user_id(user_id, topn)
        return pd.DataFrame([
            [user_id, *result] for result in results
        ], columns=["user_id", "item_id", "score"])
