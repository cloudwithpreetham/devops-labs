# Day 06 – Linux Fundamentals: Read and Write Text Files

## Overview

Day 06 focused on practicing basic Linux file input/output operations using fundamental commands.

The goal was to understand how to:

- Create files
- Write content into files
- Append new content
- Read complete or partial file contents
- Use Linux utilities for efficient text handling

These are essential day-to-day skills for log inspection, configuration management, and troubleshooting in DevOps environments.

---

## Objectives Completed

- Created a file using `touch`
- Wrote content using `>`
- Appended content using `>>`
- Used `tee -a` to write and display output simultaneously
- Read file content using `cat`
- Inspected first lines using `head`
- Inspected last lines using `tail`
- Counted lines using `wc -l`

---

## Commands Practiced

```bash
touch notes.txt
echo "Line 1 - Learning file operations" > notes.txt
echo "Line 2 - Using append operator" >> notes.txt
echo "Line 3 - Using tee command" | tee -a notes.txt

cat notes.txt
head -n 2 notes.txt
tail -n 2 notes.txt
wc -l notes.txt
```

---

## Key Learnings

### `>`

Overwrites file content.

Example:

```bash
echo "Hello" > file.txt
```

Output:

```text
Hello
```

---

### `>>`

Appends content without deleting existing data.

Example:

```bash
echo "World" >> file.txt
```

Output:

```text
Hello
World
```

---

### `tee -a`

Appends content and prints output to terminal simultaneously.

Example:

```bash
echo "New line" | tee -a file.txt
```

---

### `cat`

Displays full file content.

---

### `head`

Displays first few lines.

---

### `tail`

Displays last few lines.

---

## Real DevOps Usage

These commands are heavily used for:

- Viewing application logs
- Appending log entries
- Updating configuration files
- Reading service outputs
- Quick debugging in Linux servers
- Monitoring logs with `tail -f`

Example:

```bash
tail -f /var/log/syslog
```

---

## Project Files

```text
day-06/
├── screenshots/
├── day-06-file-io-practice.md
├── referance.md
└── README.md
```

---

## Outcome

This practice strengthened my Linux fundamentals around file handling and text operations, which are core skills required in DevOps for automation, troubleshooting, and system administration.

---

## Tags

#Linux #DevOps #90DaysOfDevOps #FileHandling #CLI #CloudEngineering
