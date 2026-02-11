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
