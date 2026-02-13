# Day 21 – Shell Scripting Cheat Sheet

## Shell Scripting Quick Reference Guide

This cheat sheet is a practical reference for Bash scripting basics, conditionals, loops, functions, text processing, debugging, and real-world DevOps one-liners.

---

## Quick Reference Table

| Topic        | Key Syntax                | Example                            |          |
| ------------ | ------------------------- | ---------------------------------- | -------- |
| Shebang      | `#!/bin/bash`             | `#!/bin/bash`                      |          |
| Run Script   | `chmod +x script.sh`      | `./script.sh`                      |          |
| Variable     | `VAR="value"`             | `NAME="DevOps"`                    |          |
| Use Variable | `$VAR`                    | `echo "$NAME"`                     |          |
| User Input   | `read VAR`                | `read NAME`                        |          |
| Argument     | `$1`, `$2`                | `./script.sh app.log`              |          |
| Exit Code    | `$?`                      | `echo $?`                          |          |
| If           | `if [ condition ]; then`  | `if [ -f file.txt ]; then`         |          |
| Case         | `case "$var" in`          | `case "$choice" in start)`         |          |
| For Loop     | `for i in list; do`       | `for i in 1 2 3; do`               |          |
| While Loop   | `while [ condition ]; do` | `while [ $count -le 5 ]; do`       |          |
| Function     | `name() { ... }`          | `greet() { echo "Hi"; }`           |          |
| Grep         | `grep pattern file`       | `grep -i "error" app.log`          |          |
| Awk          | `awk '{print $1}' file`   | `awk -F: '{print $1}' /etc/passwd` |          |
| Sed          | `sed 's/old/new/g' file`  | `sed -i 's/foo/bar/g' config.txt`  |          |
| Cut          | `cut -d':' -f1 file`      | `cut -d':' -f1 /etc/passwd`        |          |
| Sort         | `sort file`               | `sort names.txt`                   |          |
| Uniq         | `uniq -c file`            | `sort file                         | uniq -c` |
| WC           | `wc -l file`              | `wc -l app.log`                    |          |
| Debug        | `set -x`                  | `bash -x script.sh`                |          |

---

## 1. Basics

### Shebang

The shebang tells the system which interpreter should run the script.

```bash
#!/bin/bash

echo "Hello, DevOps"
```

Without a shebang, the script may run with a different shell and behave unexpectedly.

---

### Running a Script

Make the script executable:

```bash
chmod +x script.sh
```

Run using relative path:

```bash
./script.sh
```

Run directly with Bash:

```bash
bash script.sh
```

---

### Comments

Comments explain what the script does and make it easier to maintain.

```bash
# This is a single-line comment
echo "Starting script" # Inline comment
```

---

### Variables

Variables store reusable values.

```bash
NAME="DevOps"
echo "$NAME"
```

Always prefer double quotes when using variables.

```bash
FILE="my file.txt"
echo "$FILE"
```

Single quotes do not expand variables.

```bash
NAME="DevOps"
echo '$NAME'
```

Output:

```bash
$NAME
```

---

### Reading User Input

Use `read` to take input from the user.

```bash
#!/bin/bash

echo "Enter your name:"
read NAME

echo "Hello, $NAME"
```

With a prompt:

```bash
read -p "Enter username: " USERNAME
echo "User is $USERNAME"
```

---

### Command-Line Arguments

Arguments are values passed while running the script.

```bash
./script.sh app.log
```

Example:

```bash
#!/bin/bash

echo "Script name: $0"
echo "First argument: $1"
echo "Total arguments: $#"
echo "All arguments: $@"
echo "Last command exit code: $?"
```

| Variable | Meaning                   |
| -------- | ------------------------- |
| `$0`     | Script name               |
| `$1`     | First argument            |
| `$2`     | Second argument           |
| `$#`     | Number of arguments       |
| `$@`     | All arguments             |
| `$?`     | Exit code of last command |

---

## 2. Operators and Conditionals

### String Comparisons

Used to compare text values.

```bash
NAME="DevOps"

if [ "$NAME" = "DevOps" ]; then
  echo "Matched"
fi
```

| Operator | Meaning             |
| -------- | ------------------- |
| `=`      | Equal               |
| `!=`     | Not equal           |
| `-z`     | String is empty     |
| `-n`     | String is not empty |

Examples:

```bash
if [ "$USER" != "root" ]; then
  echo "User is not root"
fi
```

```bash
if [ -z "$NAME" ]; then
  echo "Name is empty"
fi
```

