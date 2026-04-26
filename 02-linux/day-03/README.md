# Day 03 – Linux Commands Practice

## Overview

Day 03 focused on building command-line confidence by practicing essential Linux commands used daily in DevOps and system administration.

The learning objective was to strengthen troubleshooting skills across:

- Process management
- File system navigation
- Networking diagnostics
- Service lifecycle management using systemd

This session also included hands-on work with **Nginx**, covering installation, process verification, port inspection, and service management.

---

## What I Practiced

### Process Management

- Listing running processes using `ps aux`
- Filtering processes with `grep`
- Understanding process termination using `kill` and `kill -9`
- Inspecting service state with `systemctl`

### File System & Logs

- Searching logs with `find`
- Viewing log content using `cat`, `less`, `head`, `tail`
- Live monitoring with `tail -f`
- Understanding Linux log locations under `/var/log`

### Networking Troubleshooting

- Checking connectivity using `ping`
- Inspecting open ports with `ss -tuln`
- Verifying DNS resolution using `dig`
- Testing service accessibility using `curl`

### Service Management

- Installing Nginx
- Verifying master and worker processes
- Confirming port exposure on port `80`
- Stopping and validating service state

---

## Files in This Directory

```text
day-03/
├── screenshots/
├── day-03-linux-commands-cheatsheet.md
├── day-03-linux-commands-practice.md
├── reference.md
└── README.md
```

### File Description

| File                                  | Purpose                                     |
| ------------------------------------- | ------------------------------------------- |
| `day-03-linux-commands-cheatsheet.md` | Quick command reference for troubleshooting |
| `day-03-linux-commands-practice.md`   | Detailed hands-on documentation             |
| `reference.md`                        | Notes/resources used during learning        |
| `screenshots/`                        | Command execution evidence                  |

---

## Key Learnings

- Linux troubleshooting starts with logs
- Real-time monitoring is critical during incidents
- Networking tools quickly identify connectivity issues
- `systemctl` is essential for service management
- Verifying process + port + logs is a standard debugging workflow

---

## Commands Practiced

```bash
find /var/log -name "*.log"
tail -f /var/log/syslog
ps aux | grep nginx
kill -9 <PID>
ss -tuln
ping -c 4 google.com
dig google.com
sudo apt install nginx -y
sudo systemctl stop nginx
sudo systemctl status nginx
```

---

## Real-World DevOps Relevance

These commands are frequently used for:

- Production debugging
- Incident response
- Service verification
- Network troubleshooting
- Application monitoring

Mastering them builds strong operational confidence.

---

## Progress

Day 03 completed successfully with:

- Documentation completed
- Cheatsheet prepared
- Screenshots captured
- Practical Linux troubleshooting performed
- Nginx service lifecycle tested

---

## Next Focus

**Day 04 – Linux Users, Groups, and Permissions**

Topics ahead:

- User creation
- Group management
- File ownership
- chmod / chown
- sudo privileges
- Secure Linux administration
