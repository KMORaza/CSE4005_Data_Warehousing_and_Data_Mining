# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 (Data Warehousing & Data Mining)
# Lab-2, Q2
"""
Write a program to execute the steps below using NumPy:
 
                      Zᵢⱼ = ∑WᵢₖXₖⱼ
         
                      σᵢⱼ(Zᵢⱼ) = 1/[1+e^(-Zᵢⱼ)]

where W and X are matrices of random numbers having dimensions (m,n) and (n,k) respectively. 
σ(Z) is a function which performs above defined operation on elements of Z.
"""
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
m = int(input("Enter the number of rows for matrix W: "))
n = int(input("Enter the number of columns for matrix W and rows for matrix X: "))
k = int(input("Enter the number of columns for matrix X: "))
W = np.random.rand(m, n) # Matrix W
X = np.random.rand(n, k) # Matrix X
Z = np.dot(W, X) # Computes Z
result = sigmoid(Z) # σ(Z)
print("\nMatrix W:")
print(W)
print("\nMatrix X:")
print(X)
print("\nMatrix Z:")
print(Z)
print("\nResult after applying sigmoid function to Z:")
print(result)
