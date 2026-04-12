# Day 81 – Introduction to Amazon EKS with Terraform

## Overview

Day 81 focused on learning Amazon Elastic Kubernetes Service (EKS) and provisioning a production-ready Kubernetes cluster using Terraform. Unlike Kind, which is designed for local development, Amazon EKS provides a managed Kubernetes control plane with high availability, scalability, AWS networking, IAM integration, and managed worker nodes.

Using the AI-BankApp Terraform configuration, I successfully provisioned an EKS cluster, connected using `kubectl`, deployed the application manually, verified all Kubernetes components, and finally cleaned up the infrastructure to avoid unnecessary AWS costs.

---

# Objectives

- Understand Amazon EKS architecture
- Learn Managed Kubernetes concepts
- Study the AI-BankApp Terraform configuration
- Provision an EKS cluster using Terraform
- Connect kubectl to EKS
- Deploy AI-BankApp manually
- Verify cluster components
- Understand AWS cost considerations
- Destroy infrastructure using Terraform

---

# What is Amazon EKS?

Amazon Elastic Kubernetes Service (EKS) is AWS's managed Kubernetes service.

Instead of managing the Kubernetes control plane yourself, AWS manages:

- Kubernetes API Server
- etcd
- Scheduler
- Controller Manager
- High Availability
- Automatic Patching
- Version Upgrades

As users, we only manage the worker nodes and the applications running on them.

---

# EKS Architecture

```
                        AWS Cloud
+---------------------------------------------------------+

                  Amazon VPC (10.0.0.0/16)

+---------------------------------------------------------+
|                                                         |
|      Public Subnets (3 AZs)                             |
|      • Load Balancers                                   |
|      • NAT Gateway                                      |
|                                                         |
|      Private Subnets (3 AZs)                            |
|      • EKS Worker Nodes                                 |
|      • Application Pods                                 |
|                                                         |
|      Intra Subnets                                      |
|      • EKS Control Plane ENIs                           |
|                                                         |
+---------------------------------------------------------+

                Amazon EKS Control Plane
                (Managed by AWS)

      • API Server
      • Scheduler
      • Controller Manager
      • etcd

                     │

            Managed Node Group

         EC2 Worker Nodes (3)

      • BankApp
      • MySQL
      • Ollama

                     │

               Kubernetes Add-ons

- CoreDNS
- kube-proxy
- VPC CNI
- Metrics Server
- EBS CSI Driver
- EKS Pod Identity Agent

                     │

                 ArgoCD via Helm
```

---

# Managed Kubernetes

Managed Kubernetes means AWS is responsible for:

- Control Plane Management
- Cluster High Availability
- Security Patches
- Kubernetes Version Upgrades
- etcd Management
- Control Plane Scaling

Users are responsible for:

- Worker Nodes
- Applications
- Namespaces
- Deployments
- Services
- Persistent Storage
- Security Policies

---

# EKS Components

## Control Plane

Managed entirely by AWS.

Components include:

- Kubernetes API Server
- Scheduler
- Controller Manager
- etcd

---

## Managed Node Groups

Worker nodes created automatically by AWS.

Features:

- Auto Scaling
- Rolling Updates
- Health Checks
- EC2 Management

---

## Networking

The cluster was deployed inside a custom VPC containing:

- 3 Public Subnets
- 3 Private Subnets
- 3 Intra Subnets

Additional networking resources:

- Internet Gateway
- NAT Gateway
- Route Tables

---

## IAM Integration

Amazon EKS integrates with IAM for:

- Cluster Authentication
- Worker Node Permissions
- IAM Roles for Service Accounts (IRSA)
- Pod Identity

---

# Kubernetes Add-ons Installed

| Add-on | Purpose |
|----------|----------|
| CoreDNS | Internal DNS |
| kube-proxy | Service networking |
| AWS VPC CNI | Assigns VPC IPs to Pods |
| Metrics Server | CPU & Memory metrics |
| AWS EBS CSI Driver | Persistent EBS Storage |
| EKS Pod Identity Agent | Pod IAM Roles |

---

# Terraform Configuration

## provider.tf

Configured:

- AWS Provider
- Kubernetes Provider
- Helm Provider

---

## variables.tf

Defined input variables such as:

- Region
- Cluster Name
- Kubernetes Version
- Node Count
- Instance Type

---

## terraform.tfvars

