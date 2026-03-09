---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
style: |
  section {
    font-family: 'Segoe UI', sans-serif;
    font-size: 22px;
  }
  h1 {
    color: #e44d26;
  }
  h2 {
    color: #264de4;
    border-bottom: 2px solid #264de4;
    padding-bottom: 6px;
  }
  code {
    background: #f4f4f4;
    border-radius: 4px;
    padding: 2px 6px;
    color: #c7254e;
  }
  pre {
    background: #1e1e1e;
    color: #d4d4d4;
    border-radius: 8px;
    padding: 16px;
    font-size: 18px;
  }
  .tip {
    background: #e8f4fd;
    border-left: 4px solid #264de4;
    padding: 10px 16px;
    border-radius: 4px;
  }
---

# 🌐 Web Development by y44k0v
## A Beginner's Guide to the Basics

Welcome! This presentation will walk you through the **core building blocks** of the web — from the very first acronyms you'll encounter to writing your first lines of HTML, CSS, and JavaScript.

---

# The Three Languages of the Web

Every website you've ever visited is built using **three technologies** working together:

| Technology | Stands for | Role |
|---|---|---|
| **HTML** | HyperText Markup Language | The **structure** — the bones |
| **CSS** | Cascading Style Sheets | The **appearance** — the skin |
| **JS** | JavaScript | The **behavior** — the muscles |

> Think of a house: HTML is the walls and rooms, CSS is the paint and decoration, JavaScript makes the doors open and lights turn on.

---

# 🧱 HTML — HyperText Markup Language

**What it does:** HTML defines the *structure and content* of a web page.

- "**HyperText**" = text that links to other text (hyperlinks!)
- "**Markup**" = you *mark up* content with tags to give it meaning
- "**Language**" = a set of rules the browser understands

**Example of what HTML defines:**
- This is a heading
- This is a paragraph
- This is an image
- This is a button

HTML is always the **starting point** of any web page.

---

# 🎨 CSS — Cascading Style Sheets

**What it does:** CSS controls *how things look* on the page.

- "**Cascading**" = styles can flow from parent to child elements, and rules have a priority order
- "**Style Sheets**" = documents full of visual rules

**CSS lets you control:**
- Colors and fonts
- Sizes and spacing
- Layout and positioning
- Animations and transitions

Without CSS, every website would look like a plain text document!

---

# ⚡ JavaScript (JS)

**What it does:** JavaScript makes web pages *interactive and dynamic*.

- It's a full programming language that runs **inside the browser**
- It can respond to user actions (clicks, typing, scrolling...)
- It can **change** the HTML and CSS on the page — live, without reloading

**JavaScript powers things like:**
- Pop-up menus and modals
- Form validation ("Please fill in your email")
- Live search results
- Games, animations, and apps

---

# 🔒 HTTP & HTTPS

Before a browser can show a page, it has to **request** it from a server. That's where HTTP comes in.

| | Stands for | What it does |
|---|---|---|
| **HTTP** | HyperText Transfer Protocol | The set of rules for *sending* data between browser and server |
| **HTTPS** | HyperText Transfer Protocol **Secure** | Same as HTTP, but the data is **encrypted** (scrambled so no one can spy on it) |

> 🔑 Always look for **HTTPS** (the padlock 🔒 in your browser bar) when entering passwords or payment info. It means your connection is secure.

---

# 🏷️ HTML Tags — The Basics

HTML is written using **tags**. A tag looks like this:

```html
<tagname> content goes here </tagname>
```

- **Opening tag:** `<tagname>`
- **Closing tag:** `</tagname>` (notice the `/`)
- Everything between them is the **content**

**Common tags:**

```html
<h1>I am a big heading</h1>
<p>I am a paragraph of text.</p>
<a href="https://google.com">Click me!</a>
<img src="photo.jpg" alt="A photo">
<button>Press me</button>
```

---

# 🏷️ HTML Tags — Block vs Inline

Tags fall into two big categories:

**Block elements** — take up the full width, start on a new line
```html
<div>  <p>  <h1>  <ul>  <li>  <section>
```

**Inline elements** — only take up as much space as they need
```html
<span>  <a>  <strong>  <em>  <img>
```

> 💡 `<div>` and `<span>` are the most generic containers. `<div>` is block, `<span>` is inline. You'll use them *constantly*.

---

# 🔖 HTML Attributes

Attributes give **extra information** to a tag. They go inside the opening tag:

```html
<tagname attribute="value"> content </tagname>
```

**The three most important attributes:**

| Attribute | Purpose | Example |
|---|---|---|
| `id` | A **unique** name for one specific element | `id="main-title"` |
| `class` | A **shared** label used on many elements | `class="card"` |
| `name` | Used in **forms** to identify input data | `name="username"` |

---

# 🔖 `id` vs `class` — What's the Difference?

**`id`** → One of a kind. Like a social security number.
```html
<h1 id="page-title">Welcome!</h1>
```
Only **one** element on the page should have this id.

---

