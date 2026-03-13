# GitHub Actions – CI/CD Learning Journey

This directory contains my hands-on GitHub Actions practice as part of my **90 Days of DevOps** learning journey.

The main goal of this section is to understand how CI/CD pipelines work in real DevOps environments by practicing workflow automation, pipeline triggers, runners, secrets, artifacts, Docker image publishing, reusable workflows, debugging, and a final capstone pipeline.

---

## Folder Structure

```bash
08-ci-cd/
└── github-actions/
    ├── day-38/
    ├── day-39/
    ├── day-40/
    ├── day-41/
    ├── day-42/
    ├── day-43/
    ├── day-44/
    ├── day-45/
    ├── day-46/
    ├── day-47/
    ├── day-48/
    └── day-49/
```

---

## Learning Timeline

| Day    | Topic                                           | Focus                                                                                            |
| ------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Day 38 | YAML Basics                                     | Learned YAML syntax, indentation, lists, dictionaries, and configuration structure               |
| Day 39 | CI/CD Concepts                                  | Understood Continuous Integration, Continuous Delivery, Continuous Deployment, and pipeline flow |
| Day 40 | First GitHub Actions Workflow                   | Created and executed the first GitHub Actions workflow                                           |
| Day 41 | Triggers & Matrix Builds                        | Practiced push, pull request, schedule, manual triggers, and matrix strategy                     |
| Day 42 | GitHub-Hosted & Self-Hosted Runners             | Learned how jobs run on GitHub-hosted and self-hosted runners                                    |
| Day 43 | Jobs, Steps, Environment Variables & Conditions | Built multi-job workflows with dependencies, env variables, and conditions                       |
| Day 44 | Secrets, Artifacts & Real Tests                 | Used GitHub secrets, uploaded artifacts, and ran automated tests                                 |
| Day 45 | Docker Build & Push                             | Built Docker images and pushed them to Docker Hub using GitHub Actions                           |
| Day 46 | Reusable Workflows & Composite Actions          | Created reusable workflows and custom composite actions                                          |
| Day 47 | Advanced Triggers                               | Practiced PR lifecycle events, cron schedules, and workflow chaining                             |
| Day 48 | GitHub Actions Debugging                        | Debugged test failures, import errors, and broken CI pipelines                                   |
| Day 49 | CI/CD Capstone Pipeline                         | Built a production-style CI/CD pipeline using reusable workflows and Docker                      |

---

## What I Practiced

- Writing GitHub Actions workflow files from scratch
- Understanding workflow structure:
  - `name`
  - `on`
  - `jobs`
  - `steps`
  - `runs-on`

- Triggering workflows using:
  - `push`
  - `pull_request`
  - `workflow_dispatch`
  - `schedule`
  - `workflow_run`

- Creating multi-job pipelines
- Controlling job execution using `needs`
- Using GitHub-hosted runners
- Setting up and testing a self-hosted runner
- Working with environment variables
- Using GitHub repository variables
- Handling secrets securely
- Uploading and downloading workflow artifacts
- Running automated tests in CI
- Building Docker images in GitHub Actions
- Pushing Docker images to Docker Hub
- Creating reusable workflows using `workflow_call`
- Creating custom composite actions
- Debugging failed workflows
- Building a complete CI/CD capstone project

---

## Tools Used

- GitHub
- GitHub Actions
- YAML
- Git
- Linux
- Docker
- Docker Hub
- Python
- Pytest
- Self-hosted runner

---

## Example Workflow

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest -v
```

---

## Key Concepts Learned

### CI/CD

CI/CD helps automate the process of testing, building, and delivering applications. It reduces manual work, improves reliability, and helps teams ship changes faster.

### GitHub Actions

GitHub Actions is a CI/CD platform built into GitHub. It allows workflows to run automatically when events happen in a repository.

### Workflow

A workflow is an automation file written in YAML. It defines when the pipeline runs and what jobs should be executed.

### Job

A job is a group of steps that runs on a runner. Jobs can run independently or depend on other jobs.

### Step

A step is a single command or action inside a job.

### Runner

A runner is the machine where the workflow job executes. It can be GitHub-hosted or self-hosted.

### Secrets

Secrets are used to store sensitive values like tokens, passwords, and API keys safely.

### Artifacts

Artifacts are files generated by a workflow that can be uploaded and downloaded after a workflow run.

### Reusable Workflows

Reusable workflows help avoid repeating the same pipeline logic in multiple workflow files.

---

## Real-World DevOps Takeaways

- CI/CD pipelines help reduce manual deployment mistakes.
- Every code change should be tested automatically.
- Secrets should never be hardcoded in repositories.
- Reusable workflows make pipelines easier to maintain.
- Docker-based CI/CD is commonly used in production.
- Workflow debugging is an important DevOps skill.
- Small, consistent improvements build strong automation habits.

---

## Final Outcome

By completing Days 38 to 49, I built a strong foundation in GitHub Actions and CI/CD automation.

This section helped me understand how DevOps teams automate testing, building, packaging, and shipping applications using production-style pipelines.

---

## Status

```bash
Section: CI/CD
Platform: GitHub Actions
Progress: Day 38 to Day 49 completed
Focus: Pipeline automation and real-world CI/CD practices
```

---

## Author

**Preetham**
DevOps Learner | 90 Days of DevOps Journey
