# Day 48 – GitHub Actions Project: End-to-End CI/CD Pipeline

## Task Overview

Day 48 was the GitHub Actions capstone project.

The goal was to build a complete production-style CI/CD pipeline using everything learned from Day 40 to Day 47:

- GitHub Actions workflow basics
- Pull request triggers
- Push triggers
- Reusable workflows
- Docker image build and push
- GitHub secrets
- Scheduled workflows
- Deployment environments
- Security scanning with Trivy

This project connects all major CI/CD concepts into one end-to-end pipeline.

---

## Project Repository

Repository name:

```text
github-actions-capstone
```

Application used:

```text
Python Flask health check app
```

Main endpoint:

```text
/health
```

Docker image:

```text
cloudwithpreetham/github-actions-capstone
```

---

## Project Structure

```text
github-actions-capstone/
├── .github/
│   └── workflows/
│       ├── reusable-build-test.yml
│       ├── reusable-docker.yml
│       ├── pr-pipeline.yml
│       ├── main-pipeline.yml
│       └── health-check.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── pytest.ini
├── requirements.txt
├── README.md
└── 2026/
    └── day-48/
        └── day-48-actions-project.md
```

---

## Application Overview

The application is a simple Python Flask app with a health check endpoint.

### `app/main.py`

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "GitHub Actions Capstone App",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Test File

### `tests/test_app.py`

```python
from app.main import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
```

---

## Pytest Configuration

### `pytest.ini`

```ini
[pytest]
pythonpath = .
testpaths = tests
```

This file was added because pytest initially failed with:

```text
ModuleNotFoundError: No module named 'app'
```

Adding `pytest.ini` and `app/__init__.py` made the Flask app importable during test execution.

---

## Dockerfile

```dockerfile
FROM python:3.12.13-slim-bookworm

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 5000

CMD ["python", "app/main.py"]
```

The Debian package upgrade step was added after Trivy detected critical vulnerabilities in the base image.

---

## Requirements

### `requirements.txt`

```text
flask==3.0.3
pytest==8.3.2
```

---

## Pipeline Architecture

```text
Pull Request opened or updated
        |
        v
Reusable Build and Test Workflow
        |
        v
PR Checks Pass


Push or merge to main
        |
        v
Reusable Build and Test Workflow
        |
        v
Prepare short commit SHA
        |
        v
Docker build and push with SHA tag
        |
        v
Docker build and push with latest tag
        |
        v
Trivy security scan
        |
        v
Deploy to production


Every 12 hours or manual trigger
        |
        v
Pull latest Docker image
        |
        v
Run container
        |
        v
Curl /health endpoint
        |
        v
Publish health check summary
```

---

## Workflow Files

This project uses five GitHub Actions workflow files.

---

## 1. Reusable Build and Test Workflow

File:

```text
.github/workflows/reusable-build-test.yml
```

Purpose:

This workflow installs dependencies and runs tests. It is reusable and can be called by other workflows.

Key features:

- Uses `workflow_call`
- Accepts Python version as input
- Accepts `run_tests` as a boolean input
- Runs pytest
- Outputs test result

### Workflow

```yaml
name: Reusable Build and Test

on:
  workflow_call:
    inputs:
      python_version:
        description: "Python version to use"
        required: false
        default: "3.12"
        type: string
      run_tests:
        description: "Whether to run tests"
        required: false
        default: true
        type: boolean
    outputs:
      test_result:
        description: "Result of the test job"
        value: ${{ jobs.build-test.outputs.test_result }}

jobs:
  build-test:
    runs-on: ubuntu-latest

    outputs:
      test_result: ${{ steps.set-result.outputs.test_result }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python_version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        id: tests
        if: ${{ inputs.run_tests }}
        continue-on-error: true
        run: |
          pytest -v

      - name: Set test result
        id: set-result
        run: |
          if [ "${{ inputs.run_tests }}" = "false" ]; then
            echo "test_result=skipped" >> "$GITHUB_OUTPUT"
          elif [ "${{ steps.tests.outcome }}" = "success" ]; then
            echo "test_result=passed" >> "$GITHUB_OUTPUT"
          else
            echo "test_result=failed" >> "$GITHUB_OUTPUT"
            exit 1
          fi
```

