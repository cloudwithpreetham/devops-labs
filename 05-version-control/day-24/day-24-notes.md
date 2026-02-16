# Day 24 – Advanced Git: Merge, Rebase, Stash & Cherry Pick

## Overview

Today I practiced advanced Git workflows used in real DevOps and software engineering teams. The main focus was understanding how branches are combined, how to temporarily save unfinished work, and how to selectively apply commits from one branch to another.

Topics covered:

- Git merge
- Fast-forward merge
- Merge commits
- Merge conflicts
- Git rebase
- Squash merge
- Git stash
- Git cherry-pick
- Visualizing Git history

---

## Task 1: Git Merge – Hands-On

### Commands Practiced

```bash
git checkout main
git pull origin main

git checkout -b feature-login
```

Created changes on `feature-login`:

```bash
echo "Login feature started" > login.txt
git add login.txt
git commit -m "feat: add login feature placeholder"

echo "Add login validation notes" >> login.txt
git add login.txt
git commit -m "docs: add login validation notes"
```

Switched back to `main` and merged:

```bash
git checkout main
git merge feature-login
```

Checked history:

```bash
git log --oneline --graph --all
```

### Observation: Fast-Forward Merge

Git performed a fast-forward merge because `main` had not changed after creating the `feature-login` branch.

In this case, Git simply moved the `main` pointer forward to the latest commit on `feature-login`.

### What is a Fast-Forward Merge?

A fast-forward merge happens when the target branch has no new commits after the feature branch was created.

Example:

```text
Before merge:

main:          A---B
                   \
feature-login:     C---D

After merge:

main:          A---B---C---D
```

No extra merge commit is created.

---

### Merge Commit Practice

Created another branch:

```bash
git checkout -b feature-signup
```

Added commits on `feature-signup`:

```bash
echo "Signup feature started" > signup.txt
git add signup.txt
git commit -m "feat: add signup feature placeholder"

echo "Signup validation added" >> signup.txt
git add signup.txt
git commit -m "feat: add signup validation notes"
```

Moved `main` ahead separately:

```bash
git checkout main
echo "Main branch update" > main-update.txt
git add main-update.txt
git commit -m "docs: add main branch update note"
```

Merged `feature-signup` into `main`:

```bash
git merge feature-signup
```

### Observation: Merge Commit

This time Git created a merge commit because both branches had moved forward independently.

Example:

```text
Before merge:

main:            A---B---E
                      \
feature-signup:        C---D

After merge:

main:            A---B---E---M
                      \   /
feature-signup:        C---D
```

`M` is the merge commit.

### When Does Git Create a Merge Commit?

Git creates a merge commit when both branches have new commits and Git needs to preserve the history of how the branches came together.

This is useful when we want to clearly show that a feature branch was merged into the main branch.

---

## Merge Conflict Practice

### How I Created a Conflict

Created a file on `main`:

```bash
git checkout main
echo "Application version: main" > app.txt
git add app.txt
git commit -m "docs: add app version note"
```

Created a new branch:

```bash
git checkout -b conflict-demo
```

Changed the same line:

```bash
echo "Application version: conflict branch" > app.txt
git add app.txt
git commit -m "docs: update app version from conflict branch"
```

Changed the same line on `main`:

```bash
git checkout main
echo "Application version: main branch updated" > app.txt
git add app.txt
git commit -m "docs: update app version from main branch"
```

Merged the branch:

```bash
git merge conflict-demo
```

### What is a Merge Conflict?

A merge conflict happens when Git cannot automatically decide which change to keep.

This usually happens when the same line of the same file is changed differently in two branches.

Git marks the conflict like this:

```text
<<<<<<< HEAD
Application version: main branch updated
=======
Application version: conflict branch
>>>>>>> conflict-demo
```

### How I Resolved the Conflict

I manually edited the file and kept the correct final version:

```text
Application version: main branch updated with conflict branch changes
```

Then I completed the merge:

```bash
git add app.txt
git commit -m "fix: resolve merge conflict in app version note"
```

---

## Task 2: Git Rebase – Hands-On

### Commands Practiced

Created a new branch:

```bash
git checkout main
git checkout -b feature-dashboard
```

Added commits:

```bash
echo "Dashboard page started" > dashboard.txt
git add dashboard.txt
git commit -m "feat: add dashboard page placeholder"

echo "Add dashboard metrics section" >> dashboard.txt
git add dashboard.txt
git commit -m "feat: add dashboard metrics section"

echo "Add dashboard notes" >> dashboard.txt
git add dashboard.txt
git commit -m "docs: add dashboard notes"
```

Moved `main` ahead:

```bash
git checkout main
echo "Main branch release note" > release.txt
git add release.txt
git commit -m "docs: add release note on main"
```

