# Day 16 – Shell Scripting Basics

## Overview

Day 16 focused on the fundamentals of shell scripting using Bash. The goal was to understand how scripts are written, executed, and used for basic automation tasks in Linux.

In this task, I practiced creating simple Bash scripts using variables, user input, conditional statements, file checks, and service status checks.

---

## Project Structure

```bash
04-scripting/
└── day-16/
    ├── screenshots/
    ├── scripts/
    │   ├── check_number.sh
    │   ├── file_check.sh
    │   ├── greet.sh
    │   ├── hello.sh
    │   ├── server_check.sh
    │   └── variables.sh
    ├── README.md
    └── task.md
```

---

## Topics Covered

- Bash shebang line
- Script execution permissions
- Variables in shell scripts
- `echo` command
- User input using `read`
- If-else conditions
- File existence checks using `-f`
- Service status checks using `systemctl`

---

## Task 1: First Shell Script

### Script: `hello.sh`

```bash
#!/bin/bash

echo "Hello, DevOps!"
```

### Commands Used

```bash
chmod +x hello.sh
./hello.sh
```

### Output

```bash
Hello, DevOps!
```

### What I Learned

The shebang line tells the system which interpreter should execute the script.

```bash
#!/bin/bash
```

If the shebang is removed, the script may still run in the current shell, but this is not reliable across different environments. Using the shebang makes the script more predictable and portable.

---

## Task 2: Variables

### Script: `variables.sh`

```bash
#!/bin/bash

NAME="Preetham"
ROLE="DevOps Engineer"

echo "Hello, I am $NAME and I am a $ROLE"

echo 'Using single quotes: Hello, I am $NAME and I am a $ROLE'
echo "Using double quotes: Hello, I am $NAME and I am a $ROLE"
```

### Commands Used

```bash
chmod +x variables.sh
./variables.sh
```

### Output

```bash
Hello, I am Preetham and I am a DevOps Engineer
Using single quotes: Hello, I am $NAME and I am a $ROLE
Using double quotes: Hello, I am Preetham and I am a DevOps Engineer
```

### What I Learned

Single quotes do not expand variables. They print the text exactly as written.

Double quotes expand variables and print their actual values.

---

## Task 3: User Input with `read`

### Script: `greet.sh`

```bash
#!/bin/bash

read -p "Enter your name: " NAME
read -p "Enter your favourite DevOps tool: " TOOL

echo "Hello $NAME, your favourite tool is $TOOL"
```

### Commands Used

```bash
chmod +x greet.sh
./greet.sh
```

### Output

```bash
Enter your name: Preetham
Enter your favourite DevOps tool: Kubernetes
Hello Preetham, your favourite tool is Kubernetes
```

### What I Learned

The `read` command is used to take input from the user during script execution. This makes shell scripts interactive.

---

## Task 4: If-Else Conditions

### Script: `check_number.sh`

```bash
#!/bin/bash

read -p "Enter a number: " NUMBER

if [ "$NUMBER" -gt 0 ]; then
    echo "$NUMBER is positive"
elif [ "$NUMBER" -lt 0 ]; then
    echo "$NUMBER is negative"
else
    echo "The number is zero"
fi
```

### Commands Used

```bash
chmod +x check_number.sh
./check_number.sh
```

### Output

```bash
Enter a number: 6
6 is positive
```

```bash
Enter a number: 0
The number is zero
```

```bash
Enter a number: -3
-3 is negative
```

### What I Learned

If-else conditions help scripts make decisions based on input or system state.

Common numeric comparison operators:

| Operator | Meaning      |
| -------- | ------------ |
| `-gt`    | Greater than |
| `-lt`    | Less than    |
| `-eq`    | Equal to     |
| `-ne`    | Not equal to |

---

## Task 5: File Check

### Script: `file_check.sh`

```bash
#!/bin/bash

read -p "Enter filename: " FILENAME

if [ -f "$FILENAME" ]; then
    echo "File exists: $FILENAME"
else
    echo "File does not exist: $FILENAME"
fi
```

### Commands Used

```bash
chmod +x file_check.sh
./file_check.sh
```

### Output

```bash
Enter filename: hello.sh
File exists: hello.sh
```

```bash
Enter filename: my_devops_file.txt
File does not exist: my_devops_file.txt
```

### What I Learned

The `-f` condition checks whether a regular file exists. This is useful in real DevOps scripts before reading logs, configuration files, or deployment files.

---

## Task 6: Server Status Check

### Script: `server_check.sh`

```bash
#!/bin/bash

SERVICE="ssh"

read -p "Do you want to check the status of $SERVICE? (y/n): " CHOICE

if [ "$CHOICE" = "y" ]; then
    if systemctl is-active --quiet "$SERVICE"; then
        echo "$SERVICE is active"
    else
        echo "$SERVICE is not active"
    fi
elif [ "$CHOICE" = "n" ]; then
    echo "Skipped."
else
    echo "Invalid choice. Please enter y or n."
fi
```

### Commands Used

```bash
chmod +x server_check.sh
./server_check.sh
```

### Output

```bash
Do you want to check the status of ssh? (y/n): y
ssh is active
```

### Note

Initially, the SSH service was not available. After installing OpenSSH server, the script was able to check the service status successfully.

This command was used to install the SSH service:

```bash
sudo apt update
sudo apt install openssh-server -y
```

---

## Useful Commands Practiced

```bash
chmod +x script_name.sh
./script_name.sh
```

```bash
systemctl is-active --quiet ssh
systemctl status ssh
```

```bash
ls -l
```

---

## Key Learnings

1. The shebang line defines which interpreter should run the script.
2. Variables are used to store reusable values in scripts.
3. Double quotes expand variables, while single quotes print text literally.
4. The `read` command allows scripts to accept user input.
5. If-else conditions are useful for decision-making in automation scripts.
6. File checks and service checks are common real-world DevOps scripting tasks.

---

## Real-World DevOps Use Cases

Shell scripting is commonly used by DevOps engineers for:

- Automating Linux administration tasks
- Checking service status
- Validating files before deployment
- Writing backup scripts
- Automating CI/CD steps
- Running health checks on servers
- Simplifying repetitive operational tasks

---

## Final Status

| Script            | Status    |
| ----------------- | --------- |
| `hello.sh`        | Completed |
| `variables.sh`    | Completed |
| `greet.sh`        | Completed |
| `check_number.sh` | Completed |
| `file_check.sh`   | Completed |
| `server_check.sh` | Completed |

---

## Conclusion

Day 16 introduced the basics of Bash scripting. These concepts are important because shell scripts are heavily used in Linux administration, DevOps automation, CI/CD pipelines, monitoring, and server management.

This task helped build a strong foundation for writing practical automation scripts in real DevOps environments.
