# Day 63 - Variables, Outputs, Data Sources and Expressions

## Overview

On Day 63 of the #90DaysOfDevOps journey, I transformed a static Terraform configuration into a reusable and environment-aware Infrastructure as Code solution.

The focus of this lab was to eliminate hardcoded values and leverage Terraform features such as Variables, Variable Files, Outputs, Data Sources, Locals, Functions, and Conditional Expressions to build flexible infrastructure deployments across multiple environments.

---

## Objectives

* Replace hardcoded values with Terraform variables
* Use `.tfvars` files for environment-specific configurations
* Generate outputs after infrastructure deployment
* Fetch dynamic values using data sources
* Create reusable values with locals
* Practice Terraform functions and expressions
* Implement environment-based resource customization

---

## Project Structure

```text
day-63/
├── provider.tf
├── variables.tf
├── terraform.tfvars
├── prod.tfvars
├── data.tf
├── locals.tf
├── outputs.tf
├── main.tf
├── terraform.tfstate
├── terraform.tfstate.backup
└── day-63-variables-outputs.md
```

---

## Infrastructure Components

This Terraform configuration provisions:

* AWS VPC
* Public Subnet
* Internet Gateway
* Route Table
* Route Table Association
* Security Group
* EC2 Instance
* S3 Bucket

---

## Variables

The following variables were implemented:

| Variable      | Type         |
| ------------- | ------------ |
| region        | string       |
| vpc_cidr      | string       |
| subnet_cidr   | string       |
| instance_type | string       |
| project_name  | string       |
| environment   | string       |
| allowed_ports | list(number) |
| extra_tags    | map(string)  |

---

## Environment Configurations

### Development

```hcl
project_name  = "terraweek"
environment   = "dev"
instance_type = "t3.micro"
```

### Production

```hcl
project_name  = "terraweek"
environment   = "prod"
instance_type = "t3.small"

vpc_cidr    = "10.1.0.0/16"
subnet_cidr = "10.1.1.0/24"
```

---

## Data Sources

Instead of hardcoding values, Terraform dynamically fetches:

### Latest Ubuntu AMI

```hcl
data "aws_ami" "ubuntu"
```

### Availability Zones

```hcl
data "aws_availability_zones" "available"
```

Benefits:

* No hardcoded AMI IDs
* Region-independent deployments
* Always uses the latest Ubuntu image

---

## Locals

Reusable local values were created for consistent naming and tagging.

```hcl
locals {
  name_prefix = "${var.project_name}-${var.environment}"

  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}
```

Example generated names:

```text
terraweek-prod-vpc
terraweek-prod-subnet
terraweek-prod-server
terraweek-prod-logs
```

---

## Conditional Expressions

Environment-specific instance sizing:

```hcl
instance_type = var.environment == "prod" ? "t3.small" : var.instance_type
```

Result:

| Environment | Instance Type |
| ----------- | ------------- |
| Dev         | t3.micro      |
| Prod        | t3.small      |

---

## Outputs

Terraform outputs expose useful infrastructure information after deployment.

```bash
terraform output
```

Example:

```text
instance_id = "i-0d6462771d9f2adb8"
instance_public_dns = "ec2-34-220-76-117.us-west-2.compute.amazonaws.com"
instance_public_ip = "34.220.76.117"
security_group_id = "sg-0bc5a5d10b9f9cdad"
subnet_id = "subnet-0048c195ee6689702"
vpc_id = "vpc-06987088bf54a4b4b"
```

---

## Terraform Functions Practiced

### upper()

```hcl
upper("terraweek")
```

### join()

```hcl
join("-", ["terra", "week", "2026"])
```

### length()

```hcl
length(["a", "b", "c"])
```

### lookup()

```hcl
lookup({dev = "t3.micro", prod = "t3.small"}, "dev")
```

### cidrsubnet()

```hcl
cidrsubnet("10.0.0.0/16", 8, 1)
```

---

## Commands Used

### Initialize Terraform

```bash
terraform init
```

### Format Configuration

```bash
terraform fmt
```

### Validate Configuration

```bash
terraform validate
```

### Plan Deployment

```bash
terraform plan
```

### Production Plan

```bash
terraform plan -var-file="prod.tfvars"
```

### Apply Changes

```bash
terraform apply -var-file="prod.tfvars"
```

### View Outputs

```bash
terraform output
```

```bash
terraform output instance_public_ip
```

```bash
terraform output -json
```

---

## Key Learnings

* Variables make Terraform configurations reusable.
* Variable files simplify multi-environment deployments.
* Outputs provide infrastructure information after deployment.
* Data sources remove dependency on hardcoded values.
* Locals reduce duplication and improve consistency.
* Conditional expressions enable environment-specific behavior.
* Terraform functions simplify data manipulation and networking calculations.
* Proper VPC DNS settings are required for EC2 public DNS hostname assignment.

---

## Outcome

Successfully built a fully parameterized Terraform infrastructure capable of supporting multiple environments with minimal changes. The configuration now follows Infrastructure as Code best practices by using dynamic values, reusable logic, and environment-aware resource provisioning.

---

## Tech Stack

* Terraform
* AWS EC2
* AWS VPC
* AWS Subnet
* AWS Internet Gateway
* AWS Route Tables
* AWS Security Groups
* AWS S3
* Ubuntu Server

---

## Author

**Preetham Pereira**

Day 63 of #90DaysOfDevOps
