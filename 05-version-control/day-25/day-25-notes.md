# Day 25 – Git Reset vs Revert & Branching Strategies

## Objective

Today I learned how to undo mistakes safely in Git using `git reset` and `git revert`.

I also learned about real-world branching strategies used by engineering teams:

- GitFlow
- GitHub Flow
- Trunk-Based Development

---

## Task 1: Git Reset – Hands-On

### Practice Setup

I created three test commits in my practice repository.

```bash
echo "Commit A change" > reset-demo.txt
git add reset-demo.txt
git commit -m "test: add commit A for reset practice"

echo "Commit B change" >> reset-demo.txt
git add reset-demo.txt
git commit -m "test: add commit B for reset practice"

echo "Commit C change" >> reset-demo.txt
git add reset-demo.txt
git commit -m "test: add commit C for reset practice"
```

Checked the commit history:

```bash
git log --oneline
```

---

## 1. `git reset --soft`

Command used:

```bash
git reset --soft HEAD~1
```

### Observation

`git reset --soft` moved `HEAD` back by one commit.

The last commit was removed from the current branch history, but the changes stayed staged.

Checked status:

```bash
git status
```

### Result

- The last commit was removed from the current branch history
- The file changes were still available
- The changes were still staged
- I could recommit them immediately

### When to use `--soft`

Use `git reset --soft` when:

- I committed too early
- I want to change the last commit message
- I want to combine commits
- I want to recommit the same changes without restaging

Example:

```bash
git reset --soft HEAD~1
git commit -m "fix: improve reset demo commit"
```

---

## 2. `git reset --mixed`

After recommitting, I tested mixed reset.

Command used:

```bash
git reset --mixed HEAD~1
```

### Observation

`git reset --mixed` moved `HEAD` back by one commit.

The last commit was removed from the current branch history, and the changes were moved back to the working directory as unstaged changes.

Checked status:

```bash
git status
```

### Result

- The last commit was removed from the current branch history
- The file changes were still available
- The changes were not staged
- I had to run `git add` again before committing

### When to use `--mixed`

Use `git reset --mixed` when:

- I want to undo a commit but keep the file changes
- I want to review changes again before staging
- I want to split one commit into multiple smaller commits

Example:

```bash
git reset --mixed HEAD~1

git add file1.md
git commit -m "docs: update file one"

git add file2.md
git commit -m "docs: update file two"
```

---

## 3. `git reset --hard`

After recommitting again, I tested hard reset.

Command used:

```bash
git reset --hard HEAD~1
```

### Observation

`git reset --hard` moved `HEAD` back by one commit.

The last commit was removed from the current branch history, and the changes were deleted from the working directory.

Checked status:

```bash
git status
```

### Result

- The last commit was removed from the current branch history
- The file changes were not staged
- The file changes were not available in the working directory
- Local changes were discarded

### When to use `--hard`

Use `git reset --hard` only when:

- I am sure I do not need the changes
- I want to completely discard local work
- I am cleaning up local experimental commits

Example:

```bash
git reset --hard HEAD~1
```

---

## Difference Between `--soft`, `--mixed`, and `--hard`

| Reset Type          | Commit History    | Staging Area          | Working Directory | Risk Level   |
| ------------------- | ----------------- | --------------------- | ----------------- | ------------ |
| `git reset --soft`  | Moves `HEAD` back | Keeps changes staged  | Keeps changes     | Safer        |
| `git reset --mixed` | Moves `HEAD` back | Unstages changes      | Keeps changes     | Usually safe |
| `git reset --hard`  | Moves `HEAD` back | Clears staged changes | Deletes changes   | Dangerous    |

---

## Which reset is destructive and why?

`git reset --hard` is destructive.

It is destructive because it:

- Removes the commit from the current branch history
- Clears staged changes
- Discards working directory changes
- Can delete local work permanently if I do not recover it with `git reflog`

---

## Should I use `git reset` on pushed commits?

Usually, no.

I should avoid using `git reset` on commits that are already pushed to a shared branch.

Reason:

- It rewrites commit history
- Other developers may already have pulled those commits
- It can create conflicts and confusion for the team

For pushed or shared commits, I should use:

```bash
git revert <commit-hash>
```

---

# Task 2: Git Revert – Hands-On

## Practice Setup

I created three test commits.

```bash
echo "Commit X change" > revert-demo.txt
git add revert-demo.txt
git commit -m "test: add commit X for revert practice"

echo "Commit Y change" >> revert-demo.txt
git add revert-demo.txt
git commit -m "test: add commit Y for revert practice"

echo "Commit Z change" >> revert-demo.txt
git add revert-demo.txt
git commit -m "test: add commit Z for revert practice"
```

Checked history:

```bash
git log --oneline
```

Example history:

```bash
abc1234 test: add commit Z for revert practice
def5678 test: add commit Y for revert practice
ghi9012 test: add commit X for revert practice
```

---

## Reverting the Middle Commit

Command used:

```bash
git revert <commit-Y-hash>
```

Example:

```bash
git revert def5678
```

### Observation

Git created a new commit that reversed the changes introduced by commit Y.

Commit Y was still visible in the Git history.

Checked log:

```bash
git log --oneline
```

### Result

- Commit X still existed
- Commit Y still existed
- Commit Z still existed
- A new revert commit was added
- The history was not rewritten

---

## How is `git revert` different from `git reset`?

`git reset` moves the branch pointer backward and can remove commits from the visible branch history.

`git revert` does not remove old commits. Instead, it creates a new commit that reverses the changes from a selected commit.

---

## Why is revert safer than reset for shared branches?

`git revert` is safer because it does not rewrite history.

It keeps the commit history clear and allows other team members to pull the new revert commit normally.

This is why `git revert` is preferred for:

