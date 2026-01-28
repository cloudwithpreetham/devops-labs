# Day 05 – Linux Troubleshooting Drill: CPU, Memory, and Logs

## Overview

Day 05 focused on building a **repeatable Linux troubleshooting workflow** by inspecting a live service, analyzing system health, reviewing logs, and documenting findings in a practical runbook.

The target service chosen for this drill was:

**SSH (`sshd`)**

This exercise simulated a real-world DevOps troubleshooting scenario where the objective was to collect evidence first, analyze signals, and take corrective action safely.

---

## Objectives

- Capture a quick system health snapshot
- Check CPU and memory utilization
- Validate disk usage and log storage
- Inspect network ports and connectivity
- Review service logs
- Perform process-level debugging
- Identify security gaps
- Document findings in a reusable runbook

---

## Commands Practiced

### Environment

```bash
uname -a
cat /etc/os-release
```

### Filesystem

```bash
mkdir /tmp/runbook-demo
cp /etc/hosts /tmp/runbook-demo/hosts-copy
```

### CPU / Memory

```bash
top
free -h
ps -o pid,pcpu,pmem,comm -p <pid>
```

### Disk / IO

```bash
df -h
sudo du -sh /var/log
```

### Network

```bash
ss -tulpn
ping -c 3 localhost
```

### Logs

```bash
journalctl -u ssh -n 50
tail -n 50 /var/log/auth.log
```

### Advanced Debugging

```bash
sudo strace -p <pid>
```

### Security

```bash
sudo ufw allow 22
sudo ufw enable
sudo ufw status
```

---

## Key Findings

- CPU utilization was healthy with system mostly idle
- Memory usage remained stable with sufficient available memory
- Disk usage was low with healthy free space
- SSH service was actively listening on port `22`
- Logs showed normal activity with no authentication failures
- Process tracing confirmed `sshd` was idle and functioning normally
- Firewall was initially inactive and was securely enabled during troubleshooting

---

## Practical Learning

This drill reinforced an important troubleshooting workflow:

**Observe → Validate → Investigate → Fix → Verify**

Instead of restarting services blindly, the focus was on:

- collecting evidence,
- understanding behavior,
- then taking action.

This is a core DevOps incident response habit.

---

## Repository Structure

```text
day-05/
├── screenshots/
├── day-05-linux-troubleshooting-runbook.md
├── reference.md
└── README.md
```

---

## Outcome

Completed a structured Linux troubleshooting drill and created a reusable runbook for future debugging scenarios involving CPU, memory, disk, networking, logs, and service-level investigation.

---

**Day 05 Completed**
