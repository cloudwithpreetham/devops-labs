# GitHub Actions Practice – Day 46

## Reusable Workflows & Composite Actions

This repository contains my Day 46 work from the **90 Days of DevOps** challenge.

The focus of this day was to learn how to avoid repeating GitHub Actions workflow logic by using **reusable workflows** and **custom composite actions**.

In real DevOps teams, CI/CD workflows are often standardized and reused across multiple projects. This improves consistency, reduces duplication, and makes pipelines easier to maintain.

---

## What I Built

For Day 46, I created:

- A reusable GitHub Actions workflow using `workflow_call`
- A caller workflow that triggers the reusable workflow
- Workflow inputs, secrets, and outputs
- A custom composite action
- A workflow that uses the composite action
- Documentation explaining the difference between reusable workflows and composite actions

---

## Project Structure

```bash
day-46/
├── github-actions-practice/
│   └── .github/
│       ├── actions/
│       │   └── setup-and-greet/
│       │       └── action.yml
│       └── workflows/
│           ├── call-build.yml
│           ├── composite-action-demo.yml
│           └── reusable-build.yml
├── screenshots/
│   ├── day-46-build-version-output.png
│   ├── day-46-call-build-success.png
│   ├── day-46-composite-action-success.png
│   ├── day-46-reusable-workflow-logs.png
│   └── day-46-workflow-files.png
├── day-46-reusable-workflows.md
├── README.md
└── task.md
```

![Workflow files](screenshots/day-46-workflow-files.png)

---

## Workflows Created

### 1. Reusable Build Workflow

File:

```bash
github-actions-practice/.github/workflows/reusable-build.yml
```

This workflow is triggered using:

```yaml
on:
  workflow_call:
```

It accepts:

| Type   | Name            | Purpose                      |
| ------ | --------------- | ---------------------------- |
| Input  | `app_name`      | Application name             |
| Input  | `environment`   | Target environment           |
| Secret | `docker_token`  | Docker token passed securely |
| Output | `build_version` | Generated build version      |

The workflow prints build details and generates a version using the short commit SHA.

Example output:

```bash
Building my-web-app for production
Docker token is set: true
Generated build version: v1.0-df5892f
```

---

### 2. Caller Workflow

File:

```bash
github-actions-practice/.github/workflows/call-build.yml
```

This workflow runs on push to the `main` branch and calls the reusable workflow.

```yaml
jobs:
  build:
    uses: ./.github/workflows/reusable-build.yml
    with:
      app_name: "my-web-app"
      environment: "production"
    secrets:
      docker_token: ${{ secrets.DOCKER_TOKEN }}
```

It also includes a second job that reads and prints the reusable workflow output:

```bash
Build version from reusable workflow: v1.0-df5892f
```

![Caller workflow success](screenshots/day-46-call-build-success.png)

![Reusable workflow logs](screenshots/day-46-reusable-workflow-logs.png)

![Build version output](screenshots/day-46-build-version-output.png)

---

### 3. Composite Action

File:

```bash
github-actions-practice/.github/actions/setup-and-greet/action.yml
```

This custom composite action:

- Accepts a `name` input
- Accepts a `language` input
- Prints a greeting
- Prints the current date
- Prints the runner operating system
- Sets an output called `greeted`

Example output:

```bash
Hello, Preetham!
Current date: <date>
Runner OS: Linux
Greeting completed: true
```

![Composite action success](screenshots/day-46-composite-action-success.png)

---

### 4. Composite Action Demo Workflow

File:

```bash
github-actions-practice/.github/workflows/composite-action-demo.yml
```

This workflow runs the custom composite action using:

```yaml
uses: ./.github/actions/setup-and-greet
```

It verifies that the local composite action can be reused inside a GitHub Actions workflow.

---

## Reusable Workflow vs Composite Action

|                              | Reusable Workflow                        | Composite Action                                             |
| ---------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| Triggered by                 | `workflow_call`                          | `uses:` in a step                                            |
| Can contain jobs?            | Yes                                      | No                                                           |
| Can contain multiple steps?  | Yes                                      | Yes                                                          |
| Lives where?                 | `.github/workflows/`                     | Commonly `.github/actions/<action-name>/`                    |
| Can accept secrets directly? | Yes                                      | No, secrets must be passed through workflow/job/step context |
| Best for                     | Reusing complete CI/CD jobs or pipelines | Reusing repeated step logic                                  |

---

## Verification

Both workflows completed successfully.

### Caller Workflow

```bash
Status: Success
Jobs:
- build / build
- print-version
```

### Composite Action Workflow

```bash
Status: Success
Job:
- greet
```

This confirms:

- The reusable workflow was called successfully
- Inputs were passed correctly
- Secrets were passed securely
- Outputs were returned to the caller workflow
- The composite action ran successfully

---

## Key Learnings

- Reusable workflows help avoid duplicate CI/CD logic.
- `workflow_call` allows one workflow to call another workflow.
- Reusable workflows are called at the job level.
- Composite actions are called inside workflow steps.
- Reusable workflows can contain full jobs.
- Composite actions can only contain steps.
- Secrets should never be printed directly in logs.
- Outputs can be passed from reusable workflows back to caller workflows.
- These patterns are useful in real-world DevOps teams.

---

## Real-World Use Cases

Reusable workflows are useful for:

- Docker image builds
- Test pipelines
- Security scans
- Deployment workflows
- Release workflows
- Environment promotion workflows

Composite actions are useful for:

- Repeated setup commands
- Tool installation
- Metadata printing
- Common validation steps
- Shared shell command logic

---

## Final Status

Day 46 completed successfully.

This task helped me understand how production teams keep GitHub Actions workflows clean, reusable, and maintainable.

---

## Challenge

**90 Days of DevOps**

Hashtags:

```text
#90DaysOfDevOps
#DevOpsKaJosh
#TrainWithShubham
```
