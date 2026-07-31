# NumPy `arange()`

## What is `np.arange()`?

`np.arange()` is used to create a NumPy array containing evenly spaced values within a specified range.

It works similarly to Python's built-in `range()` function, but returns a NumPy `ndarray` instead of a `range` object.

---

# Syntax

```python
np.arange(stop)

np.arange(start, stop)

np.arange(start, stop, step)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| start | Starting value (default = 0) |
| stop | Ending value (exclusive) |
| step | Increment or decrement value |

> **Note:** The `stop` value is **not included** in the output.

---

# Example 1

```python
import numpy as np

arr = np.arange(10)

print(arr)
```

Output

```text
[0 1 2 3 4 5 6 7 8 9]
```

Creates numbers from **0 to 9**.

---

# Example 2

```python
arr = np.arange(10, 20)
```

Output

```text
[10 11 12 13 14 15 16 17 18 19]
```

Creates numbers from **10 to 19**.

---

# Example 3

```python
arr = np.arange(10, 31, 2)
```

Output

```text
[10 12 14 16 18 20 22 24 26 28 30]
```

Creates even numbers.

---

# Example 4

```python
arr = np.arange(30, 9, -2)
```

Output

```text
[30 28 26 24 22 20 18 16 14 12 10]
```

Creates numbers in descending order.

---

# Reshaping

```python
arr = np.arange(16)

arr = arr.reshape(4,4)
```

Output

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
```

---

# Important Notes

✅ Returns a NumPy ndarray

✅ Stop value is excluded

✅ Supports positive and negative step values

✅ Can be reshaped into multiple dimensions

---

# Difference between range() and arange()

| range()                  | arange()                       |
|--------------------------|--------------------------------|
| Returns range object     | Returns ndarray                |
| Python built-in          | NumPy function                 |
| Mainly used in loops     | Used for numerical computing   |
| No vectorized operations | Supports vectorized operations |

---

# ndarray Properties

```python
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

| Property | Description |
|----------|-------------|
| ndim     | Number of dimensions |
| shape    | Shape of array |
| size     | Total elements |
| dtype    | Data type |

---

# Interview Questions

### What is np.arange()?

It creates a NumPy array containing evenly spaced values within a specified range.

---

### Is the stop value included?

No.

The stop value is excluded.

Example

```python
np.arange(1,5)
```

Output

```text
[1 2 3 4]
```

---

### Can arange() create floating point numbers?

Yes.

```python
np.arange(0,1,0.2)
```

Output

```text
[0.  0.2 0.4 0.6 0.8]
```

---

### When should you use arange()?

- Creating sequences
- Test data
- Matrix creation
- Numerical computing
- Machine Learning datasets
