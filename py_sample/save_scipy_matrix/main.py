import os
import dill
import scipy.sparse as sps


def main():
    print(os.listdir("."))
    print()

    a = [[1, 0], [2, 0]]
    mat = sps.csr_matrix(a)
    print(mat)
    print()

    print("dump:")
    with open("tmp.mat", "wb") as f:
        dill.dump(mat, f)
    print(os.listdir("."))
    print()

    print("load:")
    with open("tmp.mat", "rb") as f:
        m = dill.load(f)
    print()

    print(m)
    print()

    os.remove("tmp.mat")
    print(os.listdir("."))
    print()

    print("DONE")


if __name__ == "__main__":
    main()
