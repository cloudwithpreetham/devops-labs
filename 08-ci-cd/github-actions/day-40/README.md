# GitHub Actions Practice

This repository contains my Day 40 task from the **90 Days of DevOps** journey.

The goal of this project is to create a first GitHub Actions workflow, run it in the cloud, understand basic workflow syntax, intentionally break the pipeline, debug the failure, and fix it.

---

## Project Overview

In this project, I created a simple GitHub Actions workflow that runs automatically on every push to the repository.

The workflow performs basic CI tasks such as:

- Checking out the repository code
- Printing a greeting message
- Printing the current date and time
- Printing the branch name
- Listing repository files
- Printing the runner operating system

---

## Repository Structure

```text
github-actions-practice/
├── .github/
│   └── workflows/
│       └── hello.yml
├── 2026/
│   └── day-40/
│       ├── day-40-first-workflow.md
│       └── screenshots/
│           ├── 01-github-actions-workflow-file.png
│           ├── 02-first-green-pipeline-run.png
│           ├── 03-workflow-job-steps.png
│           ├── 04-failed-pipeline-run.png
│           └── 05-fixed-green-pipeline-run.png
├── LICENSE
└── README.md
```

---

## Workflow File

The workflow is located at:

```text
.github/workflows/hello.yml
```

---

## Workflow YAML

Screenshot of the workflow file:

![GitHub Actions workflow file](screenshots/01-github-actions-workflow-file.png)

```yaml
name: First GitHub Actions Workflow

on:
  push:

jobs:
  greet:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository code
        uses: actions/checkout@v4

      - name: Print greeting message
        run: echo "Hello from GitHub Actions!"

      - name: Print current date and time
        run: date

      - name: Print branch name
        run: echo "Branch name is ${{ github.ref_name }}"

      - name: List repository files
        run: ls -la

      - name: Print runner operating system
        run: echo "Runner OS is $RUNNER_OS"
```

---

## Workflow Explanation

### `name`

Defines the name of the workflow that appears in the GitHub Actions tab.

### `on`

Defines the event that triggers the workflow.

In this project, the workflow runs on every `push`.

### `jobs`

Defines the group of tasks that GitHub Actions should run.

This workflow has one job named `greet`.

### `runs-on`

Defines the runner environment where the job runs.

This workflow uses:

```yaml
runs-on: ubuntu-latest
```

### `steps`

Defines the individual actions or commands that run inside the job.

### `uses`

Runs a reusable GitHub Action.

Example:

```yaml
uses: actions/checkout@v4
```

This checks out the repository code into the GitHub Actions runner.

### `run`

Runs shell commands on the GitHub Actions runner.

Example:

```yaml
run: echo "Hello from GitHub Actions!"
```

---

## Pipeline Runs

### First Successful Run

The first workflow run completed successfully and showed a green checkmark.

![First successful GitHub Actions pipeline run](screenshots/02-first-green-pipeline-run.png)

### Job Steps

The `greet` job completed all steps successfully.

![GitHub Actions greet job steps](screenshots/03-workflow-job-steps.png)

### Intentional Failure

To understand pipeline failures, I intentionally added a failing step:

```yaml
- name: Break pipeline intentionally
  run: exit 1
```

This caused the workflow to fail with the error:

```text
Error: Process completed with exit code 1.
```

![Failed GitHub Actions pipeline run](screenshots/04-failed-pipeline-run.png)

### Fixed Run

After removing the failing step and pushing the fix, the pipeline passed again.

![Fixed GitHub Actions pipeline run](screenshots/05-fixed-green-pipeline-run.png)

---

## What I Learned

- GitHub Actions workflows are stored inside `.github/workflows/`.
- Workflow files are written in YAML.
- A workflow can run automatically when code is pushed.
- Jobs contain steps.
- Steps can use reusable actions or run shell commands.
- GitHub-hosted runners execute pipeline jobs in the cloud.
- A green check means the pipeline passed.
- A red cross means the pipeline failed.
- Pipeline logs help identify and debug errors.
- CI/CD failures are normal and should be debugged step by step.

---

## Final Status

The GitHub Actions workflow was created, executed, intentionally failed, debugged, fixed, and verified successfully.

This project marks my first hands-on CI pipeline using GitHub Actions.

---

## Tags

`GitHub Actions` `CI/CD` `DevOps` `YAML` `Automation` `90DaysOfDevOps`
