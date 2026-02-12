#!/bin/bash

set -euo pipefail

# Day 20 - Bash Log Analyzer and Report Generator

if [ $# -eq 0 ]; then
    echo "Error: No log file provided."
    echo "Usage: $0 <log_file>"
    exit 1
fi

LOG_FILE="$1"

if [ ! -f "$LOG_FILE" ]; then
    echo "Error: File '$LOG_FILE' does not exist."
    exit 1
fi

ANALYSIS_DATE=$(date +%Y-%m-%d)
REPORT_FILE="log_report_${ANALYSIS_DATE}.txt"

TOTAL_LINES=$(wc -l < "$LOG_FILE")
ERROR_COUNT=$(grep -Ei "ERROR|Failed" "$LOG_FILE" | wc -l)

echo "Log Analysis Started"
echo "Log File: $LOG_FILE"
echo "Date: $ANALYSIS_DATE"
echo "Total Lines Processed: $TOTAL_LINES"
echo "Total Error Count: $ERROR_COUNT"
echo

echo "--- Critical Events ---"
grep -n "CRITICAL" "$LOG_FILE" | awk -F: '{print "Line " $1 ": " substr($0, index($0,$2))}' || echo "No critical events found."
echo

echo "--- Top 5 Error Messages ---"
grep "ERROR" "$LOG_FILE" \
    | awk '{$1=$2=""; sub(/^ +/, ""); print}' \
    | sort \
    | uniq -c \
    | sort -rn \
    | head -5 || echo "No ERROR messages found."

{
    echo "Daily Log Analysis Report"
    echo "========================="
    echo
    echo "Date of Analysis: $ANALYSIS_DATE"
    echo "Log File Name: $LOG_FILE"
    echo "Total Lines Processed: $TOTAL_LINES"
    echo "Total Error Count: $ERROR_COUNT"
    echo
    echo "--- Top 5 Error Messages ---"

    grep "ERROR" "$LOG_FILE" \
        | awk '{$1=$2=""; sub(/^ +/, ""); print}' \
        | sort \
        | uniq -c \
        | sort -rn \
        | head -5 || echo "No ERROR messages found."

    echo
    echo "--- Critical Events ---"

    grep -n "CRITICAL" "$LOG_FILE" \
        | awk -F: '{print "Line " $1 ": " substr($0, index($0,$2))}' || echo "No critical events found."

} > "$REPORT_FILE"

echo
echo "Summary report generated: $REPORT_FILE"

mkdir -p archive
mv "$LOG_FILE" archive/

echo "Processed log file moved to archive/"