---

## 2. Reusable Docker Build and Push Workflow

File:

```text
.github/workflows/reusable-docker.yml
```

Purpose:

This reusable workflow logs in to Docker Hub, builds the Docker image, pushes it, and outputs the full image URL.

Key features:

- Uses `workflow_call`
- Accepts Docker username as input
- Accepts Docker image name and tag as inputs
- Uses Docker Hub token as a secret
- Outputs `image_url`

### Workflow

```yaml
name: Reusable Docker Build and Push

on:
  workflow_call:
    inputs:
      docker_username:
        description: "Docker Hub username"
        required: true
        type: string
      image_name:
        description: "Docker image name"
        required: true
        type: string
      tag:
        description: "Docker image tag"
        required: true
        type: string

    secrets:
      docker_token:
        required: true

    outputs:
      image_url:
        description: "Full Docker image URL"
        value: ${{ jobs.docker.outputs.image_url }}

jobs:
  docker:
    runs-on: ubuntu-latest

    outputs:
      image_url: ${{ steps.image-info.outputs.image_url }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Validate Docker inputs
        run: |
          if [ -z "${{ inputs.docker_username }}" ]; then
            echo "docker_username input is missing"
            exit 1
          fi

          if [ -z "${{ secrets.docker_token }}" ]; then
            echo "docker_token secret is missing"
            exit 1
          fi

          echo "Docker inputs are available"

      - name: Log in to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ inputs.docker_username }}
          password: ${{ secrets.docker_token }}

      - name: Build and push Docker image
        run: |
          IMAGE_URL="${{ inputs.docker_username }}/${{ inputs.image_name }}:${{ inputs.tag }}"
          echo "Building image: $IMAGE_URL"
          docker build -t "$IMAGE_URL" .
          docker push "$IMAGE_URL"

      - name: Set image URL output
        id: image-info
        run: |
          IMAGE_URL="${{ inputs.docker_username }}/${{ inputs.image_name }}:${{ inputs.tag }}"
          echo "image_url=$IMAGE_URL" >> "$GITHUB_OUTPUT"
```

---

## 3. Pull Request Pipeline

File:

```text
.github/workflows/pr-pipeline.yml
```

Purpose:

The PR pipeline validates pull requests before merging to `main`.

It runs tests only and does not build or push Docker images.

### Workflow

```yaml
name: PR Pipeline

on:
  pull_request:
    branches:
      - main
    types:
      - opened
      - synchronize

jobs:
  build-test:
    uses: ./.github/workflows/reusable-build-test.yml
    with:
      python_version: "3.12"
      run_tests: true

  pr-comment:
    runs-on: ubuntu-latest
    needs: build-test

    steps:
      - name: Print PR summary
        run: |
          echo "PR checks passed for branch: ${{ github.head_ref }}"
          echo "Test result: ${{ needs.build-test.outputs.test_result }}"
```

---

## 4. Main Branch Pipeline

File:

```text
.github/workflows/main-pipeline.yml
```

Purpose:

The main pipeline performs the complete CI/CD process after code is pushed or merged into `main`.

Pipeline stages:

1. Build and test
2. Prepare short SHA
3. Build and push Docker image with SHA tag
4. Build and push Docker image with latest tag
5. Run Trivy vulnerability scan
6. Deploy to production

### Workflow

