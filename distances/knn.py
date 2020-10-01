from math import floor

def scan_1d_array():
    Z = [float(i) for i in input().split()]
    return Z


def scan_2d_array(M):
    X = []
    for i in range(0, M):
      Xi = [float(j) for j in input().split()]
      X.append(Xi)
    return X

def compute_ln_norm_distance(vector1, vector2, n):
    """
    Arguments:
    vector1 -- A 1D array of size >= 1.
    vector2 -- A 1D array of size equal to size of vector1
    n       -- n in Ln norm distance (>0)

    Returns:
    Computed ln norm distance
    """
    dis = 0
    for i in range(len(vector1)):
        dis += abs(vector1[i] - vector2[i])**n
    return dis**(1/n)

def find_k_nearest_neighbors(train_X, test_example, k, n_in_ln_norm_distance):
    """
    Arguments:
    train_X                          - data of shape (number of observations ,number of features)
    test_example                     - test example of shape (1, number of features) 
    k                                - number of neighbours parameter
    n_in_ln_norm_distance            - n in the ln norm distance formula

    Returns: 
    indices of 1st k - nearest neighbors in train_X, in order with nearest first.
    """
    indices_dist_pairs = []
    index= 0
    for train_elem_x in train_X:
      distance = compute_ln_norm_distance(train_elem_x, test_example,n_in_ln_norm_distance)
      indices_dist_pairs.append([index, distance])
      index += 1
    indices_dist_pairs.sort(key = lambda x: x[1])
    top_k_pairs = indices_dist_pairs[:k]
    top_k_indices = [i[0] for i in top_k_pairs]
    return top_k_indices

def classify_points_using_knn(train_X, train_Y, test_X, k, n_in_ln_norm_distance):
    test_Y = []
    for test_elem_x in test_X:
      top_k_nn_indices = find_k_nearest_neighbors(train_X, test_elem_x, k,n_in_ln_norm_distance)
      top_knn_labels = []

      for i in top_k_nn_indices:
        top_knn_labels.append(train_Y[i])
      Y_values = list(set(top_knn_labels))

      max_count = 0
      most_frequent_label = -1
      for y in Y_values:
        count = top_knn_labels.count(y)
        if(count > max_count):
          max_count = count
          most_frequent_label = y
          
      test_Y.append(most_frequent_label)
    return test_Y

def calculate_accuracy(predicted_Y, actual_Y):
    """
    Arguments:
    predicted_Y - 1D array of predicted target values
    actual_Y - 1D array of true values 

    Returns:
    accuracy
    """
    c = 0
    for i in range(len(predicted_Y)):
        c += (predicted_Y[i] == actual_Y[i])
    
    return c/len(actual_Y)

def get_best_k_using_validation_set(train_X, train_Y, validation_split_percent,n_in_ln_norm_distance):
    """
    Returns best value of k which gives best accuracy
    """
    X = train_X[:(floor((1-(validation_split_percent/100))*len(train_X)))]
    y = train_Y[:(floor((1-(validation_split_percent/100))*len(train_X)))]
    X_test = train_X[(floor((1-(validation_split_percent/100))*len(train_X))):]
    y_test = train_Y[(floor((1-(validation_split_percent/100))*len(train_X))):]
    acc= 0
    for i in range(1,len(train_X)+1):
        acc_old = acc
        acc = calculate_accuracy(classify_points_using_knn(X, y, X_test, i, n_in_ln_norm_distance), y_test)
        if acc <= acc_old:
            break
    return i+1
            

if __name__ == "__main__":
    M = int(input())
    train_X = scan_2d_array(M)
    train_Y = scan_1d_array()
    validation_split_percent = int(input())
    n_ln_norm = int(input())
    best_k = get_best_k_using_validation_set(train_X, train_Y,validation_split_percent ,n_ln_norm)
    print(best_k)
