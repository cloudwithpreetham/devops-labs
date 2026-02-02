# Day 10 – File Permissions & File Operations

## Files Created

- devops.txt
- notes.txt
- script.sh

### Screenshot

![Task 1 - Create Files](screenshots/1_task1.png)

---

## Permission Changes

### script.sh

- Before: -rw-rw-r--
- After: -rwxrwxr-x
- Action: Added execute permission

### devops.txt

- Before: -rw-rw-r--
- After: -r--r--r--
- Action: Removed write permissions

### notes.txt

- Before: -rw-rw-r--
- After: -rw-r-----
- Action: Set secure permission (640)

### project directory

- Permission: drwxr-xr-x (755)

### Screenshots

![Task 3 - Understand Permissions](screenshots/4_task3.png)

![Task 4 - Modify Permissions](screenshots/5_task4.png)

![Task 4 - Fix](screenshots/7_task4_fix.png)

---

## Commands Used

```bash
touch devops.txt
echo "This is day-10" >> notes.txt
vim script.sh

cat notes.txt
head -n 5 /etc/passwd
tail -n 5 /etc/passwd

chmod +x script.sh
chmod -wx devops.txt
chmod 640 notes.txt

mkdir project
chmod 755 project
```

### Screenshots

![Task 2 - Read Files (1)](screenshots/2_task2.png)

![Task 2 - Read Files (2)](screenshots/3_task2.png)

---

## Key Learnings

1. Linux permissions control file security at user, group, and others level.
2. Execute permission is mandatory to run scripts.
3. Numeric permissions (640, 755) are widely used in real DevOps environments.

---

## Errors Observed

- Writing to read-only file → Permission denied
- Executing without execute permission → Permission denied

### Screenshot

![Task 5 - Test Permissions](screenshots/6_task5.png)
