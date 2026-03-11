# GitHub Actions Practice

This repository is part of my **90 Days of DevOps** learning journey.

The goal of this repository is to practice GitHub Actions from beginner to advanced level by creating real CI/CD workflows used in DevOps projects.

---

## Repository Purpose

This repo is used to learn and practice:

- GitHub Actions basics
- Workflow triggers
- Jobs and steps
- Environment variables
- Secrets
- Artifacts
- Docker build and push pipelines
- Reusable workflows
- Composite actions
- Advanced triggers
- Pull request validation
- Scheduled workflows
- Event-driven pipelines

---

## Current Focus

### Day 47 – Advanced Triggers

In Day 47, I practiced advanced GitHub Actions triggers such as:

- Pull request lifecycle events
- PR validation checks
- Scheduled cron workflows
- Path and branch filters
- Workflow chaining using `workflow_run`
- External event triggers using `repository_dispatch`

---

## Project Structure

```text
github-actions-practice/
├── .github/
│   └── workflows/
│       ├── hello.yml
│       ├── pr-check.yml
│       ├── matrix-build.yml
│       ├── multi-job.yml
│       ├── docker-publish.yml
│       ├── reusable-ci.yml
│       ├── caller-workflow.yml
│       ├── pr-lifecycle.yml
│       ├── pr-checks.yml
│       ├── scheduled-tasks.yml
│       ├── smart-triggers.yml
│       ├── ignore-docs-trigger.yml
│       ├── tests.yml
│       ├── deploy-after-tests.yml
│       └── external-trigger.yml
├── 2026/
│   ├── day-40/
│   ├── day-41/
│   ├── day-42/
│   ├── day-43/
│   ├── day-44/
│   ├── day-45/
│   ├── day-46/
│   └── day-47/
│       └── day-47-advanced-triggers.md
└── README.md
```

---

## Workflows Covered

### Basic Workflow

A simple workflow that runs on push and prints a message.

```yaml
on:
  push:
```

Used to understand the basic structure of GitHub Actions.

---

### Pull Request Workflow

Runs when a pull request is opened or updated.

```yaml
on:
  pull_request:
```

Used to validate code before merging into the main branch.

---

### Matrix Build

Runs the same job across multiple versions or environments.

Example use cases:

- Test multiple Node.js versions
- Test multiple Python versions
- Test across different operating systems

---

### Multi-Job Workflow

Used to understand job dependencies.

Example flow:

```text
build → test → deploy
```

This is a common structure in real CI/CD pipelines.

---

### Docker CI/CD Workflow

Builds and pushes a Docker image to Docker Hub.

This workflow helped me understand how CI/CD pipelines are used to package and ship applications.

---

### Reusable Workflow

Reusable workflows help avoid repeating the same workflow logic in multiple repositories.

```yaml
on:
  workflow_call:
```

This is useful for standardizing CI/CD pipelines across teams.

---

### Composite Action

Composite actions allow multiple steps to be packaged as a custom action.

This is useful when the same commands are repeated in many workflows.

---

### Advanced Trigger Workflows

Day 47 introduced event-driven workflows.

Created workflows:

```text
.github/workflows/pr-lifecycle.yml
.github/workflows/pr-checks.yml
.github/workflows/scheduled-tasks.yml
.github/workflows/smart-triggers.yml
.github/workflows/ignore-docs-trigger.yml
.github/workflows/tests.yml
.github/workflows/deploy-after-tests.yml
.github/workflows/external-trigger.yml
```

---

## Day 47 Workflow Summary

### 1. PR Lifecycle Workflow

File:

```text
.github/workflows/pr-lifecycle.yml
```

Triggers on:

```yaml
types:
  - opened
  - synchronize
  - reopened
  - closed
```

This workflow prints:

- PR event action
- PR title
- PR author
- Source branch
- Target branch

It also has a conditional step that runs only when the PR is merged.

---

### 2. PR Validation Checks

File:

```text
.github/workflows/pr-checks.yml
```

This workflow checks:

- Files larger than 1 MB
- Branch naming pattern
- PR description

Allowed branch names:

```text
feature/*
fix/*
docs/*
```

This is similar to real-world PR quality gates used by DevOps teams.

---

### 3. Scheduled Tasks

File:

```text
.github/workflows/scheduled-tasks.yml
```

This workflow runs on cron schedules:

```yaml
- cron: "30 2 * * 1"
- cron: "0 */6 * * *"
```

It also supports manual execution using:

```yaml
workflow_dispatch:
```

The workflow performs a simple health check using `curl`.

---

### 4. Smart Path Trigger

File:

```text
.github/workflows/smart-triggers.yml
```

Runs only when files inside `src/` or `app/` change.

```yaml
paths:
  - "src/**"
  - "app/**"
```

Useful in monorepos where only affected services should trigger pipelines.

---

### 5. Ignore Docs Trigger

File:

```text
.github/workflows/ignore-docs-trigger.yml
```

Skips workflow runs when only documentation files change.

```yaml
paths-ignore:
  - "*.md"
  - "docs/**"
```

This helps reduce unnecessary CI runs.

---

### 6. Workflow Chaining

Files:

```text
.github/workflows/tests.yml
.github/workflows/deploy-after-tests.yml
```

The deploy workflow runs only after the test workflow completes.

```yaml
on:
  workflow_run:
    workflows:
      - Run Tests
    types:
      - completed
```

This is useful for separating CI and CD pipelines.

---

### 7. External Trigger

File:

```text
.github/workflows/external-trigger.yml
```

Uses:

```yaml
on:
  repository_dispatch:
```

This allows external systems to trigger a GitHub Actions workflow.

Example:

```bash
gh api repos/cloud-with-preetham/github-actions-practice/dispatches \
  -f event_type=deploy-request \
  -f client_payload='{"environment":"production"}'
```

---

## Cron Notes

GitHub Actions cron uses UTC time.

| Requirement                              | Cron Expression |
| ---------------------------------------- | --------------- |
| Every Monday at 2:30 AM UTC              | `30 2 * * 1`    |
| Every 6 hours                            | `0 */6 * * *`   |
| Every weekday at 9 AM IST                | `30 3 * * 1-5`  |
| First day of every month at midnight UTC | `0 0 1 * *`     |

---

## Key Learnings

Through this repository, I learned that GitHub Actions can automate workflows based on many real-world events.

Important concepts covered:

- CI/CD automation
- Pull request checks
- Workflow dependencies
- Scheduled jobs
- Path-based triggers
- Branch-based triggers
- Event-driven pipelines
- Reusable workflow design
- Docker image publishing

---

## Real-World DevOps Use Cases

These workflows are useful for:

- Running tests before merging pull requests
- Blocking bad branch names
- Preventing large files from entering the repo
- Running scheduled health checks
- Skipping CI for documentation-only changes
- Deploying only after tests pass
- Triggering deployments from external systems
- Standardizing CI/CD pipelines across projects

---

## Skills Practiced

- GitHub Actions
- YAML
- CI/CD
- Docker CI pipeline
- Pull request automation
- Cron scheduling
- Workflow chaining
- Event-driven DevOps
- Repository automation

---

## Learning Journey

This repository is part of my daily DevOps learning practice.

Each day focuses on one practical topic and includes:

- Workflow files
- Hands-on implementation
- Documentation
- Git commits
- Screenshots where required

---

## Author

**Preetham**

DevOps Learner practicing real-world CI/CD, Docker, GitHub Actions, Cloud, and automation through hands-on projects.

---

## Tags

```text
#90DaysOfDevOps
#DevOps
#GitHubActions
#CICD
#Docker
#Automation
#TrainWithShubham
```
