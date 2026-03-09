---
marp: true
theme: default
paginate: true
backgroundColor: #0d1117
color: #e6edf3
style: |
  section {
    font-family: 'Segoe UI', system-ui, sans-serif;
    padding: 40px 60px;
  }
  h1 {
    color: #f78166;
    border-bottom: 2px solid #30363d;
    padding-bottom: 12px;
  }
  h2 {
    color: #79c0ff;
  }
  h3 {
    color: #56d364;
  }
  code {
    background: #161b22;
    color: #79c0ff;
    border-radius: 4px;
    padding: 2px 6px;
    font-size: 0.9em;
  }
  pre {
    background: #161b22 !important;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 20px;
  }
  pre code {
    color: #e6edf3;
    background: transparent;
    padding: 0;
    font-size: 0.85em;
  }
  .highlight { color: #f78166; font-weight: bold; }
  .tip {
    background: #0f2a1a;
    border-left: 4px solid #56d364;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    margin-top: 16px;
  }
  .warning {
    background: #2d1a00;
    border-left: 4px solid #d29922;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    margin-top: 16px;
  }
  .danger {
    background: #2d0a0a;
    border-left: 4px solid #f78166;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    margin-top: 16px;
  }
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.title h1 {
    font-size: 2.4em;
    border: none;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.85em;
  }
  th {
    background: #161b22;
    color: #79c0ff;
    padding: 8px 12px;
    border: 1px solid #30363d;
  }
  td {
    padding: 8px 12px;
    border: 1px solid #30363d;
  }
  tr:nth-child(even) { background: #161b22; }
---

<!-- _class: title -->

# 🌿 Git & GitHub CLI Workflow
## From Zero to Pull Request

**Tools:** `git` · `gh` · your terminal

Y44k0V

---

# 📋 What We'll Cover

1. **Setup** — Configure git & gh
2. **Core Workflow** — Clone, branch, commit, push, PR
3. **Branching Strategies** — Feature, Gitflow, trunk-based
4. **Collaboration** — Multiple PRs, reviews, merging
5. **Recovering from Mistakes** — Before & after committing
6. **Real-World Scenarios** — Putting it all together

---

# 🔧 One-Time Setup

## Configure Git Identity

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"   # VS Code as default editor
git config --global init.defaultBranch main
```

## Authenticate with GitHub CLI

```bash
gh auth login
# Follow prompts: GitHub.com → HTTPS → Login with browser
```

## Verify Everything Works

```bash
git --version   # git version 2.x.x
gh auth status  # ✓ Logged in to github.com as <username>
```

---

# 🏗️ Starting a Project

## Option A — Clone an existing repo

```bash
gh repo clone owner/repo-name
cd repo-name
```

## Option B — Create a brand new repo

```bash
mkdir my-project && cd my-project
git init
gh repo create my-project --public --source=. --push
```

## Option C — Fork someone else's repo

```bash
gh repo fork owner/repo-name --clone
cd repo-name
```

<div class="tip">💡 <code>gh repo clone</code> automatically sets up the remote for you — no manual <code>git remote add origin</code> needed.</div>

---

# 🌿 The Core Feature Branch Workflow

```
main ──────────────────────────────────────────► (production)
          │                         ▲
          └── feature/login ────────┘
                  commit  commit  PR merge
```

## Every change follows this loop:

```bash
git checkout main && git pull          # 1. Start fresh from main
git checkout -b feature/my-feature    # 2. Create a new branch
# ... make your changes ...
git add .                              # 3. Stage changes
git commit -m "feat: add my feature"  # 4. Commit with a clear message
git push -u origin feature/my-feature # 5. Push branch to GitHub
gh pr create --fill                   # 6. Open a Pull Request
```

---

# 🌳 Branching Strategies

## Strategy 1 — GitHub Flow (Simple & Popular)

```
main ← always deployable
  └── feature/X   ← branch off main, PR back to main
  └── fix/Y        ← same for bug fixes
  └── docs/Z       ← same for docs
```

**Best for:** web apps, SaaS, continuous deployment

## Strategy 2 — Gitflow (Structured Releases)

```
main        ← production releases only
develop     ← integration branch
  └── feature/X  → merges into develop
  └── release/1.0 → merges into main + develop
  └── hotfix/X   → merges into main + develop
```

**Best for:** versioned software, mobile apps, libraries

---

# 🌳 Branching Strategies (continued)

## Strategy 3 — Trunk-Based Development

```
main ← everyone commits here (or very short-lived branches < 1 day)
  └── feature/X  (lives for hours, not days)
```

**Uses feature flags** to hide incomplete work in production

**Best for:** experienced teams, CI/CD pipelines, microservices

## Naming Conventions

| Prefix | Example | Purpose |
|--------|---------|---------|
| `feature/` | `feature/user-auth` | New functionality |
| `fix/` or `bugfix/` | `fix/login-crash` | Bug fixes |
| `hotfix/` | `hotfix/security-patch` | Urgent production fix |
| `chore/` | `chore/update-deps` | Maintenance |
| `docs/` | `docs/api-guide` | Documentation |

---

# 📦 Committing Like a Pro

## Staging — Choose What to Include

```bash
git add file.txt           # Stage a specific file
git add src/               # Stage an entire folder
git add -p                 # Interactively stage chunks (hunks)
git status                 # See what's staged / unstaged
git diff --staged          # Review staged changes before committing
```

## Writing Good Commit Messages

```bash
# ✅ Good — imperative mood, explains WHY
git commit -m "feat: add OAuth login via GitHub"
git commit -m "fix: prevent crash when cart is empty"
git commit -m "refactor: extract payment logic to service class"

# ❌ Bad — vague, past tense, no context
git commit -m "fixed stuff"
git commit -m "WIP"
git commit -m "asdfasdf"
```

<div class="tip">💡 Use <strong>Conventional Commits</strong> format: <code>type(scope): description</code> — enables auto changelogs!</div>

---

# 🔀 Working with Multiple Pull Requests

## Scenario: Two features in parallel

```bash
# Feature 1 — already in progress on feature/payments
git checkout main && git pull
git checkout -b feature/notifications   # Start feature 2 from main

# Work on feature/notifications...
git add . && git commit -m "feat: add email notifications"
git push -u origin feature/notifications
gh pr create --title "Add email notifications" --body "Closes #42"
```

## Keep branches up to date with main

```bash
git checkout feature/payments
git fetch origin
git rebase origin/main          # Replay your commits on top of latest main
# OR
git merge origin/main           # Merge latest main into your branch
```

<div class="warning">⚠️ <strong>Prefer rebase</strong> to keep a clean linear history. Use merge if the branch is shared with others.</div>

---

# 🔍 Pull Requests with `gh`

## Create a PR

```bash
gh pr create                              # Interactive prompts
gh pr create --fill                       # Use branch name + last commit
gh pr create --title "My PR" \
             --body "## What changed\n- Added X\n- Fixed Y" \
             --reviewer teammate1,teammate2 \
             --label "enhancement"
```

## Manage Existing PRs

```bash
gh pr list                                # See all open PRs
gh pr view 42                             # View PR #42 in terminal
gh pr view 42 --web                       # Open PR in browser
gh pr review 42 --approve                 # Approve a PR
gh pr review 42 --request-changes \
    --body "Please add tests"             # Request changes
gh pr merge 42 --squash                   # Merge (squash commits)
gh pr merge 42 --rebase                   # Merge (rebase)
```

---

# 💥 Recovering from Mistakes — BEFORE Committing

## Undo changes to a file (not yet staged)

```bash
git restore file.txt              # Discard working directory changes
git restore .                     # Discard ALL unstaged changes ⚠️
```

## Unstage a file (staged but not committed)

```bash
git restore --staged file.txt     # Remove from staging area, keep changes
git restore --staged .            # Unstage everything
```

## Completely start over (nuclear option)

```bash
git stash                         # Save work temporarily
git stash pop                     # Bring it back later
git stash drop                    # Throw it away permanently
```

<div class="tip">💡 <code>git stash</code> is your emergency "hide this mess" button. Great before switching branches mid-work.</div>

---

# 💥 Recovering from Mistakes — AFTER Committing

## Fix the last commit (message or forgot a file)

```bash
git add forgotten-file.txt
git commit --amend --no-edit              # Add file to last commit
git commit --amend -m "corrected message" # Fix the message
```

## Undo the last commit (keep changes)

```bash
git reset --soft HEAD~1    # Undo commit, changes stay STAGED
git reset --mixed HEAD~1   # Undo commit, changes go back to UNSTAGED
```

## Undo the last commit (discard changes completely)

```bash
git reset --hard HEAD~1    # ⚠️ Permanently deletes the commit AND changes
```

<div class="danger">🚨 Never use <code>--hard</code> or <code>--amend</code> on commits already pushed to a shared branch. It rewrites history and breaks teammates' repos.</div>

---

# 💥 Recovering — After Pushing to GitHub

## The safe way: `git revert`

```bash
git revert HEAD              # Creates a NEW commit that undoes last commit
git revert abc1234           # Revert a specific commit by hash
git push                     # Safe to push — history is preserved ✅
```

## When you must rewrite history (your own branch only)

```bash
git reset --hard origin/main~1
git push --force-with-lease   # Safer than --force, checks for upstream changes
```

## Find a lost commit with reflog

```bash
git reflog                    # Shows EVERYTHING git has done (your safety net)
# Find the commit hash you want to recover
git checkout abc1234          # Inspect it
git checkout -b recovery/oops # Save it as a new branch
```

<div class="tip">💡 <code>git reflog</code> keeps 90 days of history. You can almost always recover "deleted" work.</div>

---

# 🔍 Investigating History

## Browse commits and blame

```bash
git log --oneline --graph --all    # Visual branch history
git log --oneline -10              # Last 10 commits
git show abc1234                   # Show a specific commit's diff
git blame file.txt                 # Who changed each line?
git diff main..feature/X           # Diff between two branches
```

## Find when a bug was introduced

```bash
git bisect start
git bisect bad                     # Current commit is broken
git bisect good v1.0               # This tag/commit was working
# Git checks out commits; you test and mark good/bad
git bisect good                    # or: git bisect bad
# Git finds the culprit automatically!
git bisect reset                   # Exit bisect mode
```

---

# 🚀 Complete Real-World Scenario

## "Fix a bug while a feature is in progress"

```bash
# You're mid-feature, bug report comes in!
git stash                              # Save WIP
git checkout main && git pull

git checkout -b hotfix/null-pointer    # Fix on a new branch
# ... make the fix ...
git add . && git commit -m "fix: prevent null pointer in checkout"
git push -u origin hotfix/null-pointer
gh pr create --title "Hotfix: null pointer in checkout" \
             --label "bug,priority:high"

# Back to your feature
git checkout feature/my-feature
git stash pop                          # Restore WIP
```

---

# 🚀 Complete Real-World Scenario (continued)

## "Your PR has merge conflicts"

```bash
gh pr view 55                          # Check conflict status
git checkout feature/my-feature
git fetch origin
git rebase origin/main                 # Replay your commits on main

# If conflicts appear:
# Edit the conflicted files (look for <<<<<<< markers)
git add resolved-file.txt
git rebase --continue                  # Move to next commit

# If things go badly wrong during rebase:
# Abort Rebase Operation
Cancels an in-progress rebase and returns the repository to its state before the rebase started. Use this when conflicts become too complex or you change your mind about rebasing.
git rebase --abort                     # Return to pre-rebase state

git push --force-with-lease            # Update PR branch
```

<div class="tip">💡 VS Code has an excellent merge conflict UI — open the file and click "Accept Current/Incoming/Both".</div>

---

# 📊 Quick Reference Card

| Situation | Command |
|-----------|---------|
| Discard unstaged file | `git restore file.txt` |
| Unstage a file | `git restore --staged file.txt` |
| Fix last commit | `git commit --amend` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Undo last commit (discard) | `git reset --hard HEAD~1` ⚠️ |
| Undo a pushed commit safely | `git revert HEAD` |
| Stash work in progress | `git stash` / `git stash pop` |
| Recover "deleted" commits | `git reflog` |
| Force push safely | `git push --force-with-lease` |
| Create a PR | `gh pr create --fill` |
| Merge a PR | `gh pr merge --squash` |
| Rebase on main | `git rebase origin/main` |

---

# ✅ Best Practices Summary

### Branching
- Branch off `main` for every change, no matter how small
- Use descriptive branch names: `feature/user-auth`, not `fix2`
- Delete branches after merging: `gh pr merge --delete-branch`

### Committing
- Commit early, commit often — small focused commits
- Write messages for your future self (and teammates)
- Never commit secrets, credentials, or `.env` files

### Pull Requests
- Keep PRs small and focused — easier to review
- Link to issues: `Closes #42` in the PR body
- Always review your own PR before requesting reviews

### Safety
- `git reflog` is your safety net — almost nothing is truly lost
- Never force push to `main` or shared branches
- Use `--force-with-lease` instead of `--force`

---

<!-- _class: title -->

# 🎓 Practice Exercises

1. **Fork** this repo and clone it locally with `gh repo fork`
2. Create a `feature/your-name` branch and add your name to `CONTRIBUTORS.md`
3. Open a PR with `gh pr create` — give it a good title and description
4. **Intentionally break something**, commit it, then use `git revert` to fix it
5. Create two branches simultaneously and practice resolving a merge conflict
6. Use `git bisect` to find a "bug" commit in the practice repo

---

<!-- _class: title -->

# 🌿 That's a Wrap!

## Key Takeaways

**Branch → Commit → Push → PR → Merge**

`git reflog` can recover almost anything

Never rewrite shared history

Small PRs = faster reviews = happier teams

---

*Happy committing! 🚀*

