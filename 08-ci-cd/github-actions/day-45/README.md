# GitHub Actions Practice

![Docker Publish](https://github.com/cloud-with-preetham/github-actions-practice/actions/workflows/docker-publish.yml/badge.svg)

This repository contains my hands-on GitHub Actions practice as part of my **90 Days of DevOps** learning journey.

The goal of this repository is to understand CI/CD pipelines by creating real workflows step by step, starting from basic automation and moving toward production-style Docker image build and publish pipelines.

---

## Repository Purpose

This repository is used to practice:

- GitHub Actions workflow basics
- CI/CD pipeline triggers
- Jobs and steps
- Environment variables
- GitHub Secrets
- Workflow artifacts
- Running tests in CI
- Docker image build automation
- Docker image publishing to Docker Hub

---

## Day 45: Docker Build & Push in GitHub Actions

On Day 45, I created a CI/CD pipeline that automatically builds a Docker image and pushes it to Docker Hub when code is pushed to the `main` branch.

This workflow represents a real-world DevOps pipeline where application code is packaged into a Docker image and published to a container registry automatically.

---

## What This Pipeline Does

The Docker publish workflow performs the following actions:

1. Checks out the repository code
2. Sets up Docker Buildx
3. Logs in to Docker Hub using GitHub Secrets
4. Builds the Docker image
5. Tags the image as `latest`
6. Tags the image with the short Git commit SHA
7. Pushes both tags to Docker Hub
8. Ensures Docker image push happens only from the `main` branch

---

## Project Structure

```text
day-45/
├── github-actions-practice/
│   └── .github/
│       └── workflows/
│           └── docker-publish.yml
├── screenshots/
├── day-45-docker-cicd.md
├── Dockerfile
├── index.html
├── README.md
└── task.md
```

---

## Dockerfile

The project uses a simple Nginx-based Docker image.

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
```

---

## GitHub Actions Workflow

Workflow file:

```text
github-actions-practice/.github/workflows/docker-publish.yml
```

Workflow name:

```text
Docker Publish
```

The workflow runs on:

```text
push to main
push to feature/**
pull_request to main
```

Feature branches are used to test image builds, but Docker images are only pushed when the workflow runs from the `main` branch.

---

## GitHub Secrets

The workflow uses GitHub Actions Secrets to securely authenticate with Docker Hub.

Required secrets:

```text
DOCKER_USERNAME
DOCKER_TOKEN
```

The actual secret values are never printed in workflow logs.

---

## Docker Hub Image

Docker Hub image:

```text
https://hub.docker.com/r/YOUR_DOCKER_USERNAME/github-actions-practice
```

Image tags:

```text
YOUR_DOCKER_USERNAME/github-actions-practice:latest
YOUR_DOCKER_USERNAME/github-actions-practice:sha-<short-commit-hash>
```

Replace `YOUR_DOCKER_USERNAME` with your Docker Hub username.

---

## Pull and Run the Image

Pull the Docker image:

```bash
docker pull YOUR_DOCKER_USERNAME/github-actions-practice:latest
```

Run the container:

```bash
docker run -d \
  --name github-actions-practice \
  -p 8080:80 \
  YOUR_DOCKER_USERNAME/github-actions-practice:latest
```

Verify the application:

```bash
curl http://localhost:8080
```

Expected result:

```text
Day 45 - Docker Build and Push using GitHub Actions
```

Stop and remove the container:

```bash
docker stop github-actions-practice
docker rm github-actions-practice
```

---

## CI/CD Flow

The complete pipeline flow is:

```text
Developer pushes code
        ↓
GitHub Actions workflow starts
        ↓
Repository code is checked out
        ↓
Docker image is built
        ↓
Image is tagged as latest and sha-<commit>
        ↓
Image is pushed to Docker Hub
        ↓
Server pulls the image
        ↓
Container runs the application
```

---

## Learning Progress

| Day    | Topic                                   | Status    |
| ------ | --------------------------------------- | --------- |
| Day 40 | First GitHub Actions Workflow           | Completed |
| Day 41 | Triggers and Matrix Builds              | Completed |
| Day 42 | GitHub-hosted and Self-hosted Runners   | Completed |
| Day 43 | Jobs, Steps, Env Vars, and Conditionals | Completed |
| Day 44 | Secrets, Artifacts, and Tests in CI     | Completed |
| Day 45 | Docker Build and Push in GitHub Actions | Completed |

---

## Key Learnings

Through this repository, I learned:

- How GitHub Actions workflows are structured
- How CI/CD pipelines run automatically on code changes
- How to use repository secrets securely
- How to build Docker images in CI
- How to push Docker images to Docker Hub
- How to use image tags for traceability
- How to restrict deployment steps to the `main` branch
- How real DevOps teams automate build and release workflows

---

## Author

**Preetham**
DevOps Learner | 90 Days of DevOps Journey

GitHub: [cloud-with-preetham](https://github.com/cloud-with-preetham)
