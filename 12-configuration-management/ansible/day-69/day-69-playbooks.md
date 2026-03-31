# Day 69 - Ansible Playbooks and Modules

## Objective

The goal of Day 69 was to move beyond Ansible ad-hoc commands and start writing reusable playbooks. During this lab, I learned how to automate package installation, service management, file deployment, handlers, and multi-server configuration using Ansible playbooks.

---

# Lab Environment

| Component | Details |
|-----------|---------|
| Control Node | Ubuntu |
| Managed Nodes | Amazon Linux 2023 |
| Automation Tool | Ansible |
| Inventory Groups | web, app, db |

---

# Task 1 - My First Ansible Playbook

Created `install-nginx.yml` to automate Nginx installation on the web server.

## Playbook

```yaml
---
- name: Install and start Nginx on web servers
  hosts: web
  become: true

  tasks:
    - name: Install Nginx
      yum:
        name: nginx
        state: present

    - name: Start and enable Nginx
      service:
        name: nginx
        state: started
        enabled: true

    - name: Create a custom index page
      copy:
        content: "<h1>Deployed by Ansible - TerraWeek Server</h1>"
        dest: /usr/share/nginx/html/index.html
```

## Playbook Structure

### YAML Document

```yaml
---
```

Marks the beginning of a YAML document.

### Play

```yaml
- name: Install and start Nginx on web servers
```

A play defines which hosts Ansible should configure.

### Hosts

```yaml
hosts: web
```

Targets all servers in the **web** inventory group.

### Become

```yaml
become: true
```

Runs tasks with root privileges using sudo.

### Tasks

Each task performs one operation using an Ansible module.

Examples:

- Install package
- Manage service
- Copy files

---

# Verification

First execution:

- Installed Nginx
- Started the service
- Created custom webpage

Second execution:

```
changed=0
```

This demonstrates **idempotency**, where Ansible makes changes only when required.

---

# Task 2 - Understanding Playbooks

## Difference Between Play and Task

### Play

A play targets one or more inventory groups and contains multiple tasks.

### Task

A task is a single action performed by an Ansible module.

---

## Can a Playbook Have Multiple Plays?

Yes.

A single playbook can contain multiple plays targeting different server groups.

---

## become: true

### Play Level

All tasks execute with elevated privileges.

### Task Level

Only that specific task runs with elevated privileges.

---

## What Happens if a Task Fails?

By default:

- Execution stops for that host.
- Remaining hosts continue executing.

---

# Task 3 - Essential Ansible Modules

## yum

Used to install or remove software packages.

Example:

```yaml
yum:
  name:
    - git
    - curl
    - wget
    - tree
  state: present
```

---

## service

Manages Linux services.

Example:

```yaml
service:
  name: nginx
  state: started
  enabled: true
```

---

## copy

Copies files from the control node to managed nodes.

Example:

```yaml
copy:
  src: files/app.conf
  dest: /etc/app.conf
```

---

## file

Creates directories and manages permissions.

Example:

```yaml
file:
  path: /opt/myapp
  state: directory
  mode: '0755'
```

---

## command

Executes commands without shell features.

Example:

```yaml
command: df -h
```

Used when shell functionality is unnecessary.

---

## shell

Runs commands through the shell.

Example:

```yaml
shell: ps aux | wc -l
```

Supports:

- Pipes
- Redirects
- Environment variables

---

## lineinfile

Adds or modifies a single line inside a file.

Example:

```yaml
lineinfile:
  path: /etc/environment
  line: TZ=Asia/Kolkata
```

---

## register

Stores task output into a variable.

Example:

```yaml
register: disk_output
```

---

## debug

Prints variables during playbook execution.

Example:

```yaml
debug:
  var: disk_output.stdout_lines
```

---

# command vs shell

| command | shell |
|----------|-------|
| Does not invoke shell | Executes through shell |
| Safer | Less secure |
| No pipes or redirects | Supports pipes and redirects |
| Faster | Slightly slower |

Use **command** whenever possible.

Use **shell** only when shell features are required.

---

# Task 4 - Handlers

Handlers execute only when notified by a task that has changed something.

Example:

```yaml
notify: Restart Nginx
```

Handler:

```yaml
handlers:
  - name: Restart Nginx
    service:
      name: nginx
      state: restarted
```

---

## Verification

First run:

```
RUNNING HANDLER [Restart Nginx]
```

Second run:

Handler did not execute because the configuration file was unchanged.

This avoids unnecessary service restarts.

---

# Task 5 - Useful Playbook Options

## Syntax Check

```bash
ansible-playbook --syntax-check install-nginx.yml
```

Validates playbook syntax.

---

## Check Mode

```bash
ansible-playbook install-nginx.yml --check
```

Shows what would change without making modifications.

---

## Diff Mode

```bash
ansible-playbook nginx-config.yml --check --diff
```

Displays file differences before applying changes.

---

## Verbose Output

```bash
-v
-vv
-vvv
```

Increasing verbosity provides more detailed debugging information.

---

## Limit Execution

```bash
--limit web-server
```

Runs playbook only against the specified host.

---

## List Hosts

```bash
--list-hosts
```

Displays hosts that will be targeted.

---

## List Tasks

```bash
--list-tasks
```

Displays tasks without executing them.

---

## Why use --check --diff?

This combination is extremely useful in production because it:

- previews changes
- displays configuration differences
- avoids accidental modifications
- validates deployments before execution

---

# Task 6 - Multiple Plays

Created a single playbook containing multiple plays.

## Web Servers

- Install Nginx
- Start Nginx

## Application Servers

- Install development packages
- Create application directory

## Database Servers

- Install MariaDB client utilities
- Create application data directory

Each play targeted only its respective inventory group.

---

# Challenge Faced

Amazon Linux 2023 does not provide a package named:

```
mysql
```

The playbook initially failed.

Solution:

Replaced it with:

```
mariadb1011-client-utils
```

This demonstrates the importance of adapting automation based on the operating system and package repository.

---

# Key Learnings

- Created reusable Ansible playbooks
- Understood plays, tasks, modules, and handlers
- Learned Ansible idempotency
- Practiced essential Ansible modules
- Used register and debug
- Managed services using handlers
- Executed dry runs before deployment
- Configured multiple server groups using one playbook
- Learned production-safe playbook execution techniques

---

# Screenshots

- Ansible ping successful
- First playbook execution
- Custom Nginx webpage
- Idempotent second run
- Essential modules playbook
- Essential modules execution
- Command and shell output
- app.conf verification
- Directory and environment verification
- Handler first execution
- Handler second execution
- Updated Nginx webpage
- Check mode output
- Diff mode output
- Verbose execution
- List hosts
- List tasks
- Multi-play execution
- Web server verification
- App server verification
- Database server verification

---

# Outcome

Successfully built reusable Ansible playbooks capable of installing software, configuring services, deploying files, managing handlers, and automating multiple server roles. This lab strengthened my understanding of Ansible's declarative automation model and demonstrated how idempotent playbooks simplify infrastructure management in real-world DevOps environments.
