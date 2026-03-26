# Day 64 – Terraform State Management and Remote Backends

## Overview

On Day 64 of my #90DaysOfDevOps journey, I explored one of Terraform's most critical concepts: **State Management**.

Terraform state acts as the source of truth for infrastructure and keeps track of the relationship between Terraform configuration files and actual cloud resources. In this lab, I learned how to manage state professionally using remote backends, state locking, resource imports, state manipulation, and drift detection.

---

## Objectives

- Inspect Terraform state and understand its structure
- Configure an S3 remote backend for state storage
- Enable DynamoDB-based state locking
- Import existing AWS resources into Terraform state
- Perform state operations using `state mv` and `state rm`
- Simulate and reconcile infrastructure drift
- Understand Terraform state best practices

---

## Technologies Used

- Terraform
- AWS EC2
- AWS VPC
- AWS Subnet
- AWS Security Group
- AWS S3
- AWS DynamoDB
- AWS CLI

---

## Infrastructure Created

### AWS Resources

- VPC
- Public Subnet
- Security Group
- EC2 Instance
- S3 Bucket (Remote Backend)
- DynamoDB Table (State Locking)
- Imported S3 Bucket

### Terraform Resources Managed

```text
aws_instance.web
aws_s3_bucket.logs_bucket
aws_security_group.web_sg
aws_subnet.public
aws_vpc.main
```

---

## Project Structure

```text
day-64/
├── terraform/
│   ├── backend.tf
│   ├── main.tf
│   ├── provider.tf
│   ├── variables.tf
│   └── outputs.tf
├── README.md
└── day-64-state-management.md
```

---

## Key Tasks Completed

### 1. State Inspection

Explored Terraform state using:

```bash
terraform show
terraform state list
terraform state show aws_instance.web
terraform state show aws_vpc.main
```

Learned that Terraform stores significantly more information than what is defined in configuration files, including:

- Resource IDs
- ARNs
- IP Addresses
- Availability Zones
- Tags
- Metadata
- Resource Relationships

---

### 2. Remote Backend Migration

Created:

- S3 Bucket for remote state storage
- DynamoDB Table for state locking

Migrated local state:

```bash
terraform init -migrate-state
```

Verified successful migration by checking the state file in S3.

---

### 3. State Locking

Tested state locking using two terminals.

Observed lock protection:

```text
Error acquiring the state lock
ConditionalCheckFailedException
```

This prevents multiple users from modifying infrastructure simultaneously.

---

### 4. Import Existing Infrastructure

Created an S3 bucket manually through AWS Console and imported it into Terraform:

```bash
terraform import aws_s3_bucket.imported <bucket-name>
```

Verified that the imported resource appeared in Terraform state.

---

### 5. State Surgery

#### Rename Resource

```bash
terraform state mv \
aws_s3_bucket.imported \
aws_s3_bucket.logs_bucket
```

#### Remove Resource From State

```bash
terraform state rm aws_s3_bucket.logs_bucket
```

#### Re-import Resource

```bash
terraform import \
aws_s3_bucket.logs_bucket \
<bucket-name>
```

Learned how to modify Terraform state without affecting actual infrastructure.

---

### 6. State Drift Detection

Manually modified an EC2 tag through AWS Console.

Terraform detected the drift:

```diff
- ManuallyChanged
+ Terraform-Web-Server-v2
```

Reconciled infrastructure:

```bash
terraform apply
```

Verified:

```bash
terraform plan
```

Output:

```text
No changes.
Your infrastructure matches the configuration.
```

---

## Terraform Commands Practiced

```bash
terraform show
terraform state list
terraform state show
terraform init -migrate-state
terraform import
terraform state mv
terraform state rm
terraform plan
terraform apply
terraform force-unlock
terraform refresh
```

---

## Key Learnings

- Terraform state is the source of truth.
- Remote state storage is essential for teams.
- S3 provides centralized and versioned state storage.
- DynamoDB prevents concurrent state modifications.
- Existing infrastructure can be imported into Terraform.
- State operations help refactor infrastructure safely.
- Drift detection helps maintain configuration consistency.
- State versioning protects against accidental loss.
- Proper state management is critical for production environments.

---

## Challenges Faced

### VPC and Subnet Mismatch

Initially, the EC2 instance failed to launch because the Security Group and Subnet belonged to different VPCs.

Error:

```text
Security group and subnet belong to different networks
```

Resolution:

- Created a subnet inside the custom VPC
- Explicitly attached the EC2 instance to that subnet

---

## Screenshots

Add the following screenshots:

- Terraform State in S3 Bucket
- DynamoDB Lock Table
- State Lock Error
- Resource Import Success
- Drift Detection Plan Output
- Successful Reconciliation

---

## Outcome

Successfully implemented Terraform state management best practices by:

- Migrating local state to S3
- Enabling DynamoDB locking
- Importing existing resources
- Performing state surgery
- Detecting and resolving state drift

This lab provided hands-on experience with production-grade Terraform workflows and reinforced the importance of reliable state management in Infrastructure as Code.

---

## Connect With Me

Follow my DevOps journey:

**#90DaysOfDevOps**
**#TerraWeek**
**#Terraform**
**#AWS**
**#InfrastructureAsCode**
**#DevOps**
**#CloudComputing**
**#TrainWithShubham**