```bash
if [ -n "$NAME" ]; then
  echo "Name is not empty"
fi
```

---

### Integer Comparisons

Used to compare numbers.

```bash
COUNT=10

if [ "$COUNT" -gt 5 ]; then
  echo "Count is greater than 5"
fi
```

| Operator | Meaning               |
| -------- | --------------------- |
| `-eq`    | Equal                 |
| `-ne`    | Not equal             |
| `-lt`    | Less than             |
| `-gt`    | Greater than          |
| `-le`    | Less than or equal    |
| `-ge`    | Greater than or equal |

Example:

```bash
AGE=20

if [ "$AGE" -ge 18 ]; then
  echo "Adult"
else
  echo "Minor"
fi
```

---

### File Test Operators

Used to check files and directories.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `-f`     | File exists              |
| `-d`     | Directory exists         |
| `-e`     | File or directory exists |
| `-r`     | Readable                 |
| `-w`     | Writable                 |
| `-x`     | Executable               |
| `-s`     | File is not empty        |

Examples:

```bash
if [ -f "app.log" ]; then
  echo "File exists"
fi
```

```bash
if [ -d "/var/log" ]; then
  echo "Directory exists"
fi
```

```bash
if [ -s "app.log" ]; then
  echo "File has content"
fi
```

---

### If, Elif, Else

Used to make decisions in scripts.

```bash
#!/bin/bash

STATUS="running"

if [ "$STATUS" = "running" ]; then
  echo "Service is running"
elif [ "$STATUS" = "stopped" ]; then
  echo "Service is stopped"
else
  echo "Unknown status"
fi
```

---

### Logical Operators

Used to combine conditions or commands.

| Operator | Meaning |     |     |
| -------- | ------- | --- | --- |
| `&&`     | AND     |     |     |
| `        |         | `   | OR  |
| `!`      | NOT     |     |     |

Examples:

```bash
mkdir backup && echo "Backup directory created"
```

```bash
systemctl status nginx || echo "Nginx is not running"
```

```bash
if [ ! -f "config.txt" ]; then
  echo "Config file missing"
fi
```

---

### Case Statements

Useful when checking multiple values.

```bash
#!/bin/bash

read -p "Enter action: " ACTION

case "$ACTION" in
  start)
    echo "Starting service"
    ;;
  stop)
    echo "Stopping service"
    ;;
  restart)
    echo "Restarting service"
    ;;
  *)
    echo "Invalid action"
    ;;
esac
```

---

## 3. Loops

### For Loop – List-Based

Used to repeat commands for a list of values.

```bash
for fruit in apple banana mango
do
  echo "$fruit"
done
```

Single-line format:

```bash
for item in 1 2 3; do echo "$item"; done
```

---

### For Loop – C-Style

Useful for numeric loops.

```bash
for ((i=1; i<=5; i++))
do
  echo "Number: $i"
done
```

---

### While Loop

Runs while a condition is true.

```bash
COUNT=1

while [ "$COUNT" -le 5 ]
do
  echo "Count: $COUNT"
  COUNT=$((COUNT + 1))
done
```

---

### Until Loop

Runs until a condition becomes true.

```bash
COUNT=1

until [ "$COUNT" -gt 5 ]
do
  echo "Count: $COUNT"
  COUNT=$((COUNT + 1))
done
```

---

### Break and Continue

`break` stops the loop.

```bash
for i in 1 2 3 4 5
do
  if [ "$i" -eq 3 ]; then
    break
  fi
  echo "$i"
done
```

`continue` skips the current iteration.

```bash
for i in 1 2 3 4 5
do
  if [ "$i" -eq 3 ]; then
    continue
  fi
  echo "$i"
done
```

---

### Looping Over Files

Useful for log processing and automation.

```bash
for file in *.log
do
  echo "Processing $file"
done
```

Example with gzip:

```bash
for file in *.log
do
  gzip "$file"
done
```

---

### Looping Over Command Output

Use `while read` to process command output line by line.

```bash
while read line
do
  echo "$line"
done < app.log
```

---

## 4. Functions

### Defining a Function

Functions help reuse code.

```bash
greet() {
  echo "Hello, DevOps"
}
```

---

### Calling a Function

Call the function by its name.

```bash
#!/bin/bash

greet() {
  echo "Hello, DevOps"
}

greet
```

---

### Passing Arguments to Functions

Inside functions, `$1`, `$2`, etc. refer to function arguments.

```bash
greet_user() {
  echo "Hello, $1"
}

greet_user "Preetham"
```

---

### Return Values: `return` vs `echo`

