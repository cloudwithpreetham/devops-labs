# Day 39 – What is CI/CD?

## Overview

This folder contains my Day 39 notes for the **90 Days of DevOps** challenge.

The goal of this day is to understand the core concepts of **CI/CD** before writing actual pipeline YAML files. CI/CD is one of the most important practices in DevOps because it helps teams test, build, and deploy applications in a reliable and repeatable way.

---

## Topics Covered

- Why CI/CD exists
- Problems with manual deployments
- Meaning of "it works on my machine"
- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- CI/CD pipeline anatomy
- Pipeline trigger, stage, job, step, runner, and artifact
- Text-based CI/CD pipeline diagram
- Real-world GitHub Actions workflow exploration

---

## Folder Structure

```text
day-39/
├── day-39-cicd-concepts.md
├── README.md
└── task.md
```

---

## Files

| File                      | Description                      |
| ------------------------- | -------------------------------- |
| `task.md`                 | Original Day 39 challenge task   |
| `day-39-cicd-concepts.md` | Detailed notes on CI/CD concepts |
| `README.md`               | Summary of the Day 39 work       |

---

## What I Learned

CI/CD is not just a tool like GitHub Actions, Jenkins, GitLab CI, or CircleCI. It is a software delivery practice that improves teamwork, reduces manual errors, and helps teams release code with more confidence.

### Key takeaways:

- CI helps catch bugs early by testing code automatically.
- Continuous Delivery keeps the application ready for release.
- Continuous Deployment automatically releases every successful change.
- Pipelines make software delivery consistent and repeatable.
- A failed pipeline is useful because it prevents broken code from moving forward.

---

## Pipeline Diagram

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

---

## Real-World Exploration

For this task, I explored a real open-source GitHub repository and checked its GitHub Actions workflow.

### Repository Checked

```text
FastAPI
```

### Workflow Location

```text
.github/workflows/test.yml
```

### Observations

- The workflow runs on push and pull request events.
- It contains jobs for detecting changes and running tests.
- It uses automation to verify code before changes are merged.
- This shows how real projects use CI to maintain code quality.

---

## DevOps Reflection

Before learning to write CI/CD pipelines, it is important to understand why pipelines are needed.

Manual deployment may work for small experiments, but in real teams it becomes risky. CI/CD makes the process predictable by automating testing, building, and deployment steps.

This is a core DevOps skill because modern teams expect code changes to be validated automatically before reaching production.

---

## Status

Completed Day 39 of the 90 Days of DevOps challenge.
