# NumPy `zeros()`

## What is `np.zeros()`?

`np.zeros()` creates a NumPy array filled with **zeros**.

It is commonly used to initialize arrays before storing actual data.

---

## Syntax

```python
np.zeros(shape, dtype=float)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| shape | Shape of the array (1D, 2D, 3D, nD) |
| dtype | Data type of array elements (default: float64) |

---

## Return Value

Returns a NumPy `ndarray` where all elements are initialized to **0**.

---

# Example 1 - 1D Array

```python
import numpy as np

arr = np.zeros(5)

print(arr)
```

Output

```text
[0. 0. 0. 0. 0.]
```

---

# Example 2 - Integer Array

```python
arr = np.zeros(5, dtype=int)

print(arr)
```

Output

```text
[0 0 0 0 0]
```

---

# Example 3 - 2D Array

```python
arr = np.zeros((2,3), dtype=int)

print(arr)
```

Output

```text
[[0 0 0]
 [0 0 0]]
```

---

# Example 4 - 3D Array

```python
arr = np.zeros((2,3,3), dtype=int)

print(arr)
```

Output

```text
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
```

---

# Example 5 - 4D Array

```python
arr = np.zeros((2,2,3,3), dtype=int)

print(arr)
```

---

# ndarray Properties

```python
arr = np.zeros((3,4), dtype=int)

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output

```text
Dimensions : 2
Shape      : (3,4)
Size       : 12
dtype      : int64
```

---

# Common Shapes

| Shape | Result |
|--------|--------|
| `5` | 1D Array |
| `(2,2)` | 2×2 Matrix |
| `(3,4)` | 3×4 Matrix |
| `(2,3,3)` | 3D Array |
| `(2,2,3,3)` | 4D Array |

---

# Real-world Uses

`np.zeros()` is commonly used for:

- Initializing matrices
- Image processing
- Machine Learning
- Deep Learning
- Computer Vision
- Scientific Computing
- Dynamic Programming
- Temporary result arrays

---

# zeros() vs ones() vs full()

| Function | Output |
|----------|--------|
| `zeros()` | All values are 0 |
| `ones()` | All values are 1 |
| `full()` | All values are user-defined |

Example

```python
np.zeros((2,2))

np.ones((2,2))

np.full((2,2),100)
```

---

# Interview Questions

### What is `np.zeros()`?

Creates an array filled with zeros.

---

### What is the default dtype?

`float64`

---

### Can `zeros()` create multidimensional arrays?

Yes.

Supports 1D, 2D, 3D and n-dimensional arrays.

---

### Why is `np.zeros()` used?

To initialize arrays before filling them with actual data.