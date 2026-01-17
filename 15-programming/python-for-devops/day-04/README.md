# Day 04 – File Handling & Log Analysis for DevOps

## Overview

This project focuses on using Python to read files and analyze application logs.

In real DevOps work, logs are one of the first places engineers check while troubleshooting application failures, deployment issues, server errors, or production incidents. This task demonstrates how Python can help automate basic log analysis by reading a log file, counting log levels, and generating a summary report.

## Objective

The goal of this task is to create a Python script that:

- Reads an application log file
- Identifies and counts log levels
- Prints the summary in the terminal
- Writes the summary to an output file
- Handles basic file-related errors

## Project Structure

```text
day-04/
├── app.log
├── log_analyzer.py
├── log_summary.txt
├── README.md
└── task.md
```

## Files Description

| File              | Description                                       |
| ----------------- | ------------------------------------------------- |
| `app.log`         | Sample application log file used as input         |
| `log_analyzer.py` | Python script used to analyze log messages        |
| `log_summary.txt` | Output file generated after running the script    |
| `README.md`       | Documentation for the Day 04 task                 |
| `task.md`    | Additional reference notes and learning resources |

## Log Levels Analyzed

The script checks and counts the following log levels:

| Log Level | Meaning                                             |
| --------- | --------------------------------------------------- |
| `INFO`    | Normal application activity or successful operation |
| `WARNING` | A potential issue that may need attention           |
| `ERROR`   | A failure or problem that needs troubleshooting     |

## Concepts Practiced

- Python file handling
- Reading files using `open()`
- Reading file content using `readlines()`
- String matching and searching
- Using dictionaries to store counts
- Writing output to a file
- Organizing code with functions
- Handling errors using `try / except`
- Following basic PEP8 coding practices

## How the Script Works

The script follows this flow:

1. Reads the `app.log` file.
2. Checks each log line for `INFO`, `WARNING`, and `ERROR`.
3. Stores the count of each log level in a dictionary.
4. Generates a readable summary.
5. Prints the summary in the terminal.
6. Writes the summary to `log_summary.txt`.

## How to Run

Go to the project folder:

```bash
cd day-04
```

Run the Python script:

```bash
python3 log_analyzer.py
```

## Expected Output

```text
Log Analysis Summary
--------------------
INFO messages    : 10
WARNING messages : 2
ERROR messages   : 3
Total log entries: 15

Summary written successfully to 'log_summary.txt'.
```

## Output File

After running the script, the summary is written to:

```text
log_summary.txt
```

You can verify it using:

```bash
cat log_summary.txt
```

## Error Handling

The script handles basic errors such as:

- Missing input log file
- Empty log file
- File writing issues

Example:

```text
Error: The file 'app.log' was not found.
```

## DevOps Relevance

Log analysis is an important DevOps skill because logs help engineers:

- Debug failed applications
- Investigate production incidents
- Monitor system behavior
- Identify recurring errors
- Understand application health
- Automate troubleshooting workflows

This project builds a foundation for future topics like monitoring, alerting, incident response, and observability.

## Learning Summary

In this task, I learned how to use Python to read and process log files. I practiced counting log levels using dictionaries, organizing code into functions, handling basic errors, and writing output to a file. This task helped me understand how Python can be used in DevOps for automation and troubleshooting.

## References

- Python File Handling: [https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- Python String Methods: [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- PEP8 Python Style Guide: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)
