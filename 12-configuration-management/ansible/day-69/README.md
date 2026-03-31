# Day 69 - Ansible Playbooks and Modules

This project is part of my **90 Days of DevOps** journey. On Day 69, I learned how to automate infrastructure using **Ansible Playbooks**. I created reusable playbooks to install software, manage services, configure files, use handlers, and automate multiple server groups while understanding Ansible's idempotent nature.

---

## Objectives

- Learn the structure of Ansible playbooks
- Understand plays, tasks, modules, and handlers
- Automate package installation and service management
- Practice commonly used Ansible modules
- Learn idempotency
- Perform dry runs before deployment
- Configure multiple server groups using a single playbook

---

## Project Structure

```
day-69/
├── files/
│   ├── app.conf
│   └── nginx.conf
├── install-nginx.yml
├── essential-modules.yml
├── nginx-config.yml
├── multi-play.yml
├── inventory.ini
├── day-69-playbooks.md
└── README.md
```

---

## Lab Environment

| Component | Details |
|-----------|---------|
| Control Node | Ubuntu |
| Managed Nodes | Amazon Linux 2023 |
| Automation Tool | Ansible |
| Inventory Groups | web, app, db |

---

## Playbooks Created

### install-nginx.yml

Automates:

- Install Nginx
- Start and enable Nginx
- Deploy a custom web page

---

### essential-modules.yml

Practiced essential Ansible modules:

- yum
- service
- copy
- file
- command
- shell
- lineinfile
- register
- debug

---

### nginx-config.yml

Configured Nginx using:

- Configuration file deployment
- Custom HTML page
- Handlers
- Service restart only when configuration changes

---

### multi-play.yml

Contains multiple plays for different server groups.

**Web Servers**

- Install Nginx
- Start and enable service

**Application Servers**

- Install development packages
- Create application directory

**Database Servers**

- Install MariaDB client utilities
- Create application data directory

---

## Key Ansible Concepts Learned

### Play

A play targets one or more inventory groups and contains multiple tasks.

### Task

A single unit of work performed using an Ansible module.

### Module

A reusable component that performs a specific operation such as:

- Installing packages
- Managing services
- Copying files
- Creating directories

### Handler

A special task that runs only when notified by another task that reports changes.

---

## Idempotency

One of Ansible's most powerful features is idempotency.

### First Run

```
changed=3
```

Resources were created and configured.

### Second Run

```
changed=0
```

No unnecessary changes were made because the desired state already existed.

---

## Useful Playbook Commands

### Syntax Check

```bash
ansible-playbook --syntax-check install-nginx.yml
```

### Dry Run

```bash
ansible-playbook install-nginx.yml --check
```

### Dry Run with Diff

```bash
ansible-playbook nginx-config.yml --check --diff
```

### Verbose Mode

```bash
ansible-playbook install-nginx.yml -v
ansible-playbook install-nginx.yml -vv
ansible-playbook install-nginx.yml -vvv
```

### Run Against Specific Host

```bash
ansible-playbook install-nginx.yml --limit web-server
```

### List Hosts

```bash
ansible-playbook install-nginx.yml --list-hosts
```

### List Tasks

```bash
ansible-playbook install-nginx.yml --list-tasks
```

---

## Challenge Faced

While configuring the database server, the playbook initially failed because Amazon Linux 2023 does not provide a package named:

```
mysql
```

The solution was to replace it with:

```
mariadb1011-client-utils
```

This demonstrated the importance of adapting automation based on the target operating system and package repository.

---

## Skills Gained

- Writing reusable Ansible playbooks
- Working with inventory groups
- Package management automation
- Service management
- File deployment
- Directory management
- Command execution
- Shell command execution
- Handlers and notifications
- Registering task outputs
- Debugging playbooks
- Dry-run validation
- Multi-play automation
- Infrastructure idempotency

---

## Screenshots

- Ansible inventory verification
- Successful ping to managed nodes
- First Nginx playbook execution
- Custom Nginx web page
- Idempotent second execution
- Essential modules playbook
- Essential modules execution
- Command and shell output
- Handler execution
- Handler skipped on second run
- Check mode
- Diff mode
- Verbose execution
- List hosts
- List tasks
- Multi-play execution
- Web server verification
- Application server verification
- Database server verification

---

## Key Takeaways

- Playbooks provide repeatable infrastructure automation.
- Ansible modules simplify common administrative tasks.
- Handlers prevent unnecessary service restarts.
- Idempotency ensures consistent infrastructure state.
- Dry-run and diff mode help validate production changes safely.
- Multiple plays allow different server roles to be managed from a single playbook.

---

## Outcome

Successfully built and executed multiple Ansible playbooks to automate software installation, service management, configuration deployment, handlers, and role-based server configuration. This lab strengthened my understanding of infrastructure automation and reinforced best practices for writing safe, reusable, and idempotent Ansible playbooks.
