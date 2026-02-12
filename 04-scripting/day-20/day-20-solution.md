# Day 20 – Bash Scripting Challenge: Log Analyzer and Report Generator

## Objective

The objective of this task was to create a Bash script named `log_analyzer.sh` that analyzes a log file and generates a daily summary report.

This challenge helped me practice real-world log analysis using Bash and common Linux command-line tools.

---

## Project Structure

```bash
day-20/
├── screenshots/
├── scripts/
│   ├── archive/
│   ├── log_analyzer.sh
│   └── log_report_2026-02-11.txt
├── day-20-solution.md
├── README.md
└── task.md
```

---

## Script: `scripts/log_analyzer.sh`

```bash
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
```

---

## Steps Performed

### 1. Input Validation

The script first checks whether the user provided a log file as an argument.

```bash
if [ $# -eq 0 ]; then
    echo "Error: No log file provided."
    echo "Usage: $0 <log_file>"
    exit 1
fi
```

If no file is provided, the script exits with a clear error message.

---

### 2. File Existence Check

The script checks whether the given log file exists.

```bash
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: File '$LOG_FILE' does not exist."
    exit 1
fi
```

This prevents the script from running on an invalid file path.

---

### 3. Total Lines Processed

The total number of lines in the log file is counted using `wc -l`.

```bash
TOTAL_LINES=$(wc -l < "$LOG_FILE")
```

---

### 4. Error Count

The script counts all lines containing either `ERROR` or `Failed`.

```bash
ERROR_COUNT=$(grep -Ei "ERROR|Failed" "$LOG_FILE" | wc -l)
```

The `-E` option enables extended regex, and `-i` makes the search case-insensitive.

---

### 5. Critical Events

Critical events are searched using `grep -n`, which also prints the line number.

```bash
grep -n "CRITICAL" "$LOG_FILE"
```

The output is formatted using `awk`.

```bash
awk -F: '{print "Line " $1 ": " substr($0, index($0,$2))}'
```

---

### 6. Top 5 Error Messages

The script extracts all lines containing `ERROR`, removes the timestamp fields, sorts the messages, counts duplicate messages, and displays the top 5.

```bash
grep "ERROR" "$LOG_FILE" \
    | awk '{$1=$2=""; sub(/^ +/, ""); print}' \
    | sort \
    | uniq -c \
    | sort -rn \
    | head -5
```

---

### 7. Report Generation

A report file is generated using the current date.

```bash
ANALYSIS_DATE=$(date +%Y-%m-%d)
REPORT_FILE="log_report_${ANALYSIS_DATE}.txt"
```

Example output file:

```bash
log_report_2026-02-11.txt
```

---

### 8. Archive Processed Logs

After analysis, the script creates an `archive/` directory and moves the processed log file into it.

```bash
mkdir -p archive
mv "$LOG_FILE" archive/
```

---

## Sample Output

```bash
Log Analysis Started
Log File: sample_log.log
Date: 2026-02-11
Total Lines Processed: 20
Total Error Count: 15

--- Critical Events ---
Line 8: 2026-02-11 09:30:40 CRITICAL Disk space below threshold
Line 13: 2026-02-11 10:00:01 CRITICAL Database connection lost

--- Top 5 Error Messages ---
5 ERROR Connection timed out
2 ERROR File not found
2 ERROR Permission denied
1 ERROR Disk I/O error
1 ERROR Out of memory

Summary report generated: log_report_2026-02-11.txt
Processed log file moved to archive/
```

---

## Generated Report Example

```bash
Daily Log Analysis Report
=========================

Date of Analysis: 2026-02-11
Log File Name: sample_log.log
Total Lines Processed: 20
Total Error Count: 15

--- Top 5 Error Messages ---
5 ERROR Connection timed out
2 ERROR File not found
2 ERROR Permission denied
1 ERROR Disk I/O error
1 ERROR Out of memory

--- Critical Events ---
Line 8: 2026-02-11 09:30:40 CRITICAL Disk space below threshold
Line 13: 2026-02-11 10:00:01 CRITICAL Database connection lost
```

---

## Commands and Tools Used

### `grep`

Used to search for matching keywords inside the log file.

```bash
grep "ERROR" sample_log.log
```

### `grep -n`

Used to print matching lines with their line numbers.

```bash
grep -n "CRITICAL" sample_log.log
```

### `grep -Ei`

Used to search for multiple patterns in a case-insensitive way.

```bash
grep -Ei "ERROR|Failed" sample_log.log
```

### `awk`

Used to format output and remove timestamp fields.

```bash
awk '{$1=$2=""; sub(/^ +/, ""); print}'
```

### `sort`

Used to arrange similar error messages together.

```bash
sort
```

### `uniq -c`

Used to count duplicate error messages.

```bash
uniq -c
```

### `sort -rn`

Used to sort the counted messages in descending numerical order.

```bash
sort -rn
```

### `head -5`

Used to display only the top 5 error messages.

```bash
head -5
```

### `wc -l`

Used to count total lines in the log file.

```bash
wc -l < sample_log.log
```

### `mkdir -p`

Used to create the archive directory safely.

```bash
mkdir -p archive
```

### `mv`

Used to move the processed log file into the archive directory.

```bash
mv sample_log.log archive/
```

---

## What I Learned

1. I learned how to build a practical Bash script that accepts command-line arguments and validates input.
2. I learned how to use Linux text-processing tools like `grep`, `awk`, `sort`, `uniq`, and `wc` for log analysis.
3. I learned how to generate automated summary reports and archive processed files using Bash.

---

## Real-World DevOps Use Case

Log analysis is a common responsibility for DevOps engineers and system administrators. Scripts like this can help quickly identify failures, critical events, and repeated error patterns from application or system logs.

In real environments, this script can be extended to:

- Run automatically using `cron`
- Analyze multiple logs from different servers
- Send reports through email
- Upload reports to AWS S3
- Integrate with monitoring and alerting tools

---

## Final Status

Day 20 Bash scripting challenge completed successfully.
