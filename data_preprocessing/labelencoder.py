import numpy as np
def scan_data():
    X = list(input().split())
    return np.array(X)


def convert_to_numerical_labels(X):
    uniques_values = list(set(X))
    uniques_values.sort()

    #preparing map of unique values to numerical labels
    unique_values_labels_map = {}
    for i in range(0,len(uniques_values)):
        unique_values_labels_map[uniques_values[i]]=i
    
    #converting data to numerical labels 
    X_numerical = []
    for i in range(0,len(X)):
        numerical_value = unique_values_labels_map[X[i]]
        X_numerical.append(numerical_value)

    return X_numerical
    


if __name__ == "__main__":
    X = scan_data()
    label_encoded_X = convert_to_numerical_labels(X)

    print(*label_encoded_X)
