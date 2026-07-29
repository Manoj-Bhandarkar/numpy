# 1. Introduction
"""
====================================================
        Python List vs NumPy Array
====================================================

This file demonstrates the practical differences between
Python Lists and NumPy Arrays.

Topics Covered:
1. Memory Comparison
2. Speed Comparison
3. Vectorization
4. Matrix Addition
5. Matrix Multiplication
6. Filtering
7. Mathematical Operations
"""
# ------------------------------------
# 2. Creating List and NumPy Array
import numpy as np
import time
import sys

print("=" * 50)
print("Creating Python List and NumPy Array")
print("=" * 50)

lst = [10, 20, 30, 40, 50]
arr = np.array(lst)

print("Python List :", lst)
print("NumPy Array :", arr)

# ==================================================
# Creating Python List and NumPy Array
# ==================================================
# Python List : [10, 20, 30, 40, 50]
# NumPy Array : [10 20 30 40 50]
# ------------------------------------

# 3. Memory Comparison
print("\n" + "=" * 50)
print("Memory Comparison")
print("=" * 50)

print("List Memory :", sys.getsizeof(lst), "bytes")
print("NumPy Memory :", arr.nbytes, "bytes")
# ==================================================
# Memory Comparison
# ==================================================
# List Memory : 104 bytes
# NumPy Memory : 40 bytes
# ------------------------------------

# 4. Speed Comparison
print("\n" + "=" * 50)
print("Speed Comparison")
print("=" * 50)

numbers = list(range(1_000_000))
start = time.time()
result = [x * 2 for x in numbers]
end = time.time()
print("Python List Time :", end - start)

numbers = np.arange(1_000_000)
start = time.time()
result = numbers * 2
end = time.time()
print("NumPy Time :", end - start)
# ==================================================
# Speed Comparison
# ==================================================
# Python List Time : 0.05321311950683594
# NumPy Time : 0.016694307327270508
# ------------------------------------

# 5. Vectorization
print("\n" + "=" * 50)
print("Vectorization")
print("=" * 50)

lst = [1,2,3,4]
try:
    print(lst + 1)
except Exception as e:
    print(e)
arr = np.array(lst)
print(arr + 1)
# ==================================================
# Vectorization
# ==================================================
# can only concatenate list (not "int") to list
# [2 3 4 5]

# Python lists don't support element-wise operations.
# NumPy arrays do.
# ------------------------------------

# 6. Matrix Addition
# Without NumPy
print("\n" + "=" * 50)
print("Matrix Addition Without NumPy")
print("=" * 50)

A = [[1,2], [3,4]]
B = [[5,6], [7,8]]
result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print(result)

# With NumPy
print("\nMatrix Addition Using NumPy")

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
print(A + B)

# ==================================================
# Matrix Addition Without NumPy
# ==================================================
# [[6, 8], [10, 12]]

# Matrix Addition Using NumPy
# [[ 6  8]
#  [10 12]]

# ------------------------------------
# 7. Filtering
# Without NumPy
print("\n" + "=" * 50)
print("Filtering Without NumPy")
print("=" * 50)

numbers = [10,20,30,40,50]
result = []
for i in numbers:
    if i > 25:
        result.append(i)
print(result)

# With NumPy
print("\nFiltering Using NumPy")
numbers = np.array([10,20,30,40,50])
print(numbers[numbers > 25])
# ==================================================
# Filtering Without NumPy
# ==================================================
# [30, 40, 50]

# Filtering Using NumPy
# [30 40 50]
# ------------------------------------

# 8. Mathematical Operations
# Without NumPy
numbers = [10,20,30,40]
total = sum(numbers)
average = total / len(numbers)
print(total)
print(average)

# With NumPy
numbers = np.array([10,20,30,40])
print("Sum :", np.sum(numbers))
print("Mean :", np.mean(numbers))
print("Max :", np.max(numbers))
print("Min :", np.min(numbers))
print("Standard Deviation :", np.std(numbers))
# 100
# 25.0
# Sum : 100
# Mean : 25.0
# Max : 40
# Min : 10
# Standard Deviation : 11.180339887498949
# ------------------------------------

# 9. Reshaping
print("\nReshape")
numbers = np.arange(1,10)
print(numbers)
print(numbers.reshape(3,3))
# Reshape
# [1 2 3 4 5 6 7 8 9]
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]