```yaml
name: Main Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-test:
    uses: ./.github/workflows/reusable-build-test.yml
    with:
      python_version: "3.12"
      run_tests: true

  prepare:
    runs-on: ubuntu-latest
    needs: build-test

    outputs:
      short_sha: ${{ steps.vars.outputs.short_sha }}

    steps:
      - name: Create short SHA
        id: vars
        run: |
          echo "short_sha=$(echo ${{ github.sha }} | cut -c1-7)" >> "$GITHUB_OUTPUT"

  docker-latest:
    needs: prepare
    uses: ./.github/workflows/reusable-docker.yml
    with:
      docker_username: ${{ vars.DOCKER_USERNAME }}
      image_name: github-actions-capstone
      tag: latest
    secrets:
      docker_token: ${{ secrets.DOCKER_TOKEN }}

  docker-sha:
    needs: prepare
    uses: ./.github/workflows/reusable-docker.yml
    with:
      docker_username: ${{ vars.DOCKER_USERNAME }}
      image_name: github-actions-capstone
      tag: sha-${{ needs.prepare.outputs.short_sha }}
    secrets:
      docker_token: ${{ secrets.DOCKER_TOKEN }}

  security-scan:
    runs-on: ubuntu-latest
    needs:
      - prepare
      - docker-sha

    steps:
      - name: Validate image URL
        run: |
          echo "Image to scan: ${{ needs.docker-sha.outputs.image_url }}"

          if [ -z "${{ needs.docker-sha.outputs.image_url }}" ]; then
            echo "image_url output is empty"
            exit 1
          fi

      - name: Run Trivy vulnerability scan
        uses: aquasecurity/trivy-action@v0.36.0
        with:
          image-ref: ${{ needs.docker-sha.outputs.image_url }}
          format: table
          severity: CRITICAL
          exit-code: 1
          ignore-unfixed: true
          output: trivy-report.txt

      - name: Print Trivy report
        if: always()
        run: |
          cat trivy-report.txt

      - name: Upload Trivy scan report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: trivy-scan-report
          path: trivy-report.txt

  deploy:
    runs-on: ubuntu-latest
    needs:
      - docker-latest
      - docker-sha
      - security-scan

    environment: production

    steps:
      - name: Deploy to production
        run: |
          echo "Deploying image: ${{ needs.docker-sha.outputs.image_url }} to production"
          echo "Deployment completed successfully"
```

---

## 5. Scheduled Health Check Workflow

File:

```text
.github/workflows/health-check.yml
```

Purpose:

This workflow runs every 12 hours and checks whether the latest Docker image starts successfully and responds on the `/health` endpoint.

### Workflow

```yaml
name: Scheduled Health Check

on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:

jobs:
  health-check:
    runs-on: ubuntu-latest

    steps:
      - name: Pull latest Docker image
        run: |
          docker pull ${{ vars.DOCKER_USERNAME }}/github-actions-capstone:latest

      - name: Run container
        run: |
          docker run -d --name capstone-health-check -p 5000:5000 \
            ${{ vars.DOCKER_USERNAME }}/github-actions-capstone:latest

      - name: Wait for app startup
        run: |
          sleep 5

      - name: Check health endpoint
        id: health
        continue-on-error: true
        run: |
          curl -f http://localhost:5000/health

      - name: Create health check summary
        run: |
          echo "## Health Check Report" >> "$GITHUB_STEP_SUMMARY"
          echo "- Image: ${{ vars.DOCKER_USERNAME }}/github-actions-capstone:latest" >> "$GITHUB_STEP_SUMMARY"

          if [ "${{ steps.health.outcome }}" = "success" ]; then
            echo "- Status: PASSED" >> "$GITHUB_STEP_SUMMARY"
          else
            echo "- Status: FAILED" >> "$GITHUB_STEP_SUMMARY"
          fi

          echo "- Time: $(date)" >> "$GITHUB_STEP_SUMMARY"

      - name: Stop and remove container
        if: always()
        run: |
          docker stop capstone-health-check || true
          docker rm capstone-health-check || true

      - name: Fail job if health check failed
        if: ${{ steps.health.outcome != 'success' }}
        run: |
          echo "Health check failed"
          exit 1
```

---

## GitHub Secrets and Variables

### Repository Secret

```text
DOCKER_TOKEN
```

Used for Docker Hub authentication.

### Repository Variable

```text
DOCKER_USERNAME
```

Used for Docker image naming and Docker Hub username.

The Docker username was moved to a repository variable because it is not sensitive. This also helped avoid issues with GitHub masking reusable workflow outputs that were built from secret values.

---

## Debugging Issues Faced

### Issue 1: Pytest Import Error

Error:

```text
ModuleNotFoundError: No module named 'app'
```

Root cause:

Pytest could not import the Flask app from the `app/` directory.

Fix:

- Added `app/__init__.py`
- Added `pytest.ini`

Result:

```text
Tests passed successfully
```

---

### Issue 2: Docker Hub Login Failed

Error:

