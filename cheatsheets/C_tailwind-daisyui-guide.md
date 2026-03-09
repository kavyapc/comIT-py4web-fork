# 🌼 Tailwind CSS + DaisyUI — Beginner's Guide to Responsive Static Webpages

> A practical, example-packed reference for building beautiful, responsive websites from scratch.

---

## 📦 Table of Contents

1. [Setup & Installation](#setup)
2. [How Tailwind Works](#how-tailwind-works)
3. [Typography — Headings & Text](#typography)
4. [Colors & Backgrounds](#colors)
5. [Spacing — Padding & Margin](#spacing)
6. [Flexbox](#flexbox)
7. [CSS Grid](#grid)
8. [Responsive Design](#responsive)
9. [DaisyUI — Introduction](#daisyui-intro)
10. [DaisyUI Components](#daisyui-components)
    - Buttons
    - Badges
    - Alerts
    - Cards
    - Navbar
    - Hero
    - Footer
    - Modal
    - Dropdown
    - Tabs
    - Accordion / Collapse
    - Avatar
    - Progress & Stats
    - Forms & Inputs
    - Tables
    - Toasts
11. [Themes & Customization](#themes)
12. [Full Page Example](#full-example)

---

## 1. Setup & Installation <a name="setup"></a>

### Option A — CDN (Fastest for beginners, no build tools needed)

Just drop these two lines inside the `<head>` of your HTML file:

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>My Website</title>

  <!-- Tailwind CSS + DaisyUI via CDN -->
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.10.1/dist/full.min.css" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <h1 class="text-4xl font-bold text-center mt-10">Hello, World! 🌍</h1>
</body>
</html>
```

> ✅ **Tip:** The `data-theme="light"` attribute on `<html>` sets the DaisyUI color theme. You can change it to `dark`, `cupcake`, `cyberpunk`, and many more.

---

### Option B — npm (For real projects)

```bash
npm install -D tailwindcss daisyui
npx tailwindcss init
```

In your `tailwind.config.js`:

```js
module.exports = {
  content: ["./**/*.html"],
  plugins: [require("daisyui")],
}
```

---

## 2. How Tailwind Works <a name="how-tailwind-works"></a>

Tailwind CSS is a **utility-first** CSS framework. Instead of writing custom CSS, you apply small, single-purpose classes directly in your HTML.

### Traditional CSS vs Tailwind

**Traditional CSS:**
```css
/* style.css */
.my-button {
  background-color: blue;
  color: white;
  padding: 8px 16px;
  border-radius: 8px;
}
```
```html
<button class="my-button">Click me</button>
```

**Tailwind CSS:**
```html
<button class="bg-blue-500 text-white px-4 py-2 rounded-lg">Click me</button>
```

No separate CSS file needed. Everything lives in the class attribute. 🎉

---

## 3. Typography — Headings & Text <a name="typography"></a>

### Example 1 — Heading Sizes

```html
<h1 class="text-5xl font-bold">Heading 1 — Huge</h1>
<h2 class="text-4xl font-semibold">Heading 2 — Large</h2>
<h3 class="text-3xl font-semibold">Heading 3 — Medium-Large</h3>
<h4 class="text-2xl font-medium">Heading 4 — Medium</h4>
<h5 class="text-xl font-medium">Heading 5 — Small</h5>
<h6 class="text-lg font-normal">Heading 6 — Smallest</h6>
```

**Text size classes:** `text-xs`, `text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl` ... `text-9xl`

---

### Example 2 — Font Weight

```html
<p class="font-thin">Thin text (100)</p>
<p class="font-light">Light text (300)</p>
<p class="font-normal">Normal text (400)</p>
<p class="font-medium">Medium text (500)</p>
<p class="font-semibold">Semibold text (600)</p>
<p class="font-bold">Bold text (700)</p>
<p class="font-extrabold">Extrabold text (800)</p>
<p class="font-black">Black text (900)</p>
```

---

### Example 3 — Text Alignment & Decoration

```html
<p class="text-left">Left aligned paragraph.</p>
<p class="text-center">Centered paragraph.</p>
<p class="text-right">Right aligned paragraph.</p>
<p class="text-justify">Justified paragraph — text spreads evenly to both edges of the line.</p>

<p class="underline">Underlined text</p>
<p class="line-through">Strikethrough text</p>
<p class="italic">Italic text</p>
<p class="uppercase">uppercase text</p>
<p class="capitalize">capitalize each word</p>
<p class="lowercase">LOWERCASE TEXT</p>
```

---

### Example 4 — Styled Paragraph

```html
<p class="text-base leading-relaxed text-gray-600 max-w-prose mx-auto">
  This is a nicely styled paragraph. The <code>leading-relaxed</code> class
  gives comfortable line spacing. <code>max-w-prose</code> limits the width
  to an optimal reading length (~65 characters). <code>mx-auto</code> centers it.
</p>
```

**Leading (line-height) classes:** `leading-tight`, `leading-snug`, `leading-normal`, `leading-relaxed`, `leading-loose`

---

### Example 5 — Highlighted & Colored Text

```html
<p class="text-blue-600">Blue text</p>
<p class="text-red-500">Red text</p>
<p class="text-green-700">Dark green text</p>
<p class="text-gray-400">Muted gray text</p>
<span class="bg-yellow-200 px-1 rounded">Highlighted text</span>
<span class="text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-purple-600 font-bold text-3xl">
  Gradient Text ✨
</span>
```

---

## 4. Colors & Backgrounds <a name="colors"></a>

### Example 6 — Background Colors

```html
<div class="bg-blue-100 p-4">Light blue background</div>
<div class="bg-gray-800 text-white p-4">Dark background with white text</div>
<div class="bg-gradient-to-r from-cyan-400 to-blue-500 text-white p-4">
  Gradient background
</div>
```

**Color shades go from 50 (lightest) to 950 (darkest):**
`bg-red-50`, `bg-red-100`, `bg-red-200` ... `bg-red-900`

---

## 5. Spacing — Padding & Margin <a name="spacing"></a>

Tailwind uses a spacing scale: `1 = 4px`, `2 = 8px`, `4 = 16px`, `8 = 32px`, etc.

### Example 7 — Padding

```html
<div class="p-4">Padding on all sides (16px)</div>
<div class="px-6 py-3">Horizontal padding 24px, vertical 12px</div>
<div class="pt-8 pb-2">Top 32px, bottom 8px</div>
<div class="pl-4">Left padding only</div>
```

**Classes:** `p-*` (all), `px-*` (left+right), `py-*` (top+bottom), `pt-*`, `pr-*`, `pb-*`, `pl-*`

---

### Example 8 — Margin

```html
<div class="m-4">Margin on all sides</div>
<div class="mx-auto">Horizontally centered (auto margin)</div>
<div class="mt-8 mb-4">Top margin 32px, bottom 16px</div>
<div class="space-y-4">
  <!-- Children will have 16px vertical gap between them -->
  <p>First paragraph</p>
  <p>Second paragraph</p>
  <p>Third paragraph</p>
</div>
```

---

## 6. Flexbox <a name="flexbox"></a>

Flexbox is perfect for aligning items in a **single row or column**.

### Example 9 — Basic Flex Row

```html
<div class="flex gap-4">
  <div class="bg-blue-200 p-4">Item 1</div>
  <div class="bg-blue-300 p-4">Item 2</div>
  <div class="bg-blue-400 p-4">Item 3</div>
</div>
```

---

### Example 10 — Justify & Align

```html
<!-- Space items evenly -->
<div class="flex justify-between items-center h-16 bg-gray-100 px-4">
  <span>Logo</span>
  <span>Center</span>
  <span>Right</span>
</div>

<!-- Center everything -->
<div class="flex justify-center items-center h-32 bg-gray-200">
  <p>I am perfectly centered!</p>
</div>
```

**Justify (horizontal axis):** `justify-start`, `justify-center`, `justify-end`, `justify-between`, `justify-around`, `justify-evenly`

**Align (vertical axis):** `items-start`, `items-center`, `items-end`, `items-stretch`

---

### Example 11 — Flex Column

```html
<div class="flex flex-col gap-3">
  <button class="bg-blue-500 text-white p-2 rounded">Button A</button>
  <button class="bg-green-500 text-white p-2 rounded">Button B</button>
  <button class="bg-red-500 text-white p-2 rounded">Button C</button>
</div>
```

---

### Example 12 — Flex Wrap

```html
<div class="flex flex-wrap gap-3">
  <!-- Items wrap to the next line if they don't fit -->
  <div class="bg-purple-200 p-4 w-32">Box 1</div>
  <div class="bg-purple-300 p-4 w-32">Box 2</div>
  <div class="bg-purple-400 p-4 w-32">Box 3</div>
  <div class="bg-purple-500 p-4 w-32">Box 4</div>
  <div class="bg-purple-600 p-4 w-32">Box 5</div>
</div>
```

---

### Example 13 — Flex Grow / Shrink

```html
<div class="flex gap-2">
  <div class="bg-orange-200 p-4 flex-none w-24">Fixed width</div>
  <div class="bg-orange-300 p-4 flex-1">This takes all remaining space</div>
  <div class="bg-orange-400 p-4 flex-none w-24">Fixed width</div>
</div>
```

---

## 7. CSS Grid <a name="grid"></a>

Grid is ideal for **two-dimensional layouts** (rows AND columns).

### Example 14 — Basic Grid

```html
<div class="grid grid-cols-3 gap-4">
  <div class="bg-teal-100 p-4">Column 1</div>
  <div class="bg-teal-200 p-4">Column 2</div>
  <div class="bg-teal-300 p-4">Column 3</div>
  <div class="bg-teal-400 p-4">Column 4</div>
  <div class="bg-teal-500 p-4">Column 5</div>
  <div class="bg-teal-600 p-4">Column 6</div>
</div>
```

**Grid column classes:** `grid-cols-1`, `grid-cols-2`, `grid-cols-3`, `grid-cols-4`, `grid-cols-6`, `grid-cols-12`

---

### Example 15 — Spanning Columns

```html
<div class="grid grid-cols-4 gap-4">
  <div class="col-span-4 bg-pink-300 p-4">Full width (spans 4)</div>
  <div class="col-span-2 bg-pink-200 p-4">Half width (spans 2)</div>
  <div class="col-span-2 bg-pink-200 p-4">Half width (spans 2)</div>
  <div class="col-span-1 bg-pink-100 p-4">Quarter</div>
  <div class="col-span-3 bg-pink-100 p-4">Three-quarters</div>
</div>
```

---

### Example 16 — Responsive Grid

```html
<!-- 1 column on mobile, 2 on tablet, 4 on desktop -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
  <div class="bg-indigo-100 p-6 rounded-lg">Card 1</div>
  <div class="bg-indigo-200 p-6 rounded-lg">Card 2</div>
  <div class="bg-indigo-300 p-6 rounded-lg">Card 3</div>
  <div class="bg-indigo-400 p-6 rounded-lg">Card 4</div>
</div>
```

---

## 8. Responsive Design <a name="responsive"></a>

Tailwind uses **breakpoint prefixes** — a class without a prefix applies to all screens, and prefixed classes override it at larger sizes.

| Prefix | Min Width | Device |
|--------|-----------|--------|
| (none) | 0px | Mobile first |
| `sm:` | 640px | Large phones |
| `md:` | 768px | Tablets |
| `lg:` | 1024px | Laptops |
| `xl:` | 1280px | Desktops |
| `2xl:` | 1536px | Large screens |

### Example 17 — Responsive Text & Visibility

```html
<!-- Font size grows on larger screens -->
<h1 class="text-2xl md:text-4xl lg:text-6xl font-bold">
  Responsive Heading
</h1>

<!-- Hidden on mobile, visible on desktop -->
<p class="hidden lg:block">Only visible on laptops and above</p>

<!-- Visible on mobile, hidden on desktop -->
<p class="block lg:hidden">Only visible on mobile</p>
```

---

### Example 18 — Responsive Layout

```html
<!-- Stacks vertically on mobile, side by side on desktop -->
<div class="flex flex-col md:flex-row gap-6">
  <div class="md:w-1/3 bg-yellow-100 p-6 rounded-xl">Sidebar</div>
  <div class="md:w-2/3 bg-white p-6 rounded-xl shadow">Main Content</div>
</div>
```

---

## 9. DaisyUI — Introduction <a name="daisyui-intro"></a>

**DaisyUI** is a component library built on top of Tailwind CSS. It provides pre-styled, semantic class names like `btn`, `card`, `navbar`, etc., so you don't need to write dozens of utility classes yourself.

Without DaisyUI:
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Click Me
</button>
```

With DaisyUI:
```html
<button class="btn btn-primary">Click Me</button>
```

Both look the same! DaisyUI just wraps the complexity for you. You can still add Tailwind classes on top to customize further.

---

## 10. DaisyUI Components <a name="daisyui-components"></a>

---

### 🔘 Buttons

### Example 19 — Button Variants

```html
<button class="btn">Default</button>
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-accent">Accent</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-warning">Warning</button>
<button class="btn btn-error">Error</button>
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-link">Link style</button>
<button class="btn btn-outline btn-primary">Outlined</button>
```

---

### Example 20 — Button Sizes & States

```html
<button class="btn btn-xs">Extra Small</button>
<button class="btn btn-sm">Small</button>
<button class="btn btn-md">Medium (default)</button>
<button class="btn btn-lg">Large</button>

<button class="btn btn-primary loading">Loading...</button>
<button class="btn" disabled>Disabled</button>
<button class="btn btn-primary btn-wide">Wide Button</button>
<button class="btn btn-circle btn-outline">
  <svg .../>  <!-- icon -->
</button>
```

---

### 🏷️ Badges

### Example 21 — Badge Styles

```html
<span class="badge">Default</span>
<span class="badge badge-primary">Primary</span>
<span class="badge badge-secondary">Secondary</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
<span class="badge badge-error">Error</span>
<span class="badge badge-outline">Outline</span>
<span class="badge badge-ghost">Ghost</span>

<!-- Badge inside text -->
<p>New messages <span class="badge badge-primary badge-sm ml-1">5</span></p>
```

---

### ⚠️ Alerts

### Example 22 — Alert Types

```html
<div role="alert" class="alert">
  <span>This is a default info alert.</span>
</div>

<div role="alert" class="alert alert-info">
  <span>ℹ️ Did you know? Tailwind is awesome!</span>
</div>

<div role="alert" class="alert alert-success">
  <span>✅ Your file was uploaded successfully!</span>
</div>

<div role="alert" class="alert alert-warning">
  <span>⚠️ Your account is about to expire.</span>
</div>

<div role="alert" class="alert alert-error">
  <span>❌ Something went wrong. Please try again.</span>
</div>
```

---

### 🃏 Cards

### Example 23 — Basic Card

```html
<div class="card w-96 bg-base-100 shadow-xl">
  <figure>
    <img src="https://picsum.photos/400/200" alt="Card image" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>A short description about this card. Keep it concise and friendly.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Learn More</button>
    </div>
  </div>
</div>
```

---

### Example 24 — Card Variations

```html
<!-- Compact card -->
<div class="card card-compact bg-base-200 shadow w-64">
  <div class="card-body">
    <h2 class="card-title text-sm">Compact Card</h2>
    <p class="text-xs">Less padding, smaller text.</p>
    <div class="card-actions">
      <button class="btn btn-xs btn-accent">OK</button>
    </div>
  </div>
</div>

<!-- Side image card -->
<div class="card card-side bg-base-100 shadow-lg">
  <figure><img src="https://picsum.photos/100/100" alt="Side" /></figure>
  <div class="card-body">
    <h2 class="card-title">Side Image</h2>
    <p>Image appears on the left.</p>
  </div>
</div>

<!-- Card with badge -->
<div class="card bg-base-100 shadow w-64">
  <div class="card-body">
    <h2 class="card-title">
      Product Name
      <span class="badge badge-secondary">NEW</span>
    </h2>
    <p>Great product description here.</p>
  </div>
</div>
```

---

### 🧭 Navbar

### Example 25 — Full Navbar

```html
<div class="navbar bg-base-100 shadow-md">
  <!-- Left: Logo/Brand -->
  <div class="navbar-start">
    <a class="btn btn-ghost text-xl font-bold">MyBrand</a>
  </div>

  <!-- Center: Links (hidden on mobile) -->
  <div class="navbar-center hidden lg:flex">
    <ul class="menu menu-horizontal px-1 gap-1">
      <li><a>Home</a></li>
      <li><a>About</a></li>
      <li><a>Services</a></li>
      <li><a>Contact</a></li>
    </ul>
  </div>

  <!-- Right: CTA Button -->
  <div class="navbar-end">
    <a class="btn btn-primary">Get Started</a>
  </div>
</div>
```

---

### 🦸 Hero Section

### Example 26 — Hero

```html
<div class="hero min-h-screen bg-base-200">
  <div class="hero-content text-center">
    <div class="max-w-md">
      <h1 class="text-5xl font-bold">Hello there 👋</h1>
      <p class="py-6 text-lg text-gray-500">
        Build beautiful websites faster with Tailwind CSS and DaisyUI.
        No design experience needed.
      </p>
      <button class="btn btn-primary btn-lg">Get Started</button>
      <button class="btn btn-ghost btn-lg ml-2">Learn More</button>
    </div>
  </div>
</div>

<!-- Hero with image -->
<div class="hero min-h-96 bg-base-200">
  <div class="hero-content flex-col lg:flex-row-reverse gap-10">
    <img src="https://picsum.photos/400/300" class="rounded-lg shadow-2xl" />
    <div>
      <h1 class="text-4xl font-bold">Feature Spotlight</h1>
      <p class="py-4">This layout flips at large screen sizes.</p>
      <button class="btn btn-primary">Try It Free</button>
    </div>
  </div>
</div>
```

---

### 🦶 Footer

### Example 27 — Footer

```html
<footer class="footer p-10 bg-neutral text-neutral-content">
  <nav>
    <h6 class="footer-title">Services</h6>
    <a class="link link-hover">Branding</a>
    <a class="link link-hover">Design</a>
    <a class="link link-hover">Marketing</a>
  </nav>
  <nav>
    <h6 class="footer-title">Company</h6>
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
  </nav>
  <nav>
    <h6 class="footer-title">Legal</h6>
    <a class="link link-hover">Terms of use</a>
    <a class="link link-hover">Privacy policy</a>
  </nav>
</footer>

<!-- Footer bottom bar -->
<footer class="footer footer-center p-4 bg-base-300 text-base-content">
  <aside>
    <p>Copyright © 2024 — All rights reserved by MyBrand</p>
  </aside>
</footer>
```

---

### 💬 Modal

### Example 28 — Modal Dialog

```html
<!-- Trigger button -->
<button class="btn btn-primary" onclick="my_modal.showModal()">Open Modal</button>

<!-- The modal element -->
<dialog id="my_modal" class="modal">
  <div class="modal-box">
    <h3 class="font-bold text-lg">Hello! 👋</h3>
    <p class="py-4">This is a DaisyUI modal. Press ESC or click outside to close.</p>
    <div class="modal-action">
      <form method="dialog">
        <button class="btn">Got it!</button>
      </form>
    </div>
  </div>
  <!-- Click outside backdrop to close -->
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>
```

---

### 📂 Dropdown

### Example 29 — Dropdown Menu

```html
<div class="dropdown">
  <div tabindex="0" role="button" class="btn btn-primary m-1">
    Options ▼
  </div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-52 p-2 shadow">
    <li><a>Profile</a></li>
    <li><a>Settings</a></li>
    <li><hr /></li>
    <li><a class="text-error">Logout</a></li>
  </ul>
</div>

<!-- Dropdown aligned to end -->
<div class="dropdown dropdown-end">
  <div tabindex="0" role="button" class="btn">Right-aligned ▼</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box w-52 p-2 shadow">
    <li><a>Item A</a></li>
    <li><a>Item B</a></li>
  </ul>
</div>
```

---

### 📑 Tabs

### Example 30 — Tab Navigation

```html
<div role="tablist" class="tabs tabs-bordered">
  <a role="tab" class="tab tab-active">Home</a>
  <a role="tab" class="tab">About</a>
  <a role="tab" class="tab">Contact</a>
</div>

<!-- Boxed style -->
<div role="tablist" class="tabs tabs-boxed w-fit">
  <a role="tab" class="tab">Tab 1</a>
  <a role="tab" class="tab tab-active">Tab 2</a>
  <a role="tab" class="tab">Tab 3</a>
</div>

<!-- Lifted style -->
<div role="tablist" class="tabs tabs-lifted">
  <a role="tab" class="tab">Tab A</a>
  <a role="tab" class="tab tab-active">Tab B</a>
  <a role="tab" class="tab">Tab C</a>
</div>
```

---

### 🪗 Accordion / Collapse

### Example 31 — Accordion FAQ

```html
<div class="join join-vertical w-full max-w-2xl">

  <div class="collapse collapse-arrow join-item border border-base-300">
    <input type="radio" name="faq" checked />
    <div class="collapse-title text-lg font-medium">
      What is Tailwind CSS?
    </div>
    <div class="collapse-content">
      <p>Tailwind CSS is a utility-first CSS framework that lets you style elements directly in HTML using small, reusable classes.</p>
    </div>
  </div>

  <div class="collapse collapse-arrow join-item border border-base-300">
    <input type="radio" name="faq" />
    <div class="collapse-title text-lg font-medium">
      What is DaisyUI?
    </div>
    <div class="collapse-content">
      <p>DaisyUI is a component library for Tailwind CSS that provides styled components like buttons, cards, and navbars out of the box.</p>
    </div>
  </div>

  <div class="collapse collapse-arrow join-item border border-base-300">
    <input type="radio" name="faq" />
    <div class="collapse-title text-lg font-medium">
      Do I need to know CSS to use them?
    </div>
    <div class="collapse-content">
      <p>Basic CSS knowledge helps, but these tools are specifically designed to be beginner-friendly. You can build great sites with just HTML!</p>
    </div>
  </div>

</div>
```

---

### 👤 Avatar

### Example 32 — Avatar Styles

```html
<!-- Basic circle avatar -->
<div class="avatar">
  <div class="w-16 rounded-full">
    <img src="https://picsum.photos/64/64" alt="User avatar" />
  </div>
</div>

<!-- With online indicator -->
<div class="avatar online">
  <div class="w-12 rounded-full">
    <img src="https://picsum.photos/48/48" />
  </div>
</div>

<!-- Group of avatars -->
<div class="avatar-group -space-x-4">
  <div class="avatar"><div class="w-10 rounded-full"><img src="https://picsum.photos/40/40?1" /></div></div>
  <div class="avatar"><div class="w-10 rounded-full"><img src="https://picsum.photos/40/40?2" /></div></div>
  <div class="avatar"><div class="w-10 rounded-full"><img src="https://picsum.photos/40/40?3" /></div></div>
  <div class="avatar placeholder">
    <div class="bg-neutral text-neutral-content rounded-full w-10">
      <span>+9</span>
    </div>
  </div>
</div>

<!-- Placeholder (no image) -->
<div class="avatar placeholder">
  <div class="bg-primary text-primary-content rounded-full w-12">
    <span class="text-lg font-bold">AB</span>
  </div>
</div>
```

---

### 📊 Progress & Stats

### Example 33 — Progress Bars

```html
<progress class="progress w-full" value="40" max="100"></progress>
<progress class="progress progress-primary w-full" value="70" max="100"></progress>
<progress class="progress progress-success w-full" value="90" max="100"></progress>
<progress class="progress progress-warning w-full" value="55" max="100"></progress>
<progress class="progress progress-error w-full" value="20" max="100"></progress>

<!-- Indeterminate (animated loading) -->
<progress class="progress progress-info w-full"></progress>
```

---

### Example 34 — Stat Cards

```html
<div class="stats shadow">

  <div class="stat">
    <div class="stat-figure text-primary">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-8 h-8 stroke-current">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
      </svg>
    </div>
    <div class="stat-title">Total Users</div>
    <div class="stat-value text-primary">12,400</div>
    <div class="stat-desc">↑ 21% from last month</div>
  </div>

  <div class="stat">
    <div class="stat-title">Revenue</div>
    <div class="stat-value">$4,200</div>
    <div class="stat-desc">Jan 1 - Feb 1</div>
  </div>

  <div class="stat">
    <div class="stat-title">New Signups</div>
    <div class="stat-value text-success">300</div>
    <div class="stat-desc text-success">↑ 5.7%</div>
  </div>

</div>
```

---

### 📝 Forms & Inputs

### Example 35 — Form Elements

```html
<div class="flex flex-col gap-4 max-w-md">

  <!-- Text input -->
  <label class="form-control w-full">
    <div class="label">
      <span class="label-text">Your name</span>
    </div>
    <input type="text" placeholder="John Doe" class="input input-bordered w-full" />
  </label>

  <!-- Input with error state -->
  <label class="form-control w-full">
    <div class="label">
      <span class="label-text">Email</span>
    </div>
    <input type="email" placeholder="you@example.com" class="input input-error w-full" />
    <div class="label">
      <span class="label-text-alt text-error">Please enter a valid email.</span>
    </div>
  </label>

  <!-- Select dropdown -->
  <label class="form-control w-full">
    <div class="label">
      <span class="label-text">Pick a country</span>
    </div>
    <select class="select select-bordered">
      <option disabled selected>Select...</option>
      <option>Canada</option>
      <option>USA</option>
      <option>UK</option>
    </select>
  </label>

  <!-- Textarea -->
  <label class="form-control">
    <div class="label">
      <span class="label-text">Message</span>
    </div>
    <textarea class="textarea textarea-bordered h-24" placeholder="Write your message..."></textarea>
  </label>

  <!-- Checkbox -->
  <label class="label cursor-pointer gap-3 justify-start">
    <input type="checkbox" class="checkbox checkbox-primary" />
    <span class="label-text">I agree to the terms</span>
  </label>

  <!-- Toggle switch -->
  <label class="label cursor-pointer gap-3 justify-start">
    <span class="label-text">Notifications</span>
    <input type="checkbox" class="toggle toggle-success" checked />
  </label>

  <!-- Radio buttons -->
  <div class="flex gap-4">
    <label class="label cursor-pointer gap-2">
      <input type="radio" name="plan" class="radio radio-primary" checked />
      <span class="label-text">Free</span>
    </label>
    <label class="label cursor-pointer gap-2">
      <input type="radio" name="plan" class="radio radio-primary" />
      <span class="label-text">Pro</span>
    </label>
  </div>

  <!-- Range slider -->
  <label class="form-control">
    <div class="label">
      <span class="label-text">Volume</span>
    </div>
    <input type="range" min="0" max="100" value="60" class="range range-primary" />
  </label>

  <!-- Submit button -->
  <button class="btn btn-primary w-full">Submit</button>

</div>
```

---

### 📋 Tables

### Example 36 — Styled Table

```html
<div class="overflow-x-auto">
  <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>Name</th>
        <th>Role</th>
        <th>Status</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr class="hover">
        <th>1</th>
        <td>Alice Johnson</td>
        <td>Designer</td>
        <td><span class="badge badge-success">Active</span></td>
        <td><button class="btn btn-xs btn-ghost">Edit</button></td>
      </tr>
      <tr class="hover">
        <th>2</th>
        <td>Bob Smith</td>
        <td>Developer</td>
        <td><span class="badge badge-warning">Pending</span></td>
        <td><button class="btn btn-xs btn-ghost">Edit</button></td>
      </tr>
      <tr class="hover">
        <th>3</th>
        <td>Carol White</td>
        <td>Manager</td>
        <td><span class="badge badge-error">Inactive</span></td>
        <td><button class="btn btn-xs btn-ghost">Edit</button></td>
      </tr>
    </tbody>
  </table>
</div>
```

---

### 🔔 Toast Notifications

### Example 37 — Toast

```html
<!-- Toasts are positioned fixed on the screen -->
<div class="toast toast-top toast-end">
  <div class="alert alert-success">
    <span>✅ Message sent successfully!</span>
  </div>
</div>

<!-- Bottom left toast -->
<div class="toast toast-bottom toast-start">
  <div class="alert alert-error">
    <span>❌ Connection failed.</span>
  </div>
</div>

<!-- Stack multiple toasts -->
<div class="toast">
  <div class="alert alert-info"><span>New update available.</span></div>
  <div class="alert alert-success"><span>Settings saved!</span></div>
</div>
```

> 💡 **Tip:** Use JavaScript to dynamically add/remove toast elements for real interactivity.

---

## 11. Themes & Customization <a name="themes"></a>

### Example 38 — Built-in DaisyUI Themes

Set a theme on the `<html>` element:

```html
<html data-theme="cupcake">   <!-- pastel, cute theme -->
<html data-theme="dark">      <!-- dark mode -->
<html data-theme="cyberpunk"> <!-- neon yellow & black -->
<html data-theme="retro">     <!-- warm, vintage look -->
<html data-theme="forest">    <!-- dark green nature theme -->
<html data-theme="luxury">    <!-- gold on dark background -->
<html data-theme="corporate"> <!-- clean business blue -->
```

**All available themes:** `light`, `dark`, `cupcake`, `bumblebee`, `emerald`, `corporate`, `synthwave`, `retro`, `cyberpunk`, `valentine`, `halloween`, `garden`, `forest`, `aqua`, `lofi`, `pastel`, `fantasy`, `wireframe`, `black`, `luxury`, `dracula`, `cmyk`, `autumn`, `business`, `acid`, `lemonade`, `night`, `coffee`, `winter`

---

### Example 39 — Theme Switcher (JavaScript)

```html
<select id="theme-switcher" class="select select-bordered">
  <option value="light">Light</option>
  <option value="dark">Dark</option>
  <option value="cyberpunk">Cyberpunk</option>
  <option value="retro">Retro</option>
  <option value="forest">Forest</option>
</select>

<script>
  document.getElementById('theme-switcher').addEventListener('change', function() {
    document.documentElement.setAttribute('data-theme', this.value);
  });
</script>
```

---

### Example 40 — Semantic Color Classes

DaisyUI themes use semantic colors that automatically adapt to the theme:

```html
<!-- These colors change with the theme automatically -->
<div class="bg-primary text-primary-content p-4">Primary color</div>
<div class="bg-secondary text-secondary-content p-4">Secondary color</div>
<div class="bg-accent text-accent-content p-4">Accent color</div>
<div class="bg-neutral text-neutral-content p-4">Neutral</div>
<div class="bg-base-100 p-4">Base background</div>
<div class="bg-base-200 p-4">Slightly darker base</div>
<div class="bg-base-300 p-4">Even darker base</div>
```

> 🎨 Use these semantic colors instead of fixed colors like `bg-blue-500` whenever possible. Your site will automatically look great in any theme!

---

## 12. Full Page Example <a name="full-example"></a>

Here is a complete, responsive static webpage combining everything you've learned:

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>My DaisyUI Website</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.10.1/dist/full.min.css" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-base-100">

  <!-- ── NAVBAR ── -->
  <div class="navbar bg-base-100 shadow-sm sticky top-0 z-50">
    <div class="navbar-start">
      <a class="btn btn-ghost text-xl font-bold text-primary">🌼 Bloom</a>
    </div>
    <div class="navbar-center hidden md:flex">
      <ul class="menu menu-horizontal px-1 gap-1">
        <li><a href="#features">Features</a></li>
        <li><a href="#team">Team</a></li>
        <li><a href="#pricing">Pricing</a></li>
      </ul>
    </div>
    <div class="navbar-end">
      <a class="btn btn-primary btn-sm">Sign Up Free</a>
    </div>
  </div>

  <!-- ── HERO ── -->
  <div class="hero min-h-[80vh] bg-base-200">
    <div class="hero-content text-center max-w-2xl">
      <div>
        <span class="badge badge-primary mb-4">✨ Now in beta</span>
        <h1 class="text-5xl md:text-6xl font-black leading-tight">
          Build faster.<br/>Ship smarter.
        </h1>
        <p class="py-6 text-lg text-base-content/70 max-w-prose mx-auto">
          Bloom is a modern design toolkit that helps developers build
          beautiful products without the headaches. Get started in minutes.
        </p>
        <div class="flex gap-3 justify-center flex-wrap">
          <button class="btn btn-primary btn-lg">Get Started Free</button>
          <button class="btn btn-outline btn-lg">See Demo</button>
        </div>
        <div class="stats stats-horizontal shadow mt-10">
          <div class="stat"><div class="stat-value text-primary">10K+</div><div class="stat-desc">Users</div></div>
          <div class="stat"><div class="stat-value text-secondary">99%</div><div class="stat-desc">Uptime</div></div>
          <div class="stat"><div class="stat-value text-accent">4.9★</div><div class="stat-desc">Rating</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── FEATURES ── -->
  <section id="features" class="py-20 px-4 max-w-6xl mx-auto">
    <h2 class="text-4xl font-bold text-center mb-3">Why choose Bloom?</h2>
    <p class="text-center text-base-content/60 mb-12">Everything you need to build great products</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="card bg-base-100 shadow-md hover:shadow-xl transition-shadow">
        <div class="card-body items-center text-center">
          <div class="text-4xl mb-2">⚡</div>
          <h3 class="card-title">Lightning Fast</h3>
          <p class="text-base-content/70">Built for performance from day one. No bloat, no compromises.</p>
        </div>
      </div>
      <div class="card bg-primary text-primary-content shadow-md">
        <div class="card-body items-center text-center">
          <div class="text-4xl mb-2">🎨</div>
          <h3 class="card-title">Beautiful Themes</h3>
          <p class="opacity-80">30+ built-in themes that look great out of the box.</p>
        </div>
      </div>
      <div class="card bg-base-100 shadow-md hover:shadow-xl transition-shadow">
        <div class="card-body items-center text-center">
          <div class="text-4xl mb-2">📱</div>
          <h3 class="card-title">Fully Responsive</h3>
          <p class="text-base-content/70">Looks perfect on every screen, from mobile to widescreen.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── TEAM ── -->
  <section id="team" class="py-20 px-4 bg-base-200">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-4xl font-bold mb-12">Meet the Team</h2>
      <div class="flex flex-wrap justify-center gap-8">
        <div class="flex flex-col items-center gap-2">
          <div class="avatar"><div class="w-20 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
            <img src="https://picsum.photos/80/80?random=1" />
          </div></div>
          <p class="font-bold">Alice Chen</p>
          <span class="badge badge-outline">Founder</span>
        </div>
        <div class="flex flex-col items-center gap-2">
          <div class="avatar"><div class="w-20 rounded-full ring ring-secondary ring-offset-base-100 ring-offset-2">
            <img src="https://picsum.photos/80/80?random=2" />
          </div></div>
          <p class="font-bold">Mark Torres</p>
          <span class="badge badge-outline">Lead Dev</span>
        </div>
        <div class="flex flex-col items-center gap-2">
          <div class="avatar"><div class="w-20 rounded-full ring ring-accent ring-offset-base-100 ring-offset-2">
            <img src="https://picsum.photos/80/80?random=3" />
          </div></div>
          <p class="font-bold">Sara Kim</p>
          <span class="badge badge-outline">Designer</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ── FAQ ── -->
  <section class="py-20 px-4 max-w-2xl mx-auto">
    <h2 class="text-4xl font-bold text-center mb-10">FAQ</h2>
    <div class="join join-vertical w-full">
      <div class="collapse collapse-arrow join-item border border-base-300">
        <input type="radio" name="faq" checked />
        <div class="collapse-title font-semibold">Is Bloom free to use?</div>
        <div class="collapse-content text-base-content/70">
          <p>Yes! Bloom has a generous free tier. Paid plans are available for teams and advanced features.</p>
        </div>
      </div>
      <div class="collapse collapse-arrow join-item border border-base-300">
        <input type="radio" name="faq" />
        <div class="collapse-title font-semibold">Do I need coding experience?</div>
        <div class="collapse-content text-base-content/70">
          <p>Basic HTML knowledge is enough to get started. Our documentation covers everything step-by-step.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── FOOTER ── -->
  <footer class="footer footer-center p-6 bg-neutral text-neutral-content">
    <p class="font-bold text-lg">🌼 Bloom</p>
    <p class="text-sm opacity-60">Copyright © 2024 — Made with Tailwind CSS & DaisyUI</p>
  </footer>

</body>
</html>
```

---

## 🚀 Quick Reference Cheat Sheet

| What you want | Tailwind class(es) |
|---|---|
| Center horizontally | `mx-auto` |
| Center with flex | `flex justify-center items-center` |
| Full width | `w-full` |
| Full viewport height | `h-screen` |
| Rounded corners | `rounded`, `rounded-lg`, `rounded-full` |
| Drop shadow | `shadow`, `shadow-md`, `shadow-xl` |
| Hover effect | `hover:bg-blue-600`, `hover:scale-105` |
| Transition | `transition`, `transition-all duration-300` |
| Hidden on mobile | `hidden md:block` |
| 2-col on tablet+ | `grid grid-cols-1 md:grid-cols-2` |
| Limit text width | `max-w-prose` |
| Sticky header | `sticky top-0 z-50` |
| Overflow scroll | `overflow-x-auto` |

---

*Happy building! 🌼 For more details, visit [tailwindcss.com](https://tailwindcss.com) and [daisyui.com](https://daisyui.com)*
