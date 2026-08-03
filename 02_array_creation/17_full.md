# NumPy `full()`

## What is `np.full()`?

`np.full()` creates a NumPy array where **every element is initialized with a specified value**.

Unlike `zeros()` and `ones()`, you can fill the array with **any integer, float, string, or boolean value**.

It supports **1D, 2D, 3D, and n-dimensional arrays**.

---

# Syntax

```python
np.full(shape, fill_value, dtype=None)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| shape | Shape of the array (1D, 2D, 3D, nD) |
| fill_value | Value used to fill every element |
| dtype | Optional data type |

---

## Returns

A NumPy `ndarray` filled with the specified value.

---

# Example 1 - 1D Array

```python
import numpy as np

arr = np.full(6, 9)

print(arr)
```

Output

```text
[9 9 9 9 9 9]
```

---

# Example 2 - Float Array

```python
arr = np.full(6, 9, dtype=float)

print(arr)
```

Output

```text
[9. 9. 9. 9. 9. 9.]
```

---

# Example 3 - 2D Matrix

```python
arr = np.full((3,3), 6)

print(arr)
```

Output

```text
[[6 6 6]
 [6 6 6]
 [6 6 6]]
```

---

# Example 4 - 3D Array

```python
arr = np.full((2,3,3), 8)

print(arr)
```

Output

```text
[[[8 8 8]
  [8 8 8]
  [8 8 8]]

 [[8 8 8]
  [8 8 8]
  [8 8 8]]]
```

---

# ndarray Properties

```python
arr = np.full((3,3), 6)

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

# Different Fill Values

### Fill with 0

```python
np.full((3,3), 0)
```

### Fill with 1

```python
np.full((3,3), 1)
```

### Fill with 100

```python
np.full((3,3), 100)
```

### Fill with 3.14

```python
np.full((2,2), 3.14)
```

### Fill with True

```python
np.full((2,2), True)
```

### Fill with a String

```python
np.full((2,2), "Python")
```

---

# Real-world Examples

## Initialize Marks

```python
marks = np.full(5, 35)

print(marks)
```

Output

```text
[35 35 35 35 35]
```

---

## Temperature Sensor

```python
temperature = np.full((7,), 25)

print(temperature)
```

Output

```text
[25 25 25 25 25 25 25]
```

---

## RGB Image (Gray Background)

```python
image = np.full((3,3,3), 128)

print(image.shape)
```

Output

```text
(3, 3, 3)
```

---

# Comparison

| Function | Creates |
|----------|---------|
| `np.zeros()` | Array filled with 0 |
| `np.ones()` | Array filled with 1 |
| `np.full()` | Array filled with any specified value |

---

# Interview Questions

### What does `np.full()` do?

Creates an array filled with a specified value.

---

### Can we use floating-point values?

Yes.

```python
np.full((2,2), 2.5)
```

---

### Can we store strings?

Yes.

```python
np.full((2,2), "Hello")
```

---

### What is the default dtype?

NumPy automatically infers the data type from `fill_value`.

---

### When should you use `np.full()`?

- Initializing matrices
- Creating test datasets
- Machine Learning
- Image processing
- Scientific computing