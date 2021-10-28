import pandas as pd
import torch
import pandas as pd

from metrics import ndcg_at_k, map_at_k, mrr_at_k
from ranknet import RankNet


def evaluate(df: pd.DataFrame, k: int=10):
    ndcg_score = ndcg_at_k(df, k=k)
    map_score = map_at_k(df, k=k)
    mrr_score = mrr_at_k(df, k=k)
    
    print(f"ndcg@{k}: {ndcg_score}")
    print(f"map@{k} : {map_score}")
    print(f"mrr@{k} : {mrr_score}")


def valid(model: RankNet, X: torch.Tensor, y: torch.Tensor, df: pd.DataFrame):
    model.eval()
    with torch.no_grad():
        y_pred = model(X)
        df["pred"] = y_pred.cpu().detach().numpy().copy()
        
        evaluate(df)
