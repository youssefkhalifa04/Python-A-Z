# Chapter 2 Annex - Useful Functions and Methods

This annex lists the most useful built-in functions and methods for the data types covered in this chapter.

## 1. Lists

Lists are ordered and mutable.

### Common methods

- `append(item)` adds one item at the end.
- `extend(iterable)` adds several items.
- `insert(index, item)` inserts an item at a specific position.
- `remove(item)` removes the first matching item.
- `pop(index)` removes and returns an item.
- `sort()` sorts the list in place.
- `reverse()` reverses the order of the list.
- `clear()` removes all items.

### Useful examples

```python
numbers = [4, 2, 9, 1]
numbers.append(7)
numbers.sort()
print(numbers)  # [1, 2, 4, 7, 9]

numbers.pop()
print(numbers)
```

## 2. Sequences

A sequence is an ordered collection. Lists, tuples, and strings are sequences.

### Common operations

- `len(sequence)` returns the number of items.
- `sequence[index]` accesses one item.
- `sequence[start:end]` slices a part of the sequence.
- `item in sequence` checks membership.
- `enumerate(sequence)` gives index and value in a loop.

### Useful examples

```python
text = "Python"
print(text[0])
print(text[1:4])
print("y" in text)

for index, letter in enumerate(text):
    print(index, letter)
```

## 3. Tuples

Tuples are ordered and immutable.

### Common functions and methods

- `len(tuple)` returns the number of items.
- `tuple[index]` accesses one item.
- `tuple[start:end]` slices a part of the tuple.
- `tuple.count(value)` counts occurrences.
- `tuple.index(value)` returns the position of a value.

### Useful examples

```python
point = (10, 20, 10)
print(point.count(10))
print(point.index(20))
```

## 4. Dictionaries

Dictionaries store key-value pairs.

### Common methods

- `get(key)` returns the value of a key without crashing.
- `keys()` returns all keys.
- `values()` returns all values.
- `items()` returns key-value pairs.
- `update(other_dict)` updates several entries.
- `pop(key)` removes and returns a value.
- `clear()` removes all items.

### Useful examples

```python
student = {"name": "Lina", "age": 20}
print(student.get("name"))
print(student.get("city", "Unknown"))

student.update({"course": "Python"})
print(student.items())
```

## 5. Sets

Sets are unordered collections of unique values.

### Common methods

- `add(item)` adds one item.
- `update(iterable)` adds several items.
- `remove(item)` removes an item and raises an error if missing.
- `discard(item)` removes an item without error if missing.
- `pop()` removes and returns an arbitrary item.
- `union(other_set)` returns the union of two sets.
- `intersection(other_set)` returns common items.
- `difference(other_set)` returns items in one set but not the other.
- `clear()` removes all items.

### Useful examples

```python
languages = {"Python", "Java", "Python"}
languages.add("C++")
print(languages)

print(languages.union({"Go", "Rust"}))
print(languages.intersection({"Python", "Rust"}))
```

## 6. Built-in functions you will use often

These work with many data structures:

- `len()`
- `type()`
- `sorted()`
- `list()`
- `tuple()`
- `set()`
- `dict()`

### Example

```python
values = [3, 1, 2]
print(sorted(values))
print(list((1, 2, 3)))
```