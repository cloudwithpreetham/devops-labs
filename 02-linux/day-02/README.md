# Day 02 – Linux Architecture, Processes, and systemd

## Overview

Day 02 focused on understanding how Linux works under the hood — a foundational skill for DevOps engineering.

The objective was to learn:

- Core Linux architecture
- Process lifecycle and states
- Service management with systemd
- Basic troubleshooting using Linux commands

This knowledge is essential for debugging production systems, managing services, and handling incidents confidently.

---

## Topics Covered

### Linux Architecture

- Kernel
- User Space
- Init Process
- systemd (PID 1)

### Process Management

- Process creation (`fork()`, `exec()`)
- Process IDs (PID / PPID)
- Background processes
- Process states:
  - Running (R)
  - Sleeping (S)
  - Uninterruptible Sleep (D)
  - Zombie (Z)
  - Stopped (T)

### systemd Fundamentals

- Service startup
- Service monitoring
- Restarting failed services
- Log management using journald

---

## Hands-on Practice

### Process Monitoring

Used:

```bash
ps aux
top
```

Observed:

- CPU utilization
- Memory usage
- Running vs sleeping processes
- Process hierarchy

---

### Background Process Creation

Created a test process:

```bash
sleep 1000 &
ps aux | grep sleep
```

Learned:

- Process execution in background
- PID tracking
- Process state identification

---

### Service Management

Checked SSH service:

```bash
systemctl status ssh
```

Learned:

- Active/Inactive states
- Main PID
- Service logs
- Unit files

---

### Log Analysis

Viewed logs:

```bash
journalctl -u ssh -n 20
```

Learned:

- Service startup logs
- SSH connection logs
- Restart activity

---

## Key Commands

```bash
ps aux
top
kill -9 <PID>
systemctl status <service>
journalctl -u <service> -n 20
```

---

## Project Structure

```text
day-02/
├── screenshots/
├── day-02-linux-architecture-notes.md
└── README.md
```

---

## Key Takeaways

- Linux kernel manages system resources
- Most processes remain in sleeping state until needed
- systemd is central to service management
- Logs are critical for troubleshooting
- Understanding processes improves debugging speed

---

## Screenshots Included

- Live process monitoring (`top`)
- Background process creation (`sleep`)
- SSH service status (`systemctl`)
- Service logs (`journalctl`)

---

## DevOps Insight

> In production, many incidents come down to process failures, resource exhaustion, or service misconfiguration.
> Knowing Linux internals makes troubleshooting faster and more effective.

---

## Progress

Completed Day 02 of #90DaysOfDevOps

Focused on building Linux fundamentals through practical hands-on learning.
