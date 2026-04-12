# Day 81 – Introduction to Amazon EKS with Terraform

> **90 Days of DevOps | Kubernetes Week | Amazon EKS | Terraform | AI-BankApp**

## Overview

On **Day 81**, I moved from running Kubernetes locally with **Kind** to deploying a **production-grade Kubernetes cluster on Amazon EKS** using **Terraform**.

The objective was to understand Amazon EKS architecture, provision an EKS cluster using Infrastructure as Code, manually deploy the AI-BankApp application, validate the cluster components, and learn how to manage cloud infrastructure costs through proper cleanup.

---

## Objectives

- Understand Amazon EKS architecture
- Learn the shared responsibility model of EKS
- Explore the AI-BankApp Terraform configuration
- Provision an Amazon EKS cluster using Terraform
- Connect `kubectl` to the cluster
- Deploy AI-BankApp manually
- Verify Kubernetes add-ons and workloads
- Understand EKS pricing
- Clean up AWS resources using Terraform

---

# Tech Stack

| Category | Tools |
|----------|-------|
| Cloud | AWS |
| Container Orchestration | Amazon EKS |
| Infrastructure as Code | Terraform |
| Kubernetes CLI | kubectl |
| Package Manager | Helm |
| GitOps | ArgoCD |
| Storage | AWS EBS CSI Driver |
| Monitoring | Metrics Server |
| Networking | VPC, NAT Gateway, AWS VPC CNI |

---

# Project Architecture

```
                    AWS Cloud
                         │
                         ▼
                  Amazon VPC
        ┌────────────────────────────┐
        │                            │
        │  Public Subnets            │
        │  Private Subnets           │
        │  Intra Subnets             │
        │                            │
        └─────────────┬──────────────┘
                      │
                      ▼
             Amazon EKS Cluster
        (Managed Kubernetes Control Plane)
                      │
                      ▼
            Managed Node Group
          (3 EC2 Worker Nodes)
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
    BankApp         MySQL         Ollama
                      │
                      ▼
               AWS EBS Volumes

                      │
                      ▼
                  ArgoCD (Helm)

```

---

# Amazon EKS Concepts Learned

## Managed Kubernetes

Amazon EKS manages:

- Kubernetes API Server
- Scheduler
- Controller Manager
- etcd
- Control Plane Upgrades
- High Availability

Users manage:

- Worker Nodes
- Applications
- Storage
- Networking Policies
- Kubernetes Resources

---

## EKS Components

### Control Plane

Managed by AWS and highly available across multiple Availability Zones.

### Managed Node Groups

AWS automatically provisions and manages EC2 worker nodes.

### VPC Networking

- Public Subnets
- Private Subnets
- Intra Subnets
- NAT Gateway
- Internet Gateway

### IAM Integration

- IAM Roles
- IAM Roles for Service Accounts (IRSA)
- Pod Identity

---

# Kubernetes Add-ons Installed

- CoreDNS
- kube-proxy
- AWS VPC CNI
- Metrics Server
- AWS EBS CSI Driver
- EKS Pod Identity Agent

---

# Terraform Files Overview

| File | Description |
|------|-------------|
| provider.tf | AWS, Kubernetes and Helm providers |
| variables.tf | Input variables |
| terraform.tfvars | Environment values |
| vpc.tf | Creates VPC, subnets and networking |
| eks.tf | Creates EKS cluster and node groups |
| argocd.tf | Installs ArgoCD using Helm |
| outputs.tf | Useful output commands |

---

# Hands-on Activities

## Provisioned Infrastructure

- Amazon VPC
- Public Subnets
- Private Subnets
- NAT Gateway
- Internet Gateway
- Amazon EKS Cluster
- Managed Node Group
- IAM Roles
- Security Groups
- ArgoCD
- EBS CSI Driver
- Metrics Server

---

## Connected kubectl

```bash
aws eks update-kubeconfig --name bankapp-eks --region ap-south-1
```

---

## Verified Cluster

```bash
kubectl get nodes
kubectl get pods -n kube-system
kubectl cluster-info
```

Verified:

- Worker Nodes
- CoreDNS
- kube-proxy
- Metrics Server
- AWS VPC CNI
- EBS CSI Driver
- Pod Identity Agent

---

## Deployed AI-BankApp

Applied Kubernetes manifests:

- Namespace
- ConfigMap
- Secret
- MySQL
- Ollama
- BankApp
- Services
- Persistent Volumes
- Persistent Volume Claims
- Horizontal Pod Autoscaler

---

## Validated Deployment

Verified:

- Running Pods
- Services
- PVCs
- HPA
- Application accessibility
- ArgoCD installation

---

# Commands Used

## Initialize Terraform

```bash
terraform init
```

## Review Plan

```bash
terraform plan
```

## Provision Infrastructure

```bash
terraform apply
```

## Connect kubectl

```bash
aws eks update-kubeconfig --name bankapp-eks
```

## Deploy Application

```bash
kubectl apply -f k8s/
```

## Verify Resources

```bash
kubectl get nodes
kubectl get pods -A
kubectl get pvc -n bankapp
kubectl get hpa -n bankapp
```

## Clean Up Workload

```bash
kubectl delete -f k8s/
```

## Destroy Infrastructure

```bash
terraform destroy
```

---

# EKS Cost Breakdown

| Resource | Approximate Monthly Cost |
|-----------|-------------------------:|
| EKS Control Plane | ~$73 |
| EC2 Worker Nodes | ~$91 |
| NAT Gateway | ~$33 |
| EBS Storage | ~$1.50 |
| Load Balancer | ~$18 |
| **Total** | **~$220/month** |

---

# Key Learnings

- Understood Amazon EKS architecture.
- Learned how managed Kubernetes differs from self-managed clusters.
- Explored production-grade Terraform modules.
- Provisioned infrastructure using Infrastructure as Code.
- Connected kubectl to Amazon EKS.
- Successfully deployed AI-BankApp on Kubernetes.
- Verified storage, networking and monitoring components.
- Learned the importance of cleaning up cloud resources to reduce costs.
- Destroyed the complete infrastructure using Terraform after the lab.

---

# Screenshots

Add the following screenshots to this README:

- Terraform Apply Success
- `kubectl get nodes -o wide`
- `kubectl get pods -n kube-system`
- `kubectl get pods -n bankapp`
- `kubectl get pvc -n bankapp`
- AI-BankApp Login Page
- ArgoCD Dashboard
- `kubectl get all -A`
- Terraform Destroy Success

---

# Repository Structure

```
2026/
└── day-81/
    ├── README.md
    ├── day-81-eks-intro.md
    └── screenshots/
        ├── terraform-apply.png
        ├── nodes.png
        ├── kube-system.png
        ├── bankapp-pods.png
        ├── pvc.png
        ├── bankapp-ui.png
        ├── argocd.png
        ├── cleanup.png
        └── terraform-destroy.png
```

---

# Outcome

Successfully provisioned a production-ready Amazon EKS cluster using Terraform, manually deployed the AI-BankApp application, validated Kubernetes resources, explored core EKS architecture, and cleaned up all AWS resources to avoid unnecessary cloud costs.

---

## Connect with Me

- **GitHub:** https://github.com/cloud-with-preetham
- **LinkedIn:** https://www.linkedin.com/in/preetham-pereira/

---

**#90DaysOfDevOps #AWS #AmazonEKS #Terraform #Kubernetes #CloudComputing #InfrastructureAsCode #DevOps #GitOps #ArgoCD**
