import numpy as np
from scan_utils import scan_Z_vector
from math import exp


def sigmoid(Z):
    #TODO Complete the function implementation. Read the Question text for details
    output = []
    for i in (Z):
            output.append(1/(1+exp(-i)))
    return output


if __name__ == "__main__":
  Z = scan_Z_vector()
  sigmoid_value = sigmoid(Z)
  sigmoid_value = np.round(sigmoid_value, 4)
  print(*sigmoid_value)