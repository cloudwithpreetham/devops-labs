# Terraform Infrastructure as Code Journey (Days 61–67)

## Overview

This repository contains my hands-on Terraform learning journey as part of the **90 Days of DevOps Challenge**. Over these seven days, I explored Infrastructure as Code (IaC) concepts, Terraform fundamentals, state management, remote backends, AWS infrastructure provisioning, reusable modules, workspaces, and a complete Terraform capstone project.

The goal was to understand how modern DevOps engineers automate cloud infrastructure provisioning using Terraform.

---

## Learning Progress

| Day    | Topic                           | Key Concepts                             |
| ------ | ------------------------------- | ---------------------------------------- |
| Day 61 | Terraform Fundamentals          | Providers, Resources, Variables, Outputs |
| Day 62 | AWS Infrastructure Provisioning | EC2, VPC, Security Groups                |
| Day 63 | Terraform State Management      | State Files, State Commands              |
| Day 64 | Remote Backend Configuration    | S3 Backend, State Locking                |
| Day 65 | Terraform Modules               | Reusable Infrastructure Components       |
| Day 66 | Terraform Workspaces            | Environment Isolation (Dev, Stage, Prod) |
| Day 67 | Terraform Capstone Project      | End-to-End Infrastructure Deployment     |

---

# Directory Structure

```text
11-infrastructure-as-code/
└── terraform/
    ├── day-61/
    ├── day-62/
    ├── day-63/
    ├── day-64/
    ├── day-65/
    ├── day-66/
    ├── day-67/
    └── README.md
```

---

# Skills Covered

### Terraform Basics

- Installing Terraform
- Understanding Providers
- Creating Resources
- Variables and Outputs
- Terraform Lifecycle

### Infrastructure Management

- AWS Resource Provisioning
- Infrastructure Planning
- Infrastructure Updates
- Infrastructure Destruction

### State Management

- Terraform State Files
- State Inspection
- State Tracking
- Resource Synchronization

### Remote State

- S3 Backend Configuration
- State Storage
- State Locking
- Team Collaboration

### Terraform Modules

- Module Creation
- Module Reusability
- Infrastructure Standardization
- Modular Architecture

### Terraform Workspaces

- Environment Separation
- Multi-Environment Deployment
- Workspace Management

---

# Terraform Workflow

```text
Write Configuration
        ↓
terraform init
        ↓
terraform validate
        ↓
terraform plan
        ↓
terraform apply
        ↓
Infrastructure Created
        ↓
terraform destroy
```

---

# AWS Services Used

- Amazon EC2
- Amazon VPC
- Security Groups
- Amazon S3
- IAM
- Terraform Backend Services

---

# Commands Practiced

## Initialize Terraform

```bash
terraform init
```

## Validate Configuration

```bash
terraform validate
```

## Format Files

```bash
terraform fmt
```

## Preview Changes

```bash
terraform plan
```

## Deploy Infrastructure

```bash
terraform apply
```

## View State

```bash
terraform state list
```

## Show Outputs

```bash
terraform output
```

## Destroy Infrastructure

```bash
terraform destroy
```

---

# Capstone Highlights

The Terraform Capstone Project included:

- Reusable Terraform modules
- Multiple environments using workspaces
- Remote state management
- Automated infrastructure provisioning
- AWS resource deployment
- Clean and maintainable project structure

---

# Key Learnings

- Infrastructure can be managed using code.
- Terraform provides consistent and repeatable deployments.
- State management is critical for infrastructure tracking.
- Remote backends enable collaboration and safer workflows.
- Modules improve code reusability and maintainability.
- Workspaces simplify multi-environment deployments.
- Terraform is a core DevOps skill for cloud automation.

---

# Outcome

By completing Days 61–67, I gained practical experience in:

- Infrastructure as Code (IaC)
- AWS Automation
- Terraform State Management
- Remote Backends
- Module Development
- Environment Management
- Production-Ready Terraform Workflows

This week established a strong foundation for managing cloud infrastructure through automation and industry-standard DevOps practices.

---

## Author

**Preetham**
_90 Days of DevOps Challenge_