Configured:

- AWS Region
- Cluster Name
- Node Size
- Desired Node Count

---

## vpc.tf

Created:

- Custom VPC
- Public Subnets
- Private Subnets
- Intra Subnets
- Internet Gateway
- NAT Gateway

---

## eks.tf

Provisioned:

- Amazon EKS Cluster
- Managed Node Group
- IAM Roles
- Cluster Add-ons
- EBS CSI Driver

---

## argocd.tf

Installed ArgoCD using Helm.

Service Type:

- LoadBalancer

---

## outputs.tf

Generated helper commands including:

- update-kubeconfig
- ArgoCD Password
- Cluster Information

---

# Deployment Process

## Initialize Terraform

```bash
terraform init
```

---

## Review Execution Plan

```bash
terraform plan
```

---

## Provision Infrastructure

```bash
terraform apply
```

Terraform created:

- VPC
- Subnets
- IAM Roles
- Security Groups
- EKS Cluster
- Managed Node Group
- EBS CSI Driver
- Metrics Server
- ArgoCD

---

# Connect kubectl

```bash
aws eks update-kubeconfig \
--name bankapp-eks \
--region ap-south-1
```

Verify cluster:

```bash
kubectl get nodes
```

---

# Deploy AI-BankApp

Applied manifests:

```bash
kubectl apply -f k8s/
```

Application Components:

- Namespace
- ConfigMap
- Secret
- MySQL
- Ollama
- BankApp
- Services
- PVC
- HPA

---

# Verification

Successfully verified:

- Worker Nodes
- kube-system Pods
- Metrics Server
- CoreDNS
- AWS VPC CNI
- EBS CSI Driver
- ArgoCD
- BankApp Pods
- MySQL
- Ollama
- Persistent Volumes
- Horizontal Pod Autoscaler

---

# Screenshots

## Terraform Apply

> Insert Screenshot

---

## kubectl get nodes

> Insert Screenshot

---

## kubectl get pods -n kube-system

> Insert Screenshot

---

## kubectl get pods -n bankapp

> Insert Screenshot

---

## kubectl get pvc -n bankapp

> Insert Screenshot

---

## AI-BankApp Running

> Insert Screenshot

---

## ArgoCD Dashboard

> Insert Screenshot

---

## Cleanup Verification

> Insert Screenshot of:

```bash
kubectl get all -A
```

---

# EKS Cost Breakdown

| Component | Monthly Cost (Approx.) |
|------------|-----------------------:|
| EKS Control Plane | ~$73 |
| 3 × Worker Nodes | ~$91 |
| NAT Gateway | ~$33 |
| EBS Storage | ~$1.50 |
| Load Balancer | ~$18 |
| **Total** | **~$220/month** |

---

# Why is NAT Gateway Expensive?

The NAT Gateway incurs both:

- Hourly charges
- Data processing charges

Since every worker node in the private subnet accesses the internet through the NAT Gateway for pulling images, updates, and external services, it becomes one of the most expensive networking components in an EKS environment.

---

# Cleanup

Removed the AI-BankApp workload:

```bash
kubectl delete -f k8s/
```

Destroyed the AWS infrastructure:

```bash
terraform destroy
```

Terraform Output:

```
Destroy complete! Resources: 84 destroyed.
```

This ensured that no unnecessary AWS resources continued incurring charges.

---

# Key Learnings

- Learned the architecture of Amazon EKS.
- Understood the responsibilities shared between AWS and users.
- Explored Terraform modules for VPC and EKS provisioning.
- Learned how managed node groups simplify Kubernetes operations.
- Deployed a production-style Kubernetes cluster using Infrastructure as Code.
- Successfully deployed AI-BankApp on Amazon EKS.
- Verified storage, networking, and monitoring components.
- Understood AWS pricing for EKS and the importance of cleaning up resources.
- Destroyed all infrastructure using Terraform to prevent unnecessary cloud costs.

---

# Conclusion

Day 81 provided practical experience with deploying and managing a production-ready Kubernetes environment using Amazon EKS and Terraform. It demonstrated how Infrastructure as Code simplifies cloud infrastructure provisioning while highlighting the importance of cost management through proper resource cleanup. This forms the foundation for implementing GitOps with ArgoCD in the upcoming days.

---

## Repository Structure

```
2026/
└── day-81/
    └── day-81-eks-intro.md
```
