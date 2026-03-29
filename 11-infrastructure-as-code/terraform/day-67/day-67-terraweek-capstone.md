# Day 67 – TerraWeek Capstone: Multi-Environment Infrastructure with Workspaces and Modules

## Overview

Day 67 marks the completion of TerraWeek and brings together all Terraform concepts learned throughout the week into a real-world multi-environment infrastructure project.

The objective was to create a reusable Terraform codebase capable of deploying isolated AWS environments using:

- Custom Terraform Modules
- Terraform Workspaces
- Environment-specific Variables
- Dynamic Security Group Rules
- Consistent Resource Tagging
- Infrastructure as Code Best Practices

Using a single Terraform codebase, three isolated environments were provisioned:

- Development (dev)
- Staging (stg)
- Production (prd)

Each environment received its own:

- VPC
- Public Subnet
- Internet Gateway
- Route Table
- Security Group
- EC2 Instance

All infrastructure was managed using Terraform workspaces, demonstrating how infrastructure teams manage multiple environments at scale.

---

# Project Structure

```text
terraweek-capstone/
├── main.tf
├── variables.tf
├── outputs.tf
├── providers.tf
├── locals.tf
├── dev.tfvars
├── stg.tfvars
├── prd.tfvars
├── .gitignore
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   │
│   ├── security-group/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   │
│   └── ec2-instance/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
```

![Terraform capstone project structure](screenshots/01-project-structure.png)

---

# Terraform Workspaces

Created dedicated workspaces for each environment:

```bash
terraform workspace new dev
terraform workspace new stg
terraform workspace new prd
```

Verified workspaces:

```bash
terraform workspace list
```

Output:

```text
default
dev
stg
prd
```

![Terraform workspace list showing dev, stg, and prd](screenshots/02-workspace-list.png)

---

# Workspace Questions

## 1. What does terraform.workspace return?

`terraform.workspace` returns the name of the currently selected workspace.

Example:

```hcl
terraform.workspace
```

Output:

```text
dev
```

or

```text
stg
```

or

```text
prd
```

depending on the selected workspace.

---

## 2. Where does each workspace store state?

Terraform stores state separately for each workspace:

```text
terraform.tfstate.d/
├── dev/
│   └── terraform.tfstate
├── stg/
│   └── terraform.tfstate
└── prd/
    └── terraform.tfstate
```

Each environment maintains an independent state file.

---

## 3. Workspaces vs Separate Directories

### Workspaces

Advantages:

- Single codebase
- Easier maintenance
- Consistent infrastructure
- Less duplication

### Separate Directories

Advantages:

- Complete isolation
- Independent backend configuration
- Better for large production environments

---

# Custom Module 1 – VPC

## Resources Created

- VPC
- Public Subnet
- Internet Gateway
- Route Table
- Route
- Route Table Association

## Outputs

```hcl
output "vpc_id" {}
output "subnet_id" {}
```

---

# Custom Module 2 – Security Group

## Features

- Dynamic ingress rules
- Allow-all egress
- Environment-aware tagging

Example:

```hcl
dynamic "ingress" {
  for_each = var.ingress_ports

  content {
    from_port   = ingress.value
    to_port     = ingress.value
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

## Outputs

```hcl
output "sg_id" {}
```

---

# Custom Module 3 – EC2 Instance

## Resources

- Amazon Linux 2023 EC2 Instance

## Outputs

```hcl
output "instance_id" {}
output "public_ip" {}
```

---

# Root Module

## Workspace-Aware Locals

```hcl
locals {
  environment = terraform.workspace

  name_prefix = "${var.project_name}-${local.environment}"

  common_tags = {
    Project     = var.project_name
    Environment = local.environment
    ManagedBy   = "Terraform"
    Workspace   = terraform.workspace
  }
}
```

---

# Environment Configuration

## Development

```hcl
vpc_cidr      = "10.0.0.0/16"
subnet_cidr   = "10.0.1.0/24"
instance_type = "t3.micro"

ingress_ports = [
  22,
  80
]
```

### Characteristics

- SSH enabled
- HTTP enabled
- Smallest instance

![Development security group allowing SSH and HTTP](screenshots/08-dev-security-group.png)

---

## Staging

```hcl
vpc_cidr      = "10.1.0.0/16"
subnet_cidr   = "10.1.1.0/24"
instance_type = "t3.small"

ingress_ports = [
  22,
  80,
  443
]
```

### Characteristics

- SSH enabled
- HTTP enabled
- HTTPS enabled

![Staging security group allowing SSH, HTTP, and HTTPS](screenshots/09-stg-security-group.png)

---

## Production

```hcl
vpc_cidr      = "10.2.0.0/16"
subnet_cidr   = "10.2.1.0/24"
instance_type = "m7i-flex.large"

