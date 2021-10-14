import numpy as np

from module import plus


def main():
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    result = plus(a, b)
    print(result)


if __name__ == "__main__":
    main()
