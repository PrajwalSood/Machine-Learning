import numpy as np


def scan_data(M):
    X = []
    for i in range(M):
        row = list(map(float, input().split()))
        X.append(row)
    return np.array(X)


def get_correlation_matrix(X):
    num_vars = len(X[0])
    m = len(X)
    correlation_matix = np.zeros((num_vars,num_vars))
    for i in range(0,num_vars):
        for j in range(i,num_vars):
            mean_i = np.mean(X[:,i])
            mean_j = np.mean(X[:,j])
            std_dev_i = np.std(X[:,i])
            std_dev_j = np.std(X[:,j])
            numerator = np.sum((X[:,i]-mean_i)*(X[:,j]-mean_j))
            denominator = (m)*(std_dev_i)*(std_dev_j)
            corr_i_j = numerator/denominator    
            correlation_matix[i][j] = corr_i_j
            correlation_matix[j][i] = corr_i_j
    return correlation_matix


if __name__ == "__main__":
    M = int(input())
    X = scan_data(M)
    correlation_matrix = get_correlation_matrix(X)
    N = len(X[0])
    for i in range(N):
        correlation_matrix[i] = np.round(correlation_matrix[i], 3)

    for i in range(N):
        print(*correlation_matrix[i])
