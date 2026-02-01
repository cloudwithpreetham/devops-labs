# Day 09 – Linux User & Group Management

## Overview

Day 09 focused on **Linux user and group administration**, a fundamental skill for DevOps engineers managing multi-user systems, shared resources, and access control.

This hands-on challenge covered:

- Creating Linux users with home directories
- Setting passwords securely
- Creating and managing groups
- Assigning users to multiple groups
- Configuring shared directories with group permissions
- Troubleshooting permission-related issues

---

## Objectives

The goal of this challenge was to understand how Linux handles:

- **Users** → system identities for login and process ownership
- **Groups** → logical collections of users for access control
- **Permissions** → read / write / execute access management
- **Ownership** → who controls files and directories

These concepts are critical in:

- Server administration
- CI/CD runner access
- Shared deployment environments
- Log file management
- Application permission troubleshooting

---

## Tasks Completed

### 1) User Creation

Created users:

- `tokyo`
- `berlin`
- `professor`
- `nairobi`

Verified with:

```bash
cat /etc/passwd
ls /home/
```

---

### 2) Group Creation

Created groups:

- `developers`
- `admins`
- `project-team`

Verified with:

```bash
cat /etc/group
```

---

### 3) Group Assignment

Configured memberships:

| User      | Groups                   |
| --------- | ------------------------ |
| tokyo     | developers, project-team |
| berlin    | developers, admins       |
| professor | admins                   |
| nairobi   | project-team             |

Verified with:

```bash
groups <username>
```

---

### 4) Shared Directory Permissions

Configured:

```text
/opt/dev-project
/opt/team-workspace
```

Permissions:

```bash
775
```

Ownership:

- Group ownership assigned correctly
- Group members allowed collaborative access

---

### 5) Troubleshooting & Fixes

During testing, encountered:

## Permission Denied

Cause:

- Incorrect directory permissions (`754` / `755`)

Fix:

```bash
chmod 775 <directory>
```

---

## Shell Redirection Issue

Problem:

```bash
sudo -u user echo "text" >> file
```

Did not work as expected.

Reason:

- `>>` is handled by shell, not `sudo`

Correct fix:

```bash
echo "text" | sudo -u user tee -a file
```

This is an important Linux behavior for automation and scripting.

---

## Project Structure

```text
day-09/
├── README.md
├── day-09-user-management.md
├── referance.md
└── screenshots/
```

---

## Key Learnings

- Difference between `usermod -G` and `usermod -aG`
- Importance of correct permissions (`775`)
- Group ownership with `chgrp`
- Shell redirection behavior with privilege escalation
- Real-world access control debugging

---

## DevOps Relevance

Linux permissions directly affect:

- Deployments
- Build pipelines
- Shared workspaces
- SSH access
- Container volume mounts
- Application logging
- Security hardening

Understanding this deeply prevents production incidents.

---

## Commands Practiced

```bash
useradd
passwd
groupadd
usermod
groups
mkdir
chgrp
chmod
touch
tee
ls -ld
```

---

## Outcome

Completed a practical Linux user & group management lab and gained hands-on experience with **access control, permissions, and troubleshooting**, which are essential skills for DevOps and Cloud Engineering.
