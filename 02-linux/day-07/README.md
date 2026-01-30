# Day 07 – Linux File System Hierarchy & Scenario-Based Practice

## Overview

Day 07 focused on understanding the **Linux File System Hierarchy (FHS)** and applying Linux fundamentals through **real-world troubleshooting scenarios**.

This practice helped strengthen my understanding of:

- Where important files and directories live in Linux
- How to troubleshoot system services
- How to inspect logs using `journalctl`
- How to identify CPU-heavy processes
- How Linux file permissions affect execution
- How to approach incidents step-by-step like a DevOps engineer

---

## Topics Covered

### 1) Linux File System Hierarchy

Studied essential directories and their practical use cases:

| Directory  | Purpose                         |
| ---------- | ------------------------------- |
| `/`        | Root of the Linux filesystem    |
| `/home`    | User home directories           |
| `/root`    | Root user's home directory      |
| `/etc`     | Configuration files             |
| `/var/log` | System & application logs       |
| `/tmp`     | Temporary files                 |
| `/bin`     | Essential binaries              |
| `/usr/bin` | User command binaries           |
| `/opt`     | Optional / third-party software |

---

## Scenario-Based Troubleshooting

### Service Not Starting

Commands practiced:

```bash
sudo systemctl status <service>
systemctl is-enabled <service>
journalctl -u <service> -n 50
sudo systemctl restart <service>
```

Learned:

- How to inspect service health
- How to verify boot startup
- How to read service logs

---

### High CPU Usage Investigation

Commands practiced:

```bash
top
ps aux --sort=-%cpu | head -10
```

Learned:

- How to identify CPU-consuming processes
- How to interpret system load
- How to inspect process IDs (PID)

---

### Service Logs Analysis

Commands practiced:

```bash
journalctl -u docker -n 50
journalctl -u docker -f
journalctl -xe
```

Learned:

- How to inspect historical logs
- How to follow logs in real time
- How journald helps in troubleshooting

---

### File Permission Troubleshooting

Commands practiced:

```bash
ls -l
chmod +x backup.sh
./backup.sh
```

Learned:

- Execute permission is required for scripts
- How Linux permissions work
- Safe permission modification practices

---

## Real Hands-on Work Completed

Successfully practiced:

- SSH service inspection
- SSH restart using sudo privileges
- Docker installation & service validation
- Docker log analysis
- CPU monitoring
- Script permission fixing
- Service discovery using systemctl
- Advanced log review using journalctl

---

## Files in This Folder

```text
day-07/
├── screenshots/
├── day-07-linux-fs-and-scenarios.md
├── referance.md
└── README.md
```

---

## Key Takeaways

- Logs are one of the most important troubleshooting tools
- Services may be active but disabled on boot
- Permissions are a common source of script failures
- Step-by-step troubleshooting is better than random debugging
- Understanding Linux internals is foundational for DevOps

---

## Skills Practiced

- Linux Administration
- Service Management
- Log Analysis
- CPU Monitoring
- File Permissions
- Troubleshooting Mindset
- DevOps Fundamentals

---

## Progress

**90 Days of DevOps – Day 07 Completed**

Building Linux fundamentals one day at a time.
