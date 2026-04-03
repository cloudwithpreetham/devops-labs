# Day 72 - Ansible Project: Automate Docker and Nginx Deployment

## Project Overview

This project demonstrates a complete Infrastructure as Code (IaC) workflow using **Ansible** to automate the deployment of a Dockerized application behind an Nginx reverse proxy.

The automation is organized into reusable Ansible roles that install Docker, deploy a containerized application, configure Nginx as a reverse proxy, and validate the deployment. The project follows production-style Ansible practices with modular roles, variables, templates, handlers, and idempotent playbooks.

---

## Project Architecture

```
                Control Node
              (Ubuntu + Ansible)
                     │
          SSH + Ansible Playbooks
                     │
        ┌──────────────────────────┐
        │      Amazon Linux EC2    │
        │                          │
        │  Nginx (Port 80)         │
        │         │                │
        │         ▼                │
        │ Docker Container         │
        │ nginx:latest             │
        │ Port 8080                │
        └──────────────────────────┘
```

---

## Technologies Used

- Ansible
- Amazon Linux 2023
- Docker
- Docker Hub
- Nginx
- YAML
- Jinja2 Templates
- EC2
- SSH

---

## Features

- Modular Ansible project structure
- Reusable Ansible roles
- Common server configuration
- Automated Docker installation
- Docker container deployment
- Nginx reverse proxy automation
- Jinja2 templates
- Ansible handlers
- Variables and defaults
- Health check using Ansible URI module
- Idempotent deployments
- Production-style Infrastructure as Code

---

## Project Structure

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
│   ├── docker
│   └── nginx
```

---

## Roles

### Common

Responsible for initial server configuration.

Tasks include:

- Package installation
- Hostname configuration
- Timezone configuration
- Deploy user creation

---

### Docker

Responsible for container deployment.

Tasks include:

- Install Docker
- Enable Docker service
- Pull Docker image
- Run Docker container
- Verify application health

---

### Nginx

Responsible for reverse proxy configuration.

Tasks include:

- Install Nginx
- Deploy reverse proxy template
- Validate configuration
- Reload Nginx automatically
- Enable Nginx service

---

## Deployment

Run the complete project:

```bash
ansible-playbook site.yml
```

Dry run:

```bash
ansible-playbook site.yml --check --diff
```

Run only Common role:

```bash
ansible-playbook site.yml --tags common
```

Run only Docker role:

```bash
ansible-playbook site.yml --tags docker
```

Run only Nginx role:

```bash
ansible-playbook site.yml --tags nginx
```

---

## Verification

Check Docker container:

```bash
docker ps
```

Access container directly:

```bash
curl http://localhost:8080
```

Access through Nginx reverse proxy:

```bash
curl http://localhost
```

---

## Skills Demonstrated

- Infrastructure as Code
- Configuration Management
- Docker Automation
- Nginx Automation
- Reverse Proxy Configuration
- Ansible Roles
- Variables
- Templates
- Handlers
- Group Variables
- Idempotent Playbooks
- Server Automation

---

## Learning Outcomes

By completing this project, I learned how to:

- Build reusable Ansible roles
- Automate server provisioning
- Deploy Docker containers with Ansible
- Configure Nginx using Jinja2 templates
- Use handlers for service management
- Organize Ansible projects following production best practices
- Validate deployments through automated health checks
- Adapt Ansible playbooks for Amazon Linux 2023

---

## Screenshots

This project includes screenshots demonstrating:

- Project directory structure
- Successful Ansible connectivity
- Common role execution
- Docker installation
- Docker container deployment
- Running containers
- Application running on port 8080
- Nginx reverse proxy configuration
- Full playbook execution
- Idempotent deployment verification

---

## Key Takeaways

This project combines the core concepts learned throughout the Ansible module into a complete automation workflow. Using reusable roles, templates, variables, and handlers, a fresh server can be transformed into a fully configured environment running a Dockerized application behind an Nginx reverse proxy with a single Ansible playbook.

---

## Connect With Me

If you enjoyed this project or have suggestions for improvement, feel free to connect with me and follow my **#90DaysOfDevOps** journey.