```text
Error: Username and password required
```

Root cause:

Docker credentials were not correctly available inside the reusable workflow.

Fix:

- Used Docker Hub token as a GitHub secret
- Used Docker username as a GitHub variable
- Passed required values correctly into reusable workflow

Result:

```text
Docker login succeeded
Docker image build and push succeeded
```

---

### Issue 3: Trivy Image Reference Empty

Error:

```text
could not parse reference:
```

Root cause:

The Docker image URL output was empty when passed to the Trivy scan job.

Fix:

- Changed Docker username from secret to variable
- Passed Docker username as a workflow input
- Generated `image_url` output from non-secret input values

Result:

```text
Trivy received the correct Docker image reference
```

---

### Issue 4: Trivy Found Critical Vulnerabilities

Trivy detected 2 critical vulnerabilities in:

```text
libgnutls30
```

Installed version:

```text
3.7.9-2+deb12u6
```

Fixed version:

```text
3.7.9-2+deb12u7
```

Fix:

Updated Debian packages during the Docker build:

```dockerfile
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

Result:

```text
Security scan passed successfully
```

---

## Final Main Pipeline Result

The final main branch pipeline completed successfully.

Completed stages:

```text
build-test      passed
prepare         passed
docker-sha      passed
docker-latest   passed
security-scan   passed
deploy          passed
```

Final pipeline flow:

```text
Push to main
   → Run tests
   → Prepare short SHA
   → Build and push Docker image with SHA tag
   → Build and push Docker image with latest tag
   → Run Trivy security scan
   → Deploy to production
```

---

## Screenshots

### Main Pipeline Success

Add screenshot here:

```markdown
![Main pipeline success](../../screenshots/day-48-main-pipeline-success.png)
```

### Trivy Scan Report

Add screenshot here:

```markdown
![Trivy scan report](../../screenshots/day-48-trivy-report.png)
```

### Docker Hub Image

Add screenshot here:

```markdown
![Docker Hub image](../../screenshots/day-48-dockerhub-image.png)
```

---

## Docker Hub Image

Docker Hub repository:

```text
https://hub.docker.com/r/cloudwithpreetham/github-actions-capstone
```

Tags pushed:

```text
latest
sha-<short-commit-hash>
```

Example SHA tag:

```text
sha-515c7b6
```

---

## What I Learned

From this capstone project, I learned:

1. How to design a production-style GitHub Actions CI/CD pipeline.
2. How to use reusable workflows to avoid repeating build and Docker logic.
3. How to separate PR validation from main branch deployment.
4. How to use GitHub secrets and variables correctly.
5. How to build and push Docker images automatically.
6. How to tag Docker images using both `latest` and commit SHA.
7. How to scan Docker images with Trivy.
8. How to debug CI/CD pipeline failures from logs.
9. How to fix container image vulnerabilities by updating base image packages.
10. How to use GitHub environments for production deployment simulation.

---

## What I Would Improve Next

Future improvements:

- Add staging and production environments
- Add Slack or Discord deployment notifications
- Add rollback workflow
- Add Kubernetes deployment
- Add AWS ECS or EKS deployment
- Add image signing using Cosign
- Add SBOM generation
- Add branch protection rules
- Add required status checks before merge
- Add deployment approval rules for production
- Add monitoring after deployment

---

## Final Status

```text
[✓] Flask app created
[✓] Health endpoint added
[✓] Pytest configured
[✓] Dockerfile created
[✓] Docker image builds successfully
[✓] Reusable build-test workflow created
[✓] Reusable Docker workflow created
[✓] PR pipeline created
[✓] Main CI/CD pipeline created
[✓] Scheduled health check workflow created
[✓] Docker Hub push working
[✓] Trivy security scan working
[✓] Vulnerability fixed
[✓] Production deploy job successful
```

---

## Summary

Day 48 completed a full end-to-end CI/CD pipeline using GitHub Actions.

This project is a strong DevOps portfolio item because it demonstrates:

- CI
- CD
- Docker automation
- Reusable workflows
- Security scanning
- Debugging real pipeline failures
- Production-style deployment flow

Final result:

```text
Code change → Test → Build Docker image → Push image → Scan image → Deploy
```