**`class`** → A group label. Like a team jersey number.
```html
<p class="highlight">This is important.</p>
<p class="highlight">This is also important.</p>
<p class="highlight">Me too!</p>
```
**Many** elements can share the same class. CSS and JS use it to style/target a group.

---

# 🔖 More Useful Attributes

```html
<!-- href: where a link goes -->
<a href="https://google.com">Go to Google</a>

<!-- src: the source file for an image -->
<img src="cat.jpg" alt="A cute cat">

<!-- alt: text shown if image can't load (also for accessibility) -->
<img src="dog.jpg" alt="A golden retriever">

<!-- type, placeholder: for form inputs -->
<input type="text" placeholder="Enter your name">
<input type="email" placeholder="Enter your email">

<!-- disabled: makes an element unclickable -->
<button disabled>Can't click me!</button>
```

---

# 📄 The Full HTML Structure

Every HTML file follows this skeleton:

```html
<!DOCTYPE html>
<html lang="en">

  <head>
    <!-- Invisible info about the page goes here -->
    <title>My Page Title</title>
  </head>

  <body>
    <!-- Everything VISIBLE on the page goes here -->
    <h1>Hello World!</h1>
    <p>My first web page.</p>
  </body>

</html>
```

> `<!DOCTYPE html>` tells the browser: "This is a modern HTML5 document."

---

# 🧠 The `<head>` Tag

The `<head>` is like the **control room** of your page. Its contents are **not visible** to users, but they're crucial.

```html
<head>

  <!-- Page title (shows in browser tab) -->
  <title>My Awesome Website</title>

  <!-- Character encoding — always include this! -->
  <meta charset="UTF-8">

  <!-- Makes the page look good on phones -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Description for Google search results -->
  <meta name="description" content="A beginner web dev tutorial.">

</head>
```

---

# 🧠 Linking CSS & JS in `<head>`

This is how you connect your CSS and JavaScript files to your HTML:

```html
<head>
  <meta charset="UTF-8">
  <title>My Page</title>

  <!-- 🎨 Link your CSS file -->
  <link rel="stylesheet" href="style.css">

  <!-- ⚡ Link your JavaScript file -->
  <!-- The "defer" means: wait until the page loads, then run the JS -->
  <script src="script.js" defer></script>

</head>
```

> 📁 Make sure `style.css` and `script.js` are in the **same folder** as your HTML file, or adjust the path.

---

# 🧠 Popular `<meta>` Tags — Cheat Sheet

```html
<!-- Always include these two: -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- For SEO (Search Engine Optimization): -->
<meta name="description" content="Page summary for Google">
<meta name="author" content="Your Name">

<!-- For social media previews (Open Graph): -->
<meta property="og:title" content="My Page Title">
<meta property="og:image" content="preview.jpg">
<meta property="og:description" content="Shown when you share on social media">
```

---

# 🎨 CSS — How It Works

CSS uses **rules** made of a **selector** and **declarations**:

```css
selector {
  property: value;
  property: value;
}
```

**Real example:**

```css
/* Target all <p> tags */
p {
  color: darkblue;
  font-size: 18px;
}

/* Target any element with class="highlight" */
.highlight {
  background-color: yellow;
}

/* Target the element with id="page-title" */
#page-title {
  font-size: 36px;
  font-weight: bold;
}
```

---

# 🎨 CSS — Selectors at a Glance

| Selector | Syntax | Targets |
|---|---|---|
| Tag | `p { }` | All `<p>` elements |
| Class | `.card { }` | All elements with `class="card"` |
| ID | `#hero { }` | The element with `id="hero"` |
| All | `* { }` | Every element on the page |
| Descendant | `div p { }` | `<p>` tags *inside* a `<div>` |

> 💡 **Classes** (`.`) are used for styling **groups**. **IDs** (`#`) are used for styling **one unique thing**.

---

# 🎨 CSS — The Box Model

Every HTML element is a **box**. The box has layers:

```
┌──────────────────────────────┐
│           MARGIN             │  ← Space outside the border
│  ┌────────────────────────┐  │
│  │        BORDER          │  │  ← The visible border line
│  │  ┌──────────────────┐  │  │
│  │  │     PADDING      │  │  │  ← Space between border and content
│  │  │  ┌────────────┐  │  │  │
│  │  │  │  CONTENT   │  │  │  │  ← Your text or image
│  │  │  └────────────┘  │  │  │
│  │  └──────────────────┘  │  │
│  └────────────────────────┘  │
└──────────────────────────────┘
```

```css
div {
  margin: 20px;    padding: 10px;
  border: 2px solid black;   width: 300px;
}
```

---

# 🎨 CSS — Common Properties

```css
.my-box {
  /* Text */
  color: #333333;           /* text color */
  font-size: 16px;          /* text size */
  font-family: Arial, sans-serif;
  text-align: center;

  /* Background */
  background-color: #f0f0f0;

  /* Size */
  width: 200px;
  height: 100px;

  /* Spacing */
  padding: 10px;            /* inside space */
  margin: 20px auto;        /* outside space (auto = centered) */

  /* Border */
  border: 1px solid #ccc;
  border-radius: 8px;       /* rounded corners */
}
```

