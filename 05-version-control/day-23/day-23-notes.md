# Day 23 – Git Branching & Working with GitHub

This document contains two ready-to-use files for Day 23:

1. `day-23-notes.md`
2. Updated section for `git-commands.md`

---

# File 1: day-23-notes.md

````md
# Day 23 – Git Branching & Working with GitHub

## Objective

The goal of Day 23 is to understand Git branching, work with multiple branches locally, push branches to GitHub, pull remote changes, and understand the difference between clone and fork.

---

## Task 1: Understanding Branches

### 1. What is a branch in Git?

A branch in Git is a separate line of development.

It allows developers to work on a new feature, bug fix, or experiment without directly changing the main branch.

Example:

```bash
git branch feature-1
```
````

This creates a new branch called `feature-1`.

---

### 2. Why do we use branches instead of committing everything to main?

We use branches to keep the `main` branch stable and clean.

Branches help us:

- Work on new features safely
- Test changes before merging them into `main`
- Avoid breaking production-ready code
- Collaborate with other developers
- Review changes before they become part of the main project

In real DevOps and software teams, developers usually create separate branches for features, fixes, experiments, and releases.

---

### 3. What is HEAD in Git?

`HEAD` is a pointer that shows the current branch or commit we are working on.

Usually, `HEAD` points to the latest commit of the current branch.

Example:

```bash
git status
```

If we are on the `main` branch, `HEAD` points to the latest commit on `main`.

---

### 4. What happens to your files when you switch branches?

When we switch branches, Git updates the working directory to match the files and commits of the selected branch.

This means:

- Files may appear if they exist in the new branch
- Files may disappear if they do not exist in the new branch
- File content may change based on the selected branch

Before switching branches, it is best practice to commit or stash your current changes.

---

## Task 2: Branching Commands – Hands-On

### 1. List all branches

```bash
git branch
```

This command lists all local branches.

---

### 2. Create a new branch called feature-1

```bash
git branch feature-1
```

This creates a new branch named `feature-1`.

---

### 3. Switch to feature-1

```bash
git switch feature-1
```

Alternative command:

```bash
git checkout feature-1
```

---

### 4. Create and switch to feature-2 in one command

Using modern Git command:

```bash
git switch -c feature-2
```

Using older command:

```bash
git checkout -b feature-2
```

---

### 5. Difference between git switch and git checkout

`git switch` is used mainly for switching branches.

`git checkout` is an older command that can do multiple things, such as switching branches and restoring files.

`git switch` is easier and safer for beginners because its purpose is clear.

Example:

```bash
git switch main
```

This switches to the `main` branch.

---

### 6. Make a commit on feature-1 that does not exist on main

Switch to `feature-1`:

```bash
git switch feature-1
```

Create a new file:

```bash
echo "This file was created on feature-1 branch." > feature-1-work.md
```

Stage the file:

```bash
git add feature-1-work.md
```

Commit the file:

```bash
git commit -m "feat(git): add feature branch practice notes"
```

---

### 7. Switch back to main and verify feature-1 commit is not there

```bash
git switch main
```

Check files:

```bash
ls
```

The `feature-1-work.md` file should not appear on `main` because it was committed only on the `feature-1` branch.

Check commit history:

```bash
git log --oneline
```

The commit from `feature-1` should not be visible in the `main` branch history.

---

### 8. Delete a branch no longer needed

Delete a local branch safely:

```bash
git branch -d feature-2
```

Force delete a branch:

```bash
git branch -D feature-2
```

Use `-d` when the branch is already merged.
Use `-D` only when you are sure you want to delete it forcefully.

---

## Task 3: Push to GitHub

### 1. Create a new repository on GitHub

A new empty GitHub repository was created without initializing it with a README file.

---

### 2. Connect local repository to GitHub remote

```bash
git remote add origin https://github.com/<your-username>/devops-git-practice.git
```

Verify remote:

```bash
git remote -v
```

---

### 3. Push main branch to GitHub

```bash
git push -u origin main
```

The `-u` option sets the upstream tracking branch.

---

### 4. Push feature-1 branch to GitHub

```bash
git push -u origin feature-1
```

---

### 5. Verify both branches on GitHub

Both `main` and `feature-1` branches were verified on GitHub under the branch dropdown.

---

### 6. Difference between origin and upstream

`origin` usually refers to your own remote repository on GitHub.

`upstream` usually refers to the original repository from which your fork was created.

Example:

```bash
git remote -v
```

Common setup after forking:

```bash
origin    https://github.com/your-username/project.git
upstream  https://github.com/original-owner/project.git
```

In simple words:

- `origin` = your GitHub repo
- `upstream` = original source repo

---

## Task 4: Pull from GitHub

### 1. Make a change directly on GitHub

A file was edited directly using the GitHub web editor.

---

### 2. Pull that change locally

```bash
git pull origin main
```

This downloads and merges the latest changes from the GitHub `main` branch into the local `main` branch.

---

### 3. Difference between git fetch and git pull

`git fetch` downloads changes from the remote repository but does not merge them into the current branch.

```bash
git fetch origin
```

`git pull` downloads changes and automatically merges them into the current branch.

```bash
git pull origin main
```

In simple words:

- `git fetch` = download only
- `git pull` = download + merge

Best practice:

Use `git fetch` first when you want to inspect remote changes before merging.

---

## Task 5: Clone vs Fork

### 1. What is clone?

Clone means copying a remote Git repository to your local machine.

Example:

```bash
git clone https://github.com/original-owner/project.git
```

This creates a local copy of the repository.

---

### 2. What is fork?

Fork means creating your own copy of someone else's GitHub repository under your GitHub account.

Forking is a GitHub feature, not a direct Git command.

After forking, you can clone your fork:

```bash
git clone https://github.com/your-username/project.git
```

---

### 3. Difference between clone and fork

| Clone                                                | Fork                                         |
| ---------------------------------------------------- | -------------------------------------------- |
| Git concept                                          | GitHub concept                               |
| Copies repository to local machine                   | Copies repository to your GitHub account     |
| Used to work locally                                 | Used to contribute to someone else's project |
| Does not create a new GitHub repo under your account | Creates a new GitHub repo under your account |

---

### 4. When would you clone vs fork?

Use `clone` when:

- You want a local copy of your own repository
- You have direct access to contribute to the repository
- You want to run or study a project locally

Use `fork` when:

- You want to contribute to someone else's repository
- You do not have direct write access
- You want to experiment without affecting the original project

---

### 5. After forking, how do you keep your fork in sync with the original repo?

First, add the original repository as `upstream`:

```bash
git remote add upstream https://github.com/original-owner/project.git
```

Fetch changes from upstream:

```bash
git fetch upstream
```

Switch to main:

```bash
git switch main
```

Merge upstream changes:

```bash
git merge upstream/main
```

Push updated changes to your fork:

```bash
git push origin main
```

---

## Summary

In this task, I learned:

- What Git branches are
- Why branches are important in real projects
- How to create, switch, and delete branches
- Difference between `git switch` and `git checkout`
- How to push local branches to GitHub
- Difference between `origin` and `upstream`
- Difference between `git fetch` and `git pull`
- Difference between clone and fork
- How to keep a fork synced with the original repository

---

## Real-World DevOps Note

In real DevOps teams, branching is used for feature development, bug fixes, release management, CI/CD pipelines, and collaboration.

A clean branching workflow helps teams avoid breaking production code and makes code review easier.