ingress_ports = [
  80,
  443
]
```

### Characteristics

- No SSH exposure
- HTTP enabled
- HTTPS enabled
- Larger instance type

![Production security group without SSH exposure](screenshots/10-prd-security-group.png)

---

# Deployment Verification

## Development

```text
instance_id       = i-0eef2d7683d2c500e
public_ip         = 34.219.241.109
security_group_id = sg-00baf7231222a7eb0
subnet_id         = subnet-0bd2cd10bf57c4a4f
vpc_id            = vpc-0990400f708efa0d1
```

![Development Terraform outputs](screenshots/03-dev-output.png)

---

## Staging

```text
instance_id       = i-099dd640e47762cff
public_ip         = 18.246.61.161
security_group_id = sg-090ddbcd7f1a4c0e5
subnet_id         = subnet-0fbdae518228b4c74
vpc_id            = vpc-0ae6428023f2e9702
```

![Staging Terraform outputs](screenshots/04-stg-output.png)

---

## Production

```text
instance_id       = i-0eada060a448798f4
public_ip         = 35.90.45.127
security_group_id = sg-0c944291e065d3ba4
subnet_id         = subnet-01583c829cf998683
vpc_id            = vpc-0a1b55628dbaf83a3
```

![Production Terraform outputs](screenshots/05-prd-output.png)

---

# Workspace Isolation Verification

Each workspace produced unique:

- VPC IDs
- Subnet IDs
- Security Groups
- EC2 Instances
- Public IPs

This confirms complete environment isolation while using a single Terraform codebase.

![Terraform workspace isolation proof](screenshots/14-workspace-isolation-proof.png)

## AWS Console Verification

All three VPCs were visible in AWS at the same time, each with its own CIDR range.

![All VPCs deployed for dev, stg, and prd](screenshots/06-all-vpcs.png)

The EC2 dashboard showed one instance per workspace/environment.

![All EC2 instances deployed for dev, stg, and prd](screenshots/07-all-ec2-instances.png)

The VPC detail pages confirmed separate networking for each environment.

![Development VPC details](screenshots/11-dev-vpc-details.png)

![Staging VPC details](screenshots/12-stg-vpc-details.png)

![Production VPC details](screenshots/13-prd-vpc-details.png)

---

# Terraform Best Practices Guide

## 1. File Structure

Separate files by responsibility:

- providers.tf
- variables.tf
- outputs.tf
- locals.tf
- main.tf

---

## 2. State Management

- Use remote backends
- Enable state locking
- Enable versioning
- Protect backend access

---

## 3. Variables

- Avoid hardcoded values
- Use tfvars files
- Use validation blocks

---

## 4. Modules

- One responsibility per module
- Clearly define inputs
- Clearly define outputs
- Version modules

---

## 5. Workspaces

- Separate environments
- Reduce code duplication
- Use terraform.workspace

---

## 6. Security

- Ignore state files
- Ignore secrets
- Encrypt state
- Apply least privilege

---

## 7. Commands

Always run:

```bash
terraform fmt
terraform validate
terraform plan
```

before applying.

---

## 8. Tagging

Every resource should include:

- Project
- Environment
- ManagedBy

---

## 9. Naming Convention

```text
<project>-<environment>-<resource>
```

Examples:

```text
terraweek-dev-vpc
terraweek-stg-server
terraweek-prd-sg
```

---

## 10. Cleanup

Destroy unused environments to avoid unnecessary cloud costs.

![Clean Terraform workspace after environment cleanup](screenshots/15-clean-workspace.png)

---

# TerraWeek Learning Journey

| Day | Concepts                                                         |
| --- | ---------------------------------------------------------------- |
| 61  | IaC, HCL, Terraform Basics, State                                |
| 62  | Providers, Resources, Dependencies, Lifecycle                    |
| 63  | Variables, Outputs, Data Sources, Locals                         |
| 64  | Remote Backend, Locking, Drift Detection                         |
| 65  | Custom Modules, Registry Modules                                 |
| 66  | EKS Deployment with Terraform                                    |
| 67  | Workspaces, Multi-Environment Infrastructure, Terraform Capstone |

---

# Key Takeaways

- Terraform enables infrastructure automation through code.
- Modules improve reusability and maintainability.
- Workspaces simplify environment management.
- State management is critical for production deployments.
- Tagging and naming standards improve operational visibility.
- Security should be integrated into infrastructure design.
- Infrastructure should always be reproducible, reviewable, and disposable.

Day 67 successfully concluded TerraWeek with a complete multi-environment AWS infrastructure built from a single Terraform codebase using custom modules and workspaces.
