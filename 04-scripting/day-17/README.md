# Day 17 – Shell Scripting: Loops, Arguments & Error Handling

## Overview

This project focuses on improving shell scripting skills by practicing loops, command-line arguments, package installation automation, and basic error handling.

These concepts are commonly used in real DevOps work for server setup, automation scripts, health checks, and deployment tasks.

---

## Topics Covered

- For loops
- While loops
- Shell arrays
- Command-line arguments
- Root user validation
- Package installation automation
- Basic error handling using `set -e` and `||`

---

## Project Structure

```bash
day-17/
├── screenshots/
├── scripts/
│   ├── args_demo.sh
│   ├── count.sh
│   ├── countdown.sh
│   ├── for_loop.sh
│   ├── greet.sh
│   ├── install_packages.sh
│   └── safe_script.sh
├── README.md
└── task.md
```

---

## Scripts Created

### 1. `for_loop.sh`

This script loops through a list of fruits and prints each fruit.

```bash
#!/bin/bash

fruits=("apple" "banana" "mango" "orange" "grapes")

for fruit in "${fruits[@]}"
do
    echo "Fruit: $fruit"
done
```

### Output

```bash
Fruit: apple
Fruit: banana
Fruit: mango
Fruit: orange
Fruit: grapes
```

---

### 2. `count.sh`

This script prints numbers from 1 to 10 using a `for` loop.

```bash
#!/bin/bash

for number in {1..10}
do
    echo "$number"
done
```

### Output

```bash
1
2
3
4
5
6
7
8
9
10
```

---

### 3. `countdown.sh`

This script takes a number from the user and counts down to 0 using a `while` loop.

```bash
#!/bin/bash

read -p "Enter a number: " number

while [ "$number" -ge 0 ]
do
    echo "$number"
    number=$((number - 1))
done

echo "Done!"
```

### Output

```bash
Enter a number: 10
10
9
8
7
6
5
4
3
2
1
0
Done!
```

---

### 4. `greet.sh`

This script accepts a name as a command-line argument and prints a greeting message.

If no argument is passed, it displays usage instructions.

```bash
#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: ./greet.sh <name>"
    exit 1
fi

echo "Hello, $1!"
```

### Output Without Argument

```bash
Usage: ./greet.sh <name>
```

### Output With Argument

```bash
Hello, Preetham!
```

---

### 5. `args_demo.sh`

This script demonstrates special shell variables used for command-line arguments.

```bash
#!/bin/bash

echo "Script name: $0"
echo "Total arguments: $#"
echo "All arguments: $@"
```

### Output Without Arguments

```bash
Script name: ./args_demo.sh
Total arguments: 0
All arguments:
```

### Output With Arguments

```bash
Script name: ./args_demo.sh
Total arguments: 4
All arguments: Hello this is Preetham
```

---

### 6. `install_packages.sh`

This script checks whether `nginx`, `curl`, and `wget` are installed.

If a package is missing, the script installs it using `apt`.

The script also checks whether it is being run as root. If not, it exits with a clear error message.

```bash
#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Error: Please run this script as root."
    echo "Example: sudo ./install_packages.sh"
    exit 1
fi

packages=("nginx" "curl" "wget")

for package in "${packages[@]}"
do
    echo "Checking package: $package"

    if dpkg -s "$package" &> /dev/null; then
        echo "$package is already installed."
    else
        echo "$package is not installed. Installing now..."
        apt update
        apt install -y "$package"

        if [ $? -eq 0 ]; then
            echo "$package installed successfully."
        else
            echo "Failed to install $package."
            exit 1
        fi
    fi

    echo "-------------------------"
done
```

### Output Without Root

```bash
Error: Please run this script as root.
Example: sudo ./install_packages.sh
```

### Output With Root

```bash
Checking package: nginx
nginx is already installed.
-------------------------
Checking package: curl
curl is already installed.
-------------------------
Checking package: wget
wget is already installed.
-------------------------
```

---

### 7. `safe_script.sh`

This script creates a directory inside `/tmp`, moves into it, and creates a file.

It uses `set -e` so the script exits when a command fails.

```bash
#!/bin/bash

set -e

mkdir /tmp/devops-test || echo "Directory already exists"

cd /tmp/devops-test || {
    echo "Failed to enter /tmp/devops-test"
    exit 1
}

touch devops-file.txt || {
    echo "Failed to create file"
    exit 1
}

echo "File created successfully inside /tmp/devops-test"
```

### Output

```bash
File created successfully inside /tmp/devops-test
```

When trying to read the directory directly using `cat`:

```bash
cat: /tmp/devops-test/: Is a directory
```

The file was verified using:

```bash
cat /tmp/devops-test/devops-file.txt
```

The file exists, but no content is displayed because it was created using `touch`.

---

## Commands Practiced

Make scripts executable:

```bash
chmod +x for_loop.sh
chmod +x count.sh
chmod +x countdown.sh
chmod +x greet.sh
chmod +x args_demo.sh
chmod +x install_packages.sh
chmod +x safe_script.sh
```

Run scripts:

```bash
./for_loop.sh
./count.sh
./countdown.sh
./greet.sh Preetham
./args_demo.sh Hello this is Preetham
sudo ./install_packages.sh
./safe_script.sh
```

Check shell script syntax:

```bash
bash -n *.sh
```

---

## Key Learnings

1. Loops help automate repeated tasks without writing the same command multiple times.
2. Command-line arguments make scripts flexible and reusable.
3. Error handling is important because DevOps automation should fail safely and clearly.

---

## Real-World DevOps Use Cases

Shell scripting is commonly used in DevOps for:

- Installing packages on servers
- Automating server setup
- Running health checks
- Creating files and directories
- Validating user input
- Handling script failures
- Writing backup and deployment scripts

---

## Summary

Day 17 helped me understand how shell scripts can become more useful by using loops, arguments, and error handling.

These are important foundations for writing real-world DevOps automation scripts.
