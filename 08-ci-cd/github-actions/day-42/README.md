# Day 42 – GitHub Actions Runners

## Overview

This project is part of my **90 Days of DevOps** journey.

On Day 42, I learned about **GitHub Actions runners**. A runner is the machine that executes workflow jobs in GitHub Actions.

I worked with two types of runners:

- GitHub-hosted runners
- Self-hosted runners

GitHub-hosted runners are managed by GitHub, while self-hosted runners are machines that I configure and manage myself.

---

## What I Practiced

- Created workflows using GitHub-hosted runners
- Ran jobs on multiple operating systems
- Checked pre-installed tools on Ubuntu runner
- Configured an EC2 instance as a self-hosted runner
- Ran a GitHub Actions job on my own EC2 runner
- Used custom labels to target a specific self-hosted runner
- Compared GitHub-hosted and self-hosted runners

---

## Workflows Created

```text
.github/workflows/
├── hosted-runners.yml
├── preinstalled-tools.yml
└── self-hosted.yml
```

---

## 1. GitHub-Hosted Runner Workflow

I created a workflow that runs three jobs in parallel using different operating systems:

- `ubuntu-latest`
- `windows-latest`
- `macos-latest`

Each job prints:

- OS name
- Hostname
- Current user

### Workflow

```yaml
name: GitHub Hosted Runners

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  ubuntu-job:
    name: Ubuntu Runner
    runs-on: ubuntu-latest
    steps:
      - name: Print Ubuntu runner info
        run: |
          echo "OS Name: $RUNNER_OS"
          echo "Hostname: $(hostname)"
          echo "Current User: $(whoami)"

  windows-job:
    name: Windows Runner
    runs-on: windows-latest
    steps:
      - name: Print Windows runner info
        shell: pwsh
        run: |
          Write-Output "OS Name: $env:RUNNER_OS"
          Write-Output "Hostname: $env:COMPUTERNAME"
          Write-Output "Current User: $env:USERNAME"

  macos-job:
    name: macOS Runner
    runs-on: macos-latest
    steps:
      - name: Print macOS runner info
        run: |
          echo "OS Name: $RUNNER_OS"
          echo "Hostname: $(hostname)"
          echo "Current User: $(whoami)"
```

---

## 2. Pre-installed Tools Workflow

I created another workflow to check tools already available on the Ubuntu GitHub-hosted runner.

The workflow checked:

- Docker version
- Python version
- Node.js version
- Git version

### Workflow

```yaml
name: Check Preinstalled Tools

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  check-tools:
    name: Check Tools on Ubuntu Runner
    runs-on: ubuntu-latest

    steps:
      - name: Print tool versions
        run: |
          echo "Docker Version:"
          docker --version

          echo "Python Version:"
          python3 --version

          echo "Node Version:"
          node --version

          echo "Git Version:"
          git --version
```

### Output

```text
Docker version 28.0.4
Python 3.12.3
Node v22.22.3
git version 2.54.0
```

---

## 3. Self-Hosted Runner Workflow

I configured a Linux EC2 instance as a self-hosted runner and connected it to my GitHub repository.

The runner details:

```text
Runner name: github-runner
Runner type: self-hosted
Operating system: Linux
Architecture: X64
Status: Idle
```

I then created a workflow that runs directly on this EC2 runner.

### Workflow

```yaml
name: Self Hosted Runner Demo

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  run-on-my-machine:
    name: Run Job on Self-Hosted Runner
    runs-on: [self-hosted, my-linux-runner]

    steps:
      - name: Print machine details
        run: |
          echo "Runner OS: $RUNNER_OS"
          echo "Hostname: $(hostname)"
          echo "Current User: $(whoami)"
          echo "Working Directory: $(pwd)"

      - name: Create test file on self-hosted runner
        run: |
          echo "This file was created by GitHub Actions on my self-hosted runner." > day-42-runner-test.txt
          ls -la
          cat day-42-runner-test.txt
```

### Output

```text
Runner OS: Linux
Hostname: ip-172-31-40-228
Current User: ubuntu
Working Directory: /home/ubuntu/actions-runner/_work/github-actions-practice/github-actions-practice
```

This confirmed that the GitHub Actions job successfully ran on my EC2 self-hosted runner.

---

## Screenshots

```text
day-42/screenshots/
├── day-42-hosted-runners-parallel.png
├── day-42-preinstalled-tools.png
├── day-42-self-hosted-runner-idle.png
└── day-42-self-hosted-job-running.png
```

---

## GitHub-Hosted vs Self-Hosted Runners

| Topic               | GitHub-Hosted                                                           | Self-Hosted                                                                        |
| ------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Who manages it?     | GitHub manages the runner, OS image, updates, and cleanup               | I manage the machine, runner app, updates, security, and cleanup                   |
| Cost                | Uses GitHub Actions minutes based on the GitHub plan                    | Uses my own machine, EC2 instance, VM, or server cost                              |
| Pre-installed tools | Comes with many common tools already installed                          | I decide what tools to install                                                     |
| Good for            | General CI, testing, builds, open-source projects, and multi-OS testing | Private infrastructure access, custom tools, deployments, and special environments |
| Security concern    | Limited access to private infrastructure                                | Riskier because workflow code runs on my own machine                               |

---

## Important Commands

### Start Runner Manually

```bash
cd ~/actions-runner
./run.sh
```

### Install Runner as a Service

```bash
cd ~/actions-runner
sudo ./svc.sh install
```

### Start Runner Service

```bash
sudo ./svc.sh start
```

### Check Runner Service Status

```bash
sudo ./svc.sh status
```

### Stop Runner Service

```bash
sudo ./svc.sh stop
```

---

## Issue Faced

While starting the runner manually, I saw this error:

```text
A session for this runner already exists.
Runner connect error: Error: Conflict.
```

### Reason

The runner was already connected in another session or running as a background service.

### Fix

Use only one runner mode at a time:

```text
Manual mode: ./run.sh
Service mode: sudo ./svc.sh start
```

For EC2, service mode is better because the runner stays active even after closing the SSH session.

---

## Key Learnings

- A runner is the machine that executes GitHub Actions jobs.
- GitHub-hosted runners are temporary machines managed by GitHub.
- Self-hosted runners are machines managed by the user.
- GitHub-hosted runners are useful for general CI workflows.
- Self-hosted runners are useful for private infrastructure and custom environments.
- Labels help target a specific self-hosted runner.
- Self-hosted runners require more security responsibility.
- My EC2 instance successfully ran a GitHub Actions job.

---

## Final Status

| Task                                           | Status    |
| ---------------------------------------------- | --------- |
| Created multi-OS GitHub-hosted runner workflow | Completed |
| Checked pre-installed tools on Ubuntu runner   | Completed |
| Registered self-hosted runner                  | Completed |
| Verified runner as Idle                        | Completed |
| Ran workflow on self-hosted runner             | Completed |
| Created file on self-hosted runner             | Completed |
| Used custom runner label                       | Completed |
| Compared GitHub-hosted and self-hosted runners | Completed |

---

## Conclusion

On Day 42, I learned how GitHub Actions uses runners to execute CI/CD jobs.

I tested GitHub-hosted runners across Ubuntu, Windows, and macOS. I also configured an EC2 instance as a self-hosted runner and successfully ran a workflow on my own infrastructure.

This gave me practical experience with both managed CI runners and custom self-hosted runners used in real DevOps environments.
