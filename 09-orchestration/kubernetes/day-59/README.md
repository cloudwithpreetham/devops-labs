# Day 59 – Helm: Kubernetes Package Manager

## Overview

On Day 59 of the #90DaysOfDevOps journey, I learned Helm, the package manager for Kubernetes. Helm simplifies application deployment by packaging Kubernetes resources into reusable charts, enabling easy installation, customization, upgrades, and rollbacks.

Through this lab, I installed Helm, deployed applications from the Bitnami repository, customized releases using values, performed upgrades and rollbacks, and created a custom Helm chart from scratch.

---

## Objectives

* Install and configure Helm
* Understand Helm core concepts
* Add and manage chart repositories
* Deploy applications using Helm charts
* Customize deployments using values files
* Upgrade and rollback releases
* Create and validate a custom Helm chart
* Render templates before deployment
* Clean up Helm releases

---

## Helm Core Concepts

### Chart

A Helm Chart is a package containing Kubernetes manifest templates and configuration files.

Examples:

* NGINX
* MySQL
* WordPress

### Release

A Release is a deployed instance of a Helm Chart inside a Kubernetes cluster.

Example:

```bash
helm install my-nginx bitnami/nginx
```

### Repository

A Repository is a collection of Helm Charts.

Example:

```text
https://charts.bitnami.com/bitnami
```

---

## Lab Tasks Completed

### Task 1 – Install Helm

```bash
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

helm version
helm env
```

Installed Version:

```text
v3.21.0
```

---

### Task 2 – Add Bitnami Repository

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami

helm repo update

helm search repo nginx
```

Repository Statistics:

```text
145 Bitnami Charts Available
```

---

### Task 3 – Deploy NGINX Using Helm

```bash
helm install my-nginx bitnami/nginx
```

Verification:

```bash
helm list
helm status my-nginx
kubectl get all
```

Resources automatically created:

* Deployment
* ReplicaSet
* Pod
* Service

---

### Task 4 – Customize Releases

Using command-line overrides:

```bash
helm install nginx-custom bitnami/nginx \
  --set replicaCount=3 \
  --set service.type=NodePort
```

Using a custom values file:

```bash
helm install nginx-values bitnami/nginx \
  -f custom-values.yaml
```

---

### Task 5 – Upgrade and Rollback

Upgrade release:

```bash
helm upgrade my-nginx bitnami/nginx \
  --set replicaCount=5
```

Check history:

```bash
helm history my-nginx
```

Rollback:

```bash
helm rollback my-nginx 1
```

Key Learning:

Helm rollback creates a new revision instead of overwriting previous revisions.

---

### Task 6 – Create a Custom Chart

Create chart:

```bash
helm create my-app
```

Validate chart:

```bash
helm lint my-app
```

Render templates:

```bash
helm template my-release ./my-app
```

Install chart:

```bash
helm install my-release ./my-app
```

Upgrade chart:

```bash
helm upgrade my-release ./my-app \
  --set replicaCount=5
```

---

### Task 7 – Cleanup

Remove releases:

```bash
helm uninstall my-nginx
helm uninstall nginx-custom
helm uninstall nginx-values
helm uninstall my-release
```

Verify:

```bash
helm list
```

---

## Project Structure

```text
day-59/
├── README.md
├── task.md
├── day-59-helm.md
├── custom-values.yaml
├── screenshots/
└── helm-chart/
    └── my-app/
```

---

## Screenshots

The screenshots directory contains evidence of:

* Helm installation
* Repository configuration
* Chart deployment
* Custom values deployment
* Upgrade operations
* Rollback operations
* Helm chart creation
* Helm lint validation
* Template rendering
* Custom chart installation
* Cleanup verification

---

## Key Takeaways

* Helm simplifies Kubernetes application deployment.
* Charts package multiple Kubernetes resources together.
* Releases track deployed chart versions.
* Values files allow reusable configuration management.
* Upgrades and rollbacks provide safe application lifecycle management.
* Helm templates use Go templating syntax.
* helm lint validates chart quality before deployment.
* helm template renders manifests without applying them.
* Custom charts enable reusable and scalable Kubernetes deployments.

---

## Outcome

Successfully installed Helm, deployed applications from the Bitnami repository, customized deployments using values files, performed release upgrades and rollbacks, and created a custom Helm chart using Go templates. This lab demonstrated how Helm simplifies Kubernetes application management and enables repeatable, production-ready deployments.

---

**#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham**
