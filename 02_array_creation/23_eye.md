# eye()

---

## What is `numpy.eye()`?

`numpy.eye()` is used to create a **2-dimensional array** with **1s on a specified diagonal** and **0s elsewhere**.

Unlike `numpy.identity()`, `numpy.eye()` allows you to create **rectangular matrices** and specify the diagonal position using the `k` parameter.

It is widely used in:

- Linear Algebra
- Matrix Operations
- Scientific Computing
- Machine Learning
- Deep Learning
- Computer Graphics

---

## Syntax

```python
numpy.eye(N, M=None, k=0, dtype=float)
```

---

## Parameters

### N

Number of rows in the output array.

**Required**

---

### M

Number of columns.

If omitted, `M = N`.

Default: `None`

---

### k

Specifies which diagonal contains **1s**.

| Value | Meaning |
|--------|----------|
| `0` | Main diagonal |
| `1` | One diagonal above |
| `2` | Two diagonals above |
| `-1` | One diagonal below |
| `-2` | Two diagonals below |

Default value is `0`.

---

### dtype

Specifies the data type of the array.

Example:

- int
- float
- bool

Default:

```python
float
```

---

## Return Value

Returns an object of type

```python
numpy.ndarray
```

---

## Difference between `eye()` and `identity()`

| eye() | identity() |
|--------|------------|
| Can create rectangular matrices | Creates only square matrices |
| Supports `k` parameter | Does not support `k` |
| More flexible | Simpler |

---

## Common Uses

- Identity matrix creation
- Matrix initialization
- Linear algebra
- Machine Learning
- Deep Learning
- Scientific computing
- Matrix multiplication

---

## Interview Questions

### What is the difference between `eye()` and `identity()`?

`eye()` can create rectangular matrices and supports diagonal shifting using `k`.

`identity()` creates only square identity matrices.

---

### What does `k` represent?

`k` specifies the diagonal position where **1s** are placed.

- `k = 0` → Main diagonal
- `k > 0` → Upper diagonal
- `k < 0` → Lower diagonal

---

### What is the default data type of `eye()`?

```python
float64
```

unless `dtype` is specified.

---

## Related Functions

- `numpy.identity()`
- `numpy.diag()`
- `numpy.zeros()`
- `numpy.ones()`