# Day 72 – Ansible Project: Automate Docker and Nginx Deployment

## Overview

On Day 72, I built a production-style Ansible project that automates the deployment of a Dockerized application behind an Nginx reverse proxy. The entire infrastructure is organized using reusable Ansible roles, templates, handlers, variables, and inventory files.

The project provisions a fresh server by installing Docker, deploying a containerized application, configuring Nginx as a reverse proxy, and validating the deployment through Ansible automation.

> **Environment**
>
> - Control Node: Ubuntu
> - Managed Nodes: Amazon Linux 2023 EC2
> - Automation Tool: Ansible
> - Container Runtime: Docker
> - Web Server: Nginx

---

# Objectives

- Build a complete Ansible project structure
- Organize automation using reusable roles
- Install Docker automatically
- Deploy a Docker container
- Configure Nginx as a reverse proxy
- Use variables, defaults, templates, and handlers
- Perform application health checks
- Execute idempotent deployments
- Prepare the project for production-style automation

---

# Project Directory Structure

```text
ansible-docker-project/
├── ansible.cfg
├── inventory.ini
├── site.yml
├── group_vars
│   ├── all.yml
│   └── web
│       └── vars.yml
├── roles
│   ├── common
│   │   ├── tasks
│   │   └── ...
│   ├── docker
│   │   ├── defaults
│   │   ├── handlers
│   │   ├── tasks
│   │   └── templates
│   └── nginx
│       ├── defaults
│       ├── handlers
│       ├── tasks
│       └── templates
```

---

# Technologies Used

- Ansible
- Amazon Linux 2023
- Docker
- Docker Hub
- Nginx
- Jinja2 Templates
- YAML
- SSH
- EC2

---

# Project Workflow

## 1. Configure Common Role

The Common role performs baseline server configuration.

Tasks performed:

- Update package cache
- Install common utilities
- Configure hostname
- Configure timezone
- Create deploy user

Installed packages:

- vim
- wget
- git
- tree
- jq
- unzip
- htop

---

## 2. Configure Docker Role

The Docker role automates container deployment.

Tasks performed:

- Install Docker
- Enable Docker service
- Start Docker service
- Configure deploy user permissions
- Pull Docker image
- Deploy Docker container
- Perform application health check

Default configuration:

| Variable              | Value  |
| --------------------- | ------ |
| docker_app_image      | nginx  |
| docker_app_tag        | latest |
| docker_app_name       | myapp  |
| docker_app_port       | 8080   |
| docker_container_port | 80     |

---

## 3. Configure Nginx Role

The Nginx role configures reverse proxy functionality.

Tasks performed:

- Install Nginx
- Remove default configuration
- Deploy reverse proxy template
- Validate Nginx configuration
- Enable Nginx service
- Reload Nginx using handlers

---

# Reverse Proxy Architecture

```
                Browser
                   │
                   ▼
          Nginx (Port 80)
                   │
                   ▼
        Docker Container
          nginx:latest
             Port 8080
```

---

# Master Playbook

The deployment is orchestrated through **site.yml**.

Execution order:

1. Common Role
2. Docker Role
3. Nginx Role

Deployment command:

```bash
ansible-playbook site.yml
```

Selective execution:

```bash
ansible-playbook site.yml --tags common

ansible-playbook site.yml --tags docker

ansible-playbook site.yml --tags nginx
```

---

# Verification

## Docker

Verified using:

```bash
docker ps
```

Result:

- Docker Engine installed
- Container running
- Port mapping successful

---

## Application

Verified using:

```bash
curl http://localhost:8080
```

Result:

- Default Nginx page served successfully from Docker container.

---

## Reverse Proxy

Verified using:

```bash
curl http://localhost
```

Result:

- Request successfully routed through Nginx to Docker container.

---

## Health Check

Application availability verified using the Ansible **uri** module after deployment.

---

# Idempotency

The project was executed multiple times to verify idempotent behavior.

Ansible correctly reported:

- Existing packages as **ok**
- Existing services as **ok**
- Existing configuration files as **ok**

This demonstrates that repeated executions do not unnecessarily modify the infrastructure.

---

# Amazon Linux 2023 Notes

While implementing this project on Amazon Linux 2023, a few platform-specific adjustments were required.

## curl Package Conflict

Amazon Linux ships with **curl-minimal** by default.

Installing the standard **curl** package causes dependency conflicts.

Solution:

- Removed **curl** from the package installation list.

---

## Package Manager

Instead of **yum**, Amazon Linux 2023 uses:

```bash
dnf
```

All package installation tasks were updated accordingly.

---

## Nginx Configuration

Amazon Linux includes a default server block inside:

```text
/etc/nginx/nginx.conf
```

This created a server-name conflict with the custom reverse proxy configuration.

Although the reverse proxy functioned correctly, the custom `/health` endpoint conflicted with the default configuration.

This behavior is specific to Amazon Linux's packaged Nginx configuration and does not affect the primary deployment workflow.

---

# Screenshots

Include the following screenshots:

- Project directory structure
- Successful Ansible ping
- Common role execution
- Docker installation
- Docker role execution
- Running Docker container (`docker ps`)
- Application on port 8080
- Nginx role execution
- Nginx service status
- Browser accessing application through port 80
- Successful full playbook execution
- Idempotency verification

---

# Skills Practiced

- Ansible Inventory
- Playbooks
- Roles
- Variables
- Group Variables
- Defaults
- Templates
- Handlers
- Docker Automation
- Nginx Automation
- Reverse Proxy Configuration
- Container Deployment
- Idempotent Infrastructure
- Infrastructure as Code

---

# Key Learnings

- Designed a modular Ansible project using reusable roles.
- Automated Docker installation and application deployment.
- Configured Nginx as a reverse proxy using Jinja2 templates.
- Used handlers for efficient service reloads.
- Applied Ansible variables and defaults for reusable configurations.
- Performed automated application validation using the `uri` module.
- Adapted playbooks for Amazon Linux 2023 by using `dnf` and handling package-specific differences.
- Built an end-to-end infrastructure automation workflow using Ansible.

---

# Conclusion

Day 72 combined the concepts learned throughout the Ansible module into a single production-style automation project.

Using reusable roles, templates, handlers, and variables, I automated the complete deployment of a Dockerized application behind an Nginx reverse proxy. The project demonstrates Infrastructure as Code principles, modular automation practices, and idempotent deployments that closely resemble real-world DevOps workflows.
