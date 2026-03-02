# Day 38 – YAML Basics

## Goal

The goal of Day 38 was to understand the basics of YAML before writing CI/CD pipelines.

YAML is commonly used in DevOps tools such as GitHub Actions, Docker Compose, Kubernetes, Ansible, and CI/CD platforms.

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

## Task 1: Key-Value Pairs

Created `scripts/person.yaml` with basic key-value pairs.

```yaml
name: Preetham
role: DevOps Learner
experience_years: 0
learning: true
```

### What I Learned

- YAML uses `key: value` format.
- A space is required after the colon.
- `true` is a boolean value.
- YAML files should use spaces, not tabs.

---

## Task 2: Lists

Added a list of DevOps skills and hobbies to `person.yaml`.

```yaml
skills:
  - Git
  - Docker
  - Kubernetes
  - CI/CD
  - Linux
  - AWS

hobbies: [learning DevOps, coding, reading, problem solving]
```

### Two Ways to Write Lists in YAML

#### 1. Block List Format

```yaml
skills:
  - Git
  - Docker
  - Kubernetes
```

#### 2. Inline List Format

```yaml
hobbies: [learning DevOps, coding, reading]
```

### Notes

- Block lists are better for readability.
- Inline lists are useful for short lists.
- List items must be properly indented.

---

## Task 3: Nested Objects

Created `scripts/server.yaml` with nested server and database configuration.

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
```

### What I Learned

- Nested objects are created using indentation.
- YAML usually follows 2-space indentation.
- Indentation defines parent-child relationships.
- Tabs can break YAML validation.

---

## Task 4: Multi-line Strings

Added multi-line string examples in `server.yaml`.

### Pipe Style: `|`

```yaml
startup_script_preserve: |
  #!/bin/bash
  echo "Starting application server..."
  systemctl start nginx
  systemctl status nginx
```

The `|` style preserves line breaks exactly as written.

Use `|` for:

- Shell scripts
- Configuration blocks
- Logs
- Certificates
- Commands where line breaks matter

### Fold Style: `>`

```yaml
startup_script_fold: >
  This script starts the application server,
  checks the nginx service status,
  and confirms that the server is running.
```

The `>` style folds multiple lines into one paragraph.

Use `>` for:

- Descriptions
- Notes
- Messages
- Long text paragraphs

---

## Task 5: Validate YAML

Used `yamllint` to validate YAML files.

### Install yamllint

```bash
sudo apt update
sudo apt install yamllint -y
```

### Validate Files

```bash
yamllint scripts/person.yaml
yamllint scripts/server.yaml
```

### Intentional Indentation Error

Example of broken YAML using a tab:

```yaml
server:
	name: app-server-01
```

Expected validation error:

```text
found character '\t' that cannot start any token
```

### Fixed Version

```yaml
server:
  name: app-server-01
```

---

## Task 6: Spot the Difference

### Correct YAML

```yaml
name: devops
tools:
  - docker
  - kubernetes
```

### Broken YAML

```yaml
name: devops
tools:
  - docker
    - kubernetes
```

### What Is Wrong?

The second YAML block is broken because the list items are not properly indented under `tools`.

The first item `- docker` should be indented with 2 spaces. The second item `- kubernetes` has different indentation, which makes the YAML structure invalid.

### Corrected YAML

```yaml
name: devops
tools:
  - docker
  - kubernetes
```

---

## Commands Practiced

```bash
mkdir -p 08-ci-cd/github-actions/day-38/scripts
cd 08-ci-cd/github-actions/day-38

touch scripts/person.yaml scripts/server.yaml day-38-yaml.md README.md task.md

cat scripts/person.yaml
cat scripts/server.yaml

yamllint scripts/person.yaml
yamllint scripts/server.yaml
```

---

## Key Learnings

1. YAML is simple, but indentation is very strict.
2. YAML supports key-value pairs, lists, nested objects, and multi-line strings.
3. Spaces must be used instead of tabs.
4. The `|` symbol preserves line breaks, while `>` folds lines into one paragraph.
5. YAML validation is important before using files in CI/CD pipelines.

---

## Real-World DevOps Usage

YAML is used in many DevOps tools, including:

- GitHub Actions workflows
- GitLab CI/CD pipelines
- Docker Compose files
- Kubernetes manifests
- Ansible playbooks
- Helm charts

A small YAML indentation mistake can break a pipeline, deployment, or infrastructure configuration.

---

## Final Checklist

- [x] Created `person.yaml`
- [x] Created `server.yaml`
- [x] Practiced key-value pairs
- [x] Practiced block and inline lists
- [x] Practiced nested objects
- [x] Practiced multi-line strings
- [x] Validated YAML files
- [x] Documented YAML learnings

---

## Status

Day 38 completed successfully.
