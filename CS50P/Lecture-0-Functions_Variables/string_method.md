# Common Python String Methods

Python provides many useful methods for working with strings. Here are some of the most common ones:

---

## 1. `str.lower()`
**Purpose:** Returns a lowercase version of the string.

```python
text = "Hello World!"
print(text.lower())  # Output: 'hello world!'
```

---

## 2. `str.upper()`
**Purpose:** Returns an uppercase version of the string.

```python
text = "Hello World!"
print(text.upper())  # Output: 'HELLO WORLD!'
```

---

## 3. `str.strip()`
**Purpose:** Removes leading and trailing whitespace from the string.

```python
text = "   hello   "
print(text.strip())  # Output: 'hello'
```

---

## 4. `str.split()`
**Purpose:** Splits the string into a list, using a separator (default is whitespace).

```python
text = "one two three"
print(text.split())  # Output: ['one', 'two', 'three']
```

---

## 5. `str.join()`
**Purpose:** Joins elements of an iterable with the string as a separator.

```python
words = ['one', 'two', 'three']
print(", ".join(words))  # Output: 'one, two, three'
```

---

## 6. `str.find()`
**Purpose:** Returns the lowest index of the substring if found, else -1.

```python
text = "hello world"
print(text.find("world"))  # Output: 6
```

---

## 7. `str.replace()`
**Purpose:** Replaces occurrences of a substring with another substring.

```python
text = "hello world"
print(text.replace("world", "Python"))  # Output: 'hello Python'
```

---

## 8. `str.startswith()` / `str.endswith()`
**Purpose:** Checks if the string starts or ends with a specified substring.

```python
text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.endswith("world"))    # Output: True
```

---

## 9. `str.isalpha()` / `str.isdigit()`
**Purpose:** Character type tests. `isalpha()` checks if all characters are alphabetic, `isdigit()` checks if all are digits.

```python
text1 = "hello"
text2 = "12345"
print(text1.isalpha())  # Output: True
print(text2.isdigit())  # Output: True
```

---

**Tip:** There are many more string methods in Python! See the [official documentation](https://docs.python.org/3/library/stdtypes.html#string-methods) for a full list.