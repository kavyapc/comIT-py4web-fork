# 🐍 Python Glossary — A Beginner-Friendly Guide
### By y44k0v - class 05 - feb-26
> Plain-language explanations of Python symbols, keywords, and concepts.
> No prior experience needed!

---

## ➕ Operators

Operators are **symbols that do something** to one or more values — like the buttons on a calculator.

---

### 🔢 Math Operators (Arithmetic)

| Symbol | Name | What it does | Example | Result |
|--------|------|--------------|---------|--------|
| `+` | Plus / Addition | Adds two numbers | `5 + 3` | `8` |
| `-` | Minus / Subtraction | Subtracts one from another | `10 - 4` | `6` |
| `*` | Asterisk / Multiplication | Multiplies two numbers | `3 * 4` | `12` |
| `/` | Slash / Division | Divides (always gives a decimal) | `10 / 4` | `2.5` |
| `//` | Double Slash / Floor Division | Divides and rounds **down** | `10 // 3` | `3` |
| `%` | Percent / Modulo | Gives the **remainder** after dividing | `10 % 3` | `1` |
| `**` | Double Asterisk / Exponent | Raises a number to a power | `2 ** 8` | `256` |

---

### 🟰 Assignment Operators

These **store a value** in a variable (like putting something in a labeled box).

| Symbol | Name | What it does | Example |
|--------|------|--------------|---------|
| `=` | Assignment | Stores a value | `age = 25` |
| `+=` | Plus-equals | Adds and saves | `age += 1` → same as `age = age + 1` |
| `-=` | Minus-equals | Subtracts and saves | `score -= 5` |
| `*=` | Times-equals | Multiplies and saves | `price *= 2` |
| `/=` | Divide-equals | Divides and saves | `total /= 4` |
| `//=` | Floor-divide-equals | Floor divides and saves | `x //= 3` |
| `%=` | Modulo-equals | Modulo and saves | `x %= 2` |
| `**=` | Exponent-equals | Raises to power and saves | `x **= 2` |

---

### ⚖️ Comparison Operators

These **compare two values** and give back either `True` or `False`.

| Symbol | Name | What it does | Example | Result |
|--------|------|--------------|---------|--------|
| `==` | Equal to | Are they the same? | `5 == 5` | `True` |
| `!=` | Not Equal to | Are they different? | `5 != 3` | `True` |
| `>` | Greater Than | Is left bigger? | `7 > 3` | `True` |
| `<` | Less Than | Is left smaller? | `2 < 9` | `True` |
| `>=` | Greater Than or Equal To | Left bigger or same? | `5 >= 5` | `True` |
| `<=` | Less Than or Equal To | Left smaller or same? | `3 <= 4` | `True` |

> ⚠️ Don't mix up `=` (stores a value) and `==` (compares two values)!

---

### 🔗 Logical Operators

These **combine** True/False conditions.

| Symbol | Name | What it does | Example | Result |
|--------|------|--------------|---------|--------|
| `and` | And | Both sides must be True | `5 > 3 and 2 < 4` | `True` |
| `or` | Or | At least one side must be True | `5 > 3 or 2 > 9` | `True` |
| `not` | Not | Flips True to False and vice versa | `not True` | `False` |

---

### 🔎 Identity & Membership Operators

| Symbol | Name | What it does | Example | Result |
|--------|------|--------------|---------|--------|
| `is` | Is | Are they the exact same object in memory? | `x is y` | `True` or `False` |
| `is not` | Is Not | Opposite of `is` | `x is not y` | `True` or `False` |
| `in` | In | Is this value inside something? | `"a" in "cat"` | `True` |
| `not in` | Not In | Is this value NOT inside something? | `5 not in [1,2,3]` | `True` |

---

### 🔀 Bitwise Operators

These work on numbers at the **binary (0s and 1s)** level. Less common for beginners, but good to know they exist.

