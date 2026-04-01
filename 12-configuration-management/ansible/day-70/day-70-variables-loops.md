# Day 70 – Ansible Variables, Loops, Conditionals & Handlers

## Overview

Today focused on mastering core Ansible concepts used in real-world automation:

- Variables and variable precedence
- Group variables and host variables
- Facts gathering
- Conditional execution
- Loops for automation
- Handlers for service management
- Server reporting using facts

This day builds the foundation for writing production-grade Ansible playbooks.

---

## Objectives

By the end of this day, you should understand:

- How Ansible manages variables at different levels
- How to use CLI extra variables (`-e`)
- How to use loops to avoid repetition
- How to apply conditions using `when`
- How handlers ensure idempotent service control
- How to extract system facts using the `setup` module

---

## Project Structure

```

ansible-practice/
├── inventory.ini
├── group_vars/
│ └── all.yml
├── playbooks/
│ ├── variables-demo.yml
│ ├── facts-demo.yml
│ ├── conditional-demo.yml
│ ├── loops-demo.yml
│ ├── handlers-demo.yml
│ └── server-report.yml

```

---

## Key Concepts

### 1. Variables

Variables were tested in multiple ways:

- Playbook variables
- CLI variables (`-e`)
- Group variables (`group_vars/all.yml`)

Example:

```yaml
msg: "Deploying {{ app_name }} on port {{ app_port }}"
```

---

### 2. Variable Precedence

CLI variables override all others:

```bash
ansible-playbook variables-demo.yml -e "app_name=my-app app_port=9090"
```

---

### 3. Facts Gathering

Facts provide system-level information:

```bash
ansible all -m setup
```

Common facts used:

- ansible_hostname
- ansible_default_ipv4.address
- ansible_distribution
- ansible_memtotal_mb

---

### 4. Conditionals

Used to control execution:

```yaml
when: ansible_os_family == "RedHat"
```

Examples:

- Install Nginx only on web servers
- Install DB only on db servers
- Run tasks based on RAM or environment

---

### 5. Loops

Loops eliminate repetition:

```yaml
loop:
  - git
  - wget
  - unzip
```

Complex loop example:

```yaml
loop:
  - { name: deploy, groups: wheel }
  - { name: monitor, groups: wheel }
```

---

### 6. Handlers

Handlers run only when changes occur.

Example:

```yaml
tasks:
  - name: Copy nginx config
    copy:
      src: nginx.conf
      dest: /etc/nginx/nginx.conf
    notify: Restart nginx

handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
```

---

### 7. Server Reporting

Used facts to generate structured output:

```yaml
msg:
  - "Hostname: {{ ansible_hostname }}"
  - "OS: {{ ansible_distribution }}"
  - "RAM: {{ ansible_memtotal_mb }} MB"
  - "IP: {{ ansible_default_ipv4.address }}"
```

---

## Commands Used

### Run playbooks

```bash
ansible-playbook -i inventory.ini playbooks/variables-demo.yml
ansible-playbook -i inventory.ini playbooks/facts-demo.yml
ansible-playbook -i inventory.ini playbooks/conditional-demo.yml
ansible-playbook -i inventory.ini playbooks/loops-demo.yml
ansible-playbook -i inventory.ini playbooks/handlers-demo.yml
ansible-playbook -i inventory.ini playbooks/server-report.yml
```

### Ad-hoc commands

```bash
ansible all -i inventory.ini -m shell -a "ls -ld /opt/app/*"
ansible all -i inventory.ini -m setup
```

---

## Key Learnings

- Variables follow strict precedence rules
- Facts are critical for dynamic automation
- Conditionals help target specific hosts
- Loops reduce repetitive tasks significantly
- Handlers ensure services restart only when needed
- Structured reporting improves observability

---

## Outcome

By completing Day 70, you now understand how to:

- Build dynamic playbooks
- Avoid hardcoding values
- Write reusable automation logic
- Manage system configuration at scale
