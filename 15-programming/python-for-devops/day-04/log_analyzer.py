"""
Day 04 - File Handling & Log Analysis for DevOps

This script reads an application log file, counts log levels,
prints the summary in the terminal, and writes the result to
an output file.
"""


def read_log_file(file_path):
    """
    Read log file content and return all lines.
    Handles file not found and empty file cases.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as log_file:
            lines = log_file.readlines()

        if not lines:
            raise ValueError("The log file is empty.")

        return lines

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

    except ValueError as error:
        print(f"Error: {error}")
        return []


def analyze_logs(log_lines):
    """
    Analyze log lines and count INFO, WARNING, and ERROR messages.
    """
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in log_lines:
        for log_level in log_counts:
            if log_level in line:
                log_counts[log_level] += 1

    return log_counts


def generate_summary(log_counts):
    """
    Generate a readable summary from log count data.
    """
    total_logs = sum(log_counts.values())

    summary = (
        "Log Analysis Summary\n"
        "--------------------\n"
        f"INFO messages    : {log_counts['INFO']}\n"
        f"WARNING messages : {log_counts['WARNING']}\n"
        f"ERROR messages   : {log_counts['ERROR']}\n"
        f"Total log entries: {total_logs}\n"
    )

    return summary


def write_summary(output_file, summary):
    """
    Write the log analysis summary to an output file.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(summary)

        print(f"\nSummary written successfully to '{output_file}'.")

    except OSError as error:
        print(f"Error writing summary file: {error}")


def main():
    """
    Main function to run the log analyzer.
    """
    input_file = "app.log"
    output_file = "log_summary.txt"

    log_lines = read_log_file(input_file)

    if not log_lines:
        return

    log_counts = analyze_logs(log_lines)
    summary = generate_summary(log_counts)

    print(summary)
    write_summary(output_file, summary)


if __name__ == "__main__":
    main()
