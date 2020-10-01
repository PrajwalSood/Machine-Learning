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


def mean_normalize(X, column_indices):
    for column_index in column_indices:
        column = X[:,column_index]
        min = np.min(column, axis=0) 
        max = np.max(column, axis=0)
        avg = np.average(column, axis=0)
        difference = max- min
        X[:,column_index] = (column - avg) /difference
    return X


if __name__ == "__main__":
    M = int(input())
    X = scan_data(M)
    column_indices = scan_1d_vector()
    X = mean_normalize(X, column_indices)
    X = list(X)
    X = np.round(X, 3)

    for i in range(M):
        print(*X[i])