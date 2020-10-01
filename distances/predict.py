import numpy as np
import csv
import sys

from validate import validate

"""
Predicts the target values for data in the file at 'test_X_file_path', using the weights learned during training.
Writes the predicted values to the file named "predicted_test_Y_lr.csv". It should be created in the same directory where this code file is present.
This code is provided to help you get started and is NOT a complete implementation. Modify it based on the requirements of the project.
"""

def import_data_and_weights(test_X_file_path, weights_file_path):
    test_X = np.genfromtxt(test_X_file_path, delimiter=',', dtype=np.float64, skip_header=1)
    weights = np.genfromtxt(weights_file_path, delimiter=',', dtype=np.float64)
    return test_X, weights


def predict_target_values(test_X, weights):
    # Write your code to Predict Target Variables
    test_X = np.insert(test_X, 0, 1, axis = 1)
    pred_Y = np.dot(test_X, weights.T)
    return pred_Y
    # HINT: You can use other functions which you've already implemented in coding assignments.


def write_to_csv_file(pred_Y, predicted_Y_file_name):
    pred_Y = pred_Y.reshape(len(pred_Y), 1)
    with open(predicted_Y_file_name, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(pred_Y)
        csv_file.close()


def predict(test_X_file_path):
    test_X, weights = import_data_and_weights(test_X_file_path, "WEIGHTS_FILE.csv")
    pred_Y = predict_target_values(test_X, weights)
    write_to_csv_file(pred_Y, "predicted_test_Y_lr.csv")


if __name__ == "__main__":
    test_X_file_path = sys.argv[1]
    #test_X_file_path = ('train_X_lr.csv')
    predict(test_X_file_path)
    # Uncomment to test on the training data
    #validate(test_X_file_path, actual_test_Y_file_path="train_Y_lr.csv") 