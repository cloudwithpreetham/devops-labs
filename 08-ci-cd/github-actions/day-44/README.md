# GitHub Actions Practice

This repository contains my hands-on GitHub Actions practice as part of my 90 Days of DevOps journey.

The goal of this repository is to learn CI/CD step by step by creating real workflows, testing automation concepts, and understanding how pipelines are used in real DevOps projects.

---

## Repository Purpose

This repository is focused on learning GitHub Actions through practical tasks.

Topics covered include:

- GitHub Actions workflow basics
- Workflow triggers
- Jobs and steps
- Environment variables
- Conditional execution
- GitHub-hosted runners
- Self-hosted runners
- Secrets management
- Artifacts
- Multi-job pipelines
- Running real tests in CI
- Dependency caching

---

## Current Progress

### Day 40 – First GitHub Actions Workflow

Created the first GitHub Actions workflow that runs on every push.

Key learnings:

- Workflow file structure
- `on: push` trigger
- Jobs and steps
- Running shell commands in GitHub Actions
- Viewing workflow logs in the Actions tab

---

### Day 41 – Triggers & Matrix Builds

Practiced different ways to trigger workflows.

Key learnings:

- Pull request triggers
- Scheduled workflows
- Manual workflow dispatch
- Matrix builds
- Running jobs across multiple environments

---

### Day 42 – GitHub-Hosted & Self-Hosted Runners

Learned how GitHub Actions jobs run on runners.

Key learnings:

- GitHub-hosted runners
- Self-hosted runner setup
- Runner registration
- Running workflows on custom machines
- Understanding runner lifecycle

---

### Day 43 – Jobs, Steps, Environment Variables & Conditionals

Practiced controlling workflow execution.

Key learnings:

- Multi-job workflows
- Job dependencies using `needs`
- Environment variables
- Step-level conditions
- Conditional execution with `if`
- Passing data between steps and jobs

---

### Day 44 – Secrets, Artifacts & Running Real Tests in CI

Built more practical CI workflows using secrets, artifacts, real tests, and caching.

Key learnings:

- Creating GitHub repository secrets
- Using secrets safely in workflows
- GitHub secret masking in logs
- Uploading workflow artifacts
- Downloading artifacts from GitHub Actions
- Sharing artifacts between jobs
- Running Python tests using `pytest`
- Verifying failed and passing CI runs
- Caching Python dependencies using `actions/cache`

---

## Project Structure

```text
day-44/
├── github-actions-practice/
│   └── .github/
│       └── workflows/
│           ├── artifact-between-jobs.yml
│           ├── python-tests-cache.yml
│           ├── python-tests.yml
│           ├── secrets-demo.yml
│           └── upload-artifact-demo.yml
├── screenshots/
│   ├── day-44-artifact-between-jobs.png
│   ├── day-44-artifact-download.png
│   ├── day-44-artifact-upload.png
│   ├── day-44-cache-restored.png
│   ├── day-44-secret-masked.png
│   ├── day-44-test-failed.png
│   └── day-44-test-passed.png
├── scripts/
│   ├── calculator.py
│   └── test_calculator.py
├── day-44-secrets-artifacts.md
├── README.md
└── task.md
```

---

## Workflows

### Secrets Demo

File:

```text
github-actions-practice/.github/workflows/secrets-demo.yml
```

Purpose:

- Reads GitHub repository secrets
- Confirms that secrets are configured
- Uses secrets as environment variables
- Verifies that GitHub masks secrets in logs

---

### Upload Artifact Demo

File:

```text
github-actions-practice/.github/workflows/upload-artifact-demo.yml
```

Purpose:

- Generates a test report file
- Uploads the report as a GitHub Actions artifact
- Makes the artifact downloadable from the Actions tab

---

### Artifact Between Jobs

File:

```text
github-actions-practice/.github/workflows/artifact-between-jobs.yml
```

Purpose:

- Generates an artifact in one job
- Downloads and uses the artifact in another job
- Demonstrates job-to-job file sharing

---

### Python Tests

File:

```text
github-actions-practice/.github/workflows/python-tests.yml
```

Purpose:

- Checks out the repository
- Sets up Python
- Installs `pytest`
- Runs automated Python tests
- Fails the pipeline when tests fail

---

### Python Tests With Cache

File:

```text
github-actions-practice/.github/workflows/python-tests-cache.yml
```

Purpose:

- Runs Python tests
- Caches pip dependencies
- Speeds up future workflow runs

---

## CI Test Example

The repository includes a simple Python calculator script:

```text
scripts/calculator.py
```

And a test file:

```text
scripts/test_calculator.py
```

The tests are run in CI using:

```bash
pytest scripts/
```

Expected result:

```text
2 passed
```

---

## Secrets Used

The following secrets were configured in GitHub Actions:

```text
MY_SECRET_MESSAGE
DOCKER_USERNAME
DOCKER_TOKEN
```

These secrets are not stored in the repository.

They are managed from:

```text
Repository Settings → Secrets and variables → Actions
```

---

## Important Security Notes

Secrets should never be hardcoded in workflow files or source code.

Secrets should also never be printed in CI logs.

GitHub masks secret values automatically, but the safest practice is to only check whether a secret exists and use it securely as an environment variable.

---

## Artifact Use Cases

Artifacts are useful in real-world CI/CD pipelines for storing:

- Test reports
- Build logs
- Compiled files
- Coverage reports
- Security scan reports
- Deployment packages

Artifacts help preserve important files generated during a workflow run.

---

## Caching Use Case

Caching helps reduce workflow execution time by reusing previously downloaded dependencies.

In this repository, pip dependencies are cached from:

```text
~/.cache/pip
```

This improves performance when running Python test workflows multiple times.

---

## Skills Practiced

- GitHub Actions
- CI/CD fundamentals
- YAML workflow syntax
- Secrets management
- Artifact upload and download
- Multi-job workflow design
- Python test automation
- Dependency caching
- Workflow debugging

---

## DevOps Learning Outcome

This repository helped me understand how real CI pipelines work.

Instead of only running simple commands, I practiced workflows that handle secrets, store outputs, share files between jobs, run tests, detect failures, and improve performance with caching.

These are important skills used in real DevOps and cloud engineering roles.

---

## Author

**Preetham**
DevOps Learner
GitHub: `cloud-with-preetham`