Use `return` for exit status.

```bash
check_file() {
  if [ -f "$1" ]; then
    return 0
  else
    return 1
  fi
}

check_file "app.log"

if [ "$?" -eq 0 ]; then
  echo "File exists"
else
  echo "File missing"
fi
```

Use `echo` when you want to return data.

```bash
get_date() {
  echo "$(date +%F)"
}

TODAY=$(get_date)
echo "$TODAY"
```

---

### Local Variables

Use `local` to keep variables inside a function.

```bash
show_name() {
  local NAME="DevOps"
  echo "$NAME"
}

show_name
```

---

## 5. Text Processing Commands

### Grep

Search for patterns in files.

```bash
grep "ERROR" app.log
```

| Flag | Meaning           |
| ---- | ----------------- |
| `-i` | Ignore case       |
| `-r` | Recursive search  |
| `-c` | Count matches     |
| `-n` | Show line numbers |
| `-v` | Invert match      |
| `-E` | Extended regex    |

Examples:

```bash
grep -i "error" app.log
grep -n "ERROR" app.log
grep -c "ERROR" app.log
grep -v "INFO" app.log
grep -r "password" /etc/
grep -E "ERROR|WARNING" app.log
```

---

### Awk

Used for column-based text processing.

```bash
awk '{print $1}' file.txt
```

```bash
awk -F: '{print $1}' /etc/passwd
```

```bash
awk '/ERROR/ {print}' app.log
```

```bash
awk 'BEGIN {print "Start"} {print $1} END {print "Done"}' file.txt
```

```bash
awk '{print $1, $3}' app.log
```

---

### Sed

Used to edit text streams.

```bash
sed 's/old/new/' file.txt
```

```bash
sed 's/old/new/g' file.txt
```

```bash
sed -i 's/dev/staging/g' config.txt
```

```bash
sed '/ERROR/d' app.log
```

```bash
sed -n '5p' file.txt
```

---

### Cut

Used to extract fields or columns.

```bash
cut -d':' -f1 /etc/passwd
```

```bash
cut -d',' -f2 users.csv
```

```bash
cut -c1-5 file.txt
```

---

### Sort

Sort lines alphabetically or numerically.

```bash
sort names.txt
sort -n numbers.txt
sort -r names.txt
sort -u names.txt
```

---

### Uniq

Remove or count duplicate adjacent lines.

```bash
uniq names.txt
sort names.txt | uniq -c
sort names.txt | uniq -d
sort names.txt | uniq -u
```

---

### Tr

Translate or delete characters.

```bash
echo "devops" | tr 'a-z' 'A-Z'
echo "hello world" | tr -d ' '
echo "one two three" | tr ' ' '\n'
```

---

### Wc

Count lines, words, and characters.

```bash
wc file.txt
wc -l app.log
wc -w notes.txt
wc -c file.txt
```

---

### Head and Tail

Show first or last lines of a file.

```bash
head app.log
head -n 20 app.log
tail app.log
tail -n 50 app.log
tail -f app.log
tail -f app.log | grep -i "error"
```

---

## 6. Useful Patterns and One-Liners

### Find and Delete Files Older Than 30 Days

```bash
find /var/log/myapp -type f -name "*.log" -mtime +30 -delete
```

Use case: Clean old application logs.

---

### Compress Log Files Older Than 7 Days

```bash
find /var/log/myapp -type f -name "*.log" -mtime +7 -exec gzip {} \;
```

Use case: Save disk space by compressing old logs.

---

### Count Lines in All `.log` Files

```bash
wc -l *.log
```

Use case: Quickly check log file size by line count.

---

### Count ERROR Messages in Logs

```bash
grep -i "error" *.log | wc -l
```

Use case: Quickly check how many errors occurred.

---

### Replace a String Across Multiple Files

```bash
grep -rl "old_value" . | xargs sed -i 's/old_value/new_value/g'
```

Use case: Update configuration values across files.

---

### Check if a Service is Running

```bash
systemctl is-active --quiet nginx && echo "Nginx is running" || echo "Nginx is not running"
```

Use case: Basic service health check.

---

### Monitor Disk Usage with Alert

```bash
USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$USAGE" -gt 80 ]; then
  echo "Disk usage is above 80%"
fi
```

Use case: Alert when disk usage crosses a threshold.

---

### Tail Logs and Filter Errors in Real Time

```bash
tail -f app.log | grep -i "error"
```

Use case: Live troubleshooting.

---

### Parse CSV File

```bash
awk -F',' '{print $1, $2}' users.csv
```

