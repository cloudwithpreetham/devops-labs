# Day 20 – Bash Scripting Challenge: Log Analyzer and Report Generator

## Overview

This project is part of my 90DaysOfDevOps journey. On Day 20, I built a Bash-based log analyzer that reads a server log file, identifies error-related events, extracts critical events, generates a daily summary report, and archives the processed log file.

The goal of this task is to practice real-world Linux and DevOps automation using shell scripting and common command-line tools.

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

## Files Included

| File/Folder                         | Description                                                                  |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| `scripts/log_analyzer.sh`           | Bash script used to analyze log files                                        |
| `scripts/log_report_2026-02-11.txt` | Generated summary report from the analyzed log                               |
| `scripts/archive/`                  | Directory where processed log files are moved                                |
| `day-20-solution.md`                | Detailed documentation of the approach, commands used, and learning outcomes |
| `task.md`                           | Original Day 20 task description                                             |
| `screenshots/`                      | Screenshots of script execution and output                                   |

---

## What the Script Does

The `log_analyzer.sh` script performs the following tasks:

1. Accepts a log file path as a command-line argument
2. Validates whether the argument is provided
3. Checks whether the given log file exists
4. Counts lines containing `ERROR` or `Failed`
5. Displays critical events containing `CRITICAL` with line numbers
6. Finds the top 5 most common `ERROR` messages
7. Generates a summary report file using the current date
8. Creates an `archive/` directory if it does not exist
9. Moves the processed log file into the archive directory

---

## How to Run

Move into the scripts directory:

```bash
cd day-20/scripts
```

Give executable permission to the script:

```bash
chmod +x log_analyzer.sh
```

Run the script with a log file:

```bash
./log_analyzer.sh sample_log.log
```

Example:

```bash
./log_analyzer.sh sample_log.log
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

## Generated Report

The script creates a report file in the following format:

```bash
log_report_YYYY-MM-DD.txt
```

Example:

```bash
log_report_2026-02-11.txt
```

The report contains:

- Date of analysis
- Log file name
- Total lines processed
- Total error count
- Top 5 error messages
- Critical events with line numbers

---

## Commands Used

| Command    | Purpose                                                       |
| ---------- | ------------------------------------------------------------- |
| `grep`     | Search for keywords such as `ERROR`, `Failed`, and `CRITICAL` |
| `grep -n`  | Display matching lines with line numbers                      |
| `awk`      | Format output and extract required fields                     |
| `sort`     | Sort repeated messages                                        |
| `uniq -c`  | Count duplicate error messages                                |
| `head -5`  | Display top 5 results                                         |
| `wc -l`    | Count total lines in the log file                             |
| `mkdir -p` | Create archive directory safely                               |
| `mv`       | Move processed logs into archive                              |

---

## Key Learnings

- Learned how to validate command-line arguments in Bash scripts
- Practiced log analysis using Linux text-processing commands
- Understood how to generate automated reports from log files
- Learned how to archive processed files after script execution
- Improved confidence in writing practical DevOps automation scripts

---

## Real-World Use Case

DevOps engineers and system administrators often need to analyze server logs to identify failures, errors, and critical system events. This script is a small but practical example of how Bash can be used to automate daily operational checks.

This script can be improved further by:

- Running it daily using `cron`
- Sending the generated report by email
- Uploading reports to AWS S3
- Analyzing multiple log files at once
- Integrating with monitoring tools

---

## Status

Completed Day 20 Bash scripting challenge successfully.
