import numpy as np
import torch

from ranknet import RankNet


def pairwise_loss(s_i: torch.Tensor, s_j: torch.Tensor, S_ij: int, sigma: float=1.0) -> float:
    C = torch.log1p(torch.exp(-sigma * (s_i - s_j)))

    if S_ij == -1:
        C += sigma * (s_i - s_j)
    elif S_ij == 0:
        C += 0.5 * sigma * (s_i - s_j)
    elif S_ij == 1:
        pass
    else:
        raise ValueError
    
    return C


def train(model: RankNet, optimizer: torch.optim.Adam, X: torch.Tensor, y: torch.Tensor, batch_size: int, n_sampling_combs: int) -> RankNet:
    indices = torch.randperm(X.shape[0])
    X = X[indices]
    y = y[indices]

    model.train()
    for k in range(0, X.shape[0], batch_size):
        X_batch = X[k:k+batch_size]
        y_batch = y[k:k+batch_size]

        if X_batch.shape[0] == 0:
            continue
        
        optimizer.zero_grad()
        loss = torch.zeros(1).cuda()

        y_pred = model(X_batch)

        for _ in range(n_sampling_combs):
            i, j = np.random.choice(range(min(batch_size, y_pred.shape[0])), 2)

            s_i = y_pred[i]
            s_j = y_pred[j]

            if y_batch[i] > y_batch[j]:
                s_ij = 1
            elif y_batch[i] == y_batch[j]:
                s_ij = 0
            else:
                s_ij = -1
            
            loss += pairwise_loss(s_i, s_j, s_ij)

        loss.backward()
        optimizer.step()
        
    return model
