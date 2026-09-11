# Activity: Find the Time and Space Complexity

## Objective

The objective of this activity is to analyze different code snippets and determine their **Time Complexity** and **Space Complexity** using **Big-O notation**.

---

## Complexity Analysis

### Snippet 1 — Find Maximum Element

```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`
* **Justification:** The loop checks each element of the array once, taking linear time, while only a few variables (`max_val`, `i`) are used, requiring constant extra space.

---

### Snippet 2 — Check for Duplicate Elements

```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`
* **Justification:** The two nested loops compare every possible pair of elements, resulting in quadratic time, while only loop variables are used, requiring constant extra space.

---

### Snippet 12 — Factorial Using Recursion

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`
* **Justification:** The function makes one recursive call for each value from `n` down to `1`, giving linear time, and the recursion stack can contain up to `n` calls, requiring linear space.

---

### Snippet 13 — Fibonacci Using Recursion

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

* **Time Complexity:** `O(2^n)`
* **Space Complexity:** `O(n)`
* **Justification:** Each call recursively creates two more calls (`n-1` and `n-2`), producing exponential time, while the maximum recursion depth is `n`, requiring linear stack space.

---

## Summary Table

| Snippet | Problem              | Time Complexity | Space Complexity |
| ------: | -------------------- | --------------- | ---------------- |
|       1 | Find Maximum Element | `O(n)`          | `O(1)`           |
|       2 | Check for Duplicates | `O(n²)`         | `O(1)`           |
|      12 | Factorial            | `O(n)`          | `O(n)`           |
|      13 | Fibonacci            | `O(2^n)`        | `O(n)`           |

---

## Key Concepts

* **O(1)** — Constant complexity; execution or memory usage does not grow with input size.
* **O(n)** — Linear complexity; grows proportionally with input size.
* **O(n²)** — Quadratic complexity; commonly occurs with nested loops.
* **O(2^n)** — Exponential complexity; commonly occurs in naive recursive algorithms such as Fibonacci.

### Conclusion

Analyzing time and space complexity helps determine how efficiently an algorithm performs as the input size increases. Simple loops may have linear complexity, nested loops can lead to quadratic complexity, and recursive algorithms can require additional stack space and may have significantly higher time complexity.