| Symbol | Name | What it does | Example | Result |
|--------|------|--------------|---------|--------|
| `&` | Bitwise AND | Both bits must be 1 | `6 & 3` | `2` |
| `\|` | Bitwise OR | At least one bit is 1 | `6 \| 3` | `7` |
| `^` | Bitwise XOR | Bits are different | `6 ^ 3` | `5` |
| `~` | Bitwise NOT | Flips all bits | `~5` | `-6` |
| `<<` | Left Shift | Shifts bits left (doubles the value) | `2 << 1` | `4` |
| `>>` | Right Shift | Shifts bits right (halves the value) | `4 >> 1` | `2` |

![Quake III - Fast Inverse Sqrt](assets/fast_inverse_sqrt_yt.png)

---

## 🔲 Types of Brackets

Python uses **three kinds of brackets**, each with a different job.

---

### `( )` — Round Brackets (Parentheses)

Used for calling functions, grouping math, and creating tuples.

```python
print("Hello!")           # calling a function
result = (2 + 3) * 4      # grouping: result is 20, not 14
my_tuple = (1, 2, 3)      # a tuple — ordered, but can't be changed
```

---

### `[ ]` — Square Brackets

Used for lists and accessing items by position (called **indexing**).

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # → "apple"   (counting starts at 0!)
print(fruits[-1])   # → "cherry"  (negative index counts from the end)
```

---

### `{ }` — Curly Brackets (Braces)

Used for dictionaries (key-value pairs) and sets (unique items only).

```python
# Dictionary — like a real dictionary with words and definitions
person = {"name": "Alice", "age": 30}
print(person["name"])    # → "Alice"

# Set — duplicates are automatically removed
unique = {1, 2, 3, 3, 2}
print(unique)    # → {1, 2, 3}
```

---

## 📊 Operator Precedence

When Python sees multiple operators in one line, it doesn't just go left to right — it follows a **priority order**, just like the math rule "multiply before you add."

**Higher up in the table = done first.**

| Priority | Operator(s) | Name |
|----------|-------------|------|
| 1 (highest) | `( )` | Parentheses — always first |
| 2 | `**` | Exponent |
| 3 | `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiply, divide, floor divide, modulo |
| 5 | `+`, `-` | Add, subtract |
| 6 | `<<`, `>>` | Bit shifts |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 (lowest) | `or` | Logical OR |

### Examples

```python
2 + 3 * 4           # → 14   (multiply first, then add)
(2 + 3) * 4         # → 20   (parentheses override everything)
2 ** 3 + 1          # → 9    (exponent first: 8 + 1)
not True or False   # → False (not first: False or False)
10 > 5 and 3 < 1    # → False (comparisons first, then and)
```

> 💡 **Tip:** When in doubt, use `( )` to make your intentions crystal clear!

---

## 🔀 Flow Control

Flow control is how you tell Python **which lines to run, when to run them, and how many times.**

---

### `if` / `elif` / `else` — Make Decisions

Run different code depending on whether a condition is True or False.

```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")        # runs if condition is True
elif temperature > 15:
    print("Nice weather.")            # runs if first was False, this is True
else:
    print("Bundle up, it's cold!")    # runs if all above were False
```

> `elif` means "else if" — you can have as many as you need.

---

### `for` Loop — Repeat for Each Item

Runs a block of code **once for every item** in a sequence.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# → apple
# → banana
# → cherry
```

You can also loop over a range of numbers:

```python
for i in range(5):
    print(i)
# → 0, 1, 2, 3, 4
```

---

### `while` Loop — Repeat While a Condition is True

Keeps running **as long as** something is True. Be careful — if the condition never becomes False, it loops forever!

```python
count = 0

while count < 3:
    print(f"Count is {count}")
    count += 1
# → Count is 0
# → Count is 1
# → Count is 2
```

---

### `break` — Exit a Loop Early

Stops the loop immediately, no matter what.

```python
for number in range(10):
    if number == 5:
        break           # stop the loop when we hit 5
    print(number)
# → 0, 1, 2, 3, 4
```

---

### `continue` — Skip to the Next Step

Skips the rest of the current loop cycle and jumps to the next one.

```python
for number in range(6):
    if number == 3:
        continue        # skip number 3
    print(number)
# → 0, 1, 2, 4, 5
```

---

### `pass` — Do Nothing (Placeholder)

Used when Python requires a line of code but you don't want to do anything yet. Handy when sketching out your code structure.

```python
for item in range(5):
    pass    # come back to this later
