"""
Day 05 - Object-Oriented Python for DevOps

This script analyzes a log file and counts INFO, WARNING, and ERROR messages
using a simple class-based approach.
"""


class LogAnalyzer:
    """A simple log analyzer for counting log levels."""

    def __init__(self, log_file_path, output_file_path):
        self.log_file_path = log_file_path
        self.output_file_path = output_file_path
        self.log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def read_logs(self):
        """Read log lines from the input log file."""
        try:
            with open(self.log_file_path, "r", encoding="utf-8") as log_file:
                return log_file.readlines()
        except FileNotFoundError:
            print(f"Error: Log file not found: {self.log_file_path}")
            return []
        except PermissionError:
            print(f"Error: Permission denied: {self.log_file_path}")
            return []

    def analyze_logs(self, log_lines):
        """Analyze log lines and count log levels."""
        for line in log_lines:
            for log_level in self.log_counts:
                if log_level in line:
                    self.log_counts[log_level] += 1

    def generate_summary(self):
        """Generate a readable summary of log analysis."""
        summary = "Log Analysis Summary\n"
        summary += "--------------------\n"

        for log_level, count in self.log_counts.items():
            summary += f"{log_level}: {count}\n"

        return summary

    def write_summary(self, summary):
        """Write the log summary to an output file."""
        try:
            with open(self.output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(summary)
        except PermissionError:
            print(f"Error: Permission denied: {self.output_file_path}")

    def run(self):
        """Run the complete log analysis workflow."""
        log_lines = self.read_logs()

        if not log_lines:
            return

        self.analyze_logs(log_lines)
        summary = self.generate_summary()

        print(summary)
        self.write_summary(summary)


if __name__ == "__main__":
    analyzer = LogAnalyzer(
        log_file_path="app.log", output_file_path="log_summary.txt"
    )
    analyzer.run()
