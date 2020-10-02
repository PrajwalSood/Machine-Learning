import numpy as np


def scan_X_vector(M):
  X = []
  for i in range(0, M):
    Xi = [float(j) for j in input().split()]
    Xi.insert(0, 1.0)
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

def compute_weights_using_normal_equation(X, Y, Lambda):
    matrix = np.identity(len(X[0]))
    matrix[0][0] = 0
    regularization_term = Lambda * np.matrix(matrix)
    weights = np.dot(np.linalg.inv(np.dot(X.T, X) + regularization_term), np.dot(X.T, Y))

    return weights
    


if __name__ == "__main__":
  M = int(input())
  X = scan_X_vector(M)
  Y = scan_Y_vector()
  Lambda = float(input())

  weights = compute_weights_using_normal_equation(X, Y, Lambda)
  weights = np.round(weights, 3).tolist()
  weights = [i[0] for i in weights]
  print(*weights)
