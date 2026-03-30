# Day 68 – Terraform Modules + Ansible Ad-Hoc Commands

## Task Overview

Today's objective was to provision a complete AWS infrastructure using reusable Terraform modules and manage the created EC2 instances using Ansible ad-hoc commands.

The infrastructure was organized into independent modules for networking, security, and compute resources while using Terraform Workspaces to manage the development environment. After provisioning, Ansible was configured to remotely connect to all instances and execute administrative tasks without logging into each server manually.

---

# Objectives

- Build reusable Terraform modules
- Deploy AWS infrastructure using Terraform
- Use Terraform Workspaces for environment separation
- Create multiple EC2 instances using `count`
- Configure dynamic resource naming
- Verify infrastructure deployment
- Configure Ansible inventory
- Test SSH connectivity
- Execute Ansible ad-hoc commands
- Install packages remotely
- Copy files to multiple servers
- Practice Ansible inventory groups and host patterns

---

# Project Structure

```text
day-68/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── locals.tf
│   ├── dev.tfvars
│   ├── provider.tf
│   ├── versions.tf
│   ├── modules/
│   │   ├── vpc/
│   │   ├── security-group/
│   │   └── ec2-instance/
│   └── ansible-server-key.pem
│
└── ansible-practice/
    ├── inventory
    ├── ansible.cfg
    └── hello.txt
```

---

# Terraform Tasks Completed

## Created reusable modules

- VPC Module
- Security Group Module
- EC2 Module

---

## Configured Terraform Workspace

Workspace used

```
dev
```

Environment was dynamically obtained using

```hcl
terraform.workspace
```

---

## Local Values

Configured local values for

- Environment
- Name prefix
- Common tags

---

## EC2 Module Enhancements

Implemented

- count meta-argument
- Dynamic server names
- Parameterized variables
- Outputs

Generated instances

- Web Server
- Application Server
- Database Server

---

## Infrastructure Created

Terraform successfully created

- VPC
- Public Subnet
- Internet Gateway
- Route Table
- Route Association
- Security Group
- Three EC2 Instances

---

## Terraform Outputs

Verified outputs

- VPC ID
- Subnet ID
- Security Group ID
- Instance IDs
- Public IP Addresses

---

# Ansible Tasks Completed

Configured inventory groups

```ini
[web]

[app]

[db]

[all:vars]
```

Successfully verified connectivity using

```bash
ansible all -m ping
```

---

# Executed Ad-Hoc Commands

## Check uptime

```bash
ansible all -m command -a "uptime"
```

---

## Check memory

```bash
ansible web -m command -a "free -h"
```

---

## Check disk usage

```bash
ansible all -m command -a "df -h"
```

---

## Install Git

```bash
ansible web -m package -a "name=git state=present" --become
```

---

## Verify Git

```bash
ansible web -m command -a "git --version"
```

---

## Copy file

```bash
ansible all -m copy -a "src=hello.txt dest=/tmp/hello.txt"
```

---

## Verify copied file

```bash
ansible all -m command -a "cat /tmp/hello.txt"
```

---

# Inventory Pattern Matching

Verified inventory groups

```bash
ansible application -m ping

ansible db -m ping

ansible all_servers -m ping

ansible 'web:app' -m ping

ansible 'all:!db' -m ping
```

---

# Validation

Terraform

```bash
terraform init

terraform validate

terraform apply -var-file=dev.tfvars
```

All resources were provisioned successfully.

---

Ansible

```bash
ansible all -m ping
```

All hosts responded successfully.

---

# Key Learnings

- Modular Terraform project structure
- Reusable infrastructure modules
- Terraform Workspaces
- Terraform local values
- Dynamic resource creation using count
- Parameterized Terraform modules
- Infrastructure outputs
- Ansible inventory management
- Ad-hoc command execution
- Package management using Ansible
- File distribution using copy module
- Inventory groups
- Host pattern matching
- Remote server administration using SSH

---

# Challenges Faced

### Missing AWS Key Pair

Terraform initially failed because the specified EC2 key pair did not exist.

Resolved by creating/importing the required AWS Key Pair and rerunning Terraform Apply.

---

### Multiple EC2 Provisioning

Configured the EC2 module using

```hcl
count
```

to provision multiple servers dynamically.

---

### Remote Connectivity

Verified SSH access using

```bash
ansible all -m ping
```

before executing any administrative tasks.

---

# Outcome

Successfully provisioned a reusable AWS infrastructure using Terraform Modules and Workspaces.

Managed all EC2 instances centrally using Ansible ad-hoc commands, demonstrating infrastructure provisioning, remote administration, package installation, file transfer, and inventory management in a real-world DevOps workflow.
