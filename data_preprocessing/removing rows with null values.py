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


def remove_rows_with_null_values(X):
    X_with_no_nan = []
    for row in X:
        row_contains_nan = True in np.isnan(row)
        if not row_contains_nan:
            X_with_no_nan.append(row)
    return X_with_no_nan


if __name__ == "__main__":
    M = int(input())
    X = scan_data(M)

    X = remove_rows_with_null_values(X)

    for i in X:
        print(*i)