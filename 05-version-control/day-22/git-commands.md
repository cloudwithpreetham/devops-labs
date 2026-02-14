````md
# Git Commands Reference

This file is my personal Git command reference for the 90DaysOfDevOps journey.
I will keep updating this file as I learn more Git commands.

---

## 1. Setup & Configuration

### Check Git version

```bash
git --version
```
````

Checks whether Git is installed and displays the installed Git version.

---

### Set Git username

```bash
git config --global user.name "Your Name"
```

Sets the username that will appear in Git commits.

---

### Set Git email

```bash
git config --global user.email "your-email@example.com"
```

Sets the email address that will appear in Git commits.

---

### View Git configuration

```bash
git config --list
```

Displays the current Git configuration.

---

### View configured username

```bash
git config user.name
```

Shows the Git username configured for the current system or repository.

---

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

---

### Move into the project directory

```bash
cd devops-git-practice
```

Moves into the project folder.

---

### Initialize a Git repository

```bash
git init
```

Creates a new Git repository in the current directory.

---

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

---

### Stage a specific file

```bash
git add git-commands.md
```

Adds a specific file to the staging area.

---

### Stage all changes

```bash
git add .
```

Adds all new, modified, and deleted files to the staging area.

---

### Commit staged changes

```bash
git commit -m "Add Git commands reference"
```

Saves the staged changes into the Git repository history.

---

## 4. Viewing Changes

### View unstaged changes

```bash
git diff
```

Shows changes that have been made but not staged yet.

---

### View staged changes

```bash
git diff --staged
```

Shows changes that are staged and ready to be committed.

---

### View detailed commit history

```bash
git log
```

Displays detailed commit history with commit ID, author, date, and message.

---

### View compact commit history

```bash
git log --oneline
```

Displays commit history in a short one-line format.

---

## 5. Help Commands

### Open general Git help

```bash
git help
```

Displays Git help information.

---

### Open help for a specific command

```bash
git status --help
```

Displays detailed help for the `git status` command.

---

## 6. Daily Git Workflow

```bash
git status
git add .
git commit -m "Clear commit message"
git log --oneline
```
