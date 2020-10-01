import numpy as np
from apply_one_hot_encoding import apply_one_hot_encoding

def scan_data(M):
    X = []
    for i in range(M):
        row = list(input().split())
        X.append(row)
    return np.array(X)

def scan_1d_vector():
  Z = [int(i) for i in input().split()]
  Z = np.array(Z)
  return Z


def convert_given_cols_to_one_hot(X, column_indices):
    one_hot_encoded_X = np.zeros([len(X),1])

    start_index = 0
    #acts column pointer in X

    for curr_index in column_indices:
        #adding the columns present before curr_index in X (and not present in one_hot_encoded_X), to one_hot_encoded_X
        one_hot_encoded_X=np.append(one_hot_encoded_X,X[:, start_index:curr_index], axis=1)
        
        #applying one hot encoding for current column
        one_hot_encoded_column = apply_one_hot_encoding(X[:,curr_index])

        #appending the obtained one hot encoded array to one_hot_encoded_X
        one_hot_encoded_X=np.append(one_hot_encoded_X,one_hot_encoded_column, axis=1)

        #moving the column pointer of X to next current_index
        start_index = curr_index+1

    #adding any remaining columns to one_hot_encoded_X    
    one_hot_encoded_X=np.append(one_hot_encoded_X,X[:,start_index:], axis=1)
    one_hot_encoded_X = one_hot_encoded_X[:,1:]
    return one_hot_encoded_X
    


if __name__ == "__main__":
    M = int(input())
    X = scan_data(M)
    column_indices = scan_1d_vector()

    one_hot_encoded_array = convert_given_cols_to_one_hot(X,column_indices)

    for i in one_hot_encoded_array:
        print(*i)