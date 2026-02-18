# Day 26 – GitHub CLI: Manage GitHub from Your Terminal

## Overview

Today I learned how to use the GitHub CLI (`gh`) to manage GitHub repositories, issues, pull requests, workflow runs, releases, gists, aliases, and API calls directly from the terminal.

GitHub CLI is useful for DevOps because it reduces context switching between terminal and browser. It also helps automate common GitHub tasks in scripts and CI/CD workflows.

---

## Task 1: Install and Authenticate

### Install GitHub CLI

```bash
sudo apt update
sudo apt install gh -y
```

### Verify installation

```bash
gh --version
```

### Authenticate with GitHub

```bash
gh auth login
```

During authentication, GitHub CLI asks for:

- GitHub.com or GitHub Enterprise Server
- Preferred protocol: HTTPS or SSH
- Authentication method
- Browser-based login or token-based login

### Check active GitHub account

```bash
gh auth status
```

### Observation

After logging in, `gh auth status` shows the active GitHub account, authentication method, Git protocol, and token scopes.

### What authentication methods does `gh` support?

GitHub CLI supports multiple authentication methods:

1. Browser-based authentication
2. Personal Access Token authentication
3. SSH-based Git operations after authentication
4. GitHub Enterprise authentication for organization/company GitHub instances

Browser login is the easiest for beginners. Token authentication is useful for automation, servers, and CI/CD workflows.

---

## Task 2: Working with Repositories

### Create a new GitHub repo from terminal

```bash
gh repo create gh-cli-practice --public --add-readme
```

### Clone a repo using `gh`

```bash
gh repo clone username/gh-cli-practice
```

Example:

```bash
gh repo clone cloud-with-preetham/gh-cli-practice
```

### View repo details

```bash
gh repo view username/repo-name
```

Example:

```bash
gh repo view cloud-with-preetham/devops-git-practice
```

### List all repositories

```bash
gh repo list
```

To list more repositories:

```bash
gh repo list --limit 50
```

### Open repo in browser

```bash
gh repo view --web
```

Or:

```bash
gh repo view username/repo-name --web
```

### Delete test repo

```bash
gh repo delete username/gh-cli-practice
```

### Observation

Repository management becomes faster with `gh` because creating, cloning, viewing, listing, opening, and deleting repositories can all be done from the terminal.

---

## Task 3: Issues

### Create an issue from terminal

```bash
gh issue create --title "Test issue from GitHub CLI" --body "This issue was created using gh CLI." --label "documentation"
```

For a specific repo:

```bash
gh issue create --repo username/repo-name --title "Update README" --body "Improve documentation for GitHub CLI commands." --label "documentation"
```

### List open issues

```bash
gh issue list
```

For a specific repo:

```bash
gh issue list --repo username/repo-name
```

### View a specific issue

```bash
gh issue view 1
```

### Close an issue

```bash
gh issue close 1
```

### Observation

Issues can be created, listed, viewed, and closed without opening GitHub in the browser.

### How could you use `gh issue` in a script or automation?

`gh issue` can be used in automation to:

- Create issues automatically when a script detects a failed deployment
- Open bug reports from log monitoring scripts
- Close issues when a fix is deployed
- Label issues based on error type or priority
- Generate weekly reports of open issues

Example automation idea:

```bash
#!/bin/bash

ERROR_COUNT=$(grep -c "ERROR" app.log)

if [ "$ERROR_COUNT" -gt 0 ]; then
  gh issue create \
    --title "Application errors detected" \
    --body "Found $ERROR_COUNT errors in app.log. Please investigate." \
    --label "bug"
fi
```

---

## Task 4: Pull Requests

### Create a new branch

```bash
git checkout -b update-gh-cli-notes
```

### Make a change

```bash
echo "GitHub CLI practice" >> README.md
```

### Stage and commit

```bash
git add README.md
git commit -m "docs: add GitHub CLI practice note"
```

### Push branch

```bash
git push -u origin update-gh-cli-notes
```

### Create pull request from terminal

```bash
gh pr create --title "Add GitHub CLI practice note" --body "Added notes for GitHub CLI practice."
```

Auto-fill PR title and body from commits:

```bash
gh pr create --fill
```

### List open PRs

```bash
gh pr list
```

### View PR details

```bash
gh pr view 1
```

### View PR in browser

```bash
gh pr view 1 --web
```

### Check PR status

```bash
gh pr status
```

### Merge PR from terminal

```bash
gh pr merge 1 --merge
```

### What merge methods does `gh pr merge` support?

`gh pr merge` supports:

1. Merge commit

```bash
gh pr merge 1 --merge
```

2. Squash merge

```bash
gh pr merge 1 --squash
```

3. Rebase merge

```bash
gh pr merge 1 --rebase
```

