# 🐙 Git Workflow — HTML String Manipulation Challenges

A complete guide to managing the 5 Python HTML string manipulation challenges using a professional Git workflow. You will create a GitHub repository, work in feature branches, document your results in a README with screenshots, save HTML outputs as local files, and merge your work through pull requests.

---

## 📋 Overview

Each of the 5 challenge files gets its own Git branch. Because these challenges produce **HTML string output**, each solution has two outputs to commit: a screenshot of the terminal showing the Python execution, and an `.html` file containing the printed HTML so it can be opened in a browser and visually verified.

The workflow for every challenge follows this cycle:

```
create branch → solve challenge → save HTML output → screenshot terminal → update README → push → pull request → merge
```

By the end, your `main` branch will contain all 5 solved challenges, 5 HTML output files, and a fully documented README.

---

## Phase 1 — Create the GitHub Repository

### Step 1 — Create an empty repo on GitHub

1. Log in to [github.com](https://github.com)
2. Click the **+** icon in the top-right corner and select **New repository**
3. Fill in the repository details:
   - **Repository name:** `python-html-string-challenges`
   - **Description:** `5 Python challenges to manipulate a multi-line HTML string using string methods and concatenation only`
   - **Visibility:** Public (or Private — your choice)
   - ⚠️ **Do NOT initialise with a README, .gitignore, or license** — leave all those boxes unchecked. The repo must be completely empty.
4. Click **Create repository**
5. Copy the HTTPS URL shown on the next screen — it will look like: `https://github.com/your-username/python-html-string-challenges.git`

---

## Phase 2 — Clone and Initialise Locally

### Step 2 — Clone the repository

Open your terminal, navigate to the folder where you want to work, and run:

```bash
git clone https://github.com/your-username/python-html-string-challenges.git
cd python-html-string-challenges
```

### Step 3 — Create the folder structure

Create the two folders that will hold screenshots and HTML outputs for all challenges:

```bash
mkdir screenshots
mkdir html_outputs
```

Git does not track empty folders. Add a `.gitkeep` placeholder file inside each one so they can be committed:

```bash
touch screenshots/.gitkeep html_outputs/.gitkeep
```

### Step 4 — Create the README on the `main` branch

Create a `README.md` file in the root of the project with the following initial content:

```markdown
# Python HTML String Manipulation Challenges

5 Python challenges to build and modify a minimal HTML page using string methods
and concatenation only. No parsers, no libraries — pure string primitives.

## Rules
- Only string methods (.replace, .find, .rfind, .split, .index, .count, etc.) are allowed
- String concatenation with + and += is allowed
- f-strings may be used to build values before insertion
- Converting the string to a list to index elements is NOT allowed
- No imports or external libraries of any kind

## Challenges

| # | Challenge | Branch | Status |
|---|-----------|--------|--------|
| 1 | Update Page Metadata | `challenge/01-metadata` | ⏳ Pending |
| 2 | Update Stylesheet and Script Sources | `challenge/02-assets` | ⏳ Pending |
| 3 | Inject Heading Tags | `challenge/03-headings` | ⏳ Pending |
| 4 | Add Paragraph and Image Tags | `challenge/04-content` | ⏳ Pending |
| 5 | Full Page Builder | `challenge/05-full-page` | ⏳ Pending |

## Outputs
```

### Step 5 — Commit and push the README and folders

```bash
git add README.md screenshots/.gitkeep html_outputs/.gitkeep
git commit -m "docs: initialise README and output folders"
git push origin main
```

Visit your GitHub repository in the browser and confirm the README is visible.

---

## Phase 3 — Challenge Workflow (repeat for each challenge)

The following steps are repeated **once per challenge file**. The full process is shown for Challenge 1 as a detailed example. Challenges 2–5 follow an identical pattern with their own specifics listed afterwards.

---

### 🔁 Challenge 1 — Update Page Metadata

#### Step 6 — Create and switch to a new branch

Always branch off from the latest `main`:

```bash
git checkout main
git pull origin main
git checkout -b challenge/01-metadata
```

#### Step 7 — Create the challenge file

Create `challenge_01_metadata.py` in the root of the repository and write your solution. Your script must:

- Declare the base HTML multi-line string exactly as specified in the challenge instructions
- Use `.replace()` to update the `lang` attribute and `<title>` tag using variables
- Print the final `html` string with `print(html)`

#### Step 8 — Save the HTML output to a file

Because the printed output is a valid HTML string, redirect it into the `html_outputs/` folder so it can be opened in a browser:

```bash
python challenge_01_metadata.py > html_outputs/challenge_01_output.html
```

Open `html_outputs/challenge_01_output.html` in your browser and verify it renders correctly. Check that:

- The browser tab title matches the value you assigned to `page_title`
- Right-clicking and selecting **View Page Source** shows the updated `lang` attribute and `<title>` tag

#### Step 9 — Take a screenshot of the terminal output

Run the script once more without redirecting, so the HTML output is visible in your terminal:

```bash
python challenge_01_metadata.py
```

Take a screenshot showing the printed HTML in the terminal. Make sure the `<html lang="...">` and `<title>...</title>` lines are clearly readable. Save the screenshot as `screenshots/challenge_01_terminal.png`.

#### Step 10 — Update the README

Open `README.md` and do two things:

**a)** Update the status for Challenge 1 in the table from `⏳ Pending` to `✅ Done`

