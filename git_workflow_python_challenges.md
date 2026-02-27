# 🐙 Git Workflow — Python Beginner Challenges

A complete guide to managing the 5 Python beginner challenges using a professional Git workflow. You will create a GitHub repository, work in feature branches, document your results in a README, and merge your work through pull requests.

---

## 📋 Overview

Each of the 5 challenge files gets its own Git branch. The workflow for every challenge follows the same cycle:

```
create branch → solve challenge → screenshot output → update README → push → pull request → merge
```

By the end, your `main` branch will contain all 5 solved challenges with a fully documented README.

---

## Phase 1 — Create the GitHub Repository

### Step 1 — Create an empty repo on GitHub

1. Log in to [github.com](https://github.com)
2. Click the **+** icon in the top-right corner and select **New repository**
3. Fill in the repository details:
   - **Repository name:** `python-beginner-challenges`
   - **Description:** `5 Python beginner challenges covering input, string formatting, data types and casting`
   - **Visibility:** Public (or Private — your choice)
   - ⚠️ **Do NOT initialise with a README, .gitignore, or license** — leave all those boxes unchecked. The repo must be completely empty.
4. Click **Create repository**
5. Copy the HTTPS URL shown on the next screen — it will look like: `https://github.com/your-username/python-beginner-challenges.git`

---

## Phase 2 — Clone and Initialise Locally

### Step 2 — Clone the repository

Open your terminal, navigate to the folder where you want to work, and run:

```bash
git clone https://github.com/your-username/python-beginner-challenges.git
cd python-beginner-challenges
```

### Step 3 — Create the README on the `main` branch

Create a `README.md` file in the root of the project with the following initial content:

```markdown
# Python Beginner Challenges

5 beginner-friendly Python challenges covering user input, string formatting, data types and data casting.

## Challenges

| # | Challenge | Branch | Status |
|---|-----------|--------|--------|
| 1 | Personalised Greeting | `challenge/01-greeting` | ⏳ Pending |
| 2 | Age Calculator | `challenge/02-age-calculator` | ⏳ Pending |
| 3 | Temperature Converter | `challenge/03-temperature-converter` | ⏳ Pending |
| 4 | Shopping Receipt | `challenge/04-shopping-receipt` | ⏳ Pending |
| 5 | Profile Card | `challenge/05-profile-card` | ⏳ Pending |

## Outputs
```

### Step 4 — Commit and push the README

```bash
git add README.md
git commit -m "docs: initialise README with challenge tracker"
git push origin main
```

Visit your GitHub repository in the browser and confirm the README is visible.

---

## Phase 3 — Challenge Workflow (repeat for each challenge)

The following steps are repeated **once per challenge file**, changing only the branch name, filename, and content. The full process is shown for Challenge 1 as a detailed example, followed by the quick reference for challenges 2–5.

---

### 🔁 Challenge 1 — Personalised Greeting

#### Step 5 — Create and switch to a new branch

Always branch off from the latest `main`:

```bash
git checkout main
git pull origin main
git checkout -b challenge/01-greeting
```

#### Step 6 — Create the challenge file

Create `challenge_01_greeting.py` in the root of the repository and write your solution using `input()` and f-strings to collect the user's first and last name and print a greeting.

#### Step 7 — Run the challenge and take a screenshot

Run your solution in the terminal:

```bash
python challenge_01_greeting.py
```

Take a screenshot of the terminal showing both your input and the printed output. Save the screenshot inside a `screenshots/` folder:

```
screenshots/challenge_01_output.png
```

Create the folder if it does not exist yet:

```bash
mkdir screenshots
```

#### Step 8 — Update the README

Open `README.md` and do two things:

**a)** Update the status for Challenge 1 in the table from `⏳ Pending` to `✅ Done`

**b)** Add a new output section under `## Outputs`:

```markdown
### Challenge 1 — Personalised Greeting

**Concepts:** `input()`, f-strings, string concatenation

**Solution file:** `challenge_01_greeting.py`

**Output:**

![Challenge 1 Output](screenshots/challenge_01_output.png)
```

#### Step 9 — Stage, commit and push the branch

```bash
git add challenge_01_greeting.py screenshots/challenge_01_output.png README.md
git commit -m "feat: solve challenge 01 - personalised greeting"
git push origin challenge/01-greeting
```

#### Step 10 — Create a Pull Request on GitHub

