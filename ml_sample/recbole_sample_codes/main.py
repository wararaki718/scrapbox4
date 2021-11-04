from irspack import optimizers
import scipy.sparse as sps

from irspack.dataset.movielens import MovieLens100KDataManager
from irspack.evaluator import Evaluator
from irspack.optimizers import BPRFMOptimizer
from irspack.split import split_dataframe_partial_user_holdout

from recbole.quick_start import run_recbole


def use_irspack() -> tuple:
    BASE_CUTOFF = 20
    data_manager = MovieLens100KDataManager()
    df_all = data_manager.read_interaction()
    data_all, _ = split_dataframe_partial_user_holdout(
        df_all,
        "userId",
        "movieId",
        test_user_ratio=0.2,
        val_user_ratio=0.2,
        heldout_ratio_test=0.5,
        heldout_ratio_val=0.5
    )

    data_train = data_all["train"]
    data_test = data_all["test"]
    data_val = data_all["val"]

    X_train_all: sps.csr_matrix = sps.vstack(
        [data_train.X_train, data_val.X_train, data_test.X_train], format="csr"
    )
    X_train_val_all: sps.csr_matrix = sps.vstack(
        [data_train.X_all, data_val.X_all, data_test.X_train], format="csr"
    )
    valid_evaluator = Evaluator(
        ground_truth=data_val.X_test,
        offset=data_train.n_users,
        cutoff=BASE_CUTOFF,
    )
    test_evaluator = Evaluator(
        ground_truth=data_test.X_test,
        offset=data_train.n_users + data_val.n_users,
        cutoff=BASE_CUTOFF,
    )

    n_trials = 40
    optimizer = BPRFMOptimizer(X_train_all, valid_evaluator)
    (best_param, validation_results) = optimizer.optimize(
        timeout=14400, n_trials=n_trials
    )

    print("validation results:")
    print(validation_results)
    print("")

    test_recommender = optimizer.recommender_class(X_train_val_all, **best_param)
    test_recommender.learn()
    test_scores = test_evaluator.get_scores(test_recommender, [10])

    print("test scores:")
    print(test_scores)
    print("")

    return test_scores, validation_results


def use_recbole():
    model = "BPR"
    dataset = "ml-100k"
    
    run_recbole(model=model, dataset=dataset)
    print("DONE")


def main():
    test_result, validation_result = use_irspack()
    use_recbole()

    print("irspack results:")
    print(test_result)


if __name__ == "__main__":
    main()
