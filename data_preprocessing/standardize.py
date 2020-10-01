import numpy as np

def scan_1d_vector():
  Z = [int(i) for i in input().split()]
  Z = np.array(Z)
  return Z

def scan_data(M):
    X = []
    for i in range(M):
        row = list(map(float, input().split()))
        X.append(row)
    return np.array(X)


def standardize(X, column_indices):
    for column_index in column_indices:
        column = X[:,column_index]
        mean = np.mean(column, axis=0)
        std = np.std(column, axis=0)
        X[:,column_index] = (column - mean) /std
    return X


if __name__ == "__main__":
    M = int(input())
    X = scan_data(M)
    column_indices = scan_1d_vector()
    X = standardize(X, column_indices)
    X = np.round(X, 3)
    X = list(X)

    for i in range(M):
        print(*X[i])