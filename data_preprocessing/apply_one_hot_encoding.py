import numpy as np

def scan_data():
    X = list(input().split())
    return np.array(X)


def apply_one_hot_encoding(X):
    unique_values = list(set(X))
    unique_values.sort()
    one_hot_encoding_map = {}
    counter = 0
    for x in unique_values:
        one_hot_encoding_map[x] = [0 for i in range(len(unique_values))]
        one_hot_encoding_map[x][counter] = 1
        counter += 1

    one_hot_encoded_X = []
    for x in X:
        one_hot_encoded_X.append(one_hot_encoding_map[x])

    one_hot_encoded_X = np.array(one_hot_encoded_X, dtype=int)
    return one_hot_encoded_X
            


if __name__ == "__main__":
    X = scan_data()
    one_hot_encoded_array = apply_one_hot_encoding(X)
    for i in one_hot_encoded_array:
        print(*i)
