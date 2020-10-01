from os import path
import numpy as np
import csv


def check_file_exits(predicted_test_Y_file_path):
    if not path.exists(predicted_test_Y_file_path):
        raise Exception("Couldn't find '" + predicted_test_Y_file_path +"' file")

def check_format(test_X_file_path, predicted_test_Y_file_path):
    pred_Y = []
    with open(predicted_test_Y_file_path, 'r') as file:
        reader = csv.reader(file)
        pred_Y = list(reader)
    pred_Y = np.array(pred_Y)

    test_X = np.genfromtxt(test_X_file_path, delimiter=',', \
        dtype=np.float64, skip_header=1)

    if pred_Y.shape != (len(test_X), 1):
        raise Exception("Output format is not proper")

def check_mse(actual_test_Y_file_path, predicted_test_Y_file_path):
    pred_Y = np.genfromtxt(predicted_test_Y_file_path, delimiter=',', dtype=np.float64)
    actual_Y = np.genfromtxt(actual_test_Y_file_path, delimiter=',', dtype=np.float64)
    from sklearn.metrics import mean_squared_error
    mse = mean_squared_error(actual_Y, pred_Y)
    print("MSE", mse)
    return mse

def validate(test_X_file_path, actual_test_Y_file_path):
    predicted_test_Y_file_path = "predicted_test_Y_lr.csv"
    
    check_file_exits(predicted_test_Y_file_path)
    check_format(test_X_file_path, predicted_test_Y_file_path)
    check_mse(actual_test_Y_file_path, predicted_test_Y_file_path)