import numpy as np
from implicit.als import AlternatingLeastSquares
from implicit.datasets.movielens import get_movielens
from implicit.nearest_neighbours import bm25_weight


def main():
    titles, ratings = get_movielens("100k")

    ratings.data[ratings.data < 4.0] = 0
    ratings.eliminate_zeros()
    ratings.data = np.ones(len(ratings.data))
    ratings = (bm25_weight(ratings, B=0.9) * 5).tocsr()

    user_ratings = ratings.T.tocsr()
    print(f"user_ratings: {user_ratings.shape}")
    print()

    model = AlternatingLeastSquares()
    model.fit(user_ratings)

    user_count = np.ediff1d(ratings.indptr)
    to_generate = sorted(np.arange(len(titles)), key=lambda x: -user_count[x])

    print("output result:")
    for movieid in to_generate:
        if ratings.indptr[movieid] != ratings.indptr[movieid+1]:
            title = titles[movieid]
            print(f"'{title}' similar:")
            for other, score in zip(*model.similar_items(movieid, 11)):
                print(f"  {titles[other]}: {score}")
            break
    
    print("DONE")


if __name__ == "__main__":
    main()
