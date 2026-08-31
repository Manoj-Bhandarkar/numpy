import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

print("\nMean:")
print(np.mean(arr))

print("\nVariance:")
print(np.var(arr))

print("\nStandard Deviation:")
print(np.std(arr))


# Array:
# [10 20 30 40 50]

# Mean:
# 30.0

# Variance:
# 200.0

# Standard Deviation:
# 14.142135623730951

# Small comparison example
data1 = np.array([48, 50, 52, 49, 51])
data2 = np.array([10, 30, 50, 70, 90])

print("Data 1 Standard Deviation:", np.std(data1))
print("Data 2 Standard Deviation:", np.std(data2))

# Data 1 Standard Deviation: 1.4142135623730951
# Data 2 Standard Deviation: 28.284271247461902