---

# ⚡ JavaScript — How It Works

JavaScript runs **in the browser** and can interact with the page.

The browser gives JavaScript access to the **DOM** (Document Object Model) — a live map of all the HTML elements on your page.

You can use JavaScript to:
- **Find** elements on the page
- **Read or change** their content, style, or attributes
- **Listen** for user actions (clicks, key presses...)
- **React** to those actions

> 🗺️ Think of the DOM as a family tree of all your HTML tags. JavaScript can grab any branch and change it.

---

# ⚡ JavaScript — Finding Elements

The most important JS tool for beginners:

```javascript
// Find ONE element by its id
document.getElementById("my-id")

// Find the FIRST element matching a CSS selector
document.querySelector(".my-class")
document.querySelector("#my-id")
document.querySelector("p")

// Find ALL elements matching a CSS selector
document.querySelectorAll(".card")
```

> 💡 `document` is the entire page. You're saying: "Hey page, give me this element."

---

# ⚡ JavaScript — A Real Example

**Goal:** Click a button → a `<div>` changes its message and color.

**HTML (index.html):**
```html
<div id="message-box">Hello! I am unchanged.</div>
<button id="magic-button">✨ Click me!</button>
```

**JavaScript (script.js):**
```javascript
// 1. Find the button and the div
const button = document.getElementById("magic-button");
const box = document.getElementById("message-box");

// 2. Listen for a click on the button
button.addEventListener("click", function() {
  // 3. When clicked, run this function:
  changeMessage();
});
```

---

# ⚡ JavaScript — The Function Explained

```javascript
function changeMessage() {

  // Change the text inside the div
  box.textContent = "🎉 You clicked! I have been changed by JavaScript!";

  // Change the background color using inline CSS
  box.style.backgroundColor = "lightgreen";

  // Add a CSS class (defined in style.css)
  box.classList.add("success-box");

}
```

**Let's break it down:**
- `function changeMessage() { }` → defines a reusable block of code
- `box.textContent = "..."` → changes the text inside the div
- `box.style.backgroundColor = "..."` → changes a CSS style directly
- `box.classList.add("...")` → adds a CSS class to the element

---

# ⚡ JavaScript — The CSS to go with it

**CSS (style.css):**
```css
#message-box {
  padding: 20px;
  background-color: lightyellow;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 20px;
  text-align: center;
}

/* This class is added by JavaScript when the button is clicked */
.success-box {
  border-color: green;
  font-weight: bold;
}

#magic-button {
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
}
```

---

# 🗂️ Putting It All Together

Your project folder should look like this:

```
my-website/
│
├── index.html       ← Your HTML structure
├── style.css        ← Your CSS styles
└── script.js        ← Your JavaScript
```

And your `index.html` connects them in the `<head>`:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My First Website</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js" defer></script>
</head>
```

---

# 🚀 Quick Reference — What Does What?

| I want to... | I use... |
|---|---|
| Define a heading | `<h1>` to `<h6>` in HTML |
| Write a paragraph | `<p>` in HTML |
| Create a clickable link | `<a href="...">` in HTML |
| Target one specific element | `id="..."` attribute |
| Target a group of elements | `class="..."` attribute |
| Change text color | `color:` in CSS |
| Space things out | `margin` / `padding` in CSS |
| React to a button click | `addEventListener("click", ...)` in JS |
| Change text on the page | `element.textContent = "..."` in JS |

---

# 🎓 You're Ready to Start!

You now know the **vocabulary** of web development:

- ✅ **HTML** builds the structure
- ✅ **CSS** styles the appearance
- ✅ **JavaScript** adds interactivity
- ✅ **HTTP/HTTPS** transports the page to your browser
- ✅ **Tags, attributes, id, class** are the building blocks
- ✅ **`<head>`** connects your CSS and JS files
- ✅ **Functions** in JS let you react to user actions

> 🛠️ **Next step:** Open VS Code, create the three files, and try the button example yourself!

---

# 📚 Where to Learn More

- **MDN Web Docs** → [developer.mozilla.org](https://developer.mozilla.org) — the bible of web development
- **freeCodeCamp** → [freecodecamp.org](https://freecodecamp.org) — free, project-based learning
- **The Odin Project** → [theodinproject.com](https://theodinproject.com) — free full-stack curriculum
- **W3Schools** → [w3schools.com](https://w3schools.com) — quick reference and try-it editors

> 💪 The best way to learn is to **build things** — even if they're broken at first. Every developer started exactly where you are now.

---

<!-- Last slide -->
# Thank You! 🌐

### Happy Coding!

```html
<p id="farewell">You've got this! 🚀</p>
```
```css
#farewell { color: #e44d26; font-size: 32px; }
```
```javascript
document.getElementById("farewell")
  .textContent = "Now go build something! 🛠️";
```