Rebased feature branch onto latest `main`:

```bash
git checkout feature-dashboard
git rebase main
```

Checked history:

```bash
git log --oneline --graph --all
```

### What Does Rebase Do?

Rebase moves the feature branch commits and replays them on top of another branch.

In this task, Git took the commits from `feature-dashboard` and replayed them on top of the latest `main` commit.

### History Before Rebase

```text
main:               A---B---E
                         \
feature-dashboard:        C---D---F
```

### History After Rebase

```text
main:               A---B---E
                             \
feature-dashboard:            C'---D'---F'
```

The commits look like they were created after the latest `main` commit.

### How is Rebase Different from Merge?

Merge keeps the branch history and may create a merge commit.

Rebase creates a cleaner, linear history by replaying commits on top of another branch.

### Why Should We Not Rebase Shared Commits?

Rebase rewrites commit history by creating new commit hashes.

If those commits were already pushed and other team members are using them, rebasing can create confusion, duplicate commits, or conflicts for the team.

Best practice:

- Rebase local/private branches before pushing
- Avoid rebasing public/shared branches

### When to Use Rebase vs Merge

Use rebase when:

- Working on a private local feature branch
- You want a clean linear history
- You want to update your branch with latest `main` before opening a pull request

Use merge when:

- Combining shared branches
- You want to preserve full branch history
- Working in a team where history should not be rewritten

---

## Task 3: Squash Commit vs Merge Commit

## Squash Merge Practice

Created a branch:

```bash
git checkout main
git checkout -b feature-profile
```

Added small commits:

```bash
echo "Profile page" > profile.txt
git add profile.txt
git commit -m "feat: add profile page placeholder"

echo "Fix profile typo" >> profile.txt
git add profile.txt
git commit -m "fix: correct profile typo"

echo "Format profile content" >> profile.txt
git add profile.txt
git commit -m "style: format profile content"

echo "Add profile notes" >> profile.txt
git add profile.txt
git commit -m "docs: add profile notes"
```

Merged with squash:

```bash
git checkout main
git merge --squash feature-profile
git commit -m "feat: add profile feature"
```

### Observation

Even though `feature-profile` had multiple commits, only one commit was added to `main`.

### What Does Squash Merge Do?

Squash merge combines all commits from a feature branch into one single commit before adding it to the target branch.

This keeps the main branch history clean.

### Regular Merge Practice

Created another branch:

```bash
git checkout -b feature-settings
```

Added commits:

```bash
echo "Settings page" > settings.txt
git add settings.txt
git commit -m "feat: add settings page placeholder"

echo "Add settings options" >> settings.txt
git add settings.txt
git commit -m "feat: add settings options"

echo "Add settings notes" >> settings.txt
git add settings.txt
git commit -m "docs: add settings notes"
```

Merged normally:

```bash
git checkout main
git merge feature-settings
```

### Squash Merge vs Regular Merge

Squash merge:

- Adds one clean commit to `main`
- Hides small intermediate commits
- Good for cleaning up messy feature branch history

Regular merge:

- Keeps all individual commits
- Preserves complete development history
- Useful when each commit has meaningful value

### Trade-Off of Squashing

The benefit of squash merge is a clean history.

The trade-off is that detailed commit history from the feature branch is lost on `main`.

In real projects, squash merge is useful when a branch has many small commits like:

- typo fixes
- formatting changes
- debugging commits
- temporary work-in-progress commits

---

## Task 4: Git Stash – Hands-On

### Commands Practiced

Started work without committing:

```bash
echo "Temporary dashboard update" >> dashboard.txt
```

Checked status:

```bash
git status
```

Tried switching branch:

```bash
git checkout main
```

Depending on the file changes, Git may block the switch if the changes would be overwritten.

### Saved Work Using Stash

```bash
git stash push -m "wip: temporary dashboard update"
```

Checked stash list:

```bash
git stash list
```

Switched branch safely:

```bash
git checkout main
```

Returned and restored stash:

```bash
git checkout feature-dashboard
git stash pop
```

### Stashing Multiple Times

```bash
echo "First temporary change" >> notes.txt
git stash push -m "wip: first temporary change"

echo "Second temporary change" >> notes.txt
git stash push -m "wip: second temporary change"

git stash list
```

Applied a specific stash:

```bash
git stash apply stash@{1}
```

Dropped a stash if no longer needed:

```bash
git stash drop stash@{1}
```

### Difference Between `git stash pop` and `git stash apply`

`git stash pop`:

- Applies the stash
- Removes it from the stash list
- Useful when you no longer need the saved stash after applying it

`git stash apply`:

- Applies the stash
- Keeps it in the stash list
- Useful when you want to reuse the same stash or apply it carefully

### When Would I Use Stash in Real Workflow?

I would use stash when:

