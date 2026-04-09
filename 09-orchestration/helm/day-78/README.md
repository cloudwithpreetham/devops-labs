# Day 78 – Introduction to Helm and Chart Basics

> **90 Days of DevOps Challenge**
> **Day 78 Goal:** Learn Helm fundamentals, deploy applications using community charts, manage Helm releases, and explore the internal structure of a production-grade Helm Chart.

---

## Overview

Today I started learning **Helm**, the package manager for Kubernetes.

Instead of deploying applications using multiple raw Kubernetes YAML files, Helm packages all Kubernetes resources into reusable and versioned **Charts**. During this lab, I installed Helm, deployed MySQL using the Bitnami Helm Chart, customized deployments with a `values.yaml` file, managed Helm releases, and explored the structure of a real production Helm Chart.

This day also included troubleshooting a real-world image compatibility issue while deploying the MySQL chart.

---

## Objectives

- Install Helm on Linux
- Connect Helm to a Kubernetes cluster
- Understand Helm architecture
- Learn Charts, Releases, Repositories, and Values
- Deploy MySQL using a community Helm Chart
- Customize deployments using `values.yaml`
- Manage Helm releases
- Perform upgrades and rollbacks
- Explore Helm chart structure
- Compare Helm with raw Kubernetes manifests

---

# Project Structure

```text
day-78/
├── README.md
├── task.md
├── day-78-helm-intro.md
├── mysql-values.yaml
└── screenshots/
```

---

# Lab Environment

| Component     | Version       |
| ------------- | ------------- |
| Ubuntu        | 26.04 LTS     |
| Docker        | 29.1.3        |
| Kubernetes    | Kind v1.35.0  |
| kubectl       | v1.36.2       |
| Helm          | v3.21.2       |
| Helm Chart    | Bitnami MySQL |
| Chart Version | 14.0.3        |
| MySQL Version | 9.4.0         |

---

# What I Learned

## Helm Fundamentals

- Helm Architecture
- Charts
- Releases
- Repositories
- Values
- Go Template Syntax
- Chart Version vs App Version

---

## Helm Installation

Installed:

- Docker
- kubectl
- Kind
- Helm

Verified installation using:

```bash
docker --version
kubectl version --client
kind version
helm version
```

---

## Kubernetes Cluster

Created a Kind cluster using the AI-BankApp configuration.

```bash
kind create cluster --config setup-k8s/kind-config.yml
```

Verified:

```bash
kubectl get nodes
kubectl cluster-info
```

---

## Deploying MySQL with Helm

Added the Bitnami repository.

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami

helm repo update
```

Installed MySQL.

```bash
helm install bankapp-mysql bitnami/mysql
```

Encountered an image pull issue because the default image repository referenced an unavailable image.

Resolved it by overriding the image repository.

```bash
helm install bankapp-mysql bitnami/mysql \
--set image.repository=bitnamilegacy/mysql \
--set image.tag=9.4.0-debian-12-r1 \
--set global.security.allowInsecureImages=true
```

Successfully verified:

- StatefulSet
- Service
- Secret
- PVC
- Database

---

## Using values.yaml

Created a production-style configuration file.

```yaml
auth:
  rootPassword: Test@123
  database: bankappdb

primary:
  persistence:
    size: 5Gi

metrics:
  enabled: true
```

Installed another release using:

```bash
helm install bankapp-mysql-v2 bitnami/mysql \
-f mysql-values.yaml
```

Learned that enabling optional components may introduce additional container images requiring separate configuration.

---

## Helm Release Management

Practiced:

Install

```bash
helm install
```

Upgrade

```bash
helm upgrade
```

History

```bash
helm history
```

Rollback

```bash
helm rollback
```

Uninstall

```bash
helm uninstall
```

Observed Helm revision history after upgrades and rollbacks.

---

## Exploring the Helm Chart

Downloaded the chart.

```bash
helm pull bitnami/mysql --untar
```

Explored:

```text
Chart.yaml
values.yaml
templates/
charts/
README.md
values.schema.json
```

Learned:

- Chart metadata
- Dependencies
- Go templates
- Default values
- Reusable templates

---

# Helm vs Raw Kubernetes Manifests

| Raw Manifests                    | Helm                              |
| -------------------------------- | --------------------------------- |
| Multiple YAML files              | Single Chart                      |
| Manual updates                   | Template-based                    |
| Hardcoded configuration          | Configurable values               |
| No built-in rollback             | Built-in rollback                 |
| Difficult environment management | Environment-specific values files |
| Manual dependency management     | Automatic dependency management   |

---

# Challenges Faced

## ImagePullBackOff

Problem

The MySQL image referenced by the default chart was unavailable.

Solution

Overrode the image repository to use the legacy Bitnami image.

---

## Metrics Sidecar Issue

Enabling metrics introduced the `mysqld-exporter` sidecar, which referenced another unavailable image.

This demonstrated that optional chart features may add additional containers with independent image configuration.

---

# Key Takeaways

- Learned Helm fundamentals
- Installed Helm from scratch
- Created a Kubernetes cluster using Kind
- Deployed MySQL with a community Helm Chart
- Customized deployments using `values.yaml`
- Managed Helm releases
- Explored chart internals
- Understood Go template syntax
- Learned the difference between Chart Version and App Version
- Troubleshot real-world Helm deployment issues

---

# Commands Practiced

```bash
helm repo add
helm repo update
helm search repo
helm install
helm upgrade
helm history
helm rollback
helm uninstall
helm show values
helm pull
kubectl get pods
kubectl get pvc
kubectl get secret
kubectl exec
```

---

# Outcome

By the end of Day 78, I gained hands-on experience with Helm, Kubernetes package management, release lifecycle management, configuration using values files, and Helm chart internals. This knowledge prepares me for building custom Helm Charts for the AI-BankApp in the next phase of the challenge.

---

## Next Step

**Day 79 – Creating a Custom Helm Chart for AI-BankApp**

Convert the application's raw Kubernetes manifests into a reusable, production-ready Helm Chart with configurable values and templates.

---

**#90DaysOfDevOps #Helm #Kubernetes #DevOps #CloudNative #TrainWithShubham**
