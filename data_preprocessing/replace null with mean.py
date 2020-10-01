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


def replace_null_values_with_mean(X):
    #Obtain mean of columns
    col_mean = np.round(np.nanmean(X, axis=0), 3)

    #Find indicies that we need to replace
    inds = np.where(np.isnan(X))

    #Place column means in the indices. Align the arrays using take
    X[inds] = np.take(col_mean, inds[1])
    return X


if __name__ == "__main__":
    M = int(input())
    X = scan_data(M)

    X = replace_null_values_with_mean(X)

    for i in X:
        print(*i)