Use case: Extract selected columns from a CSV file.

---

### Parse JSON from Command Line

```bash
cat response.json | jq '.status'
```

Use case: Read JSON API response values.

---

## 7. Error Handling and Debugging

### Exit Codes

Every command returns an exit code.

```bash
ls /tmp
echo $?
```

| Code  | Meaning                          |
| ----- | -------------------------------- |
| `0`   | Success                          |
| `1`   | General error                    |
| `2`   | Misuse of shell command          |
| `126` | Command found but not executable |
| `127` | Command not found                |

Exit manually:

```bash
exit 0
```

```bash
exit 1
```

Example:

```bash
if [ ! -f "app.log" ]; then
  echo "Error: app.log not found"
  exit 1
fi
```

---

### `set -e`

Exit immediately when a command fails.

```bash
#!/bin/bash
set -e

mkdir backup
cp app.log backup/
echo "Backup completed"
```

---

### `set -u`

Treat unset variables as errors.

```bash
#!/bin/bash
set -u

echo "$USERNAME"
```

If `USERNAME` is not defined, the script exits with an error.

---

### `set -o pipefail`

Detect failure inside pipelines.

```bash
#!/bin/bash
set -o pipefail

grep "ERROR" missing.log | wc -l
```

Without `pipefail`, pipeline errors may be hidden.

---

### Safe Script Mode

Common production-style Bash strict mode:

```bash
#!/bin/bash
set -euo pipefail
```

| Option            | Purpose                  |
| ----------------- | ------------------------ |
| `set -e`          | Exit on command failure  |
| `set -u`          | Error on unset variables |
| `set -o pipefail` | Catch pipeline failures  |

---

### `set -x`

Print commands before executing them.

```bash
#!/bin/bash
set -x

NAME="DevOps"
echo "$NAME"
```

Run script in debug mode:

```bash
bash -x script.sh
```

---

### Trap

Run cleanup commands when the script exits.

```bash
#!/bin/bash

cleanup() {
  echo "Cleaning temporary files..."
  rm -f /tmp/my_temp_file
}

trap 'cleanup' EXIT

touch /tmp/my_temp_file
echo "Script running..."
```

Use case: Remove temporary files even if the script fails.

---

## 8. Practical Script Template

Use this as a starting template for safer Bash scripts.

```bash
#!/bin/bash

set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
  echo "Error: File not found: $FILE"
  exit 1
fi

echo "Processing file: $FILE"

grep -i "error" "$FILE" || true

echo "Script completed successfully"
```

---

## 9. Common DevOps Use Cases

### Log Analysis

```bash
grep -i "error" app.log
grep -i "warning" app.log
grep -c "ERROR" app.log
```

---

### Backup Script Pattern

```bash
SOURCE="/var/www/html"
DEST="/backup"
DATE=$(date +%F)

tar -czf "$DEST/backup-$DATE.tar.gz" "$SOURCE"
```

---

### Check Disk Usage

```bash
df -h
```

---

### Check Memory Usage

```bash
free -h
```

---

### Check Running Processes

```bash
ps aux
ps aux | grep nginx
```

---

### Check Listening Ports

```bash
ss -tuln
```

---

### Check Service Status

```bash
systemctl status nginx
```

---

### Restart a Service

```bash
sudo systemctl restart nginx
```

---

## 10. Best Practices

- Always start scripts with a shebang.
- Use `set -euo pipefail` for safer scripts.
- Always quote variables: `"$VAR"`.
- Validate command-line arguments.
- Check if files and directories exist before using them.
- Use meaningful variable names.
- Add comments for important logic.
- Keep scripts small and focused.
- Test scripts with sample data before using them in production.
- Avoid hardcoding paths when possible.
- Use functions for reusable logic.
- Print clear error messages.
- Use exit codes properly.

---

## 11. Mini Revision Tasks

Try these to test your understanding:

1. Write a script that accepts a filename and checks whether it exists.
2. Write a script that counts `ERROR`, `WARNING`, and `INFO` lines in a log file.
3. Write a script that compresses `.log` files older than 7 days.
4. Write a function that checks if a service is running.
5. Write a script that alerts if disk usage is greater than 80%.

---

## Final Notes

Shell scripting is one of the most important DevOps skills because it helps automate repetitive system tasks.

This cheat sheet covers commands and patterns commonly used in:

- Linux administration
- Log analysis
- Backup automation
- Monitoring scripts
- CI/CD helper scripts
- Server troubleshooting

Keep improving this file as you learn new Bash commands and real-world DevOps patterns.
