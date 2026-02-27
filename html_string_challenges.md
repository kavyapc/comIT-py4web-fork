# 🧩 Python String Manipulation Challenges — HTML Builder

A series of 5 progressive challenges where you manipulate a **multi-line string** containing a minimal HTML page using **string methods and string concatenation only**. No HTML parsers, no libraries, no list indexing tricks — pure string manipulation.

---

## 📁 Project Structure

```
html_string_challenges/
├── challenge_01_metadata.py
├── challenge_02_stylesheets_and_scripts.py
├── challenge_03_headings.py
├── challenge_04_content.py
└── challenge_05_full_page.py
```

---

## 🧱 The Base Template

Every challenge file must begin by declaring the following multi-line string **exactly as shown**. Do not modify it directly — your task is to manipulate it programmatically using string methods only.

```python
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>"""
```

Copy this template at the top of each challenge file and work from there.

---

## 📐 Rules for All Challenges

These rules apply to every single challenge. Breaking them defeats the purpose of the exercise:

- You **may only use string methods** such as `.replace()`, `.find()`, `.split()`, `.strip()`, `.startswith()`, `.endswith()`, `.join()`, `.upper()`, `.lower()`, `.count()`, `.index()` and so on
- You **may use string concatenation** with `+` and in-place `+=`
- You **may use f-strings** to build new string values before inserting them
- You **may NOT** convert the string to a list to manipulate elements by index and then rejoin
- You **may NOT** use any import, library, or HTML/XML parser
- Your final result in each challenge must be printed with `print(html)` so the output is a valid, readable HTML string

---

## Challenge 1 — Update the Page Metadata (`challenge_01_metadata.py`)

**Concepts:** `.replace()`, string concatenation, f-strings

**Difficulty:** ⭐ Beginner

### Background

The `<title>` tag and the `lang` attribute on the `<html>` tag are two of the most important pieces of metadata on any web page. In this challenge you will update both dynamically using variables, practising the most fundamental string manipulation method: `.replace()`.

### Your Task

Starting from the base template:

1. Declare a variable `page_title` with a value of your choice, e.g. `"My Awesome Portfolio"`
2. Declare a variable `page_lang` with a language code of your choice, e.g. `"pt"` or `"fr"`
3. Use `.replace()` to swap `"My Page"` inside the `<title>` tag with the value of `page_title`
4. Use `.replace()` to swap `lang="en"` with a new `lang` attribute built from `page_lang` using string concatenation or an f-string
5. Print the result and verify the changes appear in the correct places

### Expected Output (example)

```html
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Awesome Portfolio</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>
```

### 🎯 Advanced Extension

The `.replace()` method accepts a third argument — a count — limiting how many occurrences it replaces. Research this and write a short comment in your file explaining why this matters when your target substring might appear more than once in a larger HTML document. Then write a version of your replacement that explicitly passes this count argument.

---

## Challenge 2 — Update Stylesheet and Script Sources (`challenge_02_stylesheets_and_scripts.py`)

**Concepts:** `.find()`, `.index()`, string slicing with computed positions, concatenation

**Difficulty:** ⭐⭐ Intermediate

### Background

Hardcoded filenames like `styles.css` and `app.js` are rarely useful in real projects. In this challenge you will replace both the `href` value in the `<link>` tag and the `src` value in the `<script>` tag — but with a constraint: you are **not allowed to use `.replace()` in this challenge**. Instead, you must locate the substrings using `.find()` or `.index()` and reconstruct the string by slicing with computed integer positions.

### Your Task

Starting from the base template:

1. Declare `stylesheet` = `"main.min.css"` and `script_file` = `"bundle.js"`
2. Locate the exact character position of `styles.css` inside `html` using `.find()` or `.index()`
3. Use that position along with `len()` to rebuild `html` by concatenating the part before the filename, your new filename, and the part after — using string slicing `[start:end]`
4. Repeat the process for `app.js`, updating it to the value of `script_file`
5. Print and verify

### Expected Output (example)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="main.min.css">
    <script src="bundle.js"></script>