**b)** Add an output section under `## Outputs`:

```markdown
### Challenge 1 — Update Page Metadata

**Concepts:** `.replace()`, f-strings, string concatenation

**Solution file:** `challenge_01_metadata.py`

**HTML output file:** `html_outputs/challenge_01_output.html`

**Terminal output:**

![Challenge 1 Terminal](screenshots/challenge_01_terminal.png)

**Browser preview:** Open `html_outputs/challenge_01_output.html` in a browser to verify
the updated `lang` attribute and `<title>` tag render correctly.
```

#### Step 11 — Stage, commit and push the branch

```bash
git add challenge_01_metadata.py \
        html_outputs/challenge_01_output.html \
        screenshots/challenge_01_terminal.png \
        README.md
git commit -m "feat: solve challenge 01 - update page metadata"
git push origin challenge/01-metadata
```

#### Step 12 — Create a Pull Request on GitHub

1. Go to your repository on GitHub — click the **Compare & pull request** button that appears after pushing
2. Fill in the pull request form:
   - **Title:** `Challenge 01 — Update Page Metadata`
   - **Description:** Describe the string methods used and what was changed in the HTML. Note that the HTML output file is included and can be opened in a browser to verify the result.
3. Confirm the base branch is `main` and the compare branch is `challenge/01-metadata`
4. Click **Create pull request**

#### Step 13 — Merge the Pull Request

1. Open the **Files changed** tab and confirm all four files are present: the `.py` solution, the `.html` output, the terminal screenshot, and the updated README
2. Click **Merge pull request** → **Confirm merge**
3. Click **Delete branch**

#### Step 14 — Pull the updated `main` locally

```bash
git checkout main
git pull origin main
```

---

### 🔁 Challenge 2 — Update Stylesheet and Script Sources

```bash
git checkout -b challenge/02-assets
```

- **File:** `challenge_02_stylesheets_and_scripts.py`
- **HTML output:** `html_outputs/challenge_02_output.html`
- **Screenshot:** `screenshots/challenge_02_terminal.png`
- **Commit message:** `feat: solve challenge 02 - update stylesheet and script sources`
- **PR title:** `Challenge 02 — Update Stylesheet and Script Sources`

**Verification note:** After opening the HTML file in a browser, use **View Page Source** to confirm the `href` and `src` values were updated correctly. Your terminal screenshot must show the printed `<link>` and `<script>` lines clearly enough to read the new filenames.

---

### 🔁 Challenge 3 — Inject Heading Tags

```bash
git checkout -b challenge/03-headings
```

- **File:** `challenge_03_headings.py`
- **HTML output:** `html_outputs/challenge_03_output.html`
- **Screenshot:** `screenshots/challenge_03_terminal.png`
- **Commit message:** `feat: solve challenge 03 - inject heading tags`
- **PR title:** `Challenge 03 — Inject Heading Tags`

**Verification note:** Open the HTML output in a browser — the `<h1>`, `<h2>`, and `<h3>` headings must be visible on the page with correct visual hierarchy. A blank page usually means the heading tags ended up outside `<body>` or contain a syntax error — check the source.

---

### 🔁 Challenge 4 — Add Paragraph and Image Tags

```bash
git checkout -b challenge/04-content
```

- **File:** `challenge_04_content.py`
- **HTML output:** `html_outputs/challenge_04_output.html`
- **Screenshot:** `screenshots/challenge_04_terminal.png`
- **Commit message:** `feat: solve challenge 04 - add paragraph and image tags`
- **PR title:** `Challenge 04 — Add Paragraph and Image Tags`

