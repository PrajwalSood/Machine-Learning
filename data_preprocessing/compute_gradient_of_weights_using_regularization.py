import numpy as np

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

def compute_gradient_of_weights_using_regularization(X, Y, W, b, Lambda):
  m = len(X)
  A = np.dot(X, W) + b
  dW = 1/m * (np.dot((A-Y).T, X) + Lambda*(W.T))
  db = 1/m * np.sum(A-Y)
  dW = dW.T
  return dW, db


if __name__ == "__main__":
  M = int(input())
  X = scan_X_vector(M)
  Y = scan_Y_vector()
  W = scan_W_vector()
  b = float(input())
  Lambda = float(input()) 

  dW, db = compute_gradient_of_weights_using_regularization(X, Y, W, b, Lambda)
  dW = np.round(dW, 3).tolist()
  dW = [i[0] for i in dW]
  b = np.round(b, 3)
  print(*dW)
  print(b)