- Shared branches
- Remote branches
- Production branches
- Team repositories

---

## When would I use revert vs reset?

### Use `git reset` when:

- The commit is local
- The commit has not been pushed
- I want to clean up my local history
- I want to edit, combine, or split commits

### Use `git revert` when:

- The commit is already pushed
- Other people may have pulled the branch
- I want a safe undo operation
- I am working on `main`, `develop`, or another shared branch

---

# Task 3: Reset vs Revert Summary

|                                  | `git reset`                                              | `git revert`                                                  |
| -------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------- |
| What it does                     | Moves `HEAD` or branch pointer back to a previous commit | Creates a new commit that reverses changes from an old commit |
| Removes commit from history?     | Yes, from visible branch history                         | No                                                            |
| Safe for shared/pushed branches? | No, because it rewrites history                          | Yes, because it preserves history                             |
| When to use                      | Local cleanup before pushing                             | Undoing pushed or shared commits safely                       |

---

# Task 4: Branching Strategies

## 1. GitFlow

### How it works

GitFlow is a branching strategy that uses multiple long-lived and short-lived branches.

Common branches:

- `main` – production-ready code
- `develop` – integration branch for upcoming work
- `feature/*` – new features
- `release/*` – release preparation
- `hotfix/*` – urgent production fixes

### Text Diagram

```text
main        ----o-------------------o----------------
               \                   /
hotfix          \----hotfix--------/

develop     ------o------o------o------o-------------
                  \      \      \
feature/login      \------o------/
feature/signup             \-----o-----/

release/v1.0                       \----o----/
```

### When/where it is used

GitFlow is useful for:

- Large teams
- Scheduled releases
- Products with multiple versions
- Enterprise projects
- Teams that need release stabilization

### Pros

- Clear structure
- Good for planned releases
- Separates development from production
- Supports hotfixes cleanly
- Useful for large teams

### Cons

- More complex
- Many branches to manage
- Slower for fast-moving teams
- Can create conflicts due to long-lived branches

---

## 2. GitHub Flow

### How it works

GitHub Flow is a simple branching strategy based on one stable `main` branch and short-lived feature branches.

Basic flow:

1. Keep `main` always deployable
2. Create a feature branch from `main`
3. Commit changes
4. Open a pull request
5. Review and test
6. Merge into `main`
7. Deploy

### Text Diagram

```text
main        ----o-----------o-----------o--------
               \           /
feature/login   \----o----o
```

### When/where it is used

GitHub Flow is useful for:

- Startups
- Small teams
- Web applications
- Continuous deployment
- Projects that ship frequently

### Pros

- Simple and beginner-friendly
- Easy to understand
- Works well with pull requests
- Good for fast delivery
- Encourages short-lived branches

### Cons

- Less suitable for complex release cycles
- Requires strong testing before merge
- `main` must stay stable
- Not ideal when maintaining multiple release versions

---

## 3. Trunk-Based Development

### How it works

In Trunk-Based Development, developers work from the main branch, also called the trunk.

Developers either:

- Commit directly to `main`, or
- Use very short-lived branches and merge quickly

Feature flags are often used to hide incomplete work until it is ready.

### Text Diagram

```text
main/trunk  ----o----o----o----o----o----o----
                  \       /
short-feature      o-----o
```

### When/where it is used

Trunk-Based Development is useful for:

- High-performing engineering teams
- Continuous integration
- Continuous delivery
- Teams with strong automated testing
- Fast release environments

### Pros

- Very fast integration
- Reduces long-running branch conflicts
- Supports CI/CD well
- Keeps code close to production
- Encourages small commits

### Cons

- Requires strong test automation
- Requires team discipline
- Incomplete features need feature flags
- Risky for beginners without proper CI checks

---

## Strategy Selection

### Which strategy would I use for a startup shipping fast?

I would use GitHub Flow.

Reason:

- Simple workflow
- Fast pull request cycle
- Easy to understand
- Good for frequent deployments
- Less branch management overhead

---

### Which strategy would I use for a large team with scheduled releases?

I would use GitFlow.

Reason:

- Better release control
- Separate `develop`, `release`, and `hotfix` branches
- Good for planned releases
- Helps manage multiple teams working together

---

### Which strategy does my favorite open-source project use?

Example project: React

React development happens openly on GitHub using pull requests.

This looks similar to GitHub Flow because contributors submit changes through branches and pull requests instead of using a heavy GitFlow structure.

---

# Task 5: Git Commands Reference Update

The `git-commands.md` file should be updated with commands from Day 22 to Day 25, including:

- Setup and config
- Basic workflow
- Branching
- Remote commands
- Merge and rebase
- Stash
- Cherry-pick
- Reset and revert

---

# Key Takeaways

- `git reset` is useful for local cleanup.
- `git reset --soft` keeps changes staged.
- `git reset --mixed` keeps changes but unstages them.
- `git reset --hard` deletes local changes and should be used carefully.
- `git revert` is safer for pushed or shared commits.
- GitFlow is best for structured releases.
- GitHub Flow is best for fast-moving teams.
- Trunk-Based Development is best for teams with strong CI/CD discipline.
- `git reflog` can help recover from many Git mistakes.

---

# Useful Commands Practiced

```bash
git log --oneline
git status
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git revert <commit-hash>
git reflog
```

---

# Submission Checklist

- [x] Created `day-25-notes.md`
- [x] Practiced `git reset --soft`
- [x] Practiced `git reset --mixed`
- [x] Practiced `git reset --hard`
- [x] Practiced `git revert`
- [x] Compared reset and revert
- [x] Documented GitFlow
- [x] Documented GitHub Flow
- [x] Documented Trunk-Based Development
- [x] Updated `git-commands.md`
- [x] Committed and pushed changes
