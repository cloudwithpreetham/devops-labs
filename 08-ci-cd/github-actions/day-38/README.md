# Day 38 – YAML Basics

## Overview

This project is part of my **90 Days of DevOps** journey.

The focus of Day 38 is to understand the basics of **YAML**, which is widely used in DevOps tools such as GitHub Actions, Docker Compose, Kubernetes, Ansible, and CI/CD pipelines.

Before writing real CI/CD workflows, it is important to understand YAML syntax, indentation, lists, nested objects, and multi-line strings.

---

## Project Structure

```bash
08-ci-cd/
└── github-actions/
    └── day-38/
        ├── scripts/
        │   ├── person.yaml
        │   └── server.yaml
        ├── day-38-yaml.md
        ├── README.md
        └── task.md
```

---

## Files Created

### `scripts/person.yaml`

This file contains basic YAML examples such as:

- Key-value pairs
- Boolean values
- Lists
- Inline lists

Example:

```yaml
name: Preetham
role: DevOps Learner
experience_years: 0
learning: true

skills:
  - Git
  - Docker
  - Kubernetes
  - CI/CD
  - Linux
  - AWS

hobbies: [learning DevOps, coding, reading, problem solving]
```

---

### `scripts/server.yaml`

This file contains more advanced YAML examples such as:

- Nested objects
- Database configuration
- Nested credentials
- Multi-line strings using `|`
- Folded strings using `>`

Example:

```yaml
server:
  name: app-server-01
  ip: 192.168.1.10
  port: 8080

database:
  host: localhost
  name: devops_db
  credentials:
    user: admin
    password: secure_password

startup_script_preserve: |
  #!/bin/bash
  echo "Starting application server..."
  systemctl start nginx
  systemctl status nginx

startup_script_fold: >
  This script starts the application server,
  checks the nginx service status,
  and confirms that the server is running.
```

---

## YAML Concepts Practiced

### 1. Key-Value Pairs

YAML stores data using a simple `key: value` format.

```yaml
role: DevOps Learner
learning: true
```

---

### 2. Lists

YAML supports two types of list formats.

Block list:

```yaml
skills:
  - Git
  - Docker
  - Kubernetes
```

Inline list:

```yaml
hobbies: [learning DevOps, coding, reading]
```

---

### 3. Nested Objects

Nested objects are created using indentation.

```yaml
database:
  credentials:
    user: admin
    password: secure_password
```

---

### 4. Multi-line Strings

The `|` symbol preserves line breaks.

```yaml
startup_script_preserve: |
  echo "Starting server"
  systemctl start nginx
```

The `>` symbol folds multiple lines into a single line.

```yaml
startup_script_fold: >
  This is a long message
  written across multiple lines.
```

---

## YAML Validation

YAML files were validated using `yamllint`.

### Install `yamllint`

```bash
sudo apt update
sudo apt install yamllint -y
```

### Validate YAML Files

```bash
yamllint scripts/person.yaml
yamllint scripts/server.yaml
```

---

## Important YAML Rules

- YAML uses spaces, not tabs.
- Indentation is very important.
- Two spaces are commonly used for indentation.
- Strings usually do not need quotes.
- `true` and `false` are booleans.
- `"true"` and `"false"` are strings.
- Incorrect indentation can break YAML files.

---

## Common YAML Mistake

Incorrect YAML:

```yaml
name: devops
tools:
  - docker
    - kubernetes
```

Correct YAML:

```yaml
name: devops
tools:
  - docker
  - kubernetes
```

The broken example fails because the list items are not properly indented under `tools`.

---

## What I Learned

- YAML is simple but very strict about indentation.
- Lists can be written in block format or inline format.
- Multi-line strings can be handled using `|` and `>`.
- YAML is used heavily in real-world DevOps tools.
- A small spacing mistake can break CI/CD pipelines or Kubernetes manifests.

---

## Real-World DevOps Use Cases

YAML is used in:

- GitHub Actions workflows
- GitLab CI/CD pipelines
- Docker Compose files
- Kubernetes manifests
- Ansible playbooks
- Helm charts
- Cloud infrastructure configuration

---

## Final Status

Completed:

- Created `person.yaml`
- Created `server.yaml`
- Practiced key-value pairs
- Practiced lists
- Practiced nested objects
- Practiced multi-line strings
- Validated YAML syntax
- Documented Day 38 learning

---

## Author

**Preetham**
DevOps Learner | 90 Days of DevOps Journey
