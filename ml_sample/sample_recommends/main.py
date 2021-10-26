from irspack.dataset.movielens import MovieLens1MDataManager

from config import Config
from movie_recommender import MovieKNNRecommender, MovieIALSRecommender


def main():
    config = Config.load("config.yml")
    data_manager = MovieLens1MDataManager()
    df = data_manager.read_interaction()
    print(df.shape)

    user_ids = df.userId.unique()
    item_ids = df.movieId.unique()

    knn_recommender = MovieKNNRecommender(config.asymmetric_cosine_knn_config)
    knn_recommender.fit(df, user_ids, item_ids)
    als_recommender = MovieIALSRecommender(config.ials_config)
    als_recommender.fit(df, user_ids, item_ids)
    print("model trained")
    print("")

    print("get_recommend items:")
    print(knn_recommender.get_recommendations(1))
    print("")
    print(als_recommender.get_recommendations(1))
    
    print("DONE")


if __name__ == "__main__":
    main()
