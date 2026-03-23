# Day 61 - Introduction to Terraform and Your First AWS Infrastructure

## Overview

Day 61 marks the beginning of my Infrastructure as Code (IaC) journey using Terraform. In this hands-on lab, I installed Terraform, configured AWS credentials, provisioned AWS resources through code, explored Terraform state management, and safely destroyed the created infrastructure.

The objective was to understand how modern DevOps teams manage cloud infrastructure in a repeatable, automated, and version-controlled manner.

---

## Learning Objectives

- Understand Infrastructure as Code (IaC)
- Learn Terraform fundamentals
- Configure AWS CLI authentication
- Create AWS resources using Terraform
- Explore Terraform state management
- Understand Terraform lifecycle commands
- Modify infrastructure through code
- Destroy infrastructure safely using Terraform

---

## Technologies Used

- Terraform
- AWS CLI
- Amazon S3
- Amazon EC2
- Linux (Ubuntu)
- Git & GitHub

---

## Project Structure

```text
day-61/
├── README.md
├── task.md
├── day-61-terraform-intro.md
├── terraform-basics/
│   ├── main.tf
│   ├── .gitignore
│   └── screenshots/
└── screenshots/
```

---

## Infrastructure as Code (IaC)

Infrastructure as Code is the practice of managing infrastructure through configuration files instead of manually creating resources through cloud consoles.

Benefits include:

- Automation
- Consistency
- Version Control
- Faster Deployments
- Reduced Human Error
- Reproducible Environments

---

## Terraform Configuration

### AWS Provider

```hcl
provider "aws" {
  region = "ap-south-1"
}
```

### S3 Bucket Resource

```hcl
resource "aws_s3_bucket" "terraweek_bucket" {
  bucket = "terraweek-preetham-2026"
}
```

### EC2 Instance Resource

```hcl
resource "aws_instance" "terraform_ec2" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = "t2.micro"

  tags = {
    Name = "TerraWeek-Day1"
  }
}
```

---

## Terraform Workflow

### Initialize Terraform

```bash
terraform init
```

Downloads required providers and initializes the working directory.

---

### Validate Configuration

```bash
terraform validate
```

Checks Terraform configuration syntax.

---

### Format Configuration

```bash
terraform fmt
```

Formats Terraform code according to best practices.

---

### Preview Changes

```bash
terraform plan
```

Shows the execution plan before applying changes.

---

### Create Infrastructure

```bash
terraform apply
```

Creates AWS resources defined in the Terraform configuration.

---

### View Current State

```bash
terraform show
```

Displays a human-readable representation of infrastructure state.

---

### List Managed Resources

```bash
terraform state list
```

Lists all resources currently managed by Terraform.

---

### Inspect Individual Resources

```bash
terraform state show aws_s3_bucket.terraweek_bucket
terraform state show aws_instance.terraform_ec2
```

Displays detailed information about specific resources.

---

### Destroy Infrastructure

```bash
terraform destroy
```

Removes all resources managed by Terraform.

---

## Terraform State Management

Terraform stores infrastructure information in:

```text
terraform.tfstate
```

The state file contains:

- Resource IDs
- Resource Attributes
- Metadata
- Infrastructure Mapping Information

Terraform uses this file to determine:

- What resources already exist
- What changes are required
- What resources need updating or deletion

---

## Important Files to Ignore

Terraform generates local files that should not be committed to Git.

### .gitignore

```gitignore
.terraform/
*.tfstate
*.tfstate.*
.terraform.lock.hcl
```

---

## Screenshots

### Terraform Initialization

- Terraform Provider Installation
- Successful Initialization

### Terraform Apply

- S3 Bucket Creation
- EC2 Instance Creation

### AWS Verification

- S3 Console Screenshot
- EC2 Console Screenshot

### Terraform State

- terraform state list
- terraform state show

### Terraform Destroy

- Successful Resource Cleanup

---

## Key Learnings

- Infrastructure can be managed entirely through code.
- Terraform follows a declarative approach.
- AWS resources can be provisioned consistently and repeatedly.
- Terraform state is critical for tracking infrastructure.
- Infrastructure changes can be previewed before execution.
- Resources can be safely destroyed when no longer required.

---

## Outcome

Successfully:

- Installed Terraform
- Configured AWS CLI
- Created an S3 Bucket using Terraform
- Created an EC2 Instance using Terraform
- Explored Terraform State Management
- Updated Infrastructure Through Code
- Destroyed Infrastructure Using Terraform

---

## Commands Summary

```bash
terraform version
aws configure
aws sts get-caller-identity

terraform init
terraform validate
terraform fmt
terraform plan
terraform apply

terraform show
terraform state list
terraform state show aws_s3_bucket.terraweek_bucket
terraform state show aws_instance.terraform_ec2

terraform destroy
```

---

## Conclusion

This project introduced the fundamentals of Terraform and Infrastructure as Code. By provisioning and managing AWS resources through configuration files, I gained practical experience with modern cloud automation practices used by DevOps and Platform Engineering teams.
