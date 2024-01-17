# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 (Data Warehousing & Data Mining)
# Lab-2, Q2
"""
Create two vectors y and ŷ having same dimensions, where ŷ should
consist of random numbers between [0,1] and y should contains 0s and 1s.
For example: y = [0,1,1,0,1,0,0,1,...,1]
Compute the given expression:

                  O = -(1/n)*∑[yᵢlog₂(ŷᵢ)+(1-yᵢ)log₂(1-ŷᵢ)]

where n is total number of elements in y and ŷ.
"""

import numpy as np
def calculate_cross_entropy(y, y_hat):
    n = len(y)
    return -(1/n)*np.sum(y*np.log2(y_hat)+(1-y)*np.log2(1-y_hat))
n = int(input("Enter the length of vectors: "))
# Vector ŷ with values between [0, 1]
y_hat = np.random.rand(n)
# Binary vector y with 0s and 1s
y = np.random.randint(2, size=n)
# Computation
cross_entropy = calculate_cross_entropy(y, y_hat)
print("Vector y:", y)
print("Vector ŷ:", y_hat)
print("Cross Entropy:", cross_entropy)

