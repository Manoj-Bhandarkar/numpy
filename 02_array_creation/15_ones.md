# NumPy `ones()`

## What is `np.ones()`?

`np.ones()` creates a NumPy array where **every element is initialized to 1**.

It is commonly used to initialize arrays, matrices, masks, and tensors for numerical computing and machine learning.

---

# Syntax

```python
np.ones(shape, dtype=float)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| shape | Shape of the array (1D, 2D, 3D, nD) |
| dtype | Data type of the array (default: float64) |

---

## Return Value

Returns a NumPy `ndarray` filled entirely with **1s**.

---

# Example 1 - 1D Array

```python
import numpy as np

arr = np.ones(6)

print(arr)
```

Output

```text
[1. 1. 1. 1. 1. 1.]
```

---

# Example 2 - Integer Array

```python
arr = np.ones(6, dtype=int)

print(arr)
```

Output

```text
[1 1 1 1 1 1]
```

---

# Example 3 - 2D Array

```python
arr = np.ones((3,3), dtype=int)

print(arr)
```

Output

```text
[[1 1 1]
 [1 1 1]
 [1 1 1]]
```

---

# Example 4 - 3D Array

```python
arr = np.ones((3,3,3), dtype=int)

print(arr)
```

Output

```text
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
```

---

# Example 5 - 4D Array

```python
arr = np.ones((2,2,3,3), dtype=int)

print(arr)
```

---

# ndarray Properties

```python
arr = np.ones((3,3), dtype=int)

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output

```text
Dimensions : 2
Shape      : (3,3)
Size       : 9
dtype      : int64
```

---

# Using `zeros()` and `ones()` Together

### Matrix Addition

```python
import numpy as np

A = np.zeros((3,3), dtype=int)

B = np.ones((3,3), dtype=int)

C = A + B

print(C)
```

Output

```text
[[1 1 1]
 [1 1 1]
 [1 1 1]]
```

---

### Matrix Multiplication (Element-wise)

```python
A = np.zeros((3,3), dtype=int)

B = np.ones((3,3), dtype=int)

C = A * B

print(C)
```

Output

```text
[[0 0 0]
 [0 0 0]
 [0 0 0]]
```

---

# Common Shapes

| Shape | Output |
|--------|--------|
| `6` | 1D Array |
| `(2,2)` | 2×2 Matrix |
| `(3,4)` | 3×4 Matrix |
| `(3,3,3)` | 3D Array |
| `(2,2,3,3)` | 4D Array |

---

# Real-world Uses

`np.ones()` is commonly used for:

- Initializing weights
- Creating masks
- Building test datasets
- Image processing
- Deep Learning tensors
- Scientific computing
- Matrix initialization

---

# zeros() vs ones() vs full()

| Function | Description |
|----------|-------------|
| `np.zeros()` | Creates an array filled with 0 |
| `np.ones()` | Creates an array filled with 1 |
| `np.full()` | Creates an array filled with any specified value |

Example

```python
np.zeros((2,2))

np.ones((2,2))

np.full((2,2), 100)
```

---

# Interview Questions

### What is `np.ones()`?

Creates a NumPy array where every element is initialized to **1**.

---

### What is the default data type?

`float64`

---

### Can `np.ones()` create multidimensional arrays?

Yes.

It supports 1D, 2D, 3D, and n-dimensional arrays.

---

### Difference between `np.zeros()` and `np.ones()`?

- `np.zeros()` initializes every element to **0**.
- `np.ones()` initializes every element to **1**.

---

### When should you use `np.ones()`?

Whenever you need a pre-initialized array of ones for mathematical operations, machine learning, or testing.