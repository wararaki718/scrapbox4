import torch
import torch.nn.functional as F

from listnet import ListNet


def listnet_loss(y_i: torch.Tensor, z_i: torch.Tensor) -> torch.Tensor:
    py = F.softmax(y_i, dim=0)
    pz = F.softmax(z_i, dim=0)

    return -torch.sum(py * torch.log(pz))


def train(model: ListNet, optimizer: torch.optim.Adam, X_train: torch.Tensor, y_train: torch.Tensor, batch_size: int) -> ListNet:
    model.train()
    for i in range(0, X_train.shape[0], batch_size):
        X_batch = X_train[i:i+batch_size]
        y_batch = y_train[i:i+batch_size]
        
        if len(X_batch) == 0:
            continue

        optimizer.zero_grad()
        y_pred = model(X_batch)
        loss = listnet_loss(y_batch, y_pred)
        loss.backward(retain_graph=True)
        optimizer.step()

    return model
