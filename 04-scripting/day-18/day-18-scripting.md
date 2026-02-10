# Day 18 – Shell Scripting: Functions & Intermediate Concepts

## Objective

The goal of Day 18 was to write cleaner and reusable shell scripts using functions, strict mode, local variables, and real-world scripting patterns.

This task helped me understand how Bash scripts can be structured like real DevOps automation scripts instead of writing all commands directly in one file.

---

## Topics Covered

- Shell functions
- Passing arguments to functions
- Local variables
- Safer scripting with `set -euo pipefail`
- Disk and memory checks
- System information reporting
- Basic process monitoring using shell commands

---

## Project Structure

```bash
day-18/
├── screenshots/
├── scripts/
│   ├── disk_check.sh
│   ├── functions.sh
│   ├── local_demo.sh
│   ├── strict_demo.sh
│   └── system_info.sh
├── day-18-scripting.md
└── task.md
```

---

## Task 1: Basic Functions

### Script: `functions.sh`

```bash
#!/bin/bash

greet() {
    echo "Hello, $1!"
}

add() {
    local num1=$1
    local num2=$2
    local sum=$((num1 + num2))

    echo "Sum: $sum"
}

greet "Preetham"
add 10 20
```

### Commands Used

```bash
chmod +x functions.sh
./functions.sh
```

### Output

```bash
Hello, Preetham!
Sum: 30
```

### Explanation

In this script, I created two reusable Bash functions.

The `greet` function accepts a name as an argument and prints a greeting message.

The `add` function accepts two numbers as arguments, stores them in local variables, calculates the sum, and prints the result.

Using functions makes scripts easier to read, reuse, and maintain.

---

## Task 2: Functions with Return Values

### Script: `disk_check.sh`

```bash
#!/bin/bash

check_disk() {
    echo "Disk usage for root filesystem:"
    df -h /
}

check_memory() {
    echo "Memory usage:"
    free -h
}

main() {
    echo "===== Disk Check ====="
    check_disk

    echo
    echo "===== Memory Check ====="
    check_memory
}

main
```

### Commands Used

```bash
chmod +x disk_check.sh
./disk_check.sh
```

### Output

```bash
===== Disk Check =====
Disk usage for root filesystem:
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p2  468G  108G  337G  25% /

===== Memory Check =====
Memory usage:
               total        used        free      shared  buff/cache   available
Mem:           19Gi        5.7Gi       10Gi       636Mi       4.2Gi       13Gi
Swap:          17Gi           0B       17Gi
```

### Explanation

This script uses separate functions for checking disk and memory usage.

- `check_disk` checks the disk usage of the root filesystem `/` using `df -h /`.
- `check_memory` checks memory usage using `free -h`.
- `main` controls the execution flow.

This approach is useful in real DevOps scripts because each function has one clear responsibility.

---

## Task 3: Strict Mode – `set -euo pipefail`

### Script: `strict_demo.sh`

```bash
#!/bin/bash
set -euo pipefail

echo "Strict mode demo started"

echo "Testing set -u with undefined variable"
# Uncomment the below line to test set -u
# echo "$UNDEFINED_VARIABLE"

echo "Testing set -e with failed command"
# Uncomment the below line to test set -e
# ls /not-existing-directory

echo "Testing pipefail"
# Uncomment the below line to test pipefail
# grep "ERROR" missing-file.log | wc -l

echo "Strict mode demo completed"
```

### Commands Used

```bash
chmod +x strict_demo.sh
./strict_demo.sh
```

### Output

```bash
Strict mode demo started
Testing set -u with undefined variable
Testing set -e with failed command
Testing pipefail
Strict mode demo completed
```

### Explanation of Strict Mode

#### `set -e`

`set -e` stops the script immediately if any command fails.

Example:

```bash
ls /not-existing-directory
```

If the directory does not exist, the script stops instead of continuing.

#### `set -u`

`set -u` stops the script when an undefined variable is used.

Example:

```bash
echo "$UNDEFINED_VARIABLE"
```

This helps catch spelling mistakes or missing variables early.

#### `set -o pipefail`

`set -o pipefail` makes a pipeline fail if any command in the pipeline fails.

Example:

```bash
grep "ERROR" missing-file.log | wc -l
```

Without `pipefail`, Bash may only check the exit status of the last command in the pipeline. With `pipefail`, the script correctly detects that `grep` failed.

### Why Strict Mode Matters

Strict mode is useful in production scripts because it prevents silent failures. This is important in DevOps automation, where a failed command should not be ignored during deployments, backups, monitoring, or cleanup tasks.

---

## Task 4: Local Variables

### Script: `local_demo.sh`

```bash
#!/bin/bash

local_variable_demo() {
    local name="Inside Function"
    echo "Local variable value: $name"
}

regular_variable_demo() {
    city="Mangalore"
    echo "Regular variable inside function: $city"
}

local_variable_demo

echo "Trying to access local variable outside function:"
echo "name value outside function: ${name:-Not accessible}"

echo

regular_variable_demo

echo "Trying to access regular variable outside function:"
echo "city value outside function: $city"
```

