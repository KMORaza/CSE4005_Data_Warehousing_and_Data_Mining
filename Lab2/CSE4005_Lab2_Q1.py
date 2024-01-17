# KHAN MOHD OWAIS RAZA
# 20BCD7138
# CSE4005 (Data Warehousing & Data Mining)
# Lab-2, Q1
"""
Write a program to multiply two matrices of size (100,100) in two methods:
(a) By using np.dot(mat_1,mat_2)
(b) By using for loops
Compare the time of execution in both the cases
"""
import numpy as np
import time
import matplotlib.pyplot as plt
import sys
## (a) By using np.dot(mat_1,mat_2)
def multiply_matrices_numpy(mat_1, mat_2):
    return np.dot(mat_1, mat_2)
## (b) By using for loops
def multiply_matrices_for_loops(mat_1, mat_2):
    result = np.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            for k in range(100):
                result[i][j] += mat_1[i][k] * mat_2[k][j]
    return result
# Matrices of size (100, 100)
mat_1 = np.random.rand(100, 100)
mat_2 = np.random.rand(100, 100)
# Execution time for NumPy dot product
start_time_np = time.time()
result_np = multiply_matrices_numpy(mat_1, mat_2)
end_time_np = time.time()
time_np = end_time_np - start_time_np
# Execution time for for loops
start_time_loops = time.time()
result_loops = multiply_matrices_for_loops(mat_1, mat_2)
end_time_loops = time.time()
time_loops = end_time_loops - start_time_loops
# Comparison of execution times
print(f"Execution time using np.dot(): {end_time_np - start_time_np} seconds")
print(f"Execution time using for loops: {end_time_loops - start_time_loops} seconds")
if np.allclose(result_np, result_loops):
    print("Same result")
else:
    print("Different result")
size_np = sys.getsizeof(result_np)
size_loops = sys.getsizeof(result_loops)
print("Space complexity using NumPy dot product:", size_np)
print("Space complexity using for loops:", size_loops)
labels = ['NumPy dot product', 'For loops']
times = [time_np, time_loops]
plt.bar(labels, times, color=['blue', 'orange'])
plt.xlabel('Matrix Multiplication Method')
plt.ylabel('Execution Time (s)')
plt.title('Comparison of Execution Times')
plt.show()
labels_space = ['NumPy dot product', 'For loops']
sizes = [size_np, size_loops]
plt.bar(labels_space, sizes, color=['green', 'red'])
plt.xlabel('Matrix Multiplication Method')
plt.ylabel('Space Complexity (bytes)')
plt.title('Comparison of Space Complexities')
plt.show()

