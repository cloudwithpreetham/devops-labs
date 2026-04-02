# Day 71 — Ansible Roles, Templates, Galaxy & Vault

## Overview

This project demonstrates production-grade Ansible automation using:

- Jinja2 Templates for dynamic configuration
- Custom Ansible Roles for modular automation
- Ansible Galaxy for reusable community roles
- Ansible Vault for secure secret management
- Multi-host orchestration using inventories

The goal is to move from basic playbooks to scalable DevOps automation patterns used in real-world environments.

---

## Project Structure

```

ansible-practice/
├── inventory.ini
├── site.yml
├── template-demo.yml
├── docker-setup.yml
├── db-setup.yml
├── group_vars/
│   └── db/
│       └── vault.yml (encrypted)
├── roles/
│   └── webserver/
│       ├── tasks/
│       ├── handlers/
│       ├── templates/
│       ├── defaults/
│       ├── vars/
│       └── meta/
├── templates/
└── README.md

```

---

## Features Implemented

### 1. Jinja2 Templates

Dynamic Nginx configuration generation using Ansible variables:

- app name
- hostname
- IP address
- custom ports

---

### 2. Custom Ansible Role (webserver)

The `webserver` role includes:

- Nginx installation
- Web root creation
- Virtual host configuration
- Index page deployment
- Service management via handlers

---

### 3. Ansible Galaxy Integration

Used community role:

```

geerlingguy.docker

```

Purpose:

- Automates Docker installation
- Handles OS-specific setup logic
- Reduces manual configuration effort

---

### 4. Docker Setup (Amazon Linux 2023)

Docker installed using native package manager:

- Docker Engine installed via `dnf`
- Service enabled and started
- ec2-user added to docker group

---

### 5. Ansible Vault (Security)

Sensitive data is encrypted using Vault:

Stored secrets:

- DB passwords
- Root credentials
- API keys

Vault ensures:

- No plaintext secrets in Git
- Secure CI/CD pipelines
- Controlled access via password file or prompt

---

## How to Run

### 1. Test Nginx template deployment

```bash
ansible-playbook -i inventory.ini template-demo.yml --diff
```

---

### 2. Run role-based deployment

```bash
ansible-playbook -i inventory.ini site.yml
```

---

### 3. Install Docker

```bash
ansible-playbook -i inventory.ini docker-setup.yml
```

---

### 4. Run DB setup with Vault

```bash
ansible-playbook -i inventory.ini db-setup.yml --ask-vault-pass
```

---

## Vault Usage

Create encrypted file:

```bash
ansible-vault create group_vars/db/vault.yml
```

View encrypted file:

```bash
ansible-vault view group_vars/db/vault.yml
```

Run with vault password file:

```bash
ansible-playbook -i inventory.ini db-setup.yml --vault-password-file .vault_pass
```

---

## Key Learnings

- Roles provide modular and reusable automation
- Templates enable dynamic configuration management
- Galaxy roles accelerate infrastructure setup
- Vault secures sensitive data in automation pipelines
- Amazon Linux requires OS-specific package handling

---

## DevOps Concepts Covered

- Infrastructure as Code (IaC)
- Configuration Management
- Secrets Management
- Role-based Architecture
- Multi-environment automation

---

## Outcome

By completing this project, I gained hands-on experience in building scalable, secure, and production-ready Ansible automation workflows used in real DevOps environments.