### Commands Used

```bash
chmod +x local_demo.sh
./local_demo.sh
```

### Output

```bash
Local variable value: Inside Function
Trying to access local variable outside function:
name value outside function: Not accessible

Regular variable inside function: Mangalore
Trying to access regular variable outside function:
city value outside function: Mangalore
```

### Explanation

The `local` keyword keeps a variable inside the function only.

In the first function, the variable `name` is declared with `local`, so it cannot be accessed outside the function.

In the second function, the variable `city` is not declared as local. Because of that, it is accessible outside the function.

Using `local` is a good practice because it avoids unwanted variable conflicts in larger shell scripts.

---

## Task 5: System Info Reporter

### Script: `system_info.sh`

```bash
#!/bin/bash
set -euo pipefail

print_section() {
    echo
    echo "========================================"
    echo "$1"
    echo "========================================"
}

show_hostname_os() {
    print_section "Hostname and OS Information"

    echo "Hostname: $(hostname)"
    echo "Operating System:"
    cat /etc/os-release | grep -E "PRETTY_NAME|VERSION="
}

show_uptime() {
    print_section "System Uptime"

    uptime
}

show_disk_usage() {
    print_section "Top 5 Disk Usage"

    df -h | sort -hr -k 5 | head -n 5
}

show_memory_usage() {
    print_section "Memory Usage"

    free -h
}

show_top_cpu_processes() {
    print_section "Top 5 CPU Consuming Processes"

    ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6
}

main() {
    echo "System Information Report"
    echo "Generated on: $(date)"

    show_hostname_os
    show_uptime
    show_disk_usage
    show_memory_usage
    show_top_cpu_processes

    echo
    echo "Report completed successfully."
}

main
```

### Command Used

```bash
./system_info.sh
```

### Output

```bash
System Information Report
Generated on: Mon Jan 1 16:04:06 IST 2026

========================================
Hostname and OS Information
========================================
Hostname: ubuntu
Operating System:
PRETTY_NAME="Ubuntu 24.04.4 LTS"
VERSION="24.04.4 LTS (Noble Numbat)"

========================================
System Uptime
========================================
16:04:06 up 4:39, 1 user, load average: 0.86, 0.44, 0.35

========================================
Top 5 Disk Usage
========================================
efivarfs        192K  131K   57K  70% /sys/firmware/efi/efivars
/dev/nvme0n1p2  468G  108G  337G  25% /
tmpfs            9.7G  157M  9.5G   2% /dev/shm
tmpfs            5.0M   12K  5.0M   1% /run/lock
tmpfs            2.0G  2.4M  2.0G   1% /run

========================================
Memory Usage
========================================
               total        used        free      shared  buff/cache   available
Mem:            19Gi       5.7Gi       10Gi       755Mi       4.4Gi       13Gi
Swap:           17Gi          0B       17Gi

========================================
Top 5 CPU Consuming Processes
========================================
    PID COMMAND         %CPU %MEM
 699869 chrome           9.6  2.5
 696368 Amazon Q Helper  5.0  4.3
 673463 chrome           3.7  1.0
 693845 code             3.0  2.0
 693892 code             2.3  3.2

Report completed successfully.
```

### Explanation

The `system_info.sh` script is a small real-world DevOps utility. It collects useful system information and displays it in a readable format.

The script uses functions for each section:

- `print_section` prints clean section headers.
- `show_hostname_os` displays hostname and OS information.
- `show_uptime` displays system uptime.
- `show_disk_usage` displays the top disk usage entries.
- `show_memory_usage` displays memory usage.
- `show_top_cpu_processes` displays the top CPU-consuming processes.
- `main` calls all functions in order.

This structure makes the script clean, reusable, and easier to debug.

---

## Commands Practiced

```bash
chmod +x functions.sh
chmod +x disk_check.sh
chmod +x strict_demo.sh
chmod +x local_demo.sh
chmod +x system_info.sh
```

```bash
./functions.sh
./disk_check.sh
./strict_demo.sh
./local_demo.sh
./system_info.sh
```

---

## What I Learned

1. Functions help organize shell scripts into reusable blocks.
2. `set -euo pipefail` makes scripts safer by stopping execution when errors happen.
3. Local variables prevent unwanted variable leaks outside functions.
4. A `main` function makes Bash scripts more structured and professional.
5. Shell scripts are useful for real DevOps tasks like health checks, monitoring, and system reporting.

---

## Real-World DevOps Use Case

In real DevOps work, shell scripting is commonly used for:

- Server health checks
- Log cleanup
- Disk monitoring
- Memory monitoring
- Backup automation
- Deployment helper scripts
- CI/CD automation steps

Writing scripts with functions and strict mode makes them more reliable and production-friendly.

---

## Final Status

Day 18 completed successfully.
