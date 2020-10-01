#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:02:45 2020

@author: prajwal
"""
def scan_1d_vector():
    Z = [float(i) for i in input().split()]
    return Z

def compute_ln_norm_distance(vector1, vector2, n):
    """
    Arguments:
    vector1 -- A 1D array of size >= 1.
    vector2 -- A 1D array of size equal to size of vector1
    n       -- n in Ln norm distance (>0)

    Returns:
    Computed ln norm distance
    """
    dis = 0
    for i in range(len(vector1)):
        dis += abs(vector1[i] - vector2[i])**n
    return dis**(1/n)


if __name__ == "__main__":
  P = scan_1d_vector()
  Q = scan_1d_vector()
  n = int(input())
  ln_norm_distance = compute_ln_norm_distance(P, Q, n)
  ln_norm_distance = round(ln_norm_distance,4)
  print(ln_norm_distance)