### How would you review someone else's PR using `gh`?

Useful commands for reviewing PRs:

```bash
gh pr list
```

```bash
gh pr view 5
```

```bash
gh pr checkout 5
```

```bash
git diff main...HEAD
```

```bash
gh pr diff 5
```

```bash
gh pr review 5 --comment --body "Looks good, but please update the README example."
```

Approve PR:

```bash
gh pr review 5 --approve
```

Request changes:

```bash
gh pr review 5 --request-changes --body "Please fix the script validation before merging."
```

### Observation

Pull requests can be fully managed from the terminal. This is very useful for real DevOps work because engineers often review code, check CI status, and merge fixes without leaving the command line.

---

## Task 5: GitHub Actions & Workflows Preview

### List workflow runs

```bash
gh run list --repo owner/repo-name
```

Example:

```bash
gh run list --repo cli/cli
```

### View a specific workflow run

```bash
gh run view RUN_ID --repo owner/repo-name
```

### Watch a workflow run live

```bash
gh run watch RUN_ID --repo owner/repo-name
```

### View workflow files

```bash
gh workflow list --repo owner/repo-name
```

### Run a workflow manually

```bash
gh workflow run workflow-name.yml
```

### How could `gh run` and `gh workflow` be useful in a CI/CD pipeline?

`gh run` and `gh workflow` can be useful in CI/CD pipelines because they allow engineers to:

- Check deployment workflow status from the terminal
- Trigger workflows manually
- Watch CI/CD jobs in real time
- Debug failed workflow runs
- Download workflow logs
- Automate release or deployment tasks

Example:

```bash
gh run list --limit 5
```

```bash
gh run view --log
```

### Observation

Even without learning GitHub Actions deeply yet, `gh run` gives a preview of how DevOps engineers monitor CI/CD pipelines directly from the terminal.

---

## Task 6: Useful `gh` Tricks

### 1. `gh api`

Make raw GitHub API calls from terminal.

```bash
gh api user
```

List repositories using API:

```bash
gh api user/repos
```

This is useful for scripting and automation.

---

### 2. `gh gist`

Create and manage GitHub Gists.

```bash
gh gist create notes.txt --public
```

List gists:

```bash
gh gist list
```

View a gist:

```bash
gh gist view GIST_ID
```

---

### 3. `gh release`

Create and manage GitHub releases.

```bash
gh release create v1.0.0 --title "v1.0.0" --notes "Initial release"
```

List releases:

```bash
gh release list
```

View release:

```bash
gh release view v1.0.0
```

---

### 4. `gh alias`

Create shortcuts for frequently used commands.

```bash
gh alias set prs 'pr list'
```

Now run:

```bash
gh prs
```

Another useful alias:

```bash
gh alias set co 'pr checkout'
```

Use it like:

```bash
gh co 5
```

---

### 5. `gh search repos`

Search GitHub repositories from terminal.

```bash
gh search repos devops --limit 10
```

Search by language:

```bash
gh search repos "devops language:Python" --limit 10
```

Search Kubernetes projects:

```bash
gh search repos kubernetes --stars ">1000" --limit 10
```

---

## Important GitHub CLI Commands Practiced

```bash
gh --version
gh auth login
gh auth status
gh repo create
gh repo clone
gh repo view
gh repo list
gh repo delete
gh issue create
gh issue list
gh issue view
gh issue close
gh pr create
gh pr list
gh pr view
gh pr status
gh pr checkout
gh pr diff
gh pr review
gh pr merge
gh run list
gh run view
gh workflow list
gh api
gh gist create
gh release create
gh alias set
gh search repos
```

---

## GitHub CLI Best Practices

- Always verify authentication using `gh auth status`
- Use `--repo owner/repo` when working outside the repo directory
- Use `--json` for scripting and automation
- Use `--fill` while creating PRs from clean commit messages
- Be careful with destructive commands like `gh repo delete`
- Use aliases for repeated commands
- Review PR diffs before approving or merging
- Prefer automation-friendly outputs for DevOps scripts

---

## Real-World DevOps Use Cases

GitHub CLI can be used by DevOps engineers to:

- Create repositories for new projects
- Automate issue creation from monitoring scripts
- Create and merge pull requests from terminal
- Check CI/CD workflow status
- Trigger GitHub Actions workflows
- Create releases during deployment
- Use GitHub API from shell scripts
- Review PRs during incident fixes

---

## Final Reflection

Today I learned that GitHub CLI is more than a simple command-line tool. It can manage repositories, issues, pull requests, workflows, releases, gists, and API calls directly from the terminal.

This is important for DevOps because many real-world tasks are automated using terminal commands and scripts. GitHub CLI will be useful later when working with CI/CD pipelines, GitHub Actions, release automation, and infrastructure repositories.
