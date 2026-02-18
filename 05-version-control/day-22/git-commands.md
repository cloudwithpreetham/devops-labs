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

Shows the current branch, working directory, and staging area status.

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

## 6. Merge and Rebase Commands

### Merge a branch into the current branch

```bash
git merge feature-login
```

Combines the `feature-login` branch into the branch you are currently on.

### Merge a branch with squash

```bash
git merge --squash feature-profile
```

Combines all commits from the branch into one staged change on the current branch.
After this, create a commit manually.

```bash
git commit -m "feat: add profile feature"
```

### Rebase current branch onto another branch

```bash
git rebase main
```

Moves the current branch commits and replays them on top of the latest `main` branch.

### Continue rebase after resolving conflicts

```bash
git rebase --continue
```

Continues an active rebase after conflicts have been resolved and staged.

### Abort an active rebase

```bash
git rebase --abort
```

Stops the rebase and returns the branch to its previous state.

---

## 7. Stash Commands

### Save uncommitted changes temporarily

```bash
git stash
```

Temporarily saves uncommitted changes and returns the working tree to a clean state.

### Save stash with a message

```bash
git stash push -m "wip: temporary dashboard update"
```

Saves uncommitted changes with a clear message.

### List all stashes

```bash
git stash list
```

Shows all saved stashes.

### Apply latest stash and remove it from stash list

```bash
git stash pop
```

Restores the latest stash and removes it from the stash list.

### Apply latest stash but keep it in stash list

```bash
git stash apply
```

Restores the latest stash but keeps it saved in the stash list.

### Apply a specific stash

```bash
git stash apply stash@{1}
```

Restores a specific stash from the stash list.

### Delete a specific stash

```bash
git stash drop stash@{1}
```

Deletes a specific stash when it is no longer needed.

---

## 8. Cherry-Pick Commands

### Cherry-pick a specific commit

```bash
git cherry-pick <commit-hash>
```

Copies one specific commit from another branch and applies it to the current branch.

---

## 9. Undo and Recovery Commands

### Undo last commit but keep changes staged

```bash
git reset --soft HEAD~1
```

Moves `HEAD` back by one commit and keeps the undone commit changes in the staging area.

### Undo last commit and unstage changes

```bash
git reset --mixed HEAD~1
```

Moves `HEAD` back by one commit and keeps the undone commit changes in the working directory as unstaged changes.

### Undo last commit and discard changes

```bash
git reset --hard HEAD~1
```

Moves `HEAD` back by one commit and deletes the undone commit changes from the working directory.
Use this carefully because it can permanently remove local work.

### Revert a specific commit safely

```bash
git revert <commit-hash>
```

Creates a new commit that reverses the changes from an older commit without rewriting history.

### View reference history

```bash
git reflog
```

Shows recent movements of `HEAD`, which can help recover commits after a reset or branch mistake.

---

## 10. Remote Repository Commands

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

## 11. GitHub CLI Authentication Commands

### Check GitHub CLI version

```bash
gh --version
```

Shows the installed GitHub CLI version.

### Authenticate GitHub CLI

```bash
gh auth login
```

Logs in to GitHub from the terminal.

### Check authentication status

```bash
gh auth status
```

Shows the active GitHub account, authentication method, and token status.

### Log out from GitHub CLI

```bash
gh auth logout
```

Logs out from the authenticated GitHub account.

---

## 12. GitHub CLI Repository Commands

### Create a public repository with README

```bash
gh repo create repo-name --public --add-readme
```

Creates a new public GitHub repository and adds a README file.

### Clone a repository using GitHub CLI

```bash
gh repo clone owner/repo
```

Clones a GitHub repository to your local machine.

### View repository details

```bash
gh repo view owner/repo
```

Shows repository details in the terminal.

### Open repository in browser

```bash
gh repo view --web
```

Opens the current repository on GitHub in a browser.

### List repositories

```bash
gh repo list
```

Lists repositories for the authenticated GitHub user.

### List more repositories

```bash
gh repo list --limit 50
```

Lists up to 50 repositories.

### Delete a repository

```bash
gh repo delete owner/repo
```

Deletes a GitHub repository.
Use this carefully because it is destructive.

---

## 13. GitHub CLI Issue Commands

### Create an issue

```bash
gh issue create --title "Title" --body "Body" --label "bug"
```

Creates a new GitHub issue.

### List open issues

```bash
gh issue list
```

Lists open issues in the current repository.

### View a specific issue

```bash
gh issue view ISSUE_NUMBER
```

Shows details for a specific issue.

### Close an issue

```bash
gh issue close ISSUE_NUMBER
```

Closes an open issue.

### Reopen an issue

```bash
gh issue reopen ISSUE_NUMBER
```

Reopens a closed issue.

---

## 14. GitHub CLI Pull Request Commands

### Create a pull request

```bash
gh pr create --title "Title" --body "Body"
```

Creates a pull request from the current branch.

### Create a pull request using commit details

```bash
gh pr create --fill
```

Creates a pull request using commit messages for the title and body.

### List open pull requests

```bash
gh pr list
```

Lists open pull requests in the current repository.

### View pull request details

```bash
gh pr view PR_NUMBER
```