**Verification note:** This challenge builds on Challenge 3's output. In the browser, all headings and the paragraph should be visible. The `<img>` tag will show a broken image icon since `hero.jpg` does not exist locally — that is expected. Use **View Page Source** to confirm the tag order matches the expected output in the challenge instructions: headings first, then `<p>`, then `<img>`, all inside `<body>`.

---

### 🔁 Challenge 5 — Full Page Builder

```bash
git checkout -b challenge/05-full-page
```

- **File:** `challenge_05_full_page.py`
- **HTML output:** `html_outputs/challenge_05_output.html`
- **Screenshot:** `screenshots/challenge_05_terminal.png`
- **Commit message:** `feat: solve challenge 05 - full page builder`
- **PR title:** `Challenge 05 — Full Page Builder`

**Verification note:** Challenge 5 prints a validation report before the final HTML. Your terminal screenshot must capture **both** the validation report and the opening lines of the HTML. If your terminal window is too short to show everything at once, scroll up after running and take two screenshots — save them as `challenge_05_terminal_validation.png` and `challenge_05_terminal_html.png` and reference both in the README output section.

When redirecting to the HTML file, be aware that the validation report will also be written into it, which will appear as text at the top of the page in the browser. To save a clean HTML file, you have two options: temporarily comment out the `print()` calls for the validation report before redirecting, or add a second `print()` to a separate script that only prints the final `html` variable. Either approach is valid — add a comment in your code explaining which you chose.

---

## Phase 4 — Final State

### Expected repository structure after all 5 challenges

```
python-html-string-challenges/
├── README.md
├── challenge_01_metadata.py
├── challenge_02_stylesheets_and_scripts.py
├── challenge_03_headings.py
├── challenge_04_content.py
├── challenge_05_full_page.py
├── html_outputs/
│   ├── challenge_01_output.html
│   ├── challenge_02_output.html
│   ├── challenge_03_output.html
│   ├── challenge_04_output.html
│   └── challenge_05_output.html
└── screenshots/
    ├── challenge_01_terminal.png
    ├── challenge_02_terminal.png
    ├── challenge_03_terminal.png
    ├── challenge_04_terminal.png
    └── challenge_05_terminal.png
```

### Expected final README table

```
| # | Challenge | Branch | Status |
|---|-----------|--------|--------|
| 1 | Update Page Metadata              | `challenge/01-metadata`  | ✅ Done |
| 2 | Update Stylesheet and Script Sources | `challenge/02-assets` | ✅ Done |
| 3 | Inject Heading Tags               | `challenge/03-headings`  | ✅ Done |
| 4 | Add Paragraph and Image Tags      | `challenge/04-content`   | ✅ Done |
| 5 | Full Page Builder                 | `challenge/05-full-page` | ✅ Done |
```

---

## 💻 Redirecting Python Output to an HTML File

The `>` operator in your terminal redirects `print()` output to a file instead of displaying it on screen:

```bash
python challenge_01_metadata.py > html_outputs/challenge_01_output.html
```

The file will contain exactly what `print(html)` would have shown in the terminal. Open it in any browser to see the rendered page. If your script also prints debug messages or a validation report, those lines will appear in the file too — make sure only the final `print(html)` call is active when generating the clean output file.

---

## 📎 Git Command Reference

| Command | Purpose |
|---|---|
| `git clone <url>` | Download the remote repo locally |
| `git checkout main` | Switch to the main branch |
| `git pull origin main` | Fetch and merge latest changes from remote main |
| `git checkout -b <branch>` | Create and switch to a new branch |
| `git add <file>` | Stage a specific file |
| `git add .` | Stage all changed files in the current directory |
| `git commit -m "message"` | Commit staged files with a message |
| `git push origin <branch>` | Push a branch to GitHub |
| `git status` | Show staged, unstaged, and untracked files |
| `git log --oneline` | View compact commit history |
| `git branch -d <branch>` | Delete a local branch after merging |

---

## ✍️ Commit Message Convention

| Prefix | Use for |
|---|---|
| `feat:` | Adding a new challenge solution |
| `docs:` | Updating the README or adding screenshots |
| `fix:` | Correcting a bug in a challenge file |
| `chore:` | Folder creation, cleanup, or housekeeping |

---

*Every HTML file you commit is a living artefact — open it in a browser at any point to see exactly what your string manipulation produced. This makes the `html_outputs/` folder genuinely useful as a project record, not just a dumping ground for files. 🚀*
