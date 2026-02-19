# 05 - Version Control

This folder contains my Version Control learning work from the **90 Days of DevOps** journey.
The focus of this section is to build strong Git and GitHub fundamentals used in real DevOps workflows.

## Overview

Version control is one of the most important skills for DevOps engineers. It helps teams track changes, collaborate safely, manage infrastructure code, and maintain clean project history.

In this module, I practiced Git basics, branching, GitHub workflows, undoing changes, advanced Git commands, GitHub CLI, and GitHub profile improvement.

## Folder Structure

```bash
05-version-control/
├── day-22/
├── day-23/
├── day-24/
├── day-25/
├── day-26/
├── day-27/
└── README.md
```

## Topics Covered

| Day    | Topic                                  | Focus Area                                                    |
| ------ | -------------------------------------- | ------------------------------------------------------------- |
| Day 22 | Introduction to Git                    | Git setup, repository creation, staging, commits, Git basics  |
| Day 23 | Git Branching & GitHub                 | Branch creation, switching branches, pushing to GitHub        |
| Day 24 | Advanced Git                           | Merge, rebase, stash, cherry-pick                             |
| Day 25 | Reset vs Revert & Branching Strategies | Safe undo workflows and team branching models                 |
| Day 26 | GitHub CLI                             | Managing GitHub repositories and pull requests from terminal  |
| Day 27 | GitHub Profile Makeover                | GitHub profile README, repository cleanup, developer branding |

## Key Skills Practiced

- Initialized and managed Git repositories
- Created and tracked files using Git
- Used staging and commit workflows correctly
- Created and switched between branches
- Pushed local repositories to GitHub
- Practiced merge, rebase, stash, and cherry-pick
- Learned the difference between `git reset` and `git revert`
- Used GitHub CLI for terminal-based GitHub management
- Improved GitHub profile and repository presentation
- Documented daily learning using Markdown

## Important Git Commands

```bash
# Check Git version
git --version

# Configure Git identity
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# Initialize repository
git init

# Check repository status
git status

# Stage files
git add .
git add <file-name>

# Commit changes
git commit -m "commit message"

# View commit history
git log --oneline

# Create and switch branch
git checkout -b <branch-name>

# Switch branch
git checkout <branch-name>

# Merge branch
git merge <branch-name>

# Push to GitHub
git push origin main
```

## GitHub CLI Commands Practiced

```bash
# Check GitHub CLI version
gh --version

# Authenticate GitHub CLI
gh auth login

# Check authentication status
gh auth status

# Create repository from terminal
gh repo create

# View repository information
gh repo view

# Create pull request
gh pr create

# List pull requests
gh pr list
```

## Real-World DevOps Relevance

Version control is used daily in DevOps roles for:

- Managing Infrastructure as Code repositories
- Tracking CI/CD pipeline changes
- Collaborating with developers and operations teams
- Reviewing pull requests before deployment
- Rolling back unsafe changes
- Maintaining clean and readable project history
- Automating GitHub workflows using CLI and scripts

## Best Practices Learned

- Write clear and meaningful commit messages
- Keep commits small and focused
- Avoid committing secrets, credentials, or sensitive files
- Use branches for features, fixes, and experiments
- Pull latest changes before pushing your work
- Prefer `git revert` for shared branches
- Use `.gitignore` to prevent unwanted files from being tracked
- Keep repository names, descriptions, and READMEs clean
- Document every project clearly for recruiters and collaborators

## Suggested Commit Message Style

```bash
git commit -m "docs: add version control module README"
```

Other examples:

```bash
git commit -m "docs: document Git basics for day 22"
git commit -m "docs: add Git branching notes for day 23"
git commit -m "docs: summarize advanced Git workflows"
git commit -m "docs: add GitHub CLI learning notes"
```

## Learning Outcome

By completing this module, I gained practical experience with Git and GitHub workflows that are required in real DevOps environments. I can now manage repositories, work with branches, undo changes safely, use GitHub from the terminal, and present my work professionally on GitHub.

## Status

Completed as part of my **90 Days of DevOps** learning journey.
