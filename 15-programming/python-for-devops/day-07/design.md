# Day 07 – Thinking Before Coding

## Script Selected

I selected my **Day 06 Log Analyzer CLI Tool**.

Script name:

```bash
log_analyzer_cli.py
```

---

## What Problem Am I Solving?

In real DevOps work, logs are checked regularly to understand application health.

Manually reading large log files takes time and can lead to missed errors.

This script helps by:

- Reading an application log file
- Counting important log levels
- Showing a clear summary
- Saving the summary into an output file

The main goal is to make log checking faster and easier.

---

## What Input Does My Script Need?

The script needs input from the user through command-line arguments.

### Required Inputs

#### 1. Log file path

The user gives the log file that should be analyzed.

Example:

```bash
--file app.log
```

#### 2. Output file path

The user gives the file where the summary should be saved.

Example:

```bash
--out summary.txt
```

### Optional Input

#### 3. Log level filter

The user can give a specific log level if they only want to check one type of message.

Example:

```bash
--level ERROR
```

---

## What Output Should My Script Give?

The script should give output in two places:

### 1. Terminal Output

The script should print a summary on the terminal so the user can quickly see the result.

Example:

```bash
Log Summary
INFO: 10
WARNING: 3
ERROR: 5
```

### 2. Output File

The same summary should be written into an output file.

Example file:

```bash
summary.txt
```

This is useful because the result can be saved for documentation or later review.

---

## What Are the Main Steps?

The script should follow these steps:

1. Accept command-line arguments from the user
2. Read the log file provided by the user
3. Check each line in the log file
4. Count log levels such as:
   - INFO
   - WARNING
   - ERROR

5. If a log level filter is provided, show only that level
6. Prepare a clean summary
7. Print the summary on the terminal
8. Write the summary into the output file
9. Handle errors properly if:
   - The file does not exist
   - The user gives wrong arguments
   - The output file cannot be written

---

## User Thinking

Before writing automation, I should think clearly:

### User kya dega?

The user will give:

- Log file path
- Output file path
- Optional log level filter

### Script kya karega?

The script will:

- Read the log file
- Analyze log messages
- Count log levels
- Generate a summary

### Output kaisa dikhega?

The output should be simple and readable.

It should be visible in:

- Terminal
- Output file

---

## Why Planning Is Important

Planning before coding helps me understand the problem clearly.

In DevOps, automation should not be written randomly because bad automation can break systems.

A good DevOps engineer should first understand:

- The problem
- The inputs
- The expected output
- The steps needed to solve it

After that, writing code becomes easier and cleaner.

---

## Final Summary

Today I did not write code.

I planned how my log analyzer CLI tool should work before coding.

This helped me understand the DevOps mindset:

```text
Think first, automate later.
```

---
