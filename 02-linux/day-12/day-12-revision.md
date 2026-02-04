# Day 12 – Revision & Consolidation (Days 01–11)

## Objective

Reinforce core Linux and DevOps fundamentals learned in the first 11 days by revisiting key concepts and performing small hands-on checks.

---

## Mindset & Plan Review (Day 01)

- Goal: Become job-ready DevOps Engineer in 90 days
- Focus areas:
  - Linux fundamentals
  - System operations
  - File permissions

- Improvements needed:
  - Faster command recall
  - More troubleshooting practice

- Plan update:
  - Add 10 minutes daily revision before new learning

---

## Processes & Services Check (Day 04/05)

### Commands Practiced

```bash
ps aux | head
systemctl status nginx
journalctl -u nginx --no-pager | tail
```

### Observations

- `ps aux` shows all running processes with CPU and memory usage
- `systemctl status` shows whether a service is active or failed
- `journalctl` helps debug issues using logs

---

## File Operations Practice (Days 06–11)

### Commands Executed

```bash
echo "DevOps Practice" >> notes.txt
chmod 644 notes.txt
chown ubuntu:ubuntu notes.txt
cp notes.txt backup.txt
mkdir test-dir
```

### Key Learnings

- `>>` appends content safely
- `chmod 644` is a safe default for files
- Ownership matters for access control
- Always verify changes using `ls -l`

---

## Cheat Sheet – Top Commands (Day 03)

```bash
ls -l
ps aux
top
systemctl status <service>
journalctl -u <service>
```

### Why These?

- Quick system inspection
- Service health checks
- Fast debugging

---

## User & Group Practice (Day 09/11)

### Commands Executed

```bash
sudo useradd -m devuser
sudo passwd devuser
sudo chown devuser:devuser notes.txt
id devuser
ls -l notes.txt
```

### Verification

- `id` confirms user and group details
- `ls -l` confirms ownership changes

---

## Mini Self-Check

### 1) 3 Commands That Save Time

- `ls -l` → check permissions and ownership
- `systemctl status` → check service status
- `journalctl -u` → view logs for debugging

---

### 2) How to Check Service Health

```bash
systemctl status nginx
ps aux | grep nginx
journalctl -u nginx
```

---

### 3) Safe Ownership & Permission Change

```bash
sudo chown devuser:devuser file.txt
chmod 644 file.txt
```

---

### 4) Focus for Next 3 Days

- Master file permissions (numeric and symbolic)
- Improve log-based debugging
- Practice Linux troubleshooting scenarios

---

## Key Takeaways

- Avoid `chmod 777`
- Logs are critical for debugging
- Ownership and permissions both matter
- Practice builds confidence

---

## Summary

Day 12 focused on strengthening Linux fundamentals, improving troubleshooting skills, and reinforcing essential DevOps practices.

Consistency and revision are helping build a strong foundation for upcoming advanced topics.
