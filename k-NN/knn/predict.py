import numpy as np
import csv
import sys
import pandas as pd

from validate import validate

"""
Predicts the target values for data in the file at 'test_X_file_path'.
Writes the predicted values to the file named "predicted_test_Y_knn.csv". It should be created in the same directory where this code file is present.
This code is provided to help you get started and is NOT a complete implementation. Modify it based on the requirements of the project.
"""

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

def import_data(test_X_file_path):
    test_X = np.genfromtxt(test_X_file_path, delimiter=',', dtype=np.float64, skip_header=1)
    return test_X


def predict_target_values(test_X, train_X, train_Y):
    # Write your code to Predict Target Variables
    # HINT: You can use other functions which you've already implemented in coding assignments.
    return classify_points_using_knn(train_X, train_Y, test_X, 7, 2)

def write_to_csv_file(pred_Y, predicted_Y_file_name):
    pred_Y = pred_Y.reshape(len(pred_Y), 1)
    with open(predicted_Y_file_name, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(pred_Y)
        csv_file.close()


def predict(test_X_file_path):
    test_X = import_data(test_X_file_path)
    pred_Y = predict_target_values(test_X, train_X, train_Y)
    write_to_csv_file(pred_Y, "predicted_test_Y_knn.csv")


if __name__ == "__main__":
    train_X = pd.read_csv('train_X_knn.csv').values
    train_Y = pd.read_csv('train_Y_knn.csv', header = None).values
    test_X_file_path = sys.argv[1]
    #test_X_file_path = 'train_X_knn.csv'
    predict(test_X_file_path)
    # Uncomment to test on the training data
    #validate(test_X_file_path, actual_test_Y_file_path="train_Y_knn.csv") 