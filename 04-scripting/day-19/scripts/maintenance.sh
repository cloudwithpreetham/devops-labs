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
