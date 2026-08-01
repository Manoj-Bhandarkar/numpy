import numpy as np

arr = np.zeros(5)

print(arr)
print("-"*20)
print(type(arr))
print("-"*20)
print(np.zeros(5, dtype=int))
print("-"*20)
print(np.zeros(5, dtype=float))
print("-"*20)
print(np.zeros(5, dtype=bool))
print("-"*20)
print(np.zeros((2,2), dtype=int))
print("-"*20)
print(np.zeros((3,4), dtype=int))
print("-"*20)
print(np.zeros((2,3,3), dtype=int))
print("-"*20)
print(np.zeros((2,2,3,3), dtype=int))

#output:
# [0. 0. 0. 0. 0.]
# --------------------
# <class 'numpy.ndarray'>
# --------------------
# [0 0 0 0 0]
# --------------------
# [0. 0. 0. 0. 0.]
# --------------------
# [False False False False False]
# --------------------
# [[0 0]
#  [0 0]]
# --------------------
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]
# --------------------
# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
# --------------------
# [[[[0 0 0]
#    [0 0 0]
#    [0 0 0]]

#   [[0 0 0]
#    [0 0 0]
#    [0 0 0]]]


#  [[[0 0 0]
#    [0 0 0]
#    [0 0 0]]

#   [[0 0 0]
#    [0 0 0]
#    [0 0 0]]]]