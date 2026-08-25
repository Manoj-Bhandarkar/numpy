import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original Array:", arr)

print("arr[1:5]:", arr[1:5])
print("arr[:4]:", arr[:4])
print("arr[3:]:", arr[3:])

# Step slicing
print("arr[::2]:", arr[::2])

# Reverse array
print("arr[::-1]:", arr[::-1])

# Original Array: [10 20 30 40 50 60 70 80]
# arr[1:5]: [20 30 40 50]
# arr[:4]: [10 20 30 40]
# arr[3:]: [40 50 60 70 80]
# arr[::2]: [10 30 50 70]
# arr[::-1]: [80 70 60 50 40 30 20 10]