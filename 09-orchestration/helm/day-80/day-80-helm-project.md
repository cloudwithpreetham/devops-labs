# Day 80 - Helm for Kubernetes Applications

## Objective

Learn how to package Kubernetes applications using Helm, create reusable templates, manage multiple environments, and deploy applications efficiently using a Helm Chart.

---

# What is Helm?

Helm is the package manager for Kubernetes.

Instead of writing multiple Kubernetes YAML files repeatedly, Helm allows us to create reusable templates and install applications with a single command.

It provides:

- Reusable Kubernetes manifests
- Environment-specific configurations
- Versioned application packages
- Easy upgrades and rollbacks
- Simplified deployments

---

# Project

**AI BankApp Helm Chart**

Created a production-style Helm chart for the AI BankApp consisting of:

- Bank Application
- MySQL Database
- Ollama AI Service

The chart supports different environments and reusable configurations.

---

# Project Structure

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

# Helm Features Implemented

- Custom Helm Chart
- Deployment Templates
- Service Templates
- ConfigMap
- Secret Management
- Persistent Volume Claims
- MySQL Deployment
- Ollama Deployment
- Environment-specific Values
- Conditional Horizontal Pod Autoscaler
- Helm Lifecycle Hooks
- Helm Test
- Chart Packaging

---

# Environment Configuration

Created separate values files for different environments.

## Development

```
values-dev.yaml
```

- Single replica
- Autoscaling disabled
- Small resource allocation

---

## Staging

```
values-staging.yaml
```

- Multiple replicas
- Autoscaling enabled
- Moderate resources

---

## Production

```
values-prod.yaml
```

- High availability
- Autoscaling enabled
- Production resource limits

---

# Helm Commands Used

## Validate Chart

```bash
helm lint .
```

---

## Render Templates

```bash
helm template bankapp-dev . -f values-dev.yaml
```

---

## Install Chart

```bash
helm install bankapp-dev . -f values-dev.yaml
```

---

## Upgrade Chart

```bash
helm upgrade bankapp-dev . -f values-dev.yaml
```

---

## List Releases

```bash
helm list
```

---

## Run Helm Tests

```bash
helm test bankapp-dev
```

---

## Package Chart

```bash
helm package .
```

---

# Kubernetes Cluster

Created a multi-node Kind cluster.

Nodes:

- 1 Control Plane
- 2 Worker Nodes

Verified using:

```bash
kubectl get nodes
```

---

# Deployment Verification

Verified the successful deployment of:

- BankApp Pod
- MySQL Pod
- Ollama Pod

Checked using:

```bash
kubectl get pods
```

---

Verified Services:

```bash
kubectl get svc
```

---

Verified Deployments:

```bash
kubectl get deployments
```

---

Verified PVCs:

```bash
kubectl get pvc
```

Both Persistent Volume Claims were successfully bound.

---

Verified HPA

```bash
kubectl get hpa
```

Development environment correctly skipped HPA because autoscaling was disabled.

---

# Helm Test

Executed:

```bash
helm test bankapp-dev
```

Result:

```
Phase: Succeeded
```

This confirmed that the deployed application passed the Helm test hook.

---

# Chart Packaging

Packaged the Helm chart using:

```bash
helm package .
```

Generated package:

```
bankapp-0.1.0.tgz
```

The chart is now ready for distribution and deployment through Helm repositories or GitOps tools.

---

# Key Learnings

- Helm simplifies Kubernetes deployments.
- Templates reduce duplication.
- Values files enable environment-specific configurations.
- ConfigMaps and Secrets improve configuration management.
- PVCs provide persistent storage.
- Helm Hooks automate lifecycle tasks.
- Helm Tests validate deployments.
- Chart packaging enables versioned application releases.
- Kind is useful for local Kubernetes development and testing.

---

# Outcome

Successfully built and deployed a production-ready Helm chart for the AI BankApp on a multi-node Kind Kubernetes cluster.

Validated deployments, services, persistent storage, lifecycle hooks, Helm tests, and packaged the application into a reusable Helm chart.
