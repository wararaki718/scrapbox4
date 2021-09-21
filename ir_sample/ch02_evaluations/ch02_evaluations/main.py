import numpy as np
from sklearn.metrics import average_precision_score, f1_score, precision_score, recall_score

from metrics import precision_at_k, recall_at_k


def main():
    n = 10
    k = 5
    y_pred = np.random.randint(2, size=n)
    y_true = np.random.randint(2, size=n)

    print("[data]")
    print(f"y_pred : {y_pred}")
    print(f"y_true : {y_true}")
    print("")
    
    print("[evaluations]")
    print(f"precision     : {precision_score(y_true, y_pred)}")
    print(f"recall        : {recall_score(y_true, y_pred)}")
    print(f"f1-score      : {f1_score(y_true, y_pred)}")
    print(f"map           : {average_precision_score(y_true, y_pred)}")
    print(f"precision@{k}   : {precision_at_k(y_true, y_pred, k)}")
    print(f"recall@{k}      : {recall_at_k(y_true, y_pred, k)}")
    print("DONE")


if __name__ == "__main__":
    main()
