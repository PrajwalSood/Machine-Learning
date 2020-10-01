#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:08:37 2020

@author: prajwal
"""
def scan_1d_vector():
    Z = [float(i) for i in input().split()]
    return Z

def compute_manhattan_distance(vector1, vector2):
    """
    Arguments:
    vector1 -- A 1D array of size > 0.
    vector2 -- A 1D array of size equal to size of vector1

    Returns:
    Computed manhattan distance
    """
    dis = 0
    for i in range(len(vector1)):
        dis += abs(vector1[i] - vector2[i])
    return dis

if __name__ == "__main__":
  P = scan_1d_vector()
  Q = scan_1d_vector()
  manhattan_distance = compute_manhattan_distance(P, Q)
  manhattan_distance = round(manhattan_distance,4)
  print(manhattan_distance)