Shows details for a specific pull request.

### Open pull request in browser

```bash
gh pr view PR_NUMBER --web
```

Opens a pull request on GitHub in a browser.

### Show pull request status

```bash
gh pr status
```

Shows pull request status for the current repository.

### Checkout a pull request locally

```bash
gh pr checkout PR_NUMBER
```

Checks out a pull request branch locally.

### View pull request diff

```bash
gh pr diff PR_NUMBER
```

Shows the code changes in a pull request.

### Approve a pull request

```bash
gh pr review PR_NUMBER --approve
```

Approves a pull request.

### Comment on a pull request

```bash
gh pr review PR_NUMBER --comment --body "message"
```

Adds a review comment to a pull request.

### Request changes on a pull request

```bash
gh pr review PR_NUMBER --request-changes --body "message"
```

Requests changes on a pull request.

### Merge pull request with merge commit

```bash
gh pr merge PR_NUMBER --merge
```

Merges a pull request using a merge commit.

### Merge pull request with squash

```bash
gh pr merge PR_NUMBER --squash
```

Squashes pull request commits into one commit before merging.

### Merge pull request with rebase

```bash
gh pr merge PR_NUMBER --rebase
```

Rebases pull request commits before merging.

---

## 15. GitHub CLI Actions Commands

### List workflow runs

```bash
gh run list
```

Lists recent GitHub Actions workflow runs.

### View workflow run details

```bash
gh run view RUN_ID
```

Shows details for a specific workflow run.

### Watch a workflow run live

```bash
gh run watch RUN_ID
```

Watches a workflow run until it completes.

### View workflow logs

```bash
gh run view --log
```

Shows logs for a workflow run.

### List workflows

```bash
gh workflow list
```

Lists GitHub Actions workflows in the repository.

### Trigger a workflow manually

```bash
gh workflow run workflow.yml
```

Runs a GitHub Actions workflow manually.

---

## 16. GitHub CLI Extra Commands

### Call GitHub API

```bash
gh api user
```

Calls the GitHub API and shows authenticated user details.

### List repositories using GitHub API

```bash
gh api user/repos
```

Lists repositories using a raw GitHub API call.

### Create a public gist

```bash
gh gist create file.txt --public
```

Creates a public GitHub Gist.

### List gists

```bash
gh gist list
```

Lists GitHub Gists.

### Create a release

```bash
gh release create v1.0.0 --title "v1.0.0" --notes "Initial release"
```

Creates a GitHub release.

### List releases

```bash
gh release list
```

Lists GitHub releases.

### Create a GitHub CLI alias

```bash
gh alias set prs 'pr list'
```

Creates a shortcut for a frequently used GitHub CLI command.

### Search GitHub repositories

```bash
gh search repos devops --limit 10
```

Searches GitHub repositories from the terminal.

---

## 17. Clone and Fork Commands

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

## 18. Help Commands

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

## 19. Quick Reference

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

### Merge workflow

```bash
git switch main
git merge feature-login
git log --oneline --graph --all
```

### Rebase workflow

```bash
git switch feature-dashboard
git rebase main
git log --oneline --graph --all
```

### Squash merge workflow

```bash
git switch main
git merge --squash feature-profile
git commit -m "feat: add profile feature"
```

### Stash workflow

```bash
git status
git stash push -m "wip: temporary change"
git stash list
git switch main
git switch feature-branch
git stash pop
```

### Cherry-pick workflow

```bash
git log --oneline
git switch main
git cherry-pick <commit-hash>
git log --oneline --graph --all
```

### Reset workflow

```bash
git log --oneline
git reset --soft HEAD~1
git status
```

### Revert workflow

```bash
git log --oneline
git revert <commit-hash>
git log --oneline
```

### Recovery workflow

```bash
git reflog
git log --oneline
```

### GitHub workflow

```bash
git remote add origin https://github.com/<your-username>/devops-git-practice.git
git remote -v
git push -u origin main
git push -u origin feature-1
git pull origin main
```

### GitHub CLI authentication workflow

```bash
gh --version
gh auth login
gh auth status
```

### GitHub CLI repository workflow

```bash
gh repo create repo-name --public --add-readme
gh repo clone owner/repo
gh repo view owner/repo
gh repo list --limit 50
```

### GitHub CLI issue workflow

```bash
gh issue create --title "Title" --body "Body" --label "bug"
gh issue list
gh issue view ISSUE_NUMBER
gh issue close ISSUE_NUMBER
```

### GitHub CLI pull request workflow

```bash
gh pr create --fill
gh pr list
gh pr view PR_NUMBER
gh pr diff PR_NUMBER
gh pr review PR_NUMBER --approve
gh pr merge PR_NUMBER --squash
```

### GitHub CLI Actions workflow

```bash
gh run list
gh run view RUN_ID
gh run watch RUN_ID
gh workflow list
gh workflow run workflow.yml
```

### GitHub CLI extras workflow

```bash
gh api user
gh gist create file.txt --public
gh release create v1.0.0 --title "v1.0.0" --notes "Initial release"
gh alias set prs 'pr list'
gh search repos devops --limit 10
```

### Fork sync workflow

```bash
git remote add upstream https://github.com/original-owner/project.git
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```
