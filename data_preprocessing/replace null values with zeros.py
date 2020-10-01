import numpy as np


def scan_data(M):
    X = []
    for i in range(M):
        row = list(input().split())
        for j in range(len(row)):
            if row[j] == 'null':
                row[j] = np.NaN
            else:
                row[j] = float(row[j])
        X.append(row)

    X = np.array(X)
    return X


def replace_null_values_with_zeros(X):
    array_with_true_where_nan = np.isnan(X)
    X[array_with_true_where_nan] = 0
    return X


if __name__ == "__main__":
    M = int(input())
    X = scan_data(M)

    X = replace_null_values_with_zeros(X)

    for i in X:
        print(*i)