</head>
<body>
</body>
</html>
```

### 🎯 Advanced Extension

Both `.find()` and `.index()` accept optional `start` and `end` arguments to search within a substring range. Rewrite your solution so that when searching for `app.js`, you pass a `start` argument to `.find()` that begins searching only after the position of `</head>` — even though `app.js` appears before it. Then explain in a comment why restricting search ranges becomes critical when maintaining large HTML templates with repeated attribute names like `src` or `href`.

---

## Challenge 3 — Inject Heading Tags (`challenge_03_headings.py`)

**Concepts:** `.find()`, `.split()` on a specific separator, string concatenation, multi-line string building

**Difficulty:** ⭐⭐ Intermediate

### Background

The `<body>` tag is empty in our template. You will now inject heading content inside it. The challenge is that you must insert new content **between** `<body>` and `</body>` without using `.replace()` on those tags themselves — instead you must split the string on a carefully chosen separator and reassemble it. This forces you to think carefully about which substrings are safe to split on.

### Your Task

Starting from the base template:

1. Declare three variables: `h1` = `"Welcome to My Page"`, `h2` = `"About This Project"`, `h3` = `"Technical Details"`
2. Build a `body_content` string by concatenating the heading tags around those variables, with a newline `\n` and appropriate indentation (4 spaces) between each tag — do not hardcode the tag content, always use the variables
3. Use `.split("<body>")` to divide `html` into exactly 2 parts
4. Rebuild `html` by concatenating: part 0 + `"<body>\n"` + `body_content` + part 1
5. Print and verify that the headings appear correctly nested inside `<body>` and `</body>`

### Expected Output (example)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
    <h1>Welcome to My Page</h1>
    <h2>About This Project</h2>
    <h3>Technical Details</h3>
</body>
</html>
```

### 🎯 Advanced Extension

`.split()` with a separator will produce as many parts as there are occurrences of that separator plus one. What would happen to your string reconstruction if `<body>` appeared more than once — for instance, inside a comment or a code sample displayed on the page? Write a version of your solution that uses `.split("<body>", 1)` with a maxsplit of `1` and add a comment explaining why this is safer and should always be the default approach for HTML manipulation via splitting.

---

## Challenge 4 — Add Paragraph and Image Tags (`challenge_04_content.py`)

**Concepts:** `.find()`, `.rfind()`, multi-step string reconstruction, f-strings, `\n` and indentation management

**Difficulty:** ⭐⭐⭐ Advanced

### Background

In this challenge you will add both `<p>` and `<img>` tags inside the body, but the catch is that you must **insert them after the last heading tag** that already exists — meaning you cannot simply split on `<body>` again or you will lose the headings. You must locate the insertion point dynamically using `.rfind()` to find the last closing heading tag, then reconstruct precisely.

Start this challenge from the **output of Challenge 3** (copy the final state of `html` from challenge 3 as your starting variable here), not from the blank base template.

### Your Task

1. Declare the following variables:
   - `paragraph_text` = `"This project was built entirely using Python string methods."`
   - `img_src` = `"hero.jpg"`
   - `img_alt` = `"A hero image for the page"`
2. Build `p_tag` as a properly formatted `<p>` tag string using `paragraph_text`
3. Build `img_tag` as a self-closing `<img>` tag using `img_src` and `img_alt` — construct the full attribute string via concatenation, not `.replace()`
4. Use `.rfind()` to locate the position of the **last closing tag** among `</h1>`, `</h2>`, `</h3>` that appears in the string — you must check all three and determine which appears latest using comparison of their positions
5. From that position, calculate the end of that closing tag line and insert your `p_tag` and `img_tag` after it with correct newlines and 4-space indentation
6. Print and verify

### Expected Output (example)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
    <h1>Welcome to My Page</h1>
    <h2>About This Project</h2>
    <h3>Technical Details</h3>
    <p>This project was built entirely using Python string methods.</p>
    <img src="hero.jpg" alt="A hero image for the page">
