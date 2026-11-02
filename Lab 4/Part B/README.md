
# Part B: Predict the Output — Python Dictionaries

## 📌 Overview

This section focuses on predicting the output of Python programs involving dictionaries. The objective is to understand dictionary behavior, copying, comprehensions, built-in methods, and common runtime errors.

## 🎯 Objectives

- Understand dictionary aliasing and shallow copying.
- Practice dictionary comprehensions.
- Learn how `setdefault()`, `pop()`, and `popitem()` work.
- Understand how Python handles equivalent dictionary keys.
- Identify errors caused by modifying a dictionary during iteration.
- Explain the output of each program.

## Q1. Dictionary Aliasing

### Code
```python
d = {"a": 1, "b": 2}
d2 = d
d2["c"] = 3
print(len(d))
```

### Expected Output
```text
3
```

### Explanation
`d2 = d` makes both variables refer to the same dictionary. Adding `"c"` through `d2` also modifies `d`, so its length becomes 3.

## Q2. Shallow Copy

### Code
```python
d = {"x": [1]}
e = d.copy()
e["x"].append(2)
print(d)
```

### Expected Output
```text
{'x': [1, 2]}
```

### Explanation
The `.copy()` method creates a shallow copy. The inner list is shared between `d` and `e`, so appending `2` through `e` also changes the list inside `d`.

## Q3. Dictionary Comprehension with a Condition

### Code
```python
print({k: v for k, v in zip("abc", range(3)) if v})
```

### Expected Output
```text
{'b': 1, 'c': 2}
```

### Explanation
`zip()` pairs the letters with the numbers: `a: 0`, `b: 1`, and `c: 2`. The condition `if v` excludes the pair whose value is `0`.

## Q4. The `setdefault()` Method

### Code
```python
d = {"a": 1}
print(d.setdefault("a", 9), d.setdefault("b", 5), d)
```

### Expected Output
```text
1 5 {'a': 1, 'b': 5}
```

### Explanation
- `setdefault("a", 9)` returns `1` because `"a"` already exists.
- `setdefault("b", 5)` inserts `"b": 5` because the key is missing.
- The dictionary now contains both entries.

## Q5. Equivalent Dictionary Keys

### Code
```python
d = {1: "a", 1.0: "b", True: "c"}
print(d, len(d))
```

### Expected Output
```text
{1: 'c'} 1
```

### Explanation
In Python, `1`, `1.0`, and `True` compare equal and have the same hash value. They therefore refer to the same dictionary key. Each assignment replaces the value associated with that key, so the final value is `"c"`.

## Q6. Deleting a Key During Iteration

### Code
```python
d = {"a": 1, "b": 2, "c": 3}
for k in d:
    if d[k] == 2:
        del d[k]
```

### Expected Result
```text
RuntimeError: dictionary changed size during iteration
```

### Explanation
Deleting a dictionary key while iterating directly over the dictionary changes its size. Python raises a `RuntimeError` when the iterator detects this structural change. A safe alternative is to iterate over `list(d)` or collect the keys to delete before removing them.

## Q7. The `pop()` and `popitem()` Methods

### Code
```python
d = {"a": 1, "b": 2}
print(d.pop("z", None), d.popitem())
```

### Expected Output
```text
None ('b', 2)
```

### Explanation
- `pop("z", None)` returns `None` because `"z"` does not exist and a default value was supplied.
- `popitem()` removes and returns the last inserted key-value pair. In this case, it returns `("b", 2)`.

## Q8. Dictionary Comprehension with Duplicate Values

### Code
```python
print({v: k for k, v in {"a": 1, "b": 1}.items()})
```

### Expected Output
```text
{1: 'b'}
```

### Explanation
The comprehension reverses each key-value pair. Both original values are `1`, so both entries attempt to use `1` as the new key. Dictionary keys must be unique, and the later value (`"b"`) overwrites the earlier one (`"a"`).

---

## 📝 Summary of Concepts

| Question | Concept |
|---|---|
| Q1 | Aliasing |
| Q2 | Shallow copy |
| Q3 | Dictionary comprehension |
| Q4 | `setdefault()` |
| Q5 | Equivalent dictionary keys |
| Q6 | Modifying a dictionary during iteration |
| Q7 | `pop()` and `popitem()` |
| Q8 | Duplicate keys in a comprehension |

## 🧪 Practice Instructions

1. Write down your predicted output before executing each snippet.
2. Run each program using Python 3.x.
3. Compare your prediction with the actual result.
4. For each incorrect prediction, write one sentence explaining why.
5. Revise the relevant dictionary concept.

## 📚 Learning Outcomes

After completing this section, students should be able to explain dictionary references, shallow copies, comprehensions, built-in dictionary methods, equivalent keys, and common runtime errors.

---

**Author:** Ishaan Sharma  
**Lab:** Python Dictionary — Part B
