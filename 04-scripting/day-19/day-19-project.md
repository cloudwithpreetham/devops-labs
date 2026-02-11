# Day 19 – Shell Scripting Project: Log Rotation, Backup & Crontab

## Overview

On Day 19, I worked on a shell scripting mini project focused on real-world DevOps maintenance tasks.

This project covers:

- Log rotation automation
- Server backup automation
- Crontab scheduling
- Scheduled maintenance scripting
- Error handling using shell scripts

---

## Project Structure

```bash
04-scripting/day-19/
├── screenshots/
├── scripts/
│   ├── backup.sh
│   ├── log_rotate.sh
│   └── maintenance.sh
├── test-backup/
│   └── backup-2026-05-25.tar.gz
├── test-logs/
│   └── app.log
├── test-source/
│   └── file.txt
├── day-19-project.md
└── task.md
```

---

## Task 1: Log Rotation Script

### Script Name

`log_rotate.sh`

### Purpose

The purpose of this script is to rotate application logs by compressing old `.log` files and deleting old `.gz` files. This helps reduce disk usage and keeps the log directory clean.

### Script Code

```bash
#!/bin/bash

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <log_directory>"
    exit 1
fi

LOG_DIR="$1"

if [ ! -d "$LOG_DIR" ]; then
    echo "Error: Directory does not exist: $LOG_DIR"
    exit 1
fi

echo "Starting log rotation for: $LOG_DIR"

COMPRESSED_COUNT=$(find "$LOG_DIR" -type f -name "*.log" -mtime +7 | wc -l)
find "$LOG_DIR" -type f -name "*.log" -mtime +7 -exec gzip {} \;

DELETED_COUNT=$(find "$LOG_DIR" -type f -name "*.gz" -mtime +30 | wc -l)
find "$LOG_DIR" -type f -name "*.gz" -mtime +30 -delete

echo "Log rotation completed"
echo "Files compressed: $COMPRESSED_COUNT"
echo "Old compressed files deleted: $DELETED_COUNT"
```

### Commands Used

```bash
chmod +x scripts/log_rotate.sh
./scripts/log_rotate.sh test-logs/
```

### Sample Output

```bash
Starting log rotation for: test-logs/
Log rotation completed
Files compressed: 0
Old compressed files deleted: 0
```

### Explanation

This script performs the following steps:

1. Checks whether exactly one argument is passed.
2. Stores the log directory path in the `LOG_DIR` variable.
3. Validates whether the given directory exists.
4. Compresses `.log` files older than 7 days using `gzip`.
5. Deletes `.gz` files older than 30 days.
6. Prints the number of compressed and deleted files.

---

## Task 2: Server Backup Script

### Script Name

`backup.sh`

### Purpose

The purpose of this script is to create a compressed backup archive of a source directory and store it in a backup destination directory.

### Script Code

```bash
#!/bin/bash

set -euo pipefail

if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_directory> <backup_destination>"
    exit 1
fi

SOURCE_DIR="$1"
BACKUP_DEST="$2"
DATE=$(date +%Y-%m-%d)
BACKUP_NAME="backup-$DATE.tar.gz"
BACKUP_PATH="$BACKUP_DEST/$BACKUP_NAME"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory does not exist: $SOURCE_DIR"
    exit 1
fi

if [ ! -d "$BACKUP_DEST" ]; then
    echo "Backup destination does not exist. Creating: $BACKUP_DEST"
    mkdir -p "$BACKUP_DEST"
fi

echo "Starting backup"
echo "Source: $SOURCE_DIR"
echo "Destination: $BACKUP_PATH"

tar -czf "$BACKUP_PATH" "$SOURCE_DIR"

if [ -f "$BACKUP_PATH" ]; then
    BACKUP_SIZE=$(du -h "$BACKUP_PATH" | awk '{print $1}')
    echo "Backup created successfully"
    echo "Archive name: $BACKUP_NAME"
    echo "Archive size: $BACKUP_SIZE"
else
    echo "Error: Backup failed"
    exit 1
fi

OLD_BACKUPS_COUNT=$(find "$BACKUP_DEST" -type f -name "backup-*.tar.gz" -mtime +14 | wc -l)
find "$BACKUP_DEST" -type f -name "backup-*.tar.gz" -mtime +14 -delete

echo "Old backups deleted: $OLD_BACKUPS_COUNT"
echo "Backup process completed"
```

### Commands Used

```bash
chmod +x scripts/backup.sh
./scripts/backup.sh test-source/ test-backup/
```

### Sample Output

```bash
Starting backup
Source: test-source/
Destination: test-backup//backup-2026-05-25.tar.gz
Backup created successfully
Archive name: backup-2026-05-25.tar.gz
Archive size: 4.0K
Old backups deleted: 0
Backup process completed
```

### Explanation

This script performs the following steps:

