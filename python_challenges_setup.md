# 🐍 Python Beginner Challenges – Setup Guide

A step-by-step guide to setting up 5 beginner-friendly Python challenges covering **user input**, **string formatting**, **data types**, and **data casting**.

---

## 📁 Project Structure

Create a folder called `python_challenges/` and add the following 5 files inside it:

```
python_challenges/
├── challenge_01_greeting.py
├── challenge_02_age_calculator.py
├── challenge_03_temperature_converter.py
├── challenge_04_shopping_receipt.py
└── challenge_05_profile_card.py
```

---

## ✅ Prerequisites

Before starting, make sure you have:

- Python 3.x installed — verify with `python --version` in your terminal
- A code editor (VS Code, PyCharm, or even a plain text editor)
- A terminal or command prompt to run your files

---

## Challenge 1 — Personalised Greeting (`challenge_01_greeting.py`)

**Concepts:** `input()`, string formatting with f-strings

**Goal:** Ask the user for their first and last name, then print a formatted greeting message.

**Setup Steps:**
1. Create `challenge_01_greeting.py`
2. Use `input()` to collect the user's first name and last name as separate inputs
3. Store each in its own variable (e.g. `first_name`, `last_name`)
4. Use an f-string to print: `Hello, <First> <Last>! Welcome to Python.`
5. Run with `python challenge_01_greeting.py` and verify the output

**Example output:**
```
Enter your first name: Jane
Enter your last name: Doe
Hello, Jane Doe! Welcome to Python.
```

---

## Challenge 2 — Age Calculator (`challenge_02_age_calculator.py`)

**Concepts:** `input()`, data casting with `int()`, arithmetic, string formatting

**Goal:** Ask the user for their birth year and calculate their current age.

**Setup Steps:**
1. Create `challenge_02_age_calculator.py`
2. Use `input()` to ask for the user's birth year — note this returns a **string**
3. Cast the result to an integer using `int()`
4. Subtract the birth year from the current year (e.g. `2025`) to get the age
5. Print the result using an f-string: `You are approximately <age> years old.`
6. Run the file and test with a few different years

**Example output:**
```
Enter your birth year: 1998
You are approximately 27 years old.
```

---

## Challenge 3 — Temperature Converter (`challenge_03_temperature_converter.py`)

**Concepts:** `input()`, casting with `float()`, arithmetic, f-strings with formatting specifiers

**Goal:** Ask the user for a temperature in Celsius and convert it to Fahrenheit.

**Setup Steps:**
1. Create `challenge_03_temperature_converter.py`
2. Use `input()` to ask for a temperature in Celsius
3. Cast the input to a `float` using `float()`
4. Apply the formula: `fahrenheit = (celsius * 9/5) + 32`
5. Print the result rounded to 2 decimal places using an f-string: `{fahrenheit:.2f}`
6. Run the file and test with values like `0`, `100`, and `37`

**Example output:**
```
Enter temperature in Celsius: 100
100.0°C is equal to 212.00°F
```

---

## Challenge 4 — Shopping Receipt (`challenge_04_shopping_receipt.py`)

**Concepts:** `input()`, `float()`, `int()`, f-strings, basic arithmetic, string alignment

**Goal:** Ask the user for 3 item names and their prices, then print a formatted receipt with a total.

**Setup Steps:**
1. Create `challenge_04_shopping_receipt.py`
2. Use `input()` to collect a name and price for 3 separate items (6 inputs total)
3. Cast each price to a `float`
4. Calculate the total by summing all 3 prices
5. Print a formatted receipt using f-strings, aligning item names and prices neatly
6. Display the total at the bottom, formatted to 2 decimal places

**Example output:**
```
Enter item 1 name: Apples
Enter item 1 price: 1.50
...
---------------------
 Apples         $1.50
 Bread          $2.30
 Milk           $1.20
---------------------
 TOTAL          $5.00
```

---

## Challenge 5 — Profile Card (`challenge_05_profile_card.py`)

**Concepts:** `input()`, `int()`, `float()`, `str()`, f-strings, multiple data types together

**Goal:** Collect various details about the user and display a neatly formatted profile card, demonstrating use of multiple data types.

**Setup Steps:**
1. Create `challenge_05_profile_card.py`
2. Use `input()` to collect: name (`str`), age (`int`), height in metres (`float`), and favourite number (`int`)
3. Cast each input to its appropriate data type
4. Calculate the user's height in centimetres by multiplying height by `100` and casting to `int`
5. Build a profile card output using f-strings, displaying all collected and derived data
6. Run the file and confirm all data types are handled correctly without errors

**Example output:**
```
Enter your name: Alex
Enter your age: 24
Enter your height in metres: 1.75
Enter your favourite number: 7

================================
        YOUR PROFILE CARD
================================
 Name:              Alex
 Age:               24 years
 Height:            1.75m (175cm)
 Favourite Number:  7
================================
```

---

## 🏃 Running All Challenges

From inside the `python_challenges/` folder, run any file with:

```bash
python challenge_01_greeting.py
python challenge_02_age_calculator.py
python challenge_03_temperature_converter.py
python challenge_04_shopping_receipt.py
python challenge_05_profile_card.py
```

---

## 📚 Key Concepts Reference

| Concept | Example |
|---|---|
| User input | `name = input("Enter name: ")` |
| Cast to int | `age = int(input("Enter age: "))` |
| Cast to float | `price = float(input("Enter price: "))` |
| Cast to string | `label = str(42)` |
| f-string | `f"Hello, {name}!"` |
| Format decimals | `f"{value:.2f}"` |

---

*Happy coding! 🎉 These 5 challenges build on each other — try completing them in order.*
