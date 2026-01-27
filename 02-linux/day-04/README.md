# Day 04 – Linux Practice: Processes and Services

## Overview

Day 04 focused on hands-on Linux fundamentals by working directly with:

- Process monitoring
- Service inspection using systemd
- Log analysis
- Basic troubleshooting workflow

This exercise helped build operational confidence with commands commonly used by DevOps engineers during production debugging.

---

## Objectives

The goal of this practice was to:

- Understand running processes in Linux
- Inspect active services using `systemctl`
- Analyze logs using `journalctl` and `syslog`
- Follow a troubleshooting workflow
- Connect Linux debugging with cloud infrastructure concepts

---

## Commands Practiced

### Process Commands

```bash
ps aux | head -10
top
```

Learned:

- Process hierarchy
- PID understanding
- CPU / Memory monitoring
- Kernel threads
- System load interpretation

---

### Service Commands

```bash
systemctl list-units --type=service --state=running
systemctl status ssh
```

Learned:

- Active service inspection
- Service health checks
- Service states (`active`, `running`, `failed`)
- Port listening verification

---

### Log Commands

```bash
journalctl -u ssh --no-pager | tail -10
tail -n 20 /var/log/syslog
```

Learned:

- Authentication logs
- Service startup logs
- System-level log inspection
- Root cause discovery using logs

---

## Real Troubleshooting Scenario

### Problem Found

While inspecting system logs, an issue was discovered with **AWS Systems Manager (SSM Agent)**:

```text
AccessDeniedException
EC2RoleProvider Failed to connect
```

### Root Cause

Incorrect IAM configuration:

- Policy attached to IAM User
- No IAM Role attached to EC2 instance

### Fix Applied

Created and attached:

```text
AmazonSSMManagedInstanceCore
```

to EC2 IAM Role.

Restarted service:

```bash
sudo systemctl restart snap.amazon-ssm-agent.amazon-ssm-agent.service
```

### Verification

Logs confirmed:

```text
Successfully connected with instance profile role
Credentials ready
```

Issue resolved successfully.

---

## Key Learnings

- `ps` → static process snapshot
- `top` → real-time monitoring
- `systemctl` → service management
- `journalctl` → service log analysis
- `syslog` → system-wide logging
- Logs reveal root cause faster than assumptions
- IAM Role ≠ IAM User
- EC2 uses temporary credentials via IMDS

---

## Folder Structure

```text
day-04/
├── screenshots/
├── day-04-linux-practice.md
├── README.md
└── referance.md
```

---

## DevOps Takeaway

Production troubleshooting usually follows:

```text
Observe → Investigate → Identify Root Cause → Fix → Verify
```

This day was a practical introduction to that workflow.

---

## Tech Used

- Linux (Ubuntu)
- systemd
- journalctl
- syslog
- AWS EC2
- AWS IAM
- AWS Systems Manager (SSM)

---

## Author

**Preetham**
Building consistency through #90DaysOfDevOps
