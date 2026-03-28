# Day 66 – Provisioning Amazon EKS with Terraform

## Overview

Day 66 focused on deploying a production-style Amazon EKS (Elastic Kubernetes Service) cluster using Terraform. The objective was to automate the provisioning of networking resources, IAM roles, managed node groups, and the Kubernetes control plane through Infrastructure as Code (IaC).

This lab provided hands-on experience with:

- Terraform AWS Provider
- Terraform EKS Module
- Amazon EKS Cluster
- Managed Node Groups
- VPC and Networking
- IAM Roles and Policies
- kubectl Integration
- EKS Authentication and Access Entries
- Infrastructure Cleanup

---

## Architecture

```text
                    +----------------------+
                    |   Terraform CLI      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |      AWS EKS         |
                    +----------+-----------+
                               |
        +----------------------+----------------------+
        |                                             |
        v                                             v
+------------------+                     +------------------+
| Public Subnets   |                     | Private Subnets  |
| 10.0.1.0/24      |                     | 10.0.11.0/24     |
| 10.0.2.0/24      |                     | 10.0.12.0/24     |
+------------------+                     +------------------+
        |                                             |
        +----------------------+----------------------+
                               |
                               v
                    +----------------------+
                    |  EKS Node Group      |
                    |  Managed Workers     |
                    +----------------------+
```

---

# Project Structure

```bash
terraform-eks/
├── providers.tf
├── variables.tf
├── terraform.tfvars
├── vpc.tf
├── eks.tf
└── outputs.tf
```

---

## Tasks Performed

### 1. Validate AWS Credentials

Verified Terraform IAM user credentials and AWS account access.

```bash
aws sts get-caller-identity
aws configure list
```

Output confirmed:

- IAM User: terraform-user
- AWS Account Access
- Default Region: us-west-2

---

### 2. Initialize Terraform

Downloaded required providers and modules.

```bash
terraform init
```

Providers installed:

- hashicorp/aws
- hashicorp/kubernetes

---

### 3. Validate Terraform Configuration

Checked configuration syntax and resource definitions.

```bash
terraform fmt -recursive
terraform validate
```

Result:

```text
Success! The configuration is valid.
```

---

### 4. Review Execution Plan

Generated infrastructure plan.

```bash
terraform plan
```

Resources included:

- VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- IAM Roles
- EKS Cluster
- Managed Node Group
- KMS Encryption

Total Planned Resources:

```text
55 resources
```

---

### 5. Deploy Amazon EKS

Applied Terraform configuration.

```bash
terraform apply
```

Terraform successfully provisioned:

- EKS Cluster
- Worker Nodes
- Networking Components
- IAM Resources

---

### 6. Configure kubectl Access

Updated kubeconfig for the new cluster.

```bash
aws eks update-kubeconfig \
  --region us-west-2 \
  --name terraweek-eks
```

Generated context:

```text
arn:aws:eks:us-west-2:646313138990:cluster/terraweek-eks
```

---

### 7. Troubleshoot Authentication Issues

Initial cluster access failed.

Error:

```text
You must be logged in to the server
```

Investigation Steps:

```bash
aws eks get-token
kubectl config view --minify
aws eks describe-cluster
aws eks list-access-entries
kubectl auth whoami
```

Root Cause:

Terraform IAM user was not automatically granted cluster access through EKS Access Entries.

Solution:

Re-generated kubeconfig and ensured access mapping was updated.

```bash
aws eks update-kubeconfig \
  --name terraweek-eks \
  --region us-west-2
```

---

### 8. Verify Cluster Health

Checked worker nodes.

```bash
kubectl get nodes
```

Output:

```text
Ready
Ready
```

Verified system workloads.

```bash
kubectl get pods -A
```

Observed:

- CoreDNS
- kube-proxy
- aws-node

All running successfully.

---

### 9. Verify Managed Node Group

Confirmed node group status.

```bash
aws eks describe-nodegroup \
  --cluster-name terraweek-eks \
  --region us-west-2
```

Result:

```text
ACTIVE
```

---

### 10. Destroy Infrastructure

Removed EKS resources.

```bash
terraform destroy
```

---

## Cleanup Challenge

Terraform destroy initially failed because some AWS resources were still attached.

Errors included:

```text
DependencyViolation
Subnet has dependencies
VPC has dependencies
Internet Gateway cannot be detached
```

---

### Investigation Commands

Checked remaining resources.

```bash
aws ec2 describe-network-interfaces
aws ec2 describe-security-groups
aws ec2 describe-route-tables
aws ec2 describe-subnets
aws ec2 describe-nat-gateways
aws elb describe-load-balancers
```

Found:

- Orphaned Classic Load Balancer
- Residual Security Group
- Route Table Dependency

---

### Manual Cleanup

Deleted lingering ELB resources and dependency chains.

Verified:

```bash
aws eks list-clusters
```

Output:

```text
[]
```

Confirmed:

```bash
No Subnets
No ENIs
No NAT Gateways
No EKS Clusters
```

---

### Final Destroy

Executed:

```bash
terraform destroy
```

Terraform removed the remaining VPC successfully.

Output:

```text
Destroy complete!
Resources: 1 destroyed.
```

---

## Key Learnings

### Amazon EKS

- Managed Kubernetes service on AWS
- Simplifies control plane management
- Supports managed worker nodes

### Terraform EKS Module

Benefits:

- Faster cluster provisioning
- Reusable architecture
- Production-ready defaults

### EKS Authentication

Authentication requires:

- IAM Identity
- Access Entries
- aws eks get-token integration

### Networking

Understanding:

- Public Subnets
- Private Subnets
- NAT Gateway
- Route Tables
- Security Groups

is critical for Kubernetes deployments.

### Infrastructure Cleanup

Important lessons:

- Always remove Kubernetes Services of type LoadBalancer before destroy.
- ELBs can leave behind ENIs and Security Groups.
- Dependency violations require resource investigation before VPC deletion.

---

## Commands Reference

```bash
terraform init

terraform validate

terraform plan

terraform apply

aws eks update-kubeconfig \
  --region us-west-2 \
  --name terraweek-eks

kubectl get nodes

kubectl get pods -A

aws eks list-access-entries \
  --cluster-name terraweek-eks \
  --region us-west-2

terraform destroy
```

---

## Outcome

Successfully provisioned an Amazon EKS cluster using Terraform, validated Kubernetes node health, troubleshot IAM authentication issues, explored EKS Access Entries, and performed a complete infrastructure teardown while resolving AWS dependency violations manually.

This lab provided practical experience in deploying and managing Kubernetes infrastructure on AWS using Infrastructure as Code.
