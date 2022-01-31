import os

import scipy.sparse as sps


def main():
    a = [
        [0, 0, 1],
        [0, 2, 0]
    ]
    s = sps.csr_matrix(a)
    print(s.shape)

    filename = "sample.npz"
    with open(filename, "wb") as f:
        sps.save_npz(f, s)
    print(os.listdir())
    print()

    with open(filename, "rb") as f:
        t = sps.load_npz(f)
    print(t.shape)

    os.remove(filename)
    print(os.listdir())
    print()
    print("DONE")


if __name__ == "__main__":
    main()
