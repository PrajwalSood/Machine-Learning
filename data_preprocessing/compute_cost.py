import numpy as np
from logistic_regression import sigmoid

def scan_X_vector(M):
  X = []
  for i in range(0, M):
    Xi = [float(j) for j in input().split()]
    X.append(Xi)
  X = np.array(X)
  return X

def scan_Y_vector():
  Y = [[float(i)] for i in input().split()]
  Y = np.array(Y)
  return Y

def scan_W_vector():
  W = [[float(i)] for i in input().split()]
  W = np.array(W)
  return W

def compute_cost(X, Y, W, b, Lambda):
    Z = np.dot(X, W) + b
    A = sigmoid(Z)
    cost = (-1/M) * np.sum(Y * np.log(A) + (1-Y) * np.log(1-A)) 
    regularisation_cost = (Lambda * np.sum(np.square(W))) / (2 * M) 
    return cost + regularisation_cost


if __name__ == "__main__":
  M = int(input())
  X = scan_X_vector(M)
  Y = scan_Y_vector()
  W = scan_W_vector()
  b = float(input())
  Lambda = float(input()) 

  cost = compute_cost(X, Y, W, b, Lambda)
  print(round(cost, 3))
