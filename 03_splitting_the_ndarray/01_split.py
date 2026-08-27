import numpy as np

a = np.arange(1, 13)

print("Original Array:")
print(a)

result = np.split(a, 3)
print(result)
print("After Splitting:")
for x in result:
    print(x)
    
#output

# [ 1  2  3  4  5  6  7  8  9 10 11 12]
# [array([1, 2, 3, 4]), array([5, 6, 7, 8]), array([ 9, 10, 11, 12])]
# After Splitting:
# [1 2 3 4]
# [5 6 7 8]

# [ 9 10 11 12]