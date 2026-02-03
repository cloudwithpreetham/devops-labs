# Day 11 – Linux File Ownership (chown & chgrp)

## Overview

On Day 11, I focused on mastering **Linux file ownership and group management**, one of the most important Linux fundamentals for DevOps and system administration.

This hands-on lab covered:

* Understanding file owner and group ownership
* Changing file owner using `chown`
* Changing file group using `chgrp`
* Changing owner + group in one command
* Applying recursive ownership changes using `-R`
* Managing ownership across multi-user and multi-group environments

These concepts are critical in real-world DevOps work for:

* Application deployments
* Log file management
* Shared directories
* CI/CD artifacts
* Container volume permissions
* Linux server security

---

## Files in this Directory

```text
day-11/
├── README.md
├── day-11-file-ownership.md
├── referance.md
└── screenshots/
```

---

## What I Practiced

### Understanding Ownership

Learned Linux ownership format:

```bash
-rw-r--r-- 1 owner group size date filename
```

Example:

```bash
-rw-r--r-- 1 tokyo vault-team 0 Apr 22 access-codes.txt
```

Where:

* **tokyo** → owner
* **vault-team** → group

---

### Owner Changes (`chown`)

Practiced:

```bash
sudo chown tokyo devops-file.txt
sudo chown berlin devops-file.txt
```

Learned:

* Owner controls the file
* Ownership determines permission behavior

---

### Group Changes (`chgrp`)

Practiced:

```bash
sudo chgrp heist-team team-notes.txt
```

Learned:

* Groups enable shared access
* Useful for team collaboration and service accounts

---

### Owner + Group Combined

Practiced:

```bash
sudo chown professor:heist-team project-config.yaml
```

Learned:

* Efficient way to update ownership in one command

---

### Recursive Ownership

Practiced:

```bash
sudo chown -R professor:planners heist-project/
```

Learned:

* `-R` updates all subdirectories and files
* Essential for application folders and deployment directories

---

## Real DevOps Connection

This skill is directly used for:

### Application directories

```bash
sudo chown -R appuser:appgroup /opt/myapp
```

### Log directories

```bash
sudo chown -R appuser:appgroup /var/log/myapp
```

### Jenkins workspace

```bash
sudo chown -R jenkins:jenkins /var/lib/jenkins
```

### Docker mounted volumes

```bash
sudo chown -R 1000:1000 ./data
```

---

## Key Learnings

* Every Linux file has an **owner**
* Every Linux file belongs to a **group**
* `chown` changes ownership
* `chgrp` changes group ownership
* `-R` recursively changes ownership
* Proper ownership prevents permission errors
* Never use unsafe permissions like `777`

---

## Outcome

By completing Day 11, I strengthened my Linux fundamentals and improved my understanding of how ownership and permissions work in production environments.

This is foundational knowledge for becoming job-ready in DevOps.

---

## Tags

`Linux` `DevOps` `System Administration` `Permissions` `Ownership` `chown` `chgrp` `90DaysOfDevOps`
