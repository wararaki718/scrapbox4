import numpy as np


def min_edit_distance(source: str, target: str) -> int:
    n = len(source)+1
    m = len(target)+1

    D = np.zeros((n, m))
    for i in range(1, n):
        D[i, 0] = D[i-1, 0] + 1 # delete
    
    for i in range(1, m):
        D[0, i] = D[0, i-1] + 1 # insert
    
    for i in range(n-1):
        for j in range(m-1):
            cost = 0 if source[i] == target[j] else 1
            D[i+1, j+1] = min(
                D[i, j+1] + 1, # delete
                D[i, j] + cost, # replace
                D[i+1, j] + 1 # insert
            )

    return int(D[n-1, m-1])


if __name__ == "__main__":
    source = "ntion"
    target = "ution"

    print(f"{source} - {target}: {min_edit_distance(source, target)}")
    print("DONE")
