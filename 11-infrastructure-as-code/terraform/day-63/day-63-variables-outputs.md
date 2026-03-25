# Day 63 - Variables, Outputs, Data Sources and Expressions

## Objective

The goal of Day 63 was to make Terraform configurations dynamic, reusable, and environment-aware by replacing hardcoded values with variables, outputs, data sources, locals, and expressions.

---

# Task 1: Variables

## variables.tf

```hcl
variable "region" {
  description = "AWS Region"
  type        = string
  default     = "us-west-2"
}

variable "vpc_cidr" {
  description = "VPC CIDR Block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnet_cidr" {
  description = "Subnet CIDR Block"
  type        = string
  default     = "10.0.1.0/24"
}

variable "instance_type" {
  description = "EC2 Instance Type"
  type        = string
  default     = "t3.micro"
}

variable "project_name" {
  description = "Project Name"
  type        = string
}

variable "environment" {
  description = "Deployment Environment"
  type        = string
  default     = "dev"
}

variable "allowed_ports" {
  description = "Allowed Ingress Ports"
  type        = list(number)

  default = [
    22,
    80,
    443
  ]
}

variable "extra_tags" {
  description = "Additional Tags"
  type        = map(string)
  default     = {}
}
```

## Terraform Variable Types

Terraform supports several variable types:

| Type   | Description                  |
| ------ | ---------------------------- |
| string | Text values                  |
| number | Numeric values               |
| bool   | True or False                |
| list   | Ordered collection of values |
| map    | Key-value pairs              |

---

# Task 2: Variable Files

## terraform.tfvars (Development)

```hcl
project_name  = "terraweek"
environment   = "dev"
instance_type = "t3.micro"
```

## prod.tfvars (Production)

```hcl
project_name  = "terraweek"
environment   = "prod"
instance_type = "t3.small"

vpc_cidr    = "10.1.0.0/16"
subnet_cidr = "10.1.1.0/24"
```

---

# Variable Precedence

Terraform applies variable values using the following precedence order:

Lowest Priority → Highest Priority

```text
Variable Defaults
↓
TF_VAR_* Environment Variables
↓
terraform.tfvars
↓
*.auto.tfvars
↓
-var-file
↓
-var
```

### Examples

Default:

```hcl
variable "environment" {
  default = "dev"
}
```

Environment Variable:

```bash
export TF_VAR_environment="staging"
```

Variable File:

```hcl
environment = "prod"
```

CLI Override:

```bash
terraform plan -var="environment=production"
```

The CLI value takes highest precedence.

---

# Task 3: Outputs

## outputs.tf

```hcl
output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_id" {
  value = aws_subnet.public.id
}

output "instance_id" {
  value = aws_instance.main.id
}

output "instance_public_ip" {
  value = aws_instance.main.public_ip
}

output "instance_public_dns" {
  value = aws_instance.main.public_dns
}

output "security_group_id" {
  value = aws_security_group.main.id
}
```

## Terraform Outputs

```bash
terraform output
```

Output:

```text
instance_id = "i-0d6462771d9f2adb8"
instance_public_dns = "ec2-34-220-76-117.us-west-2.compute.amazonaws.com"
instance_public_ip = "34.220.76.117"
security_group_id = "sg-0bc5a5d10b9f9cdad"
subnet_id = "subnet-0048c195ee6689702"
vpc_id = "vpc-06987088bf54a4b4b"
```

### Screenshot

Add a screenshot here showing:

```bash
terraform output
```

and

```bash
terraform output -json
```

---

# Task 4: Data Sources

## data.tf

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}
```

### Resource vs Data Source

#### Resource

Creates infrastructure.

```hcl
resource "aws_instance" "main" {}
```

Examples:

* VPC
* EC2
* Security Groups
* S3 Buckets

#### Data Source

Reads existing information.

```hcl
data "aws_ami" "ubuntu" {}
```

Examples:

* AMIs
* Availability Zones
* Existing VPCs

Data Sources are read-only and do not create infrastructure.

---

# Task 5: Locals

## locals.tf

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

### Benefits

* Reusable naming convention
* Consistent tagging
* Reduced code duplication
* Easier maintenance

Generated resource names:

```text
terraweek-prod-vpc
terraweek-prod-subnet
terraweek-prod-server
terraweek-prod-logs
```

---

# Task 6: Expressions and Functions

## Conditional Expression

```hcl
instance_type = var.environment == "prod" ? "t3.small" : var.instance_type
```

### Result

| Environment | Instance Type |
| ----------- | ------------- |
| dev         | t3.micro      |
| prod        | t3.small      |

---

# Useful Terraform Functions

## 1. upper()

Converts text to uppercase.

```hcl
upper("terraweek")
```

Output:

```text
TERRAWEEK
```

---

## 2. join()

Joins multiple strings.

```hcl
join("-", ["terra", "week", "2026"])
```

Output:

```text
terra-week-2026
```

---

## 3. length()

Returns item count.

```hcl
length(["a", "b", "c"])
```

Output:

```text
3
```

---

## 4. lookup()

Retrieves values from maps.

```hcl
lookup({
  dev  = "t3.micro"
  prod = "t3.small"
}, "dev")
```

Output:

```text
t2.micro
```

---

## 5. cidrsubnet()

Creates subnet CIDRs dynamically.

```hcl
cidrsubnet("10.0.0.0/16", 8, 1)
```

Output:

```text
10.0.1.0/24
```

---

# Variable vs Local vs Output vs Data

| Component   | Purpose                                  |
| ----------- | ---------------------------------------- |
| Variable    | Accept input values                      |
| Local       | Store reusable computed values           |
| Output      | Display and export values                |
| Data Source | Read existing infrastructure information |

---

# Troubleshooting

### Public DNS Not Assigned

Initially, the EC2 instance received a Public IP but no Public DNS hostname.

Problem:

```text
instance_public_dns = ""
```

Root Cause:

The VPC was created without DNS settings enabled.

Solution:

```hcl
enable_dns_support   = true
enable_dns_hostnames = true
```

After recreating the EC2 instance:

```text
instance_public_dns = "ec2-34-220-76-117.us-west-2.compute.amazonaws.com"
```

---

# Key Learnings

* Terraform variables make configurations reusable.
* tfvars files allow environment-specific deployments.
* Outputs expose infrastructure details after deployment.
* Data sources eliminate hardcoded values.
* Locals improve consistency and reduce duplication.
* Conditional expressions enable environment-aware infrastructure.
* Built-in functions simplify infrastructure calculations.
* Proper VPC DNS settings are required for EC2 public DNS hostnames.

---

# Conclusion

Successfully converted a static Terraform configuration into a reusable, environment-aware Infrastructure as Code solution using Variables, Outputs, Data Sources, Locals, Functions, and Conditional Expressions. The infrastructure now supports multiple environments with minimal configuration changes while following Terraform best practices.
