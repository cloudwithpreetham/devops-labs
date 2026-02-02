# Day 10 – Linux File Permissions & File Operations

## Overview

Day 10 focused on one of the most important Linux fundamentals for DevOps Engineers: **file permissions and file operations**.

In Linux, every file and directory has permissions that control who can:

- Read (`r`)
- Write (`w`)
- Execute (`x`)

Understanding permissions is critical for:

- Running shell scripts
- Securing configuration files
- Managing shared directories
- Preventing unauthorized access
- Troubleshooting "Permission denied" errors

This hands-on challenge helped reinforce practical Linux permission management.

---

## Objectives

The goal of this challenge was to:

- Create files using Linux commands
- Read file contents using CLI tools
- Understand Linux permission models
- Modify permissions using `chmod`
- Execute shell scripts
- Test permission restrictions
- Observe Linux security behavior

---

## Hands-on Tasks Completed

### 1) File Creation

Created multiple files for practice:

- `devops.txt`
- `notes.txt`
- `script.sh`

Commands used:

```bash id="4yp9xn"
touch devops.txt
echo "This is day-10" >> notes.txt
vim script.sh
```

---

### 2) File Reading

Practiced reading files using:

```bash id="3y5s5n"
cat notes.txt
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
vim -R script.sh
```

Learned how Linux stores user information in `/etc/passwd`.

---

### 3) Permission Analysis

Inspected file permissions using:

```bash id="ow73w7"
ls -l
```

Permission format learned:

```id="lwht0m"
-rwxrwxrwx
```

Meaning:

- First character → file type
- Next 3 → owner permissions
- Next 3 → group permissions
- Last 3 → others permissions

---

### 4) Permission Changes

Modified permissions using:

```bash id="cf5o1y"
chmod +x script.sh
chmod -wx devops.txt
chmod 640 notes.txt
chmod 755 project
```

Examples learned:

| Permission | Meaning                                |
| ---------- | -------------------------------------- |
| 755        | Owner full access, others read/execute |
| 644        | Owner write, others read               |
| 640        | Owner read/write, group read only      |
| 600        | Owner only access                      |

---

### 5) Permission Testing

Tested Linux access controls:

- Tried writing to read-only files
- Tried executing non-executable scripts
- Observed **Permission denied** errors

This demonstrated how Linux enforces file security.

---

## Project Structure

```id="w13m88"
day-10/
├── screenshots/
├── day-10-file-permissions.md
├── reference.md
└── README.md
```

---

## Key Learnings

- Linux permissions are fundamental to system security
- `chmod` supports symbolic and numeric permission modes
- Execute permission is required to run scripts
- Directories require execute permission for access/traversal
- Incorrect permissions can create security vulnerabilities

---

## Real DevOps Relevance

File permissions are used daily in DevOps for:

- Deployment scripts
- CI/CD pipelines
- Secret management
- SSH key protection
- Config file hardening
- Container filesystem security

Examples:

```bash id="x2n0cf"
chmod 600 ~/.ssh/id_rsa
chmod +x deploy.sh
chmod 640 app.env
chmod 755 scripts/
```

---

## Commands Practiced

```bash id="pimjdp"
touch
cat
vim
head
tail
ls -l
chmod
mkdir
```

---

## Outcome

Successfully completed:

- File creation
- File reading
- Permission inspection
- Permission modification
- Permission testing
- Security understanding

Strong Linux fundamentals are being built step by step.

---

**#90DaysOfDevOps**
**#DevOpsKaJosh**
**#TrainWithShubham**
