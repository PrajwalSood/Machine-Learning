#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:06:45 2020

@author: prajwal
"""


def scan_1d_vector():
    Z = [float(i) for i in input().split()]
    return Z

def compute_euclidean_distance(vector1, vector2):
    """
    Arguments:
    vector1 -- A 1D array of size > 0
    vector2 -- A 1D array of size equal to size of vector1

    Returns:
    Computed euclidean distance 
    """
    dis = 0
    for i in range(len(vector1)):
        dis += abs(vector1[i] - vector2[i])**2
    return dis**(1/2)

if __name__ == "__main__":
  P = scan_1d_vector()
  Q = scan_1d_vector()
  euclidean_distance = compute_euclidean_distance(P, Q)
  euclidean_distance = round(euclidean_distance,4)
  print(euclidean_distance)
  
