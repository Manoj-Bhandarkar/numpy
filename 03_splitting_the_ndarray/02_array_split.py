import numpy as np

a = np.arange(1, 11)

print("Original Array:")
print(a)

result = np.array_split(a, 3)

print("After Splitting:")

for x in result:
    print(x)

# output
# Original Array:
# [ 1  2  3  4  5  6  7  8  9 10]

# After Splitting:
# [1 2 3 4]
# [5 6 7]
# [ 8  9 10]