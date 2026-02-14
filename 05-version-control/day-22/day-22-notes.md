# Day 22 – Introduction to Git: Your First Repository

## Overview

Today I started learning Git, which is one of the most important tools in DevOps.

Git is used to track file changes, maintain project history, collaborate with teams, and manage code safely.
In DevOps, Git is commonly used with GitHub, GitLab, Jenkins, Docker, Kubernetes, Terraform, and CI/CD pipelines.

---

## Tasks Completed

- Verified Git installation
- Configured Git username and email
- Created a new folder called `devops-git-practice`
- Initialized a Git repository using `git init`
- Checked repository status using `git status`
- Explored the hidden `.git/` directory
- Created a Git commands reference file
- Staged and committed changes
- Viewed commit history using `git log`
- Practiced making multiple commits

---

## Commands Practiced

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --list
mkdir devops-git-practice
cd devops-git-practice
git init
ls -la
git status
git add .
git diff
git diff --staged
git commit -m "Add Git commands reference"
git log
git log --oneline
```

---

## Task 6: Git Workflow Questions

### 1. What is the difference between `git add` and `git commit`?

`git add` moves changes from the working directory to the staging area.

`git commit` saves the staged changes permanently into the Git repository history.

In simple words:

- `git add` prepares the changes
- `git commit` records the changes

Example:

```bash
git add git-commands.md
git commit -m "Add Git commands reference"
```

---

### 2. What does the staging area do? Why doesn't Git just commit directly?

The staging area is a middle step between editing files and committing them.

It allows us to choose exactly which changes should be included in the next commit.

Git does not commit directly because sometimes we may change many files, but we may not want to commit everything together.
The staging area helps us create clean and meaningful commits.

Example:

```bash
git add git-commands.md
git commit -m "Update Git commands reference"
```

---

### 3. What information does `git log` show you?

`git log` shows the commit history of the repository.

It usually displays:

- Commit ID
- Author name
- Author email
- Commit date and time
- Commit message

Example:

```bash
git log
```

For a shorter view:

```bash
git log --oneline
```

---

### 4. What is the `.git/` folder and what happens if you delete it?

The `.git/` folder is the main folder where Git stores repository information.

It contains commit history, branches, configuration, and internal Git data.

If the `.git/` folder is deleted, the project will no longer be a Git repository.
The files will still remain, but Git will stop tracking them.

Example:

```bash
ls -la
```

This command shows hidden files and folders, including `.git/`.

---

### 5. What is the difference between a working directory, staging area, and repository?

Git has three main areas:

#### Working Directory

The working directory is where we create, edit, and delete files.

Example:

```bash
nano git-commands.md
```

#### Staging Area

The staging area is where we prepare changes before committing them.

Example:

```bash
git add git-commands.md
```

#### Repository

The repository is where Git permanently stores committed changes.

Example:

```bash
git commit -m "Add Git notes"
```

---

## Git Workflow Summary

The basic Git workflow is:

```bash
edit files
git status
git add .
git commit -m "Meaningful commit message"
git log --oneline
```

---

## Multiple Commit Practice

I practiced making multiple commits to build a clean Git history.

Example commit flow:

```bash
git add git-commands.md
git commit -m "Add initial Git commands reference"

git add git-commands.md
git commit -m "Add Git repository setup commands"

git add git-commands.md day-22-notes.md
git commit -m "Add Day 22 Git workflow notes"
```

---

## Key Learnings

- Git tracks file changes over time
- `git status` helps understand the current repository state
- `git add` stages changes before committing
- `git commit` saves changes into Git history
- `.git/` contains all Git repository data
- Clear commit messages make project history easier to understand
- DevOps engineers use Git daily for scripts, automation, infrastructure code, and CI/CD workflows

---

## Final Notes

Today I created my first Git repository and started building my personal Git command reference.

I will keep updating `git-commands.md` as I learn more Git commands in the upcoming days.
