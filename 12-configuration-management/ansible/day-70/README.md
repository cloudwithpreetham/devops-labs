# Day 70 – Ansible Variables, Loops, Conditionals & Handlers

## Overview

This project demonstrates core Ansible fundamentals used in real-world DevOps automation:

- Variables and variable precedence
- Group variables and host variables
- Facts gathering
- Conditional execution
- Loops for automation
- Handlers for service management
- Server reporting using Ansible facts

---

## Project Structure

```

ansible-practice/
├── inventory.ini
├── group_vars/
│   └── all.yml
├── playbooks/
│   ├── variables-demo.yml
│   ├── facts-demo.yml
│   ├── conditional-demo.yml
│   ├── loops-demo.yml
│   ├── handlers-demo.yml
│   └── server-report.yml

````

---

## Key Features Implemented

### 1. Variables Management
- Playbook variables
- CLI variables using `-e`
- Group variables using `group_vars/all.yml`

Example:
```yaml
msg: "Deploying {{ app_name }} on port {{ app_port }}"
````

---

### 2. Variable Precedence

CLI variables override all others:

```bash
ansible-playbook variables-demo.yml -e "app_name=my-app app_port=9090"
```

---

### 3. Facts Gathering

System information collected using Ansible facts:

* OS details
* Memory
* CPU
* Network interfaces
* Hostname

Command:

```bash
ansible all -m setup
```

---

### 4. Conditional Execution

Tasks executed based on conditions:

* Install Nginx only on web servers
* Install MariaDB only on DB servers
* Environment-based execution
* OS-based execution

Example:

```yaml
when: ansible_os_family == "RedHat"
```

---

### 5. Loops

Used to avoid repetition:

* Multiple users creation
* Multiple directories creation
* Multiple package installation

Example:

```yaml
loop:
  - git
  - wget
  - unzip
```

---

### 6. Handlers

Handlers run only when changes occur:

* Nginx restart only when config changes

Example:

```yaml
notify: Restart nginx
```

---

### 7. Server Reporting

Generated structured system report using facts:

* Hostname
* OS version
* RAM
* IP address
* CPU info

---

## How to Run

### Execute all playbooks:

```bash
ansible-playbook -i inventory.ini playbooks/variables-demo.yml
ansible-playbook -i inventory.ini playbooks/facts-demo.yml
ansible-playbook -i inventory.ini playbooks/conditional-demo.yml
ansible-playbook -i inventory.ini playbooks/loops-demo.yml
ansible-playbook -i inventory.ini playbooks/handlers-demo.yml
ansible-playbook -i inventory.ini playbooks/server-report.yml
```

---

## Ad-hoc Commands

```bash
ansible all -i inventory.ini -m setup
ansible all -i inventory.ini -m shell -a "ls -ld /opt/app/*"
```

---

## Key Learnings

* Variables follow precedence rules (CLI > playbook > group vars)
* Facts enable dynamic configuration
* Conditionals control execution flow
* Loops reduce duplication in playbooks
* Handlers ensure idempotent service management
* Structured reporting improves observability

---

## Outcome

After completing this lab, you are able to:

* Write dynamic Ansible playbooks
* Automate multi-server configurations
* Use conditions and loops effectively
* Manage services using handlers
* Generate system reports using facts
