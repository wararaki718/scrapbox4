import scipy.sparse as sps
import torch


def main():
    # torch sparse tensor
    idx = [[0, 1, 1], [2, 0, 2]]
    val = [3, 4, 5]
    s = torch.sparse_coo_tensor(idx, val, (2, 3))
    print(s)
    print(s.to_dense())
    print()
    
    # scipy sparse matrix
    sp = sps.csr_matrix([[1, 0, 1], [0, 2, 0], [3, 3, 0], [0, 0, 4], [0, 5, 5]])
    print(sp)
    print(sp.todense())
    print()

    # scipy coo sparse -> torch coo sparse
    s = sp.tocoo()
    s = torch.sparse_coo_tensor([s.row, s.col], s.data, s.shape)
    print(s)
    print(s.to_dense())
    print()

    print(sp[0:2].todense())
    print()

    if torch.cuda.is_available():
        s = s.cuda()
        print(s)
    
    print("DONE")


if __name__ == "__main__":
    main()
