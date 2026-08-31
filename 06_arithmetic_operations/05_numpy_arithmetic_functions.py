import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 10])

print("Array A:", a)
print("Array B:", b)

print("\nnp.add():")
print(np.add(a, b))

print("\nnp.subtract():")
print(np.subtract(a, b))

print("\nnp.multiply():")
print(np.multiply(a, b))

print("\nnp.divide():")
print(np.divide(a, b))

print("\nnp.power():")
print(np.power(a, 2))

print("\nnp.mod():")
print(np.mod(a, b))

# Array A: [10 20 30 40]
# Array B: [ 2  4  5 10]

# np.add():
# [12 24 35 50]

# np.subtract():
# [ 8 16 25 30]

# np.multiply():
# [ 20  80 150 400]

# np.divide():
# [5. 5. 6. 4.]

# np.power():
# [ 100  400  900 1600]

# np.mod():
# [0 0 0 0]