1. Checks whether two arguments are provided.
2. Stores the source directory and backup destination in variables.
3. Creates a timestamped backup name using the current date.
4. Validates whether the source directory exists.
5. Creates the backup destination directory if it does not exist.
6. Creates a `.tar.gz` archive using the `tar` command.
7. Verifies that the archive was created successfully.
8. Prints the archive name and size.
9. Deletes backups older than 14 days.

---

## Task 3: Crontab

### Command to Check Existing Cron Jobs

```bash
crontab -l
```

### Cron Syntax

```bash
* * * * * command
│ │ │ │ │
│ │ │ │ └── Day of week 0-7
│ │ │ └──── Month 1-12
│ │ └────── Day of month 1-31
│ └──────── Hour 0-23
└────────── Minute 0-59
```

---

## Cron Entries

### Run `log_rotate.sh` every day at 2 AM

```bash
0 2 * * * /home/ubuntu/04-scripting/day-19/scripts/log_rotate.sh /var/log/myapp
```

### Run `backup.sh` every Sunday at 3 AM

```bash
0 3 * * 0 /home/ubuntu/04-scripting/day-19/scripts/backup.sh /home/ubuntu/myapp /home/ubuntu/backups
```

### Run a health check script every 5 minutes

```bash
*/5 * * * * /home/ubuntu/04-scripting/day-19/scripts/health_check.sh
```

### Important Note

These cron entries are documented for learning. Before applying them using `crontab -e`, the file paths should be updated based on the actual project location.

---

## Task 4: Scheduled Maintenance Script

### Script Name

`maintenance.sh`

### Purpose

The purpose of this script is to combine log rotation and backup automation into one scheduled maintenance workflow.

### Script Code

```bash
#!/bin/bash

set -euo pipefail

LOG_FILE="/var/log/maintenance.log"

LOG_DIR="/var/log/myapp"
SOURCE_DIR="/home/ubuntu/myapp"
BACKUP_DEST="/home/ubuntu/backups"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | sudo tee -a "$LOG_FILE" > /dev/null
}

run_log_rotation() {
    log_message "Starting log rotation"

    if ./log_rotate.sh "$LOG_DIR" >> /tmp/log_rotate_output.log 2>&1; then
        while read -r line; do
            log_message "$line"
        done < /tmp/log_rotate_output.log

        log_message "Log rotation completed successfully"
    else
        log_message "Log rotation failed"
        cat /tmp/log_rotate_output.log | while read -r line; do
            log_message "$line"
        done
    fi

    rm -f /tmp/log_rotate_output.log
}

run_backup() {
    log_message "Starting server backup"

    if ./backup.sh "$SOURCE_DIR" "$BACKUP_DEST" >> /tmp/backup_output.log 2>&1; then
        while read -r line; do
            log_message "$line"
        done < /tmp/backup_output.log

        log_message "Backup completed successfully"
    else
        log_message "Backup failed"
        cat /tmp/backup_output.log | while read -r line; do
            log_message "$line"
        done
    fi

    rm -f /tmp/backup_output.log
}

log_message "Scheduled maintenance started"

run_log_rotation
run_backup

log_message "Scheduled maintenance finished"
```

### Cron Entry to Run Maintenance Daily at 1 AM

```bash
0 1 * * * /home/ubuntu/04-scripting/day-19/scripts/maintenance.sh
```

### Explanation

This script performs the following steps:

1. Defines a maintenance log file.
2. Defines paths for logs, source directory, and backup destination.
3. Uses a function to write timestamped log messages.
4. Runs the log rotation script.
5. Runs the backup script.
6. Stores output in `/var/log/maintenance.log`.

---

## Testing Performed

### Syntax Check

```bash
bash -n scripts/log_rotate.sh
bash -n scripts/backup.sh
bash -n scripts/maintenance.sh
```

### Permission Setup

```bash
chmod +x scripts/log_rotate.sh
chmod +x scripts/backup.sh
chmod +x scripts/maintenance.sh
```

### Test Log Rotation

```bash
./scripts/log_rotate.sh test-logs/
```

### Test Backup

```bash
./scripts/backup.sh test-source/ test-backup/
```

---

## What I Learned

1. Log rotation is important for managing disk usage on Linux servers.

2. Backup scripts help automate data protection and reduce manual operational work.

3. Crontab is useful for scheduling repeated DevOps maintenance tasks automatically.

---

## Real-World DevOps Use Case

In real production environments, DevOps engineers use scripts like these to automate routine maintenance tasks such as:

- Compressing old application logs
- Deleting outdated archives
- Creating scheduled backups
- Running health checks
- Reducing manual server maintenance

This project helped me understand how shell scripts and cron jobs work together in real DevOps operations.

---

## Conclusion

Day 19 helped me practice practical shell scripting by building a log rotation script, a backup script, and a scheduled maintenance workflow.

These tasks are useful in real DevOps roles because automation improves consistency, saves time, and keeps systems clean and reliable.
