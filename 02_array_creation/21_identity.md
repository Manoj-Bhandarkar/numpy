# NumPy `identity()`

## What is `np.identity()`?

`np.identity()` creates a **square identity matrix**.

An identity matrix is a special matrix in which:

- All diagonal elements are **1**
- All other elements are **0**
- Number of rows = Number of columns (N × N)

It always returns a **2D NumPy ndarray**.

---

# Syntax

```python
np.identity(n, dtype=float)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| n | Size of the square matrix (N × N) |
| dtype | Data type (optional) |

---

## Returns

A square identity matrix (`ndarray`).

---

# Example 1

```python
import numpy as np

arr = np.identity(3)

print(arr)
```

Output

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

# Example 2

```python
arr = np.identity(3, dtype=int)

print(arr)
```

Output

```text
[[1 0 0]
 [0 1 0]
 [0 0 1]]
```

---

# Example 3

```python
arr = np.identity(6, dtype=int)

print(arr)
```

Output

```text
[[1 0 0 0 0 0]
 [0 1 0 0 0 0]
 [0 0 1 0 0 0]
 [0 0 0 1 0 0]
 [0 0 0 0 1 0]
 [0 0 0 0 0 1]]
```

---

# ndarray Properties

```python
arr = np.identity(6)

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output

```text
Dimensions : 2
Shape      : (6,6)
Size       : 36
dtype      : float64
```

---

# Rules

✅ Creates only **square matrices**

✅ Supports custom data types

✅ Always returns a **2D ndarray**

❌ Cannot create a 3D identity matrix

```python
np.identity((2,3,3))
```

Produces

```text
TypeError
```

---

# identity() vs eye()

| identity() | eye() |
|------------|--------|
| Creates only N × N matrix | Can create rectangular matrices |
| Diagonal starts at main diagonal | Diagonal can be shifted using `k` |
| Simpler | More flexible |

Example

```python
np.identity(3)

np.eye(3)

np.eye(3,5)

np.eye(4, k=1)
```

---

# Real-world Uses

- Matrix multiplication
- Linear Algebra
- Machine Learning
- Computer Graphics
- Transformation matrices
- Solving linear equations

---

# Interview Questions

### What is an identity matrix?

A square matrix having 1s on the main diagonal and 0s elsewhere.

---

### Does `np.identity()` create rectangular matrices?

No.

---

### Which function is more flexible?

`np.eye()`

---

### What is the default dtype?

`float64`

---

### Can `np.identity()` create a 3D matrix?

No.