```

---

### `try` / `except` / `finally` — Handle Errors Gracefully

Lets your program **deal with errors** instead of crashing.

```python
try:
    result = 10 / 0              # this causes an error
except ZeroDivisionError:
    print("You can't divide by zero!")   # runs if that specific error happens
except:
    print("Some other error happened.")  # catches any other error
finally:
    print("This always runs, error or not.")
```

> `finally` is optional — use it for cleanup tasks that must always happen.

---

### `match` / `case` — Pattern Matching (Python 3.10+)

A cleaner way to check a value against many possibilities (similar to long `if/elif` chains).

```python
command = "quit"

match command:
    case "start":
        print("Starting...")
    case "quit":
        print("Goodbye!")
    case _:
        print("Unknown command.")    # _ is the catch-all, like else
```

---

## 🧰 Functions

A **function** is a **reusable block of code** you give a name to. Write it once, use it many times.

---

### Defining a Function — `def`

Use `def` to create a function. The code inside only runs when you **call** the function by name.

```python
def greet():
    print("Hello, world!")

greet()    # calling the function → "Hello, world!"
```

---

### Parameters & Arguments

**Parameters** are the input variable names in the function definition.
**Arguments** are the actual values you pass in when calling.

```python
def greet(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")          # "Alice" is the argument → "Hello, Alice!"
greet("Bob")            # → "Hello, Bob!"
```

---

### Default Parameter Values

Give a parameter a **fallback value** so it works even if no argument is passed.

```python
def greet(name="stranger"):
    print(f"Hello, {name}!")

greet("Alice")    # → "Hello, Alice!"
greet()           # → "Hello, stranger!"
```

---

### `return` — Send Back a Result

`return` sends a value back out of the function so you can use it elsewhere. The function stops as soon as `return` is hit.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)    # → 8
```

---

### `*args` — Accept Any Number of Positional Arguments

Use `*args` when you don't know how many arguments will be passed. They arrive as a **tuple**.

```python
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))          # → 6
print(add_all(10, 20, 30, 40))   # → 100
```

---

### `**kwargs` — Accept Any Number of Named Arguments

Use `**kwargs` to accept any number of **keyword (named) arguments**. They arrive as a **dictionary**.

```python
def introduce(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

introduce(name="Alice", age=30, city="Paris")
# → name: Alice
# → age: 30
# → city: Paris
```

---

### Keyword Arguments

You can call a function using the **parameter name** to be extra clear about what goes where — order doesn't matter when you do this.

```python
def describe(color, size):
    print(f"A {size} {color} box.")

describe(size="large", color="red")    # → "A large red box."
```

---

### Scope — Where Variables Live

A variable created **inside** a function only exists inside that function. This is called **local scope**.

```python
def my_function():
    message = "I'm local!"    # only exists inside this function
    print(message)

my_function()
# print(message)    # ❌ Error! 'message' doesn't exist out here
```

Variables created **outside** all functions are in **global scope** and can be read from anywhere.

---

### `global` Keyword

If you need to **change** a global variable from inside a function, declare it with `global` first.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)    # → 1
```

---

### Docstrings — Documenting Your Function

A **docstring** is a description written right after `def`, inside triple quotes `"""`. It tells other people (and future you) what the function does.

```python
def add(a, b):
    """Takes two numbers and returns their sum."""
    return a + b

help(add)    # displays the docstring
```

---

### Lambda Functions — Tiny One-Line Functions

A **lambda** is a small, unnamed function written in a single line. Great for short, simple operations that don't need a full `def`.

**Syntax:** `lambda parameters: expression`

```python
# Normal function
def square(x):
    return x * x

# Same thing as a lambda
square = lambda x: x * x

print(square(5))    # → 25
```

Lambdas really shine when used **inside other functions** as a quick rule or instruction:

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(key=lambda x: x)
print(numbers)    # → [1, 1, 2, 3, 4, 5, 9]

# Sort a list of name-score pairs by the score (second item)
scores = [("Alice", 88), ("Bob", 95), ("Carol", 72)]
scores.sort(key=lambda pair: pair[1])
print(scores)    # → [('Carol', 72), ('Alice', 88), ('Bob', 95)]
```

> 💡 Use lambdas for **short, simple logic**. For anything more complex, stick with a regular `def` function.

---

### Built-in Functions Worth Knowing

These come with Python — no need to import anything.

| Function | What it does | Example |
|----------|--------------|---------|
| `print()` | Displays output | `print("Hi")` |
| `input()` | Gets text from the user | `name = input("Your name: ")` |
| `len()` | Counts items | `len([1,2,3])` → `3` |
| `range()` | Creates a sequence of numbers | `range(5)` → `0,1,2,3,4` |
| `type()` | Shows the data type | `type(3.14)` → `<class 'float'>` |
| `int()` | Converts to integer | `int("42")` → `42` |
| `str()` | Converts to string | `str(100)` → `"100"` |
| `float()` | Converts to decimal | `float("3.14")` → `3.14` |
| `sum()` | Adds up a list | `sum([1,2,3])` → `6` |
| `min()` | Finds smallest value | `min([3,1,2])` → `1` |
| `max()` | Finds largest value | `max([3,1,2])` → `3` |
| `sorted()` | Returns a sorted list | `sorted([3,1,2])` → `[1,2,3]` |
| `abs()` | Absolute value (removes minus sign) | `abs(-7)` → `7` |
| `round()` | Rounds a number | `round(3.7)` → `4` |
| `enumerate()` | Loops with an index and value together | `for i, v in enumerate(["a","b"])` |
| `zip()` | Combines two lists step by step | `zip([1,2], ["a","b"])` |

---

## 📋 Full Cheat Sheet

### Operators at a Glance

| Category | Symbols |
|----------|---------|
| Math | `+` `-` `*` `/` `//` `%` `**` |
| Assignment | `=` `+=` `-=` `*=` `/=` `//=` `%=` `**=` |
| Comparison | `==` `!=` `>` `<` `>=` `<=` |
| Logical | `and` `or` `not` |
| Identity | `is` `is not` |
| Membership | `in` `not in` |
| Bitwise | `&` `\|` `^` `~` `<<` `>>` |

---

### Operator Precedence (Highest → Lowest)

```
( )  →  **  →  unary +/-/~  →  * / // %  →  + -  →  << >>
  →  &  →  ^  →  |  →  comparisons  →  not  →  and  →  or
```

---

### Brackets at a Glance

| Bracket | Name | Used for |
|---------|------|----------|
| `( )` | Parentheses | Function calls, math grouping, tuples |
| `[ ]` | Square brackets | Lists, indexing items |
| `{ }` | Curly braces | Dictionaries, sets |

---

### Flow Control at a Glance

| Keyword | What it does |
|---------|--------------|
| `if` | Run code only if a condition is True |
| `elif` | Check another condition if the first was False |
| `else` | Run code when all conditions above were False |
| `for` | Loop over each item in a sequence |
| `while` | Loop as long as a condition stays True |
| `break` | Exit the loop immediately |
| `continue` | Skip to the next loop cycle |
| `pass` | Do nothing — placeholder for future code |
| `try` | Attempt code that might cause an error |
| `except` | Handle a specific error |
| `finally` | Always run this block, error or not |
| `match` / `case` | Check a value against multiple patterns |

---

### Functions at a Glance

| Concept | What it means |
|---------|---------------|
| `def` | Creates a named function |
| Parameter | The variable name in a function's definition |
| Argument | The actual value passed when calling a function |
| Default value | A fallback used when no argument is given |
| `return` | Sends a value back out of the function |
| `*args` | Accepts any number of positional arguments (as a tuple) |
| `**kwargs` | Accepts any number of keyword arguments (as a dict) |
| Local scope | A variable that only exists inside a function |
| Global scope | A variable that exists everywhere in the file |
| `global` | Lets a function modify a global variable |
| Docstring | A description of what a function does, in `"""triple quotes"""` |
| `lambda` | A tiny one-line anonymous function |

---

*Happy coding! 🎉 The best way to learn Python is to write it — even small experiments count.*
