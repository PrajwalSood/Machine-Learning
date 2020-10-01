#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:09:06 2020

@author: prajwal
"""
def scan_1d_vector():
    Z = [float(i) for i in input().split()]
    return Z

def compute_hamming_distance(vector1, vector2):
    """
    Arguments:
    vector1 -- A 1D array of size > 0.
    vector2 -- A 1D array of size equal to size of vector1

    Returns:
    Computed hamming distance
    """
    dis = len(vector1)
    for i in range(dis):
        dis -= 1*(vector1[i] == vector2[i]) 
    return dis



if __name__ == "__main__":
  P = scan_1d_vector()
  Q = scan_1d_vector()
  hamming_distance = compute_hamming_distance(P, Q)
  print(hamming_distance)

