# 04 - Scripting

This section of my **90 Days of DevOps** journey focuses on shell scripting with Bash.

Shell scripting is an essential DevOps skill because it helps automate repetitive tasks, manage Linux systems, analyze logs, create backups, schedule jobs with cron, and build small operational tools.

---

## Topics Covered

- Shell scripting basics
- Variables and user input
- Conditional statements
- Loops
- Command-line arguments
- Error handling
- Functions
- Strict mode
- Log analysis
- Log rotation
- Backup automation
- Crontab scheduling
- Shell scripting cheat sheet

---

## Project Structure

```bash
04-scripting/
├── day-16/
│   ├── screenshots/
│   ├── scripts/
│   │   ├── check_number.sh
│   │   ├── file_check.sh
│   │   ├── greet.sh
│   │   ├── hello.sh
│   │   ├── server_check.sh
│   │   └── variables.sh
│   ├── README.md
│   └── task.md
├── day-17/
│   ├── screenshots/
│   ├── scripts/
│   │   ├── args_demo.sh
│   │   ├── count.sh
│   │   ├── countdown.sh
│   │   ├── for_loop.sh
│   │   ├── greet.sh
│   │   ├── install_packages.sh
│   │   └── safe_script.sh
│   ├── README.md
│   └── task.md
├── day-18/
│   ├── screenshots/
│   ├── scripts/
│   │   ├── disk_check.sh
│   │   ├── functions.sh
│   │   ├── local_demo.sh
│   │   ├── strict_demo.sh
│   │   └── system_info.sh
│   ├── day-18-scripting.md
│   └── task.md
├── day-19/
│   ├── screenshots/
│   ├── scripts/
│   │   ├── backup.sh
│   │   ├── log_rotate.sh
│   │   └── maintenance.sh
│   ├── day-19-project.md
│   └── task.md
├── day-20/
│   ├── screenshots/
│   ├── scripts/
│   │   ├── log_analyzer.sh
│   │   └── log_report_2026-02-12.txt
│   ├── README.md
│   ├── day-20-solution.md
│   └── task.md
├── day-21/
│   ├── day-21-shell_scripting_cheatsheet.md
│   └── task.md
└── README.md
```

---

## Day-wise Progress

| Day    | Topic                                | Description                                                                                         |
| ------ | ------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Day 16 | Shell Scripting Basics               | Learned shebangs, variables, user input, `echo`, file checks, service checks, and basic conditions. |
| Day 17 | Loops, Arguments, and Error Handling | Practiced loops, command-line arguments, package installation, and basic error handling.            |
| Day 18 | Functions and Intermediate Concepts  | Used functions, local variables, system checks, disk checks, and strict mode.                       |
| Day 19 | Log Rotation, Backup, and Crontab    | Built practical scripts for log rotation, server backup automation, and maintenance tasks.          |
| Day 20 | Log Analyzer Project                 | Created a Bash script to analyze logs and generate summary reports.                                 |
| Day 21 | Shell Scripting Cheat Sheet          | Prepared a personal Bash scripting reference guide.                                                 |

---

## Key Shell Scripting Concepts

### Shebang

```bash
#!/bin/bash
```

The shebang tells the system which interpreter should execute the script.

### Running a Script

```bash
chmod +x script.sh
./script.sh
```

You can also run a script directly with Bash:

```bash
bash script.sh
```

### Variables

```bash
name="DevOps"
echo "Welcome to $name"
```

Variables store reusable values inside scripts.

### User Input

```bash
read -p "Enter your name: " name
echo "Hello, $name"
```

The `read` command takes input from the user.

### Conditions

```bash
if [ "$age" -ge 18 ]; then
    echo "Eligible"
else
    echo "Not eligible"
fi
```

Conditions help scripts make decisions.

### Loops

```bash
for item in linux git docker kubernetes; do
    echo "$item"
done
```

Loops repeat tasks automatically.

### Command-line Arguments

```bash
echo "First argument: $1"
echo "Total arguments: $#"
```

Arguments allow scripts to accept input from the terminal.

### Functions

```bash
greet() {
    echo "Hello, $1"
}

greet "DevOps Engineer"
```

Functions keep scripts clean, reusable, and organized.

### Strict Mode

```bash
set -euo pipefail
```

Strict mode makes scripts safer by stopping execution when errors occur, unset variables are used, or commands in a pipeline fail.

---

## Scripts Built

### Log Rotation Script

Created a script to:

- Accept a log directory as input
- Compress old `.log` files
- Delete old `.gz` files
- Print compressed and deleted file counts
- Validate directory input

### Backup Script

Created a script to:

- Accept source and destination directories
- Create timestamped backup files
- Compress backups using `tar.gz`
- Validate input paths
- Support automation with cron

### Maintenance Script

Created a script to:

- Combine routine maintenance checks
- Reuse log rotation and backup ideas
- Keep operational tasks easier to run repeatedly

### Log Analyzer Script

Created a script to:

- Accept a log file as an argument
- Count `INFO`, `WARNING`, and `ERROR` messages
- Extract top error messages
- Generate a report file
- Handle invalid input safely

---

## Example Commands Used

```bash
chmod +x script.sh
./script.sh
bash script.sh
```

```bash
find /var/log/myapp -name "*.log" -mtime +7
gzip app.log
tar -czf backup.tar.gz /path/to/source
```

```bash
crontab -e
crontab -l
```

---

## Crontab Examples

Run a backup every day at 1 AM:

```bash
0 1 * * * /path/to/backup.sh /source /backup
```

Run log rotation every Sunday at 2 AM:

```bash
0 2 * * 0 /path/to/log_rotate.sh /var/log/myapp
```

---

## Skills Practiced

- Writing executable Bash scripts
- Automating Linux tasks
- Handling script inputs
- Validating files and directories
- Using loops and conditions
- Writing reusable functions
- Creating log reports
- Compressing and archiving files
- Scheduling scripts with cron
- Documenting scripts clearly

---

## DevOps Relevance

Shell scripting is used by DevOps engineers for:

- Server automation
- Log cleanup
- Backup scheduling
- Deployment helper scripts
- Monitoring checks
- System maintenance
- Incident troubleshooting
- CI/CD support tasks

These exercises helped me build a strong foundation for real-world Linux and DevOps automation.

---

## Learning Outcome

By completing Days 16 to 21, I learned how to write practical Bash scripts that solve real system administration problems.

This section improved my confidence in automating Linux tasks and prepared me for advanced DevOps topics like Docker, CI/CD, Kubernetes, and cloud automation.

---

## Author

**Preetham Pereira**
90 Days of DevOps Journey
