# Day 68 - Terraform Modules with Multiple EC2 Instances & Ansible Ad-Hoc Commands

![Terraform](https://img.shields.io/badge/Terraform-v1.x-623CE4?style=for-the-badge&logo=terraform)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20VPC-FF9900?style=for-the-badge&logo=amazonaws)
![Ansible](https://img.shields.io/badge/Ansible-Core%202.16-EE0000?style=for-the-badge&logo=ansible)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu)

---

# Project Overview

On **Day 68** of my **90 Days of DevOps** journey, I combined **Terraform** and **Ansible** to automate both infrastructure provisioning and server management.

Using reusable Terraform modules, I provisioned a complete AWS environment consisting of:

- Custom VPC
- Public Subnet
- Internet Gateway
- Route Table
- Security Group
- Three Amazon Linux EC2 instances

After provisioning, I configured **Ansible** to remotely manage the servers using ad-hoc commands for administration, software installation, file distribution, and inventory pattern matching.

This project demonstrates the complete Infrastructure as Code (IaC) workflow—from provisioning cloud infrastructure to configuring servers.

---

# Project Architecture

```text
                    Terraform
                        │
                        ▼
              AWS Infrastructure
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   Web Server      App Server      DB Server
        │               │               │
        └───────────────┼───────────────┘
                        │
                   Ansible Control Node
                        │
          SSH + Inventory + Ad-Hoc Commands
```

---

# Project Structure

```text
day-68/
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── locals.tf
│   ├── provider.tf
│   ├── versions.tf
│   ├── dev.tfvars
│   ├── modules/
│   │   ├── ec2-instance/
│   │   ├── security-group/
│   │   └── vpc/
│   └── ansible-server-key.pem
│
└── ansible-practice/
    ├── inventory
    ├── ansible.cfg
    └── hello.txt
```

---

# Technologies Used

- Terraform
- AWS EC2
- AWS VPC
- AWS Security Groups
- AWS Internet Gateway
- Terraform Modules
- Terraform Workspaces
- Ansible Core 2.16
- Amazon Linux 2023
- Ubuntu

---

# Objectives

- Build reusable Terraform modules
- Provision AWS infrastructure
- Use Terraform Workspaces
- Deploy multiple EC2 instances
- Configure Ansible inventory
- Execute Ansible ad-hoc commands
- Install packages remotely
- Transfer files across servers
- Practice inventory groups and host patterns

---

# Terraform Implementation

## Modules Created

### VPC Module

Responsible for

- VPC
- Public Subnet
- Internet Gateway
- Route Table
- Route Association

---

### Security Group Module

Configured

- SSH (22)
- HTTP (80)

---

### EC2 Module

Reusable module supporting

- Dynamic AMI
- Instance type
- Security Groups
- Multiple server creation using `count`
- Dynamic naming

---

# Workspace Configuration

Environment separation was achieved using

```bash
terraform workspace
```

Current workspace

```text
dev
```

---

# Local Values

Implemented

```hcl
locals {
  environment = terraform.workspace
}
```

This automatically generated environment-specific names and tags.

---

# Multiple EC2 Instances

Created three EC2 instances dynamically using

```hcl
count
```

Servers deployed

- Web Server
- Application Server
- Database Server

Example naming

```text
terraweek-dev-web
terraweek-dev-app
terraweek-dev-db
```

---

# Infrastructure Provisioned

Terraform created

- 1 VPC
- 1 Public Subnet
- 1 Internet Gateway
- 1 Route Table
- 1 Route Association
- 1 Security Group
- 3 EC2 Instances

---

# Terraform Commands

Initialize

```bash
terraform init
```

Validate

```bash
terraform validate
```

Apply

```bash
terraform apply -var-file=dev.tfvars
```

Outputs

```bash
terraform output
```

Destroy

```bash
terraform destroy -var-file=dev.tfvars
```

---

# Ansible Inventory

Configured inventory

```ini
[web]
web-server

[app]
app-server

[db]
db-server

[all:vars]
ansible_user=ec2-user
```

---

# Connectivity Test

Verified SSH connectivity

```bash
ansible all -m ping
```

Result

```text
SUCCESS
```

for all three servers.

---

# Ansible Ad-Hoc Commands

## Check Uptime

```bash
ansible all -m command -a "uptime"
```

---

## Memory Usage

```bash
ansible web -m command -a "free -h"
```

---

## Disk Usage

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

## Copy File

```bash
echo "Hello from Ansible" > hello.txt

ansible all -m copy -a "src=hello.txt dest=/tmp/hello.txt"
```

---

## Verify File

```bash
ansible all -m command -a "cat /tmp/hello.txt"
```

Output

```text
Hello from Ansible
```

---

# Inventory Pattern Matching

Tested

```bash
ansible application -m ping

ansible db -m ping

ansible all_servers -m ping

ansible 'web:app' -m ping

ansible 'all:!db' -m ping
```

Successfully verified all inventory groups and host selection patterns.

---

# Screenshots

## Terraform

- Terraform Init
- Terraform Validate
- Terraform Apply
- Terraform Outputs

---

## AWS

- EC2 Dashboard
- VPC
- Security Group
- Subnet

---

## Ansible

- Ping All Hosts
- Uptime Command
- Memory Check
- Disk Usage
- Git Installation
- Git Version
- Copy Module
- File Verification
- Inventory Pattern Matching

---

# Challenges Faced

## Missing AWS Key Pair

Terraform initially failed because the EC2 Key Pair did not exist.

**Resolution**

Created/imported the required key pair and reran Terraform Apply successfully.

---

## Dynamic EC2 Provisioning

Implemented the `count` meta-argument to provision multiple servers from a single reusable module.

---

## Remote Connectivity

Verified SSH connectivity using the Ansible Ping module before running administrative tasks.

---

# Key Learnings

- Terraform Modules
- Terraform Workspaces
- Local Values
- Terraform Outputs
- AWS Infrastructure Provisioning
- Dynamic Resource Creation
- EC2 Automation
- Infrastructure as Code
- Ansible Inventory
- Ad-Hoc Commands
- Remote Package Installation
- File Distribution
- Inventory Groups
- Host Pattern Matching
- Infrastructure Automation

---

# Outcome

Successfully built a modular AWS infrastructure using Terraform and managed all deployed EC2 instances using Ansible.

This project demonstrates an end-to-end DevOps workflow where infrastructure provisioning and configuration management are automated using industry-standard tools.

---

# Repository

```text
devops-labs/
└── 12-configuration-management/
    └── ansible/
        └── day-68/
```

---

# Author

**Preetham**

**90 Days of DevOps Journey**

Day 68 - Terraform Modules + Ansible Ad-Hoc Commands
