# Day 80 - Helm for Kubernetes Applications

Learned how to package Kubernetes applications using **Helm**, create reusable templates, manage multiple environments, and deploy applications on a **multi-node Kind Kubernetes cluster**.

---

# Project Overview

As part of the AI BankApp DevOps project, I created a production-style Helm chart that deploys the following services:

- AI BankApp
- MySQL Database
- Ollama AI Service

The chart supports multiple environments, persistent storage, lifecycle hooks, and automated testing.

---

# Tech Stack

- Kubernetes
- Helm 3
- Kind
- Docker
- MySQL
- Ollama
- YAML

---

# Helm Chart Structure

```
helm-chart/
└── bankapp/
    ├── Chart.yaml
    ├── values.yaml
    ├── values-dev.yaml
    ├── values-staging.yaml
    ├── values-prod.yaml
    ├── templates/
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   ├── configmap.yaml
    │   ├── secret.yaml
    │   ├── mysql-deployment.yaml
    │   ├── ollama-deployment.yaml
    │   ├── pvc.yaml
    │   ├── hpa.yaml
    │   ├── hooks/
    │   │   └── pre-install-job.yaml
    │   └── tests/
    │       └── test-connection.yaml
    └── charts/
```

---

# Features Implemented

- Reusable Helm templates
- Deployment templates
- Service templates
- ConfigMap
- Secret management
- Persistent Volume Claims (PVC)
- MySQL deployment
- Ollama deployment
- Environment-specific values
- Conditional Horizontal Pod Autoscaler (HPA)
- Helm lifecycle hooks
- Helm test hooks
- Chart packaging

---

# Environment Configuration

## Development

- Single replica
- Autoscaling disabled
- Lightweight resources

## Staging

- Multiple replicas
- Autoscaling enabled
- Moderate resource allocation

## Production

- High availability
- Autoscaling enabled
- Production-ready resource limits

---

# Multi-Node Kind Cluster

Created a local Kubernetes cluster using Kind.

| Node | Role |
|------|------|
| bankapp-control-plane | Control Plane |
| bankapp-worker | Worker |
| bankapp-worker2 | Worker |

Verify cluster:

```bash
kubectl get nodes
```

---

# Helm Workflow

### Validate Chart

```bash
helm lint .
```

### Render Templates

```bash
helm template bankapp-dev . -f values-dev.yaml
```

### Install Chart

```bash
helm install bankapp-dev . -f values-dev.yaml
```

### Upgrade Release

```bash
helm upgrade bankapp-dev . -f values-dev.yaml
```

### List Releases

```bash
helm list
```

### Run Helm Tests

```bash
helm test bankapp-dev
```

### Package Chart

```bash
helm package .
```

---

# Deployment Verification

## Running Pods

```bash
kubectl get pods
```

Verified:

- AI BankApp
- MySQL
- Ollama

---

## Services

```bash
kubectl get svc
```

Verified ClusterIP services for:

- BankApp
- MySQL
- Ollama

---

## Deployments

```bash
kubectl get deployments
```

Confirmed all deployments were successfully rolled out.

---

## Persistent Volume Claims

```bash
kubectl get pvc
```

Verified:

- MySQL PVC
- Ollama PVC

Both PVCs were successfully **Bound**.

---

## Horizontal Pod Autoscaler

```bash
kubectl get hpa
```

No HPA resources were created for the development environment because autoscaling was intentionally disabled.

---

# Helm Test

Executed:

```bash
helm test bankapp-dev
```

Output:

```
Phase: Succeeded
```

This confirmed that the deployed application passed the Helm test successfully.

---

# Packaged Helm Chart

Packaged the chart using:

```bash
helm package .
```

Generated package:

```
bankapp-0.1.0.tgz
```

The Helm chart is now ready to be shared or deployed using Helm repositories or GitOps tools like Argo CD.

---

# Key Learnings

- Helm simplifies Kubernetes application deployment.
- Templates eliminate repetitive YAML.
- Values files allow environment-specific configurations.
- ConfigMaps and Secrets separate configuration from application code.
- PVCs provide persistent storage for stateful workloads.
- Helm Hooks automate deployment lifecycle events.
- Helm Tests validate application deployments.
- Chart packaging enables reusable and version-controlled deployments.
- Kind provides an excellent local Kubernetes environment for Helm development.

---

# Project Outcome

Successfully built a production-style Helm chart for the AI BankApp and deployed it on a multi-node Kind Kubernetes cluster.

Validated deployments, services, persistent storage, lifecycle hooks, Helm tests, and packaged the application into a reusable Helm chart ready for GitOps and production workflows.

---

# Screenshots

- Helm Chart Structure
- Helm Lint
- Helm Template Output
- Kind Cluster Nodes
- Running Pods
- Services
- Persistent Volume Claims
- Helm Release
- Helm Test Success
- Packaged Helm Chart

---

## Repository

```
day-80/
├── README.md
├── task.md
├── screenshots/
└── helm-chart/
```
