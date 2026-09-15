# PYTHON CHEAT SHEET

## 1. BASICS

|  |  |
| --- | --- |
| `x = 5` / `x: int = 5` | assignment / typed |
| `type(x)` `len(x)` `print(x)` `input("msg")` | built-ins |
| `+` `-` `*` `/` `//` `%` `**` | arithmetic |
| `==` `!=` `>` `<` `>=` `<=` `and` `or` `not` | comparison & logical |
| `=` `+=` `-=` `*=` `/=` `%=` | assignment operators |

**Types:** `int` `float` `str` `bool` (`True`/`False`) `None`**F-string:** `f"{val:.2f}"` `f"{val:>10}"` `f"{val:,}"` `f"{name!r}"`

**Conditionals:** `if`/`elif`/`else` — **For:** `for i in range(start, stop, step)` — **While:** `while condition:` — **Break:** `break`/`continue`

---

## 2. DATA STRUCTURES

| Structure | Syntax | Key Methods |
| --- | --- | --- |
| **List** `[]` | mutable, ordered | `.append(x)` `.extend(lst)` `.insert(i,x)` `.remove(x)` `.pop(i)` `.sort()` `.reverse()` `.clear()` `.copy()` |
| **Tuple** `()` | immutable, ordered | `.count(x)` `.index(x)` |
| **Dict** `{k:v}` | mutable, key-value | `.get(k,default)` `.keys()` `.values()` `.items()` `.update(d)` `.pop(k)` `.clear()` |
| **Set** `{}` | mutable, unique | `.add(x)` `.update(lst)` `.remove(x)` `.discard(x)` `.pop()` |

**Slicing:** `lst[start:stop:step]` `lst[-1]` `lst[::-1]` (reverse) **Swap:** `a, b = b, a` — **Unpack:** `x, y, z = my_tuple`**Set ops:** `a | b` union · `a & b` intersect · `a - b` diff · `a ^ b` sym diff **Copy:** `lst[:]` or `lst.copy()` (shallow) · `[i[:] for i in lst]` (deep) **Freq pattern:** `d[k] = d.get(k, 0) + 1`

---

## 3. COMPREHENSIONS

```
[x**2 for x in lst]                    # basic
[x for x in lst if x > 0]             # filtered
[f(i) for i in range(n) if cond]      # combined
{k: v for k, v in pairs}              # dict comp
{len(w) for w in words}               # set comp
```

---

## 4. FUNCTIONS

```python
def name(param, default=val):     # default param
    return expr

def f(*args): ...                 # positional args (tuple)
def f(**kwargs): ...              # keyword args (dict)
```

**Scope:** `global x` (modify global) · `nonlocal x` (modify enclosing) **Lambda:** `lambda x, y: x + y`**HOF:** `sorted(lst, key=lambda x: x["k"])` · `filter(fn, lst)` · `map(fn, lst)` · `reduce(fn, lst, init)`

**Recursion:** base case + recursive case (`factorial(0)=1`, `fib(0)=0, fib(1)=1`)

**Decorator:** `@decorator` — wraps function with extra behavior. Always use `@wraps(func)` inside. **Closure:** inner function captures outer variable + `nonlocal`

---

## 5. ERROR HANDLING

```python
try:
    risky_code()
except ValueError as e:          # catch specific error
    handle(e)
except (TypeError, KeyError):    # multiple
    handle()
else:
    no_error_code()              # runs if NO exception
finally:
    cleanup()                    # ALWAYS runs
```

**Raise:** `raise ValueError("msg")` — **Custom:** `class MyError(Exception): pass`**Common errors:** `ValueError` `TypeError` `ZeroDivisionError` `IndexError` `KeyError` `FileNotFoundError` `AttributeError`

---

## 6. OOP

```python
class Child(Parent):              # inheritance
    def __init__(self, a, b):
        super().__init__(a)       # call parent ctor
        self.__b = b              # private
        self._c = 0               # protected

    def __str__(self): return "..."   # print() uses this
    def method(self): ...
```

**Encapsulation:** public `self.x` · protected `self._x` · private `self.__x`**Polymorphism:** same method name, different class behavior **Abstract:** `from abc import ABC, abstractmethod` — `class X(ABC):` + `@abstractmethod def m(self): pass`**Interface:** abstract class with only abstract methods **Composition:** `self.obj = OtherClass()` (has-a) vs inheritance (is-a)

| `__init__` | constructor | `super()` | parent methods | `isinstance(obj, Cls)` | type check |
| --- | --- | --- | --- | --- | --- |

---

## 7. UNIT TESTING

```python
import unittest
class TestX(unittest.TestCase):
    def setUp(self): ...          # before EACH test
    def tearDown(self): ...       # after EACH test
    def test_method(self):
        self.assertEqual(a, b)
        self.assertTrue(x)
        self.assertFalse(x)
        self.assertIn(a, b)
        self.assertIsNone(x)
        self.assertIsInstance(x, Cls)
        with self.assertRaises(Err): code()
if __name__ == "__main__": unittest.main()
```

**Rule:** test method names **must** start with `test_`

---

## 8. FILE I/O & JSON

```python
with open("f.txt", "r") as f:    # auto-closes
    content = f.read()            # whole file
    lines = f.readlines()         # list of lines

with open("f.txt", "w") as f:
    f.write("text")

import json
with open("f.json","r") as f: data = json.load(f)      # read
with open("f.json","w") as f: json.dump(data, f, indent=2)  # write
```

**Modes:** `"r"` read · `"w"` write (overwrites) · `"a"` append **Safe read:** wrap in `try/except FileNotFoundError`

---

## 9. STRING METHODS

| Method | Result |
| --- | --- |
| `.lower()` `.upper()` `.strip()` | case & whitespace |
| `.split(sep)` `.replace(old,new)` | transform |
| `.find(sub)` `.count(sub)` `.startswith(s)` `.endswith(s)` | search |
| `.isalpha()` `.isdigit()` `.isalnum()` | validation |
| `", ".join(lst)` | join list to string |

**ord("A")=65** · **chr(65)="A"** · **"A"&lt;=ch&lt;="Z"** · **"a"&lt;=ch&lt;="z"**

---

## 10. QUICK RECIPES

```
Palindrome:  cleaned == cleaned[::-1]           (after .lower() + removing non-alnum)
Anagram:     sorted(w1.lower()) == sorted(w2.lower())
Divisors:    [i for i in range(1,n+1) if n%i==0]
Caesar:      chr((ord(ch)-base+shift)%26 + base)   (base=ord("A") or ord("a"))
Deep copy:   [i[:] for i in nested]
Shallow:     lst.copy() or lst[:]
Frequency:   d[k] = d.get(k, 0) + 1
Sort by key: sorted(lst, key=lambda x: x["field"])
```

---

## 11. MUST-KNOW RULES

1. `self` = first param of every class method (not counted as argument)
2. `__init__` runs when creating object · `__str__` runs on `print(obj)`
3. `super().__init__()` in child → calls parent constructor
4. `@abstractmethod` → subclass MUST implement it · cannot instantiate ABC
5. `global x` = modify global var · `nonlocal x` = modify enclosing var
6. `with open()` = auto-close files · always prefer it
7. `try/else` = runs if no error · `finally` = always runs
8. Test methods must start with `test_` · `setUp()` before each · `tearDown()` after each
9. `raise Error("msg")` to throw · `except Error as e` to catch