1. Go to your repository on GitHub — you will see a banner saying your branch was recently pushed with a **Compare & pull request** button. Click it.
2. Fill in the pull request form:
   - **Title:** `Challenge 01 — Personalised Greeting`
   - **Description:** Briefly describe what the challenge does and which Python concepts it covers
3. Confirm the base branch is `main` and the compare branch is `challenge/01-greeting`
4. Click **Create pull request**

#### Step 11 — Merge the Pull Request

1. Review the file changes in the **Files changed** tab
2. If everything looks correct, click **Merge pull request**
3. Click **Confirm merge**
4. Click **Delete branch** to keep the repository clean

#### Step 12 — Pull the updated `main` locally

```bash
git checkout main
git pull origin main
```

Your local `main` branch now contains the solved challenge. You are ready to start the next one.

---

### 🔁 Challenge 2 — Age Calculator

```bash
git checkout -b challenge/02-age-calculator
```

- **File:** `challenge_02_age_calculator.py`
- **Screenshot:** `screenshots/challenge_02_output.png`
- **Commit message:** `feat: solve challenge 02 - age calculator`
- **PR title:** `Challenge 02 — Age Calculator`

---

### 🔁 Challenge 3 — Temperature Converter

```bash
git checkout -b challenge/03-temperature-converter
```

- **File:** `challenge_03_temperature_converter.py`
- **Screenshot:** `screenshots/challenge_03_output.png`
- **Commit message:** `feat: solve challenge 03 - temperature converter`
- **PR title:** `Challenge 03 — Temperature Converter`

---

### 🔁 Challenge 4 — Shopping Receipt

```bash
git checkout -b challenge/04-shopping-receipt
```

- **File:** `challenge_04_shopping_receipt.py`
- **Screenshot:** `screenshots/challenge_04_output.png`
- **Commit message:** `feat: solve challenge 04 - shopping receipt`
- **PR title:** `Challenge 04 — Shopping Receipt`

---

### 🔁 Challenge 5 — Profile Card

```bash
git checkout -b challenge/05-profile-card
```

- **File:** `challenge_05_profile_card.py`
- **Screenshot:** `screenshots/challenge_05_output.png`
- **Commit message:** `feat: solve challenge 05 - profile card`
- **PR title:** `Challenge 05 — Profile Card`

---

## Phase 4 — Final State

### Expected repository structure after all 5 challenges

```
python-beginner-challenges/
├── README.md
├── challenge_01_greeting.py
├── challenge_02_age_calculator.py
├── challenge_03_temperature_converter.py
├── challenge_04_shopping_receipt.py
├── challenge_05_profile_card.py
└── screenshots/
    ├── challenge_01_output.png
    ├── challenge_02_output.png
    ├── challenge_03_output.png
    ├── challenge_04_output.png
    └── challenge_05_output.png
```

### Expected final README table

```
| # | Challenge | Branch | Status |
|---|-----------|--------|--------|
| 1 | Personalised Greeting     | `challenge/01-greeting`              | ✅ Done |
| 2 | Age Calculator            | `challenge/02-age-calculator`        | ✅ Done |
| 3 | Temperature Converter     | `challenge/03-temperature-converter` | ✅ Done |
| 4 | Shopping Receipt          | `challenge/04-shopping-receipt`      | ✅ Done |
| 5 | Profile Card              | `challenge/05-profile-card`          | ✅ Done |
```

---

## 📎 Git Command Reference

| Command | Purpose |
|---|---|
| `git clone <url>` | Download the remote repo locally |
| `git checkout main` | Switch to the main branch |
| `git pull origin main` | Fetch and merge latest changes from remote main |
| `git checkout -b <branch>` | Create and switch to a new branch |
| `git add <file>` | Stage a file for commit |
| `git commit -m "message"` | Commit staged files with a message |
| `git push origin <branch>` | Push a branch to GitHub |
| `git branch` | List all local branches |
| `git status` | Show staged, unstaged, and untracked files |
| `git log --oneline` | View compact commit history |

---

## ✍️ Commit Message Convention

| Prefix | Use for |
|---|---|
| `feat:` | Adding a new challenge solution |
| `docs:` | Updating the README or adding screenshots |
| `fix:` | Correcting a bug in a challenge file |
| `chore:` | Folder creation, cleanup, or config changes |

---

*Following this workflow for every challenge builds the same habits used in real development teams — branch per feature, document as you go, review before merging. 🚀*
