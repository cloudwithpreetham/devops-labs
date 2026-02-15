# Git Commands Reference

This file is my personal Git command reference for the 90DaysOfDevOps journey.
I will keep updating this file as I learn more Git commands.

---

## 1. Setup and Configuration

### Check Git version

```bash
git --version
```

Checks whether Git is installed and displays the installed Git version.

### Set Git username

```bash
git config --global user.name "Your Name"
```

Sets the username that will appear in Git commits.

### Set Git email

```bash
git config --global user.email "your-email@example.com"
```

Sets the email address that will appear in Git commits.

### View Git configuration

```bash
git config --list
```

Displays the current Git configuration.

### View configured username

```bash
git config user.name
```

Shows the Git username configured for the current system or repository.

### View configured email

```bash
git config user.email
```

Shows the Git email configured for the current system or repository.

---

## 2. Repository Setup

### Create a new directory

```bash
mkdir devops-git-practice
```

Creates a new project folder.

### Move into the project directory

```bash
cd devops-git-practice
```

Moves into the project folder.

### Initialize a Git repository

```bash
git init
```

Creates a new Git repository in the current directory.

### List all files including hidden files

```bash
ls -la
```

Shows all files and folders, including the hidden `.git/` directory.

---

## 3. Basic Git Workflow

### Check repository status

```bash
git status
```

Shows the current state of the working directory and staging area.

### Stage a specific file

```bash
git add git-commands.md
```

Adds a specific file to the staging area.

### Stage all changes

```bash
git add .
```

Adds all new, modified, and deleted files to the staging area.

### Commit staged changes

```bash
git commit -m "Add Git commands reference"
```

Saves the staged changes into the Git repository history.

### Daily workflow

```bash
git status
git add .
git commit -m "Clear commit message"
git log --oneline
```

This is the basic workflow for checking changes, staging them, committing them, and viewing recent history.

---

## 4. Viewing Changes and History

### View unstaged changes

```bash
git diff
```

Shows changes that have been made but not staged yet.

### View staged changes

```bash
git diff --staged
```

Shows changes that are staged and ready to be committed.

### View detailed commit history

```bash
git log
```

Displays detailed commit history with commit ID, author, date, and message.

### View compact commit history

```bash
git log --oneline
```

Displays commit history in a short one-line format.

### View commit history with branch graph

```bash
git log --oneline --graph --all
```

Shows commit history with branch structure.

---

## 5. Branch Commands

### List all local branches

```bash
git branch
```

Shows all local branches in the repository.

### List local and remote branches

```bash
git branch -a
```

Shows both local and remote branches.

### Create a new branch

```bash
git branch feature-1
```

Creates a new branch called `feature-1`.

### Switch to another branch

```bash
git switch feature-1
```

Switches to the `feature-1` branch.

### Create and switch to a new branch

```bash
git switch -c feature-2
```

Creates a new branch and switches to it immediately.

### Older way to switch branches

```bash
git checkout feature-1
```

Switches to an existing branch using the older `checkout` command.

### Older way to create and switch branches

```bash
git checkout -b feature-2
```

Creates and switches to a new branch using the older `checkout` command.

### Delete a local branch safely

```bash
git branch -d feature-2
```

Deletes a branch only if it has already been merged.

### Force delete a local branch

```bash
git branch -D feature-2
```

Force deletes a branch even if it has not been merged.

---

## 6. Remote Repository Commands

### Add GitHub remote repository

```bash
git remote add origin https://github.com/<your-username>/devops-git-practice.git
```

Connects the local repository to a GitHub repository.

### View remote repositories

```bash
git remote -v
```

Shows the remote repository URLs.

### Push main branch to GitHub

```bash
git push -u origin main
```

Pushes the local `main` branch to GitHub and sets upstream tracking.

### Push a feature branch to GitHub

```bash
git push -u origin feature-1
```

Pushes the local `feature-1` branch to GitHub.

### Fetch latest changes from GitHub

```bash
git fetch origin
```

Downloads remote changes but does not merge them automatically.

### Pull latest changes from GitHub

```bash
git pull origin main
```

Downloads and merges changes from the remote `main` branch.

---

## 7. Clone and Fork Commands

### Clone a repository

```bash
git clone https://github.com/original-owner/project.git
```

Creates a local copy of a remote repository.

### Clone your fork

```bash
git clone https://github.com/<your-username>/project.git
```

Clones your forked repository to your local machine.

### Add upstream remote

```bash
git remote add upstream https://github.com/original-owner/project.git
```

Adds the original repository as `upstream`.

### Fetch changes from upstream

```bash
git fetch upstream
```

Downloads the latest changes from the original repository.

### Merge upstream changes into main

```bash
git switch main
git merge upstream/main
```

Updates your local `main` branch with changes from the original repository.

### Push synced changes to your fork

```bash
git push origin main
```

Pushes the updated local branch to your GitHub fork.

---

## 8. Help Commands

### Open general Git help

```bash
git help
```

Displays Git help information.

### Open help for a specific command

```bash
git status --help
```

Displays detailed help for the `git status` command.

---

## 9. Quick Reference

### First-time Git setup

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --list
```

### Create and commit in a new repository

```bash
mkdir devops-git-practice
cd devops-git-practice
git init
git status
git add .
git commit -m "Initial commit"
git log --oneline
```

### Branch workflow

```bash
git branch
git switch -c feature-1
git status
git add .
git commit -m "Add feature work"
git switch main
```

### GitHub workflow

```bash
git remote add origin https://github.com/<your-username>/devops-git-practice.git
git remote -v
git push -u origin main
git push -u origin feature-1
git pull origin main
```

### Fork sync workflow

```bash
git remote add upstream https://github.com/original-owner/project.git
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```
