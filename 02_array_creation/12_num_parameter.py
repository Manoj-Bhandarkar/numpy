import numpy as np

print(np.linspace(1, 10, num=5))
print("-"*20)
print(np.linspace(10, 100, num=10))
print("-"*20)
print(np.linspace(0, 20, 5))
print("-"*20)
print(np.linspace(0, 20, 5, endpoint=False))
print("-"*20)
arr, step = np.linspace(
    1,
    10,
    num=5,
    retstep=True
)
print(arr)
print("Step Size :", step)