</body>
</html>
```

### 🎯 Advanced Extension

The insertion logic you wrote depends on knowing which closing heading tag appears last. Generalise this: write a helper snippet (still no imports, no functions unless you define them yourself inline) that builds a list of candidate closing tags `["</h1>", "</h2>", "</h3>"]`, iterates over them to find all their positions via `.rfind()`, filters out any that return `-1` (not found), and picks the maximum position. This should replace any hardcoded tag assumptions and work correctly even if the HTML only contains an `<h1>` and no `<h2>` or `<h3>`.

---

## Challenge 5 — Full Page Builder (`challenge_05_full_page.py`)

**Concepts:** All previous methods combined, multi-step transformation pipeline, string validation

**Difficulty:** ⭐⭐⭐⭐ Expert

### Background

This is the culminating challenge. You will start from the **original base template** (not the output of any previous challenge) and perform **all transformations in sequence** — building the complete modified page from scratch using only string methods and concatenation. You must also perform basic string validation checks along the way to confirm your transformations succeeded before proceeding to the next one.

Think of this as building a minimal templating pipeline using nothing but Python's built-in string capabilities.

### Your Task

Starting fresh from the base template, perform all of the following transformations **in order**:

**Step 1 — Metadata**
Update `lang` to `"es"` and `<title>` to `"Full Page Challenge"` using `.replace()`

**Step 2 — Assets**
Update the stylesheet href to `"app.min.css"` and script src to `"main.bundle.js"` using position-based slicing (no `.replace()`)

**Step 3 — Validate Step 2**
Before continuing, use `.count()` to assert that `"styles.css"` and `"app.js"` no longer appear in `html`. Print a confirmation message if both return `0`, or print a specific error message identifying which one was not replaced if either returns more than `0`. Do not use `assert` — build this check yourself using `if` statements and string methods only.

**Step 4 — Headings**
Inject an `<h1>`, `<h2>`, and `<h3>` into the body using `.split("<body>", 1)` and string concatenation

**Step 5 — Paragraph and Image**
Insert a `<p>` tag and an `<img>` tag after the last heading tag using `.rfind()` and position-based reconstruction

**Step 6 — Add a second paragraph**
Use `.find("</body>")` to locate the closing body tag and insert a second `<p>` tag immediately before it — this `<p>` should contain a string that itself includes the `<title>` content, extracted dynamically from `html` using `.find("<title>")`, `.find("</title>")` and slicing

**Step 7 — Final Validation**
Before printing, verify all of the following using string methods and print a status report:
- `<title>Full Page Challenge</title>` is present — use `.count()`
- `<h1>`, `<h2>`, and `<h3>` all appear — use `.count()` for each
- `<img` appears exactly once — use `.count()`
- `<p>` appears exactly twice — use `.count()`
- The string starts with `<!DOCTYPE html>` — use `.startswith()`
- The string ends with `</html>` after stripping whitespace — use `.strip()` and `.endswith()`

Print a labelled line for each check showing ✅ or ❌ and the checked condition.

**Step 8 — Print the final HTML**
Print the complete final `html` string.

### Expected Validation Report (example)

```
--- Validation Report ---
✅ <title> is correct
✅ <h1> found
✅ <h2> found
✅ <h3> found
✅ <img> appears exactly once
✅ <p> appears exactly twice
✅ Starts with <!DOCTYPE html>
✅ Ends with </html>
-------------------------
```

### 🎯 Advanced Extension

The second paragraph in Step 6 requires you to extract the title text dynamically from the string. Extend this idea: write a generalised extraction snippet that, given any tag name as a string variable (e.g. `tag = "h1"`), locates the **first occurrence** of that opening and closing tag pair and returns the content between them — using only `.find()`, `len()`, and slicing. Test it against `"title"`, `"h1"`, `"h2"`, and `"h3"` and print each result. This is the core idea behind a minimal HTML content extractor — built entirely from string primitives.

---

## 📚 String Methods Reference

| Method | Purpose | Example |
|---|---|---|
| `.replace(old, new, count)` | Swap substrings | `s.replace("en", "pt", 1)` |
| `.find(sub, start, end)` | First index or -1 | `s.find("</body>")` |
| `.rfind(sub)` | Last index or -1 | `s.rfind("</h3>")` |
| `.index(sub)` | First index or error | `s.index("<title>")` |
| `.split(sep, maxsplit)` | Break into parts | `s.split("<body>", 1)` |
| `.strip()` | Remove surrounding whitespace | `s.strip()` |
| `.startswith(prefix)` | Check beginning | `s.startswith("<!DOCTYPE")` |
| `.endswith(suffix)` | Check end | `s.endswith("</html>")` |
| `.count(sub)` | Count occurrences | `s.count("<p>")` |
| `len(sub)` | Length of a string | `len("<title>")` |

---

## 💡 Tips for All Challenges

When computing an insertion point from `.find()`, always account for the full length of the separator you split or searched on using `len()`. Off-by-one errors are the most common bug in position-based string reconstruction — print intermediate position values to debug them.

When rebuilding a string via slicing, the pattern is always: `html[:position] + new_content + html[position:]`. Getting the position right is everything.

For the advanced extensions, you are expected to go beyond the obvious solution. The goal is not just correct output but a solution that would hold up if the HTML template grew to hundreds of lines with repeated tag names, multiple stylesheets, or nested structures.

---

*These challenges are intentionally constrained. The restrictions exist to build deep intuition for how strings work at a low level — skills that transfer directly to parsing, templating, code generation, and data transformation tasks in the real world. 🚀*
