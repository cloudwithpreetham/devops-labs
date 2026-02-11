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
