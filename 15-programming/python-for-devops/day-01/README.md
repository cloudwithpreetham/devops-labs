# Day 01 – Introduction to Python for DevOps

## Overview

Today’s task was to create a simple Python script for checking basic system health.

The script takes threshold values from the user for CPU, memory, and disk usage. It then uses the `psutil` Python library to fetch the current system metrics and compares those values with the user-defined thresholds.

This task helped me understand how Python can be used in DevOps for basic automation, monitoring, and troubleshooting.

---

## Task Requirement

The goal was to write a Python script that:

- Takes CPU, memory, and disk threshold values from user input
- Fetches real system metrics using the `psutil` library
- Compares actual usage against threshold values
- Prints the result clearly in the terminal

---

## Tools and Technologies Used

- Python
- psutil
- Linux Terminal
- VS Code
- Git
- GitHub
- Python virtual environment

---

## Project Structure

```bash
day-01/
├── reference.md
└── system_health.py
```

---

## Python Library Used

The script uses the `psutil` library to fetch system metrics.

Install `psutil` using:

```bash
pip install psutil
```

If using Python 3:

```bash
pip3 install psutil
```

---

## Script Name

```bash
system_health.py
```

---

## How the Script Works

The script follows this flow:

1. Displays a title: `DevOps System Health Checker`
2. Takes CPU threshold input from the user
3. Takes memory threshold input from the user
4. Takes disk threshold input from the user
5. Fetches current CPU usage using `psutil.cpu_percent()`
6. Fetches current memory usage using `psutil.virtual_memory()`
7. Fetches current disk usage using `psutil.disk_usage()`
8. Compares each metric with the given threshold
9. Prints whether each metric is normal or above the threshold

---

## Command Used to Run the Script

```bash
cd day-01/
python system_health.py
```

---

## Terminal Input Used

```bash
Enter CPU threshold percentage: 10
Enter Memory threshold percentage: 30
Enter Disk threshold percentage: 50
```

---

## Terminal Output

```bash
DevOps System Health Checker
--------------------------------
Enter CPU threshold percentage: 10
Enter Memory threshold percentage: 30
Enter Disk threshold percentage: 50

========== System Health Report ==========

CPU Usage: 1.4%
CPU Threshold: 10.0%
Status: OK - CPU usage is normal

Memory Usage: 26.9%
Memory Threshold: 30.0%
Status: OK - Memory usage is normal

Disk Usage: 23.0%
Disk Threshold: 50.0%
Status: OK - Disk usage is normal
```

---

## Output Screenshot

The script was executed successfully from the terminal, and the output showed that CPU, memory, and disk usage were all within the given threshold limits.

Suggested screenshot file name:

```bash
day-01-python-system-health-output.png
```

---

## Concepts Practiced

### User Input

Used `input()` to take CPU, memory, and disk threshold values from the user.

### Functions

Used functions to organize the script and keep the code clean.

### Conditional Statements

Used `if / else` conditions to decide whether each metric is normal or above the threshold.

### Loops

Used loops to process system metrics and display results without repeating code manually.

### System Monitoring

Used `psutil` to fetch real-time system information such as:

- CPU usage
- Memory usage
- Disk usage

---

## Why This Matters in DevOps

DevOps engineers often write scripts to automate checks and monitor servers.

This script is a small but practical example of how Python can help with:

- Checking server health
- Monitoring resource usage
- Validating system conditions
- Supporting troubleshooting
- Building future automation workflows

This is a basic foundation for monitoring and alerting in real DevOps environments.

---

## Key Learning

Today I learned how to use Python for a real DevOps-style task.

I practiced taking user input, fetching system metrics, comparing values with thresholds, and printing a clear health report in the terminal.

This helped me understand how small automation scripts can support monitoring and reliability in DevOps work.

---

## Conclusion

Day 01 introduced me to Python scripting for DevOps.

I created a simple system health checker that takes user-defined thresholds, checks current CPU, memory, and disk usage, and prints a clean terminal report.

This is my first step toward using Python for DevOps automation and system monitoring.
