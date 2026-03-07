# GitHub Actions Practice – Day 43

## Jobs, Steps, Environment Variables & Conditionals

This project is part of my **90 Days of DevOps** learning journey.

On Day 43, I practiced how to control the flow of a GitHub Actions pipeline using multiple jobs, job dependencies, environment variables, job outputs, and conditional execution.

---

## Project Overview

In real-world DevOps pipelines, jobs do not always run in a simple straight line.

A production CI/CD pipeline may need to:

- Build the application first
- Run tests only after the build succeeds
- Deploy only after tests pass
- Run some jobs only on the `main` branch
- Skip some jobs for pull requests
- Pass values between jobs
- Run independent jobs in parallel
- Print a final pipeline summary

This project demonstrates those concepts using GitHub Actions workflow files.

---

## Repository Structure

```text
github-actions-practice/
│
├── .github/
│   └── workflows/
│       ├── multi-job.yml
│       ├── env-vars.yml
│       ├── job-outputs.yml
│       ├── conditionals.yml
│       └── smart-pipeline.yml
│
├── 2026/
│   └── day-43/
│       └── day-43-jobs-steps.md
│
└── README.md
```

---

## Workflows Created

## 1. Multi-Job Workflow

File:

```text
.github/workflows/multi-job.yml
```

This workflow demonstrates job dependencies.

Jobs created:

```text
build → test → deploy
```

The `build` job runs first.

The `test` job runs only after `build` succeeds.

The `deploy` job runs only after `test` succeeds.

Key concept used:

```yaml
needs: build
```

and:

```yaml
needs: test
```

![Multi-job workflow graph](screenshots/01-multi-job-workflow-graph.png)

---

## 2. Environment Variables Demo

File:

```text
.github/workflows/env-vars.yml
```

This workflow demonstrates environment variables at three levels:

- Workflow level
- Job level
- Step level

Environment variables used:

```yaml
APP_NAME: myapp
ENVIRONMENT: staging
VERSION: 1.0.0
```

It also prints GitHub context values:

```yaml
${{ github.sha }}
${{ github.actor }}
```

These values show:

- The commit SHA that triggered the workflow
- The GitHub user who triggered the workflow

![Environment variables output](screenshots/02-env-vars-output.png)

---

## 3. Job Outputs Demo

File:

```text
.github/workflows/job-outputs.yml
```

This workflow demonstrates how to pass data from one job to another.

The first job generates the current date:

```bash
echo "today=$(date)" >> $GITHUB_OUTPUT
```

The second job reads the output using:

```yaml
${{ needs.generate-date.outputs.today }}
```

This is useful in real pipelines when passing:

- Docker image tags
- Build versions
- Release numbers
- Artifact names
- Deployment URLs
- Test summaries

![Job outputs result](screenshots/03-job-outputs-result.png)

---

## 4. Conditionals Demo

File:

```text
.github/workflows/conditionals.yml
```

This workflow demonstrates conditional execution.

Concepts practiced:

```yaml
if: github.event_name == 'push'
```

Runs the job only on push events.

```yaml
if: github.ref == 'refs/heads/main'
```

Runs the step only on the `main` branch.

```yaml
if: failure()
```

Runs a step only when a previous step fails.

```yaml
continue-on-error: true
```

Allows the workflow to continue even when a step fails.

![Conditionals workflow run](screenshots/04-conditionals-workflow.png)

---

## 5. Smart Pipeline

File:

```text
.github/workflows/smart-pipeline.yml
```

This workflow combines multiple concepts into one pipeline.

Jobs created:

```text
lint
test
summary
```

The `lint` and `test` jobs run in parallel.

The `summary` job waits for both jobs using:

```yaml
needs: [lint, test]
```

Pipeline flow:

```text
lint ┐
     ├── summary
test ┘
```

The summary job prints:

- Whether the push is from `main` or a feature branch
- The commit message

![Smart pipeline workflow graph](screenshots/05-smart-pipeline-graph.png)

---

## Key GitHub Actions Concepts Learned

## `needs:`

The `needs:` keyword creates job dependencies.

Example:

```yaml
needs: build
```

This means the current job waits for the `build` job to finish successfully before starting.

Without `needs:`, jobs run in parallel by default.

---

## `env:`

The `env:` keyword is used to define environment variables.

Environment variables can be defined at:

- Workflow level
- Job level
- Step level

Example:

```yaml
env:
  APP_NAME: myapp
```

---

## `outputs:`

The `outputs:` keyword allows one job to expose values to other jobs.

Example:

```yaml
outputs:
  today: ${{ steps.date-step.outputs.today }}
```

Another job can read the value using:

```yaml
${{ needs.generate-date.outputs.today }}
```

---

## `if:`

The `if:` keyword controls whether a job or step should run.

Example:

```yaml
if: github.ref == 'refs/heads/main'
```

This runs only when the workflow is triggered from the `main` branch.

---

## `continue-on-error`

The `continue-on-error` option allows a step to fail without stopping the entire workflow.

Example:

```yaml
continue-on-error: true
```

This is useful for optional checks, experimental jobs, or non-blocking validations.

---

## Verification Checklist

- [x] Created a multi-job workflow
- [x] Verified `build → test → deploy` dependency chain
- [x] Used workflow-level environment variables
- [x] Used job-level environment variables
- [x] Used step-level environment variables
- [x] Printed GitHub SHA
- [x] Printed GitHub actor
- [x] Created job outputs
- [x] Passed data between jobs
- [x] Used branch-based conditionals
- [x] Used event-based conditionals
- [x] Tested `continue-on-error`
- [x] Created a smart pipeline
- [x] Ran `lint` and `test` jobs in parallel
- [x] Created a final `summary` job

---

## Real-World DevOps Use Cases

These concepts are used in real CI/CD pipelines to:

- Run builds before tests
- Deploy only after all checks pass
- Deploy only from the `main` branch
- Skip production jobs for pull requests
- Pass Docker image tags between jobs
- Generate release versions
- Run independent jobs in parallel
- Create final pipeline summaries
- Make pipelines safer and more controlled

---

## Learning Outcome

After completing this task, I understand how GitHub Actions workflows can be structured like real CI/CD pipelines.

I learned that jobs run in parallel by default and that `needs:` is used to control job order.

I also practiced passing data between jobs, using environment variables, and controlling workflow behavior with conditionals.

This is an important step toward building production-ready CI/CD pipelines as a DevOps engineer.

---

## Author

**Preetham**

Part of my **90 Days of DevOps** journey.

---

## Tags

```text
#90DaysOfDevOps
#DevOpsKaJosh
#TrainWithShubham
#GitHubActions
#DevOps
#CICD
```
