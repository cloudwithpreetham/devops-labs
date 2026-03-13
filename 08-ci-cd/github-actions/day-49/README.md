# GitHub Actions Capstone – DevSecOps CI/CD Pipeline

## Project Overview

This project is a GitHub Actions capstone project built as part of the `90DaysOfDevOps` journey.

The goal of this project is to build a real-world CI/CD pipeline that can:

- Run automated tests
- Build Docker images
- Scan Docker images for vulnerabilities
- Push Docker images to Docker Hub
- Deploy only after successful validation
- Use reusable GitHub Actions workflows
- Add DevSecOps security checks into the pipeline

This project demonstrates how CI/CD and DevSecOps work together in a practical DevOps workflow.

---

## Tech Stack

| Tool                     | Purpose                             |
| ------------------------ | ----------------------------------- |
| GitHub Actions           | CI/CD automation                    |
| Python                   | Application runtime                 |
| Pytest                   | Automated testing                   |
| Docker                   | Container image build               |
| Docker Hub               | Container registry                  |
| Trivy                    | Docker image vulnerability scanning |
| GitHub Secrets           | Secure credential management        |
| GitHub Dependency Review | Dependency vulnerability checks     |
| GitHub Secret Scanning   | Secret detection                    |

---

## Project Structure

```text
github-actions-capstone/
├── .github/
│   └── workflows/
│       ├── health-check.yml
│       ├── main-pipeline.yml
│       ├── pr-pipeline.yml
│       ├── reusable-build-test.yml
│       └── reusable-docker.yml
├── app/
│   └── main.py
├── tests/
│   └── test_app.py
├── 2026/
│   └── day-49/
│       ├── day-49-devsecops.md
│       └── screenshots/
├── Dockerfile
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

## CI/CD Pipeline Flow

The main pipeline runs on every push to the `main` branch.

```text
Push to main
    |
    v
Build and Test
    |
    v
Prepare Short SHA
    |
    v
Build Docker Image :latest
    |
    v
Run Trivy Vulnerability Scan
    |
    v
Push Docker Image :latest
    |
    v
Build Docker Image :sha-xxxxxxx
    |
    v
Run Trivy Vulnerability Scan
    |
    v
Push Docker Image :sha-xxxxxxx
    |
    v
Deploy to Production
```

---

## Workflow Files

### `main-pipeline.yml`

Main CI/CD pipeline.

Responsibilities:

- Runs on push to `main`
- Calls reusable build and test workflow
- Generates short commit SHA
- Builds Docker images with `latest` and SHA tags
- Deploys after successful Docker image validation

---

### `reusable-build-test.yml`

Reusable workflow for Python build and test.

Responsibilities:

- Checks out the code
- Sets up Python
- Installs dependencies
- Runs tests using `pytest`

---

### `reusable-docker.yml`

Reusable workflow for Docker build, scan, and push.

Responsibilities:

- Logs in to Docker Hub
- Builds Docker image
- Runs Trivy vulnerability scan
- Pushes Docker image only if the scan passes
- Exposes Docker image URL as workflow output

---

### `pr-pipeline.yml`

Pull request validation workflow.

Responsibilities:

- Runs checks on pull requests
- Validates code before merge
- Runs dependency review security checks

---

### `health-check.yml`

Health check workflow.

Responsibilities:

- Performs basic pipeline or application health validation
- Helps confirm workflow execution

---

## Docker Image

The project uses a slim Python base image:

```dockerfile
FROM python:3.12.13-slim-bookworm
```

The Docker image is built using:

```bash
docker build -t <dockerhub-username>/github-actions-capstone:latest .
```

The image is pushed to Docker Hub after passing the Trivy scan.

---

## DevSecOps Security Checks

This project includes DevSecOps practices to catch security problems early in the pipeline.

### 1. Docker Image Vulnerability Scan

Trivy scans the Docker image before it is pushed.

```yaml
- name: Scan Docker Image for Vulnerabilities
  uses: aquasecurity/trivy-action@v0.36.0
  with:
    image-ref: ${{ env.IMAGE_URL }}
    format: "table"
    exit-code: "1"
    severity: "CRITICAL,HIGH"
    ignore-unfixed: true
```

If fixable HIGH or CRITICAL vulnerabilities are found, the pipeline fails.

---

### 2. Dependency Review

Dependency Review checks new dependencies introduced in pull requests.

```yaml
- name: Check Dependencies for Vulnerabilities
  uses: actions/dependency-review-action@v4
  with:
    fail-on-severity: critical
```

This prevents critical vulnerable dependencies from being merged.

---

### 3. Secret Scanning

GitHub Secret Scanning is used to detect exposed secrets such as:

- API keys
- GitHub tokens
- AWS access keys
- Docker tokens
- Database passwords

Secrets are not stored in source code. They are stored securely using GitHub Secrets.

---

### 4. Push Protection

Push protection helps block secrets before they enter the repository.

This reduces the risk of accidentally committing sensitive credentials.

---

### 5. Restricted Workflow Permissions

Workflow permissions are restricted using:

```yaml
permissions:
  contents: read
```

This follows the principle of least privilege.

---

## Required GitHub Secrets and Variables

### Secrets

| Name              | Purpose                 |
| ----------------- | ----------------------- |
| `DOCKERHUB_TOKEN` | Docker Hub access token |

### Variables

| Name                 | Purpose             |
| -------------------- | ------------------- |
| `DOCKERHUB_USERNAME` | Docker Hub username |

Configure them here:

```text
Repository → Settings → Secrets and variables → Actions
```

---

## Running Tests Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
```

---

## Building Docker Image Locally

Build the Docker image:

```bash
docker build -t github-actions-capstone:local .
```

Run the container:

```bash
docker run -p 5000:5000 github-actions-capstone:local
```

Test the app:

```bash
curl http://localhost:5000
```

---

## Trivy Scan Locally

If Trivy is installed locally, scan the image with:

```bash
trivy image github-actions-capstone:local
```

Scan only HIGH and CRITICAL vulnerabilities:

```bash
trivy image --severity HIGH,CRITICAL github-actions-capstone:local
```

---

## Final Pipeline Result

The final GitHub Actions pipeline completed successfully.

Completed jobs:

```text
build-test     - Passed
prepare        - Passed
docker-latest  - Passed
docker-sha     - Passed
deploy         - Passed
```

This confirms that the project now has a working CI/CD pipeline with DevSecOps checks.

---

## Key Learnings

Through this project, I learned how to:

- Create reusable GitHub Actions workflows
- Build and test a Python application in CI
- Build Docker images automatically
- Push Docker images to Docker Hub
- Use SHA-based Docker image tags
- Scan Docker images using Trivy
- Fail a pipeline when security issues are detected
- Use GitHub Secrets instead of hardcoded credentials
- Add dependency security checks to pull requests
- Apply least-privilege permissions in workflows

---

## Final Outcome

This project demonstrates a practical DevSecOps-enabled CI/CD pipeline.

The pipeline can:

```text
Build → Test → Dockerize → Scan → Push → Deploy
```

Security is now part of the automation process instead of being a manual step after deployment.
