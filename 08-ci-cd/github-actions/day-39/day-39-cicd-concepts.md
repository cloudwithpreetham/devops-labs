# Day 39 – What is CI/CD?

## Goal

The goal of this day is to understand why CI/CD exists before writing any pipeline YAML.

CI/CD is not just a tool. It is a software delivery practice that helps teams test, build, and release code in a safer, faster, and more repeatable way.

---

## Task 1: The Problem

### Scenario

A team of 5 developers is pushing code to the same repository and manually deploying the application to production.

### 1. What can go wrong?

Many things can go wrong in this setup:

- Developers may overwrite each other's changes.
- Bugs may reach production because code is not tested automatically.
- Manual deployment steps may be missed.
- One developer may deploy old code by mistake.
- The application may work on one laptop but fail on another server.
- Rollbacks become difficult if nobody tracks exactly what was deployed.
- The team may waste time debugging environment differences.
- Production deployments become stressful because the process depends on humans.

### 2. What does "it works on my machine" mean?

"It works on my machine" means the code runs correctly on a developer's local system but fails in another environment such as a teammate's laptop, staging, or production.

This is a real problem because local machines may have different:

- Operating systems
- Dependency versions
- Environment variables
- Database versions
- Configuration files
- Network settings
- Installed tools

CI/CD solves this by running the code in a clean and consistent environment every time.

### 3. How many times a day can a team safely deploy manually?

A team can deploy manually a few times a day only if the process is simple and well-documented.

In real projects, manual deployments are risky because every deployment depends on human memory and careful execution. As the application grows, manual deployment becomes slow, error-prone, and difficult to repeat.

With CI/CD, teams can deploy more frequently because testing, building, and deployment steps are automated.

---

## Task 2: CI vs CD vs CD

## Continuous Integration

Continuous Integration means developers frequently merge code changes into a shared repository. Every change is automatically tested and validated.

CI usually runs on every push or pull request. It catches problems like syntax errors, failed tests, broken builds, and dependency issues early.

### Real-world example

A developer pushes code to GitHub. GitHub Actions automatically installs dependencies, runs unit tests, checks code quality, and reports whether the change is safe to merge.

---

## Continuous Delivery

Continuous Delivery means the application is always kept in a deployable state. After code passes tests and build stages, it can be released to production with manual approval.

The main difference from CI is that Continuous Delivery prepares the release, but a human usually decides when to deploy.

### Real-world example

A team pushes code to the main branch. The pipeline runs tests, builds a Docker image, pushes it to Docker Hub, and prepares it for production. A release manager clicks "Deploy" when ready.

---

## Continuous Deployment

Continuous Deployment means every successful change is automatically deployed to production without manual approval.

This is used by teams with strong automated testing, monitoring, rollback systems, and confidence in their pipeline.

### Real-world example

A small web application team pushes a bug fix to the main branch. The pipeline tests the code, builds the Docker image, and automatically deploys it to production if all checks pass.

---

## Quick Comparison

| Practice               | What It Does                              | Human Approval Needed? |
| ---------------------- | ----------------------------------------- | ---------------------- |
| Continuous Integration | Tests and validates code changes          | No                     |
| Continuous Delivery    | Keeps code ready for release              | Yes                    |
| Continuous Deployment  | Automatically releases code to production | No                     |

---

## Task 3: Pipeline Anatomy

## Trigger

A trigger is the event that starts the pipeline.

Examples:

- Code push
- Pull request
- Manual button click
- Scheduled time
- Release tag creation

Example:

```yaml
on:
  push:
    branches:
      - main
```

---

## Stage

A stage is a logical phase in the pipeline.

Common stages:

- Build
- Test
- Security scan
- Package
- Deploy

Example:

```text
Build Stage -> Test Stage -> Deploy Stage
```

---

## Job

A job is a unit of work inside a pipeline stage. Jobs run on a runner.

Example jobs:

- Install dependencies
- Run tests
- Build Docker image
- Deploy to staging

---

## Step

A step is a single command or action inside a job.

Examples:

```bash
npm install
npm test
docker build -t myapp:latest .
```

---

## Runner

A runner is the machine that executes the pipeline job.

Examples:

- GitHub-hosted runner
- Self-hosted runner
- Linux runner
- Windows runner
- macOS runner

Example:

```yaml
runs-on: ubuntu-latest
```

---

## Artifact

An artifact is an output produced by a pipeline job.

Examples:

- Docker image
- Test report
- Build package
- Log file
- Compiled application
- Coverage report

Artifacts are useful because later stages can reuse them.

---

## Task 4: CI/CD Pipeline Diagram

Scenario:

A developer pushes code to GitHub. The app is tested, built into a Docker image, and deployed to a staging server.

```text
Developer
   |
   | git push
   v
GitHub Repository
   |
   | Trigger: push to main branch
   v
CI/CD Pipeline Starts
   |
   v
+----------------------+
| Stage 1: Test        |
|----------------------|
| - Checkout code      |
| - Install deps       |
| - Run unit tests     |
+----------------------+
   |
   | Tests passed
   v
+----------------------+
| Stage 2: Build       |
|----------------------|
| - Build Docker image |
| - Tag Docker image   |
| - Push to registry   |
+----------------------+
   |
   | Image pushed
   v
+----------------------+
| Stage 3: Deploy      |
|----------------------|
| - Connect to staging |
| - Pull new image     |
| - Restart container  |
+----------------------+
   |
   v
Staging Server Updated
```

### Simple Flow

```text
Push Code -> Run Tests -> Build Docker Image -> Push Image -> Deploy to Staging
```

---

## Task 5: Explore in the Wild

## Repository Chosen

I explored the FastAPI open-source GitHub repository.

FastAPI is a popular Python web framework used to build APIs.

## Workflow File Checked

```text
.github/workflows/test.yml
```

## What triggers it?

The workflow is triggered by:

- Pushes to the `master` branch
- Pull requests when they are opened or synchronized
- A weekly scheduled run using cron

## How many jobs does it have?

From the workflow file, I noticed at least these jobs:

- `changes`
- `test`

The `changes` job checks whether important source files changed.

The `test` job runs the test suite across different operating systems and Python versions.

## What does it do?

My best guess:

The workflow checks whether relevant files changed, sets up Python, installs dependencies, and runs FastAPI's test suite.

It also uses a matrix strategy to test different combinations of:

- Operating systems
- Python versions
- Dependency versions
- Test configurations

This helps maintainers catch bugs before changes are merged.

---

## Key Learnings

- CI/CD helps teams reduce manual mistakes.
- CI catches bugs early before code reaches production.
- Continuous Delivery prepares code for release.
- Continuous Deployment releases code automatically after all checks pass.
- A pipeline is made of triggers, stages, jobs, steps, runners, and artifacts.
- A failed pipeline is not a failure of DevOps. It is the pipeline protecting the application.

---

## Real-World DevOps Notes

In real DevOps teams:

- Every pull request should run tests automatically.
- Code should not be merged if the pipeline fails.
- Secrets should never be hard-coded in pipeline files.
- Docker images should be tagged properly.
- Production deployment should have rollback options.
- Monitoring should confirm whether deployment was successful.

---

## Final Summary

CI/CD is the automation backbone of modern software delivery.

Instead of manually testing, building, and deploying applications, teams use pipelines to make the process repeatable and reliable.

Today I learned that CI/CD is not just about tools like GitHub Actions, Jenkins, or GitLab CI. It is about building confidence in every code change before it reaches users.
