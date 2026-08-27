import numpy as np

a = np.arange(1, 13).reshape(3, 4)

print("Original Matrix:")
print(a)

result = np.hsplit(a, 2)

print("After Horizontal Splitting:")

for x in result:
    print(x)

# Original Matrix:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# After Horizontal Splitting:
# [[1 2]
#  [5 6]
#  [9 10]]

# [[ 3  4]
#  [ 7  8]
#  [11 12]]