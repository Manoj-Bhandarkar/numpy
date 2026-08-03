# NumPy `hstack()` and `vstack()`

## Introduction

NumPy provides stacking functions to combine multiple arrays.

The two most commonly used functions are:

- `np.hstack()` → Horizontal stacking
- `np.vstack()` → Vertical stacking

Both return a new NumPy ndarray.

---

# 1. Horizontal Stack (`hstack()`)

## Syntax

```python
np.hstack((array1, array2, ...))
```

### Rule

- Number of **rows must be the same**.
- Columns can be different.

Example

```python
import numpy as np

A = np.array([[10,20],
              [30,40]])

B = np.array([[100,200,300],
              [400,500,600]])

C = np.hstack((A,B))

print(C)
```

Output

```text
[[ 10  20 100 200 300]
 [ 30  40 400 500 600]]
```

---

# 2. Vertical Stack (`vstack()`)

## Syntax

```python
np.vstack((array1, array2, ...))
```

### Rule

- Number of **columns must be the same**.
- Rows can be different.

Example

```python
A = np.array([[10,20],
              [30,40]])

B = np.array([[100,200],
              [400,500],
              [600,300]])

C = np.vstack((A,B))

print(C)
```

Output

```text
[[ 10  20]
 [ 30  40]
 [100 200]
 [400 500]
 [600 300]]
```

---

# hstack() vs vstack()

| Feature | hstack() | vstack() |
|----------|----------|-----------|
| Direction | Horizontal | Vertical |
| Rows | Must match | Can differ |
| Columns | Can differ | Must match |
| Axis | axis=1 | axis=0 |

---

# Working with 1D Arrays

```python
a = np.array([10,20,30])
b = np.array([100,200,300])
```

### hstack()

```python
print(np.hstack((a,b)))
```

Output

```text
[ 10 20 30 100 200 300]
```

---

### vstack()

```python
print(np.vstack((a,b)))
```

Output

```text
[[ 10  20  30]
 [100 200 300]]
```

---

# Common Error

```python
a = np.array([10,20,30,40])
b = np.array([100,200,300])

np.vstack((a,b))
```

Error

```text
ValueError:
all the input array dimensions except for the concatenation axis must match exactly
```

Reason:

- First array has 4 columns.
- Second array has 3 columns.

---

# Fix

```python
a = a.reshape(4,1)
b = b.reshape(3,1)

print(np.vstack((a,b)))
```

Output

```text
[[ 10]
 [ 20]
 [ 30]
 [ 40]
 [100]
 [200]
 [300]]
```

---

# Real-world Example

## Student Data

```python
physics = np.array([[80],[90],[75]])

maths = np.array([[70],[95],[88]])

result = np.hstack((physics, maths))

print(result)
```

Output

```text
[[80 70]
 [90 95]
 [75 88]]
```

---

## Monthly Sales

```python
jan = np.array([[1000,1200]])

feb = np.array([[1300,1400]])

sales = np.vstack((jan,feb))

print(sales)
```

Output

```text
[[1000 1200]
 [1300 1400]]
```

---

# Interview Questions

### What is `hstack()`?

Combines arrays horizontally.

---

### What is `vstack()`?

Combines arrays vertically.

---

### What condition is required for `hstack()`?

Number of rows must be equal.

---

### What condition is required for `vstack()`?

Number of columns must be equal.

---

### Which axis does `hstack()` use?

Axis = 1

---

### Which axis does `vstack()` use?

Axis = 0