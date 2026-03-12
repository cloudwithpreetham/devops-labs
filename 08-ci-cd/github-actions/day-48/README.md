# GitHub Actions Capstone – End-to-End CI/CD Pipeline

This repository is part of my **90DaysOfDevOps** journey.

The goal of this project is to build a production-style CI/CD pipeline using **GitHub Actions**, **Docker**, **reusable workflows**, **Docker Hub**, **Trivy security scanning**, and a simulated production deployment.

This is the Day 48 GitHub Actions capstone project.

---

## Project Overview

This project contains a simple Python Flask application with a health check endpoint.

The application is tested, containerized, pushed to Docker Hub, scanned for vulnerabilities, and deployed through a GitHub Actions pipeline.

Pipeline flow:

```text
Code Push
   → Build and Test
   → Create Short SHA
   → Build Docker Image
   → Push Docker Image to Docker Hub
   → Run Trivy Security Scan
   → Deploy to Production
```

---

## Workflow Badges

![Main Pipeline](https://github.com/cloud-with-preetham/github-actions-capstone/actions/workflows/main-pipeline.yml/badge.svg)

![PR Pipeline](https://github.com/cloud-with-preetham/github-actions-capstone/actions/workflows/pr-pipeline.yml/badge.svg)

![Scheduled Health Check](https://github.com/cloud-with-preetham/github-actions-capstone/actions/workflows/health-check.yml/badge.svg)

---

## Tech Stack

- Python
- Flask
- Pytest
- Docker
- Docker Hub
- GitHub Actions
- Reusable Workflows
- Trivy
- GitHub Environments

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

## Application Endpoints

| Endpoint  | Method | Description                 |
| --------- | ------ | --------------------------- |
| `/`       | GET    | Returns application status  |
| `/health` | GET    | Returns health check status |

Example health response:

```json
{
  "status": "healthy"
}
```

---

## Run Locally

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

### 2. Activate the virtual environment

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app/main.py
```

The app will run on:

```text
http://localhost:5000
```

### 5. Test the health endpoint

```bash
curl http://localhost:5000/health
```

Expected output:

```json
{
  "status": "healthy"
}
```

---

## Run Tests

```bash
pytest -v
```

Expected result:

```text
1 passed
```

---

## Run with Docker

### 1. Build the Docker image

```bash
docker build -t github-actions-capstone .
```

### 2. Run the container

```bash
docker run -d --name github-actions-capstone -p 5000:5000 github-actions-capstone
```

### 3. Test the health endpoint

```bash
curl http://localhost:5000/health
```

### 4. Stop and remove the container

```bash
docker stop github-actions-capstone
docker rm github-actions-capstone
```

---

## Docker Image

Docker Hub repository:

```text
cloudwithpreetham/github-actions-capstone
```

Tags used:

```text
latest
sha-<short-commit-hash>
```

Example:

```text
cloudwithpreetham/github-actions-capstone:latest
cloudwithpreetham/github-actions-capstone:sha-515c7b6
```

---

## GitHub Actions Workflows

This project uses five workflow files.

---

### 1. Reusable Build and Test Workflow

File:

```text
.github/workflows/reusable-build-test.yml
```

Purpose:

- Checkout source code
- Set up Python
- Install dependencies
- Run tests
- Return test result as workflow output

Used by:

- PR Pipeline
- Main Pipeline

---

### 2. Reusable Docker Workflow

File:

```text
.github/workflows/reusable-docker.yml
```

Purpose:

- Login to Docker Hub
- Build Docker image
- Push Docker image
- Return image URL as workflow output

Used by:

- Main Pipeline

---

### 3. Pull Request Pipeline

File:

```text
.github/workflows/pr-pipeline.yml
```

Trigger:

```text
pull_request to main
```

PR event types:

```text
opened
synchronize
```

Purpose:

- Run tests on pull requests
- Validate code before merge
- Avoid Docker image push on PRs

Flow:

```text
PR opened or updated
   → Build and Test
   → Print PR summary
```

---

### 4. Main Branch Pipeline

File:

```text
.github/workflows/main-pipeline.yml
```

Trigger:

```text
push to main
```

Purpose:

- Run tests
- Build Docker images
- Push images to Docker Hub
- Run Trivy vulnerability scan
- Deploy to production environment

Flow:

```text
Push to main
   → Build and Test
   → Prepare short SHA
   → Build and push SHA image
   → Build and push latest image
   → Trivy security scan
   → Deploy
```

---

### 5. Scheduled Health Check Workflow

File:

```text
.github/workflows/health-check.yml
```

Triggers:

```text
Every 12 hours
Manual workflow_dispatch
```

Purpose:

- Pull latest Docker image
- Run container
- Check `/health` endpoint
- Publish health check summary
- Clean up container

Flow:

```text
Schedule or manual trigger
   → Pull latest image
   → Run container
   → Curl /health
   → Publish report
   → Stop and remove container
```

---

## CI/CD Pipeline Architecture

```text
Developer pushes code
        |
        v
GitHub Actions starts
        |
        v
Reusable Build-Test Workflow
        |
        v
Pytest validation
        |
        v
Docker image build
        |
        v
Docker Hub push
        |
        v
Trivy vulnerability scan
        |
        v
Production deployment simulation
```

---

## DevSecOps Integration

This project includes a basic DevSecOps step using Trivy.

Trivy scans the Docker image for vulnerabilities before the deploy job runs.

The scan is configured to fail the pipeline if a critical vulnerability is found.

```text
Docker Image
   → Trivy Scan
   → Block deployment if CRITICAL vulnerability exists
```

During implementation, Trivy detected critical vulnerabilities in the base image package:

```text
libgnutls30
```

The issue was fixed by updating Debian packages during the Docker build:

```dockerfile
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

After the fix, the security scan passed successfully.

---

## GitHub Secrets and Variables

### Repository Secret

| Name           | Purpose                 |
| -------------- | ----------------------- |
| `DOCKER_TOKEN` | Docker Hub access token |

### Repository Variable

| Name              | Purpose             |
| ----------------- | ------------------- |
| `DOCKER_USERNAME` | Docker Hub username |

Docker username is stored as a variable because it is not sensitive.

Docker token is stored as a secret because it is sensitive.

---

## Final Pipeline Status

The final main branch pipeline completed successfully.

Completed jobs:

```text
build-test      passed
prepare         passed
docker-sha      passed
docker-latest   passed
security-scan   passed
deploy          passed
```

---

## Key Learnings

Through this project, I learned how to:

- Build a real CI/CD pipeline using GitHub Actions
- Use reusable workflows with `workflow_call`
- Separate PR validation from main branch deployment
- Use GitHub secrets and variables correctly
- Build and push Docker images automatically
- Tag Docker images with `latest` and short commit SHA
- Scan Docker images using Trivy
- Debug real CI/CD pipeline failures from logs
- Fix container image vulnerabilities
- Use GitHub environments for deployment simulation

---

## Future Improvements

Planned improvements:

- Add staging and production environments
- Add manual approval rules for production
- Add Slack or Discord notifications
- Add rollback workflow
- Deploy to AWS ECS or EKS
- Add Kubernetes manifests
- Add Terraform infrastructure provisioning
- Add SBOM generation
- Add image signing with Cosign
- Add branch protection rules
- Add required status checks before merge

---

## 90DaysOfDevOps Progress

This project is part of my DevOps learning journey.

Day 48 focus:

```text
GitHub Actions Project: End-to-End CI/CD Pipeline
```

Final result:

```text
Code → Test → Build → Push → Scan → Deploy
```

This project represents a complete CI/CD foundation used in real DevOps workflows.
