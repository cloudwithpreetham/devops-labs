# GitHub Actions Practice – Day 41

This repository contains my hands-on practice for **Day 41 of 90 Days of DevOps**.

The focus of this day was learning different GitHub Actions workflow triggers and matrix builds.

---

## Topics Covered

- Pull request workflow triggers
- Scheduled workflow triggers using cron
- Manual workflow triggers using `workflow_dispatch`
- Workflow input parameters
- Matrix builds
- Matrix exclusions
- `fail-fast` behavior in matrix jobs

---

## Repository Structure

```text
github-actions-practice/
├── .github/
│   └── workflows/
│       ├── hello.yml
│       ├── pr-check.yml
│       ├── manual.yml
│       └── matrix.yml
└── 2026/
    └── day-41/
        └── day-41-triggers.md
```

---

## Workflows

### 1. First GitHub Actions Workflow

File:

```text
.github/workflows/hello.yml
```

Purpose:

- Runs on every push
- Prints a basic message
- Introduces the basic structure of a GitHub Actions workflow

---

### 2. Pull Request Check Workflow

File:

```text
.github/workflows/pr-check.yml
```

Purpose:

- Runs when a pull request is opened or updated
- Runs only for pull requests targeting the `main` branch
- Prints the pull request source branch name

Trigger used:

```yaml
on:
  pull_request:
    branches:
      - main
    types:
      - opened
      - synchronize
```

![Pull request check workflow run](screenshots/day-41-pr-check-run.png)

---

### 3. Manual Environment Workflow

File:

```text
.github/workflows/manual.yml
```

Purpose:

- Allows manual workflow execution from the GitHub Actions tab
- Accepts an environment input
- Supports `staging` and `production`

Trigger used:

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Choose deployment environment"
        required: true
        default: "staging"
        type: choice
        options:
          - staging
          - production
```

![Manual workflow dispatch run](screenshots/day-41-manual-workflow-run.png)

---

### 4. Python Matrix Build Workflow

File:

```text
.github/workflows/matrix.yml
```

Purpose:

- Runs the same job across multiple Python versions and operating systems
- Demonstrates matrix builds
- Excludes one specific matrix combination
- Tests `fail-fast: false`

Matrix used:

```yaml
strategy:
  fail-fast: false
  matrix:
    os:
      - ubuntu-latest
      - windows-latest
    python-version:
      - "3.10"
      - "3.11"
      - "3.12"
    exclude:
      - os: windows-latest
        python-version: "3.10"
```

Final matrix result:

```text
3 Python versions × 2 operating systems = 6 jobs
6 jobs - 1 excluded combination = 5 jobs
```

![Matrix build workflow run](screenshots/day-41-matrix-build-run.png)

---

## Cron Practice

Daily midnight UTC schedule:

```yaml
on:
  schedule:
    - cron: "0 0 * * *"
```

Cron expression for every Monday at 9 AM UTC:

```text
0 9 * * 1
```

---

## Key Learnings

- GitHub Actions workflows are event-driven.
- `pull_request` workflows are useful for validating code before merging.
- `workflow_dispatch` is useful when manual control is required.
- `schedule` allows workflows to run automatically using cron.
- Matrix builds help test across multiple versions and environments.
- `exclude` removes unwanted matrix combinations.
- `fail-fast: false` allows other matrix jobs to continue even if one job fails.

---

## Real-World DevOps Usage

In real DevOps projects, these workflow triggers are commonly used for:

- Running tests before merging pull requests
- Triggering manual deployments to staging or production
- Running scheduled security scans
- Testing applications across multiple runtime versions
- Checking compatibility across Linux and Windows environments

---

## Commands Used

```bash
mkdir -p .github/workflows
mkdir -p 2026/day-41

git add .github/workflows/pr-check.yml
git commit -m "ci: add pull request trigger workflow"

git add .github/workflows/manual.yml
git commit -m "ci: add manual workflow dispatch trigger"

git add .github/workflows/matrix.yml
git commit -m "ci: add matrix build workflow with fail-fast control"

git add 2026/day-41/day-41-triggers.md
git commit -m "docs: add day 41 GitHub Actions trigger notes"
```

---

## Status

Day 41 completed successfully.

The workflows were created, tested, and documented with screenshots.

---

## Learning Journey

This repository is part of my **90 Days of DevOps** learning journey.

Hashtags:

```text
#90DaysOfDevOps
#DevOpsKaJosh
#TrainWithShubham
```
