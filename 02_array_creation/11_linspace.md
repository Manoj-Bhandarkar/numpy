# NumPy `linspace()`

## What is `np.linspace()`?

`np.linspace()` creates an array of evenly spaced numbers over a specified interval.

Unlike `np.arange()`, where you specify the **step size**, `np.linspace()` lets you specify the **number of values** you want.

---

## Syntax

```python
np.linspace(
    start,
    stop,
    num=50,
    endpoint=True,
    retstep=False,
    dtype=None
)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| start | Starting value of the sequence |
| stop | Ending value of the sequence |
| num | Number of equally spaced values (default = 50) |
| endpoint | Include the stop value (default = True) |
| retstep | Return the spacing between values |
| dtype | Data type of the output array |

---

## Example 1 - Default Behavior

```python
import numpy as np

arr = np.linspace(1, 10)

print(arr)
```

Output

```text
[1.         1.18367347 ... 10.]
```

### Explanation

- Start = 1
- Stop = 10
- Default number of values = 50
- Stop value is included

---

## Example 2 - Specify Number of Values

```python
arr = np.linspace(1, 10, num=5)

print(arr)
```

Output

```text
[ 1.    3.25  5.5   7.75 10. ]
```

---

## Example 3 - Return Step Size

```python
arr, step = np.linspace(
    1,
    10,
    num=5,
    retstep=True
)

print(arr)
print(step)
```

Output

```text
[ 1.    3.25  5.5   7.75 10. ]
2.25
```

---

## Example 4 - endpoint=False

```python
arr = np.linspace(
    0,
    20,
    num=5,
    endpoint=False
)

print(arr)
```

Output

```text
[ 0.  4.  8. 12. 16.]
```

The stop value (20) is **not included**.

---

## ndarray Properties

```python
arr = np.linspace(10,100,num=10)

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output

```text
Dimension : 1
Shape     : (10,)
Size      : 10
dtype      : float64
```

---

# linspace() vs arange()

| Feature | linspace() | arange() |
|----------|------------|----------|
| Based on | Number of values | Step size |
| Stop value | Included by default | Excluded |
| Default output | 50 values | Depends on step |
| Floating-point precision | Better | Can have rounding issues |
| Best for | Scientific computing | Simple sequences |

---

# When to Use linspace()

- Plotting graphs
- Machine Learning
- Data Science
- Signal Processing
- Numerical Analysis
- Mathematical simulations

---

# Common Mistakes

### Wrong

```python
np.linspace(1,10,2)
```

Some beginners think `2` is the step size.

It is **not**.

It means **generate 2 values**.

Output

```text
[1. 10.]
```

---

### Correct

```python
np.arange(1,11,2)
```

Output

```text
[1 3 5 7 9]
```

---

# Interview Questions

### What is `np.linspace()`?

It creates evenly spaced values over a specified interval.

---

### What is the default value of `num`?

50

---

### Is the stop value included?

Yes.

By default, `endpoint=True`.

---

### What does `retstep=True` do?

It returns the spacing between consecutive values.

---

### Difference between `linspace()` and `arange()`?

- `arange()` uses **step size**
- `linspace()` uses **number of samples**