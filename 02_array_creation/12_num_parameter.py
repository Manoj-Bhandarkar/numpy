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

# output:
# [ 1.    3.25  5.5   7.75 10.  ]
# --------------------
# [ 10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]
# --------------------
# [ 0.  5. 10. 15. 20.]
# --------------------
# [ 0.  4.  8. 12. 16.]
# --------------------
# [ 1.    3.25  5.5   7.75 10.  ]
# Step Size : 2.25