import numpy as np
import statistics

data = [10, 20, 20, 30, 40, 20, 50]

arr = np.array(data)

print("Array:")
print(arr)

print("\nMean using NumPy:")
print(np.mean(arr))

print("\nMedian using NumPy:")
print(np.median(arr))

print("\nMode using statistics module:")
print(statistics.mode(data))

print("\nMultimode:")
print(statistics.multimode(data))

# Array:
# [10 20 20 30 40 20 50]

# Mean using NumPy:
# 27.142857142857142

# Median using NumPy:
# 20.0

# Mode using statistics module:
# 20

# Multimode:
# [20]