# GitHub Actions Capstone – End-to-End CI/CD Pipeline

This project is part of my **90DaysOfDevOps** journey.

The goal of this project was to build a complete, production-style CI/CD pipeline using **GitHub Actions**, **Docker**, **Docker Hub**, **Reusable Workflows**, **Trivy security scanning**, and a simulated production deployment.

---

## Workflow Badges

![Main Pipeline](https://github.com/cloud-with-preetham/github-actions-capstone/actions/workflows/main-pipeline.yml/badge.svg)

![PR Pipeline](https://github.com/cloud-with-preetham/github-actions-capstone/actions/workflows/pr-pipeline.yml/badge.svg)

![Scheduled Health Check](https://github.com/cloud-with-preetham/github-actions-capstone/actions/workflows/health-check.yml/badge.svg)

---

# STAR Format Project Summary

## Situation

Modern software teams need reliable CI/CD pipelines to test, package, scan, and deploy applications automatically.

Manual deployment creates common problems such as:

- Missed test execution
- Unstable builds
- Inconsistent Docker image tags
- Manual Docker image publishing
- Lack of vulnerability scanning
- No clear separation between pull request checks and production deployment

As part of Day 48 of my 90DaysOfDevOps journey, I built a GitHub Actions capstone project to simulate a real-world CI/CD pipeline.

The project uses a simple Python Flask application as the workload and focuses on automating the software delivery process from code commit to deployment.

---

## Task

The task was to design and implement an end-to-end CI/CD pipeline that could:

- Run automated tests on every pull request
- Prevent Docker image publishing from pull request workflows
- Run a full CI/CD pipeline on pushes to the `main` branch
- Build Docker images automatically
- Push Docker images to Docker Hub with proper tags
- Use reusable workflows to avoid duplicate pipeline logic
- Scan Docker images for critical vulnerabilities
- Deploy only after successful test, build, push, and scan stages
- Run scheduled health checks every 12 hours
- Document the complete pipeline architecture

The final expected output was:

- A working Flask application
- A Dockerfile
- Automated tests
- At least three GitHub Actions workflow files
- A successful main branch CI/CD pipeline
- Docker image published to Docker Hub
- Trivy scan report uploaded as an artifact
- Day 48 documentation

---

## Action

### 1. Created a Simple Flask Application

I created a lightweight Python Flask application with two endpoints:

| Endpoint  | Method | Purpose                     |
| --------- | ------ | --------------------------- |
| `/`       | GET    | Returns application status  |
| `/health` | GET    | Returns health check status |

Health endpoint response:

```json
{
  "status": "healthy"
}
```

---

### 2. Added Automated Testing

I added a Pytest test case to validate the `/health` endpoint.

Test file:

```text
tests/test_app.py
```

The test checks:

- HTTP status code is `200`
- Response body returns `{"status": "healthy"}`

I also fixed a Python import issue by adding:

```text
app/__init__.py
pytest.ini
```

This solved the initial error:

```text
ModuleNotFoundError: No module named 'app'
```

---

### 3. Containerized the Application

I created a Dockerfile to package the Flask application into a Docker image.

The Dockerfile uses:

```dockerfile
FROM python:3.12.13-slim-bookworm
```

I also added Debian package updates during the build to fix vulnerabilities found by Trivy:

```dockerfile
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

---

### 4. Created a Reusable Build and Test Workflow

Workflow file:

```text
.github/workflows/reusable-build-test.yml
```

Purpose:

- Checkout code
- Set up Python
- Install dependencies
- Run tests
- Return test result as an output

This workflow is called by both:

- Pull Request Pipeline
- Main Branch Pipeline

This avoids repeating the same build and test logic in multiple workflow files.

---

### 5. Created a Reusable Docker Build and Push Workflow

Workflow file:

```text
.github/workflows/reusable-docker.yml
```

Purpose:

- Login to Docker Hub
- Build Docker image
- Push Docker image
- Return image URL as output

This workflow accepts:

- Docker username
- Image name
- Image tag
- Docker token secret

I used:

```text
DOCKER_USERNAME
```

as a GitHub repository variable because it is not sensitive.

I used:

```text
DOCKER_TOKEN
```

as a GitHub repository secret because it is sensitive.

---

### 6. Created a Pull Request Pipeline

Workflow file:

```text
.github/workflows/pr-pipeline.yml
```

Trigger:

```text
pull_request to main
```

Event types:

```text
opened
synchronize
```

Purpose:

- Run tests on pull requests
- Validate code before merge
- Print PR summary
- Avoid Docker image build and push on PRs

PR pipeline flow:

```text
PR opened or updated
   → Build and test
   → Print PR summary
```

---

### 7. Created the Main Branch CI/CD Pipeline

Workflow file:

```text
.github/workflows/main-pipeline.yml
```

Trigger:

```text
push to main
```

Pipeline flow:

```text
Push to main
   → Build and test
   → Prepare short SHA
   → Build and push SHA-tagged Docker image
   → Build and push latest Docker image
   → Run Trivy vulnerability scan
   → Deploy to production
```

Docker image tags used:

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

### 8. Added Trivy Security Scanning

I added Trivy to scan the Docker image before deployment.

The scan checks for:

```text
CRITICAL
```

severity vulnerabilities.

The pipeline was configured to fail if critical vulnerabilities were found:

```yaml
severity: CRITICAL
exit-code: 1
```

During implementation, Trivy found two critical vulnerabilities in:

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

I fixed this by updating Debian packages inside the Docker image build.

---

### 9. Created a Scheduled Health Check Workflow

Workflow file:

```text
.github/workflows/health-check.yml
```

Triggers:

```text
schedule
workflow_dispatch
```

Cron schedule:

```text
0 */12 * * *
```

Purpose:

- Pull latest Docker image
- Run container
- Wait for app startup
- Curl `/health`
- Generate GitHub Actions step summary
- Stop and remove container

Health check flow:

```text
Every 12 hours or manual trigger
   → Pull latest image
   → Run container
   → Curl /health
   → Publish health report
   → Cleanup container
```

---

## Result

The final CI/CD pipeline completed successfully.

Main pipeline job status:

```text
build-test      passed
prepare         passed
docker-sha      passed
docker-latest   passed
security-scan   passed
deploy          passed
```

Final pipeline result:

```text
Code Push
   → Test
   → Build Docker Image
   → Push to Docker Hub
   → Scan Image
   → Deploy
```

The project successfully demonstrated:

- CI automation
- Docker image automation
- Reusable GitHub Actions workflows
- GitHub secrets and variables
- Docker Hub integration
- SHA-based image tagging
- Security scanning with Trivy
- Deployment simulation using GitHub environments
- Scheduled health checks
- Debugging real pipeline failures

---

# Project Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +--> PR Pipeline
   |       |
   |       v
   |    Build and Test Only
   |
   +--> Main Pipeline
   |       |
   |       v
   |    Build and Test
   |       |
   |       v
   |    Docker Build and Push
   |       |
   |       v
   |    Trivy Security Scan
   |       |
   |       v
   |    Production Deployment
   |
   +--> Scheduled Health Check
           |
           v
        Pull Image
           |
           v
        Run Container
           |
           v
        Check /health
```

---

# Tech Stack

| Category           | Tool                |
| ------------------ | ------------------- |
| Application        | Python Flask        |
| Testing            | Pytest              |
| Containerization   | Docker              |
| CI/CD              | GitHub Actions      |
| Registry           | Docker Hub          |
| Security Scanning  | Trivy               |
| Deployment Control | GitHub Environments |
| Scheduling         | GitHub Actions Cron |

---

# Project Structure

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

# Application Details

## `app/main.py`

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

# Running Locally

## 1. Create virtual environment

```bash
python3 -m venv venv
```

## 2. Activate virtual environment

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the app

```bash
python app/main.py
```

Application URL:

```text
http://localhost:5000
```

Health check:

```bash
curl http://localhost:5000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

# Running Tests

```bash
pytest -v
```

Expected result:

```text
1 passed
```

---

# Running with Docker

## 1. Build image

```bash
docker build -t github-actions-capstone .
```

## 2. Run container

```bash
docker run -d --name github-actions-capstone -p 5000:5000 github-actions-capstone
```

## 3. Test health endpoint

```bash
curl http://localhost:5000/health
```

## 4. Cleanup

```bash
docker stop github-actions-capstone
docker rm github-actions-capstone
```

---

# Docker Hub Image

Docker Hub repository:

```text
cloudwithpreetham/github-actions-capstone
```

Tags:

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

# GitHub Secrets and Variables

## Repository Secret

| Name           | Purpose                 |
| -------------- | ----------------------- |
| `DOCKER_TOKEN` | Docker Hub access token |

## Repository Variable

| Name              | Purpose             |
| ----------------- | ------------------- |
| `DOCKER_USERNAME` | Docker Hub username |

---

# Key Problems Solved

## 1. Pytest Import Failure

Problem:

```text
ModuleNotFoundError: No module named 'app'
```

Fix:

```text
Added app/__init__.py
Added pytest.ini
```

---

## 2. Docker Login Failure

Problem:

```text
Error: Username and password required
```

Fix:

```text
Moved Docker username to repository variable
Used Docker token as repository secret
Passed values correctly into reusable workflow
```

---

## 3. Empty Trivy Image Reference

Problem:

```text
could not parse reference:
```

Fix:

```text
Generated image_url output from non-secret workflow inputs
Validated image URL before scanning
```

---

## 4. Critical Trivy Vulnerability

Problem:

```text
libgnutls30 had CRITICAL vulnerabilities
```

Fix:

```text
Updated Debian packages during Docker image build
```

---

# Key Learnings

This project helped me understand:

- How production-style CI/CD pipelines are structured
- Why reusable workflows are important
- How pull request pipelines differ from main branch pipelines
- How Docker image tagging works in CI/CD
- How GitHub secrets and variables should be used
- How to scan container images before deployment
- How to debug pipeline errors from logs
- How to fix vulnerabilities in Docker images
- How scheduled health checks work
- How deployment environments fit into CI/CD workflows

---

# Future Improvements

Planned improvements:

- Add staging and production environments
- Add production approval rules
- Add Slack or Discord deployment notifications
- Add rollback workflow
- Deploy to AWS ECS
- Deploy to Kubernetes or EKS
- Add Terraform infrastructure automation
- Add SBOM generation
- Add image signing with Cosign
- Add branch protection rules
- Add required status checks before merge
- Add monitoring and alerting after deployment

---

# Final Outcome

This project completed a full end-to-end CI/CD pipeline.

Final result:

```text
Code → Test → Build → Push → Scan → Deploy
```

This project is a strong DevOps portfolio item because it shows practical experience with:

- GitHub Actions
- Docker
- CI/CD
- DevSecOps
- Workflow debugging
- Production-style automation
