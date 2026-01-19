import argparse
from pathlib import Path


class LogAnalyzer:
    """Analyze log files and generate log level summaries."""

    VALID_LEVELS = {"INFO", "WARNING", "ERROR"}

    def __init__(self, file_path, level=None):
        self.file_path = Path(file_path)
        self.level = level.upper() if level else None
        self.summary = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def validate_file(self):
        """Check whether the log file exists."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"Log file not found: {self.file_path}")

        if not self.file_path.is_file():
            raise ValueError(f"Invalid file path: {self.file_path}")

    def analyze_logs(self):
        """Read the log file and count log levels."""
        self.validate_file()

        with self.file_path.open("r", encoding="utf-8") as log_file:
            for line in log_file:
                for log_level in self.summary:
                    if log_level in line:
                        if self.level is None or self.level == log_level:
                            self.summary[log_level] += 1

        return self.summary

    def generate_report(self):
        """Generate formatted summary report."""
        report_lines = ["Log Analysis Summary", "--------------------"]

        if self.level:
            report_lines.append(f"Filtered Level: {self.level}")

        for log_level, count in self.summary.items():
            if self.level is None or self.level == log_level:
                report_lines.append(f"{log_level}: {count}")

        return "\n".join(report_lines)

    def write_report(self, output_path):
        """Write summary report to output file."""
        output_file = Path(output_path)

        with output_file.open("w", encoding="utf-8") as file:
            file.write(self.generate_report())


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="CLI Log Analyzer for DevOps")

    parser.add_argument("--file", required=True, help="Path to the input log file")

    parser.add_argument(
        "--out", default="summary.txt", help="Path to the output summary file"
    )

    parser.add_argument(
        "--level",
        choices=LogAnalyzer.VALID_LEVELS,
        help="Filter logs by level: INFO, WARNING, or ERROR",
    )

    return parser.parse_args()


def main():
    """Main function to run the CLI tool."""
    args = parse_arguments()

    try:
        analyzer = LogAnalyzer(args.file, args.level)
        analyzer.analyze_logs()

        report = analyzer.generate_report()
        print(report)

        analyzer.write_report(args.out)
        print(f"\nSummary written to: {args.out}")

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