- I am working on a feature and suddenly need to switch to another branch
- I need to pull latest changes but my working directory is dirty
- I want to temporarily save experimental changes
- I am not ready to commit yet but need a clean working tree

Example real-world case:

A production bug comes in while I am working on a new feature. I can stash my current work, switch to a hotfix branch, fix the issue, and later come back to my original work.

---

## Task 5: Cherry Picking

### Commands Practiced

Created a hotfix branch:

```bash
git checkout main
git checkout -b feature-hotfix
```

Added three commits:

```bash
echo "Hotfix change one" > hotfix-one.txt
git add hotfix-one.txt
git commit -m "fix: add first hotfix change"

echo "Hotfix change two" > hotfix-two.txt
git add hotfix-two.txt
git commit -m "fix: add second hotfix change"

echo "Hotfix change three" > hotfix-three.txt
git add hotfix-three.txt
git commit -m "fix: add third hotfix change"
```

Found commit hashes:

```bash
git log --oneline
```

Switched to `main`:

```bash
git checkout main
```

Cherry-picked only the second commit:

```bash
git cherry-pick <second-commit-hash>
```

Verified history:

```bash
git log --oneline --graph --all
```

### What Does Cherry-Pick Do?

Cherry-pick copies a specific commit from one branch and applies it onto the current branch.

It does not merge the full branch.

Only the selected commit is applied.

### When Would I Use Cherry-Pick in a Real Project?

Cherry-pick is useful when:

- A bug fix exists on another branch and is needed urgently on `main`
- Only one specific commit from a feature branch is required
- A release branch needs a selected fix without merging unfinished work
- A hotfix needs to be applied to multiple branches

Example:

A developer fixes a security issue on a feature branch, but the full feature is not ready. The team can cherry-pick only the security fix into `main` or a release branch.

### What Can Go Wrong With Cherry-Picking?

Cherry-picking can cause problems when:

- The selected commit depends on earlier commits that were not cherry-picked
- The same change is applied multiple times
- Merge conflicts occur
- History becomes harder to understand if overused

Best practice:

Use cherry-pick carefully and only when there is a clear reason to apply one specific commit.

---

## Merge vs Rebase Comparison

| Topic         | Merge                            | Rebase                                 |
| ------------- | -------------------------------- | -------------------------------------- |
| History style | Preserves branch history         | Creates linear history                 |
| Commit hashes | Existing commits stay the same   | Rewrites commits with new hashes       |
| Merge commit  | May create a merge commit        | Does not create merge commit           |
| Best for      | Shared branches and team history | Local/private branch cleanup           |
| Risk          | Safer for shared work            | Risky if used on pushed/shared commits |

---

## Squash Merge vs Regular Merge Comparison

| Topic                   | Squash Merge                  | Regular Merge                    |
| ----------------------- | ----------------------------- | -------------------------------- |
| Main branch history     | Clean and compact             | Detailed                         |
| Number of commits added | One commit                    | Multiple commits or merge commit |
| Best for                | Messy feature branches        | Meaningful commit history        |
| Trade-off               | Loses detailed commit history | History can become noisy         |

---

## Important Learnings

- Merge combines branches while preserving history.
- Fast-forward merge happens when the target branch has not moved ahead.
- Merge commits are created when both branches have separate commits.
- Rebase rewrites commits and creates a cleaner linear history.
- Rebase should not be used on shared commits.
- Squash merge is useful for keeping `main` clean.
- Stash helps save unfinished work temporarily.
- Cherry-pick applies only selected commits from another branch.
- `git log --oneline --graph --all` is very useful for understanding branch history.

---

## Real-World DevOps Notes

In DevOps projects, Git workflows matter because infrastructure code, CI/CD pipeline files, Kubernetes manifests, and automation scripts are usually managed through Git.

Good Git practices help teams:

- Avoid breaking the main branch
- Review changes safely through pull requests
- Keep deployment history clean
- Roll back changes more easily
- Work on hotfixes without disturbing feature work

For production repositories, it is better to:

- Keep `main` stable
- Use feature branches
- Pull latest changes before starting work
- Prefer pull requests for review
- Avoid force-pushing shared branches
- Write clear commit messages
- Use stash only for temporary work, not long-term storage

---

## Final Summary

Day 24 helped me understand how professional Git workflows are managed in real projects.

I learned that merge, rebase, squash, stash, and cherry-pick solve different problems:

- Merge is used to combine branches safely.
- Rebase is used to clean up local branch history.
- Squash is used to combine multiple small commits into one clean commit.
- Stash is used to temporarily save unfinished work.
- Cherry-pick is used to apply one specific commit from another branch.

These commands are important for working confidently in DevOps teams where Git is used to manage application code, infrastructure code, CI/CD pipelines, and production hotfixes.
