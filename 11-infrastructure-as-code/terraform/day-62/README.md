# Day 62 - Providers, Resources and Dependencies

## Overview

On Day 62 of the #90DaysOfDevOps journey, I explored Terraform Providers, Resources, Dependencies, Lifecycle Rules, and Infrastructure Graphs by building a complete AWS networking stack from scratch.

This hands-on lab demonstrated how Terraform automatically manages resource creation order using dependency relationships and how explicit dependencies can be enforced when required.

---

## Objectives

- Configure the AWS Provider
- Understand Terraform version constraints
- Build a complete AWS networking infrastructure
- Learn implicit and explicit dependencies
- Visualize Terraform dependency graphs
- Work with lifecycle meta-arguments
- Understand Terraform destroy order

---

## Technologies Used

- Terraform
- AWS VPC
- AWS EC2
- AWS Security Groups
- AWS S3
- Graphviz
- AWS CLI

---

## Infrastructure Created

### Networking Components

- VPC (`10.0.0.0/16`)
- Public Subnet (`10.0.1.0/24`)
- Internet Gateway
- Route Table
- Route Table Association

### Security Components

- Security Group
  - SSH (22)
  - HTTP (80)
  - All outbound traffic

### Compute Components

- Amazon Linux EC2 Instance
- Public IP Assignment

### Storage Components

- S3 Bucket for application logs

---

## Provider Configuration

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}
```

---

## Terraform Workflow

### Initialize

```bash
terraform init
```

### Validate

```bash
terraform validate
```

### Plan

```bash
terraform plan
```

### Apply

```bash
terraform apply
```

### Visualize Dependency Graph

```bash
terraform graph | dot -Tpng > graph.png
```

### Destroy Infrastructure

```bash
terraform destroy
```

---

## Dependency Types

### Implicit Dependencies

Terraform automatically creates dependencies when resources reference other resources.

Example:

```hcl
vpc_id = aws_vpc.main.id
```

Terraform understands:

```text
VPC → Subnet
```

without requiring any additional configuration.

---

### Explicit Dependencies

Used when Terraform cannot automatically determine the relationship.

Example:

```hcl
depends_on = [
  aws_instance.main
]
```

This forces Terraform to create the EC2 instance before the S3 bucket.

---

## Dependency Graph

```text
VPC
├── Subnet
├── Internet Gateway
├── Security Group
│     └── EC2 Instance
│             └── S3 Bucket
└── Route Table
      └── Route Table Association
```

---

## Lifecycle Rules

### create_before_destroy

```hcl
lifecycle {
  create_before_destroy = true
}
```

Creates replacement resources before removing old ones.

---

### prevent_destroy

```hcl
lifecycle {
  prevent_destroy = true
}
```

Protects critical infrastructure from accidental deletion.

---

### ignore_changes

```hcl
lifecycle {
  ignore_changes = [tags]
}
```

Ignores updates made outside Terraform.

---

## Key Learnings

- Terraform Providers connect Terraform with cloud platforms.
- Version constraints improve stability and reproducibility.
- Terraform automatically builds dependency graphs.
- Resource references create implicit dependencies.
- `depends_on` creates explicit dependencies.
- Lifecycle rules provide advanced infrastructure control.
- Terraform destroys resources in reverse dependency order.
- State drift occurs when infrastructure changes outside Terraform.

---

## Screenshots

### Terraform Execution

- terraform-init.png
- terraform-plan.png
- terraform-apply.png

### AWS Resources

- aws-vpc.png
- aws-subnet.png
- aws-ec2.png

### Dependency Graph

- graph.png

---

## Outcome

Successfully provisioned and managed a complete AWS networking environment using Terraform while understanding how Terraform handles dependencies, lifecycle management, and infrastructure orchestration.

This lab strengthened my Infrastructure as Code (IaC) fundamentals and provided practical experience with real-world Terraform workflows.

---

## Tags

#90DaysOfDevOps #Terraform #AWS #DevOps #InfrastructureAsCode #CloudComputing #DevOpsKaJosh #TrainWithShubham
