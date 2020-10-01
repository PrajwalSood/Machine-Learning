import numpy as np

def scan_correlation_matrix(M):
    X = []
    for i in range(M):
        row = list(map(float, input().split()))
        X.append(row)
    return np.array(X)

def select_features(corr_mat, T1, T2):
    n=len(corr_mat)
    filtered_features = []
    for i in range(1,n):
        if (abs(corr_mat[i][0]) > T1):
            filtered_features.append(i)
    m = len(filtered_features)
    removed_features = []
    selected_features = list(filtered_features)
    for i in range(0,m):
        for j in range(i+1,m):
            f1 = filtered_features[i]
            f2 = filtered_features[j]
            if (f1 not in removed_features and f2 not in removed_features): 
                if (abs(corr_mat[f1][f2]) > T2):
                    selected_features.remove(f2)
                    removed_features.append(f2)

    return selected_features

if __name__ == "__main__":
    M = int(input())
    corr_mat = scan_correlation_matrix(M)
    T1 = float(input())
    T2 = float(input())
    
    selected_features = select_features(corr_mat, T1, T2)
    print(*selected_features)