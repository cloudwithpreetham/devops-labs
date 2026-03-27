# Day 65 – Terraform Modules: Build Reusable Infrastructure

## Project Overview

This project demonstrates how to create and use reusable Terraform modules for provisioning AWS infrastructure. Instead of defining all resources in a single Terraform configuration, custom modules were created for EC2 instances and Security Groups. Additionally, the official AWS VPC module from the Terraform Registry was used to simplify network provisioning.

The goal of this lab was to understand Terraform module architecture, improve code reusability, and follow Infrastructure as Code best practices used in production environments.

---

## Technologies Used

* Terraform
* AWS EC2
* AWS VPC
* AWS Security Groups
* Terraform Registry Modules
* Infrastructure as Code (IaC)

---

## Architecture

```text
                        ┌─────────────────┐
                        │   Root Module   │
                        └────────┬────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        ▼                        ▼                        ▼

┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│   VPC Module    │   │ Security Group  │   │  EC2 Module      │
│ (Registry)      │   │ (Custom)        │   │ (Custom)         │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         ▼                     ▼                     ▼

    AWS VPC          Security Group        Web Server EC2
    Public Subnets   Ports 22,80,443       API Server EC2
    Private Subnets
```

---

## Project Structure

```text
terraform/
├── providers.tf
├── variables.tf
├── outputs.tf
├── locals.tf
├── main.tf
│
└── modules/
    ├── ec2-instance/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    │
    └── security-group/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

---

## Custom Modules

### EC2 Instance Module

Reusable module used to provision EC2 instances with configurable:

* AMI ID
* Instance Type
* Subnet
* Security Groups
* Tags

Outputs:

* Instance ID
* Public IP
* Private IP

---

### Security Group Module

Reusable module used to create Security Groups with dynamic ingress rules.

Features:

* Dynamic ingress block
* Configurable ports
* Reusable across environments
* Open egress traffic

Example:

```hcl
ingress_ports = [22, 80, 443]
```

Automatically creates:

* SSH (22)
* HTTP (80)
* HTTPS (443)

---

## Terraform Registry Module

The project uses the official AWS VPC module:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

Benefits:

* Reduced configuration effort
* Built-in best practices
* Consistent VPC architecture
* Rich outputs for reuse

---

## Resources Created

### Networking

* 1 VPC
* 2 Public Subnets
* 2 Private Subnets
* 1 Internet Gateway
* Route Tables
* Route Associations

### Security

* 1 Security Group

### Compute

* 2 EC2 Instances

  * terraweek-web
  * terraweek-api

---

## Terraform Commands

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

### View State

```bash
terraform state list
```

### Destroy

```bash
terraform destroy
```

---

## Module Outputs

### Security Group

```hcl
module.web_sg.sg_id
```

### Web Server

```hcl
module.web_server.public_ip
```

### API Server

```hcl
module.api_server.public_ip
```

---

## Learning Outcomes

By completing this lab, I learned:

* How Terraform modules work
* Difference between root and child modules
* Creating reusable Infrastructure as Code
* Using variables and outputs effectively
* Implementing dynamic blocks
* Consuming Terraform Registry modules
* Managing module versions
* Structuring Terraform projects for scalability

---

## Screenshots

### Terraform Init

![Terraform Init](screenshots/01-terraform-init.png)

### Terraform Validate

![Terraform Validate](screenshots/02-terraform-validate.png)

### Terraform Plan

![Terraform Plan](screenshots/03-terraform-plan.png)

### Terraform Apply

![Terraform Apply](screenshots/04-terraform-apply.png)

### Terraform State List

![Terraform State List](screenshots/05-terraform-state-list.png)

### AWS VPC

![AWS VPC](screenshots/06-aws-vpc.png)

### AWS Subnets

![AWS Subnets](screenshots/07-aws-subnets.png)

### AWS Security Groups

![AWS Security Groups](screenshots/08-aws-security-groups.png)

### EC2 Instances Running

![EC2 Instances Running](screenshots/09-aws-ec2-servers-running.png)

### EC2 Instance Tags

![EC2 Instance Tags](screenshots/10-aws-instance-tags.png)

---

## Key Takeaways

* Modules make Terraform configurations reusable and maintainable.
* Dynamic blocks reduce repetitive code.
* Registry modules accelerate infrastructure deployment.
* Outputs enable communication between modules.
* Version pinning improves deployment consistency.
* Modular design is essential for large-scale cloud environments.

---

## Conclusion

This project demonstrated how Terraform modules can be used to create scalable, reusable, and maintainable infrastructure. By combining custom modules with Terraform Registry modules, complex AWS environments can be provisioned efficiently while following industry best practices.

---

**#90DaysOfDevOps**
**#Terraform**
**#InfrastructureAsCode**
**#AWS**
**#DevOps**
**#TrainWithShubham**
