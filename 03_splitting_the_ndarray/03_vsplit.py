import numpy as np

a = np.arange(1, 13).reshape(4, 3)

print("Original Matrix:")
print(a)

result = np.vsplit(a, 2)

print("After Vertical Splitting:")

for x in result:
    print(x)


# output
# Original Matrix:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# After Vertical Splitting:

# [[1 2 3]
#  [4 5 6]]

# [[ 7  8  9]
#  [10 11 12]]