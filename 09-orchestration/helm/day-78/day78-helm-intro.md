# Day 78 – Introduction to Helm and Chart Basics

## Objective

The goal of this lab was to learn the fundamentals of Helm, the package manager for Kubernetes. I explored Helm concepts, deployed MySQL using a community Helm chart, customized deployments using a values file, managed Helm releases, and inspected the internal structure of a production-grade Helm chart.

---

# Lab Environment

| Component     | Version          |
| ------------- | ---------------- |
| OS            | Ubuntu 26.04 LTS |
| Kubernetes    | Kind v1.35.0     |
| kubectl       | v1.36.2          |
| Helm          | v3.21.2          |
| Docker        | v29.1.3          |
| Helm Chart    | Bitnami MySQL    |
| Chart Version | 14.0.3           |
| MySQL Version | 9.4.0            |

---

# Task 1 – Understanding Helm Concepts

## What is Helm?

Helm is the package manager for Kubernetes. It simplifies application deployment by packaging Kubernetes manifests into reusable and versioned packages called **Charts**. Instead of manually applying multiple YAML files, Helm installs and manages an application using a single command.

---

## Core Concepts

### Chart

A Helm Chart is a package that contains Kubernetes manifests, templates, default configuration values, metadata, and dependencies required to deploy an application.

Example:

- Deployment
- Service
- ConfigMap
- Secret
- Persistent Volume Claim

All are packaged together inside a Helm Chart.

---

### Release

A Release is a running instance of a Helm Chart deployed in a Kubernetes cluster.

Example:

```text
Chart
└── bitnami/mysql

Release
└── bankapp-mysql
```

The same chart can be installed multiple times using different release names.

---

### Repository

A Helm Repository is a collection of Helm Charts hosted online.

Popular repositories include:

- Bitnami
- Grafana
- Prometheus Community
- Argo

---

### Values

Values customize a Helm Chart without modifying its templates.

Example:

```yaml
auth:
  rootPassword: Test@123

primary:
  persistence:
    size: 5Gi
```

Values can be supplied using:

- `--set`
- `values.yaml`

---

# Why Helm Instead of Raw Kubernetes Manifests?

The AI-BankApp project contains multiple Kubernetes manifests:

- bankapp-deployment.yml
- mysql-deployment.yml
- service.yml
- secrets.yml
- pvc.yml
- pv.yml
- configmap.yml
- gateway.yml
- hpa.yml
- cert-manager.yml

Managing all these files manually across development, staging, and production environments is time-consuming and error-prone.

Helm solves this by providing:

- Template-based deployments
- Environment-specific configuration
- Version control
- Easy rollback
- Dependency management
- Community-maintained charts

---

# Task 2 – Install Helm and Create Kubernetes Cluster

## Installed Tools

Verified installation of:

```bash
docker --version
kubectl version --client
kind version
helm version
```

Successfully created a Kind cluster using the AI-BankApp configuration.

```bash
kind create cluster --config setup-k8s/kind-config.yml
```

Verified cluster:

```bash
kubectl get nodes
```

Result:

- 1 Control Plane
- 2 Worker Nodes

Verified Helm connectivity:

```bash
helm list
```

---

# Task 3 – Deploy MySQL Using Helm

Added the Bitnami repository.

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami

helm repo update
```

Installed MySQL.

```bash
helm install bankapp-mysql bitnami/mysql
```

Encountered an image pull error because the default image repository referenced an unavailable image.

Error:

```text
ImagePullBackOff
docker.io/bitnami/mysql:9.4.0-debian-12-r1
```

Resolved the issue by overriding the image repository.

```bash
helm install bankapp-mysql bitnami/mysql \
  --set image.repository=bitnamilegacy/mysql \
  --set image.tag=9.4.0-debian-12-r1 \
  --set global.security.allowInsecureImages=true
```

Successfully deployed MySQL.

Verified resources:

```bash
helm list

kubectl get all

kubectl get pvc

kubectl get secret
```

Verified database:

```bash
kubectl exec -it bankapp-mysql-0 -- \
mysql -uroot -pTest@123 \
-e "SHOW DATABASES;"
```

Database created successfully:

```text
bankappdb
```

---

# Task 4 – Deploy Using Values File

Created:

```text
mysql-values.yaml
```

Contents:

```yaml
auth:
  rootPassword: Test@123
  database: bankappdb

image:
  repository: bitnamilegacy/mysql
  tag: 9.4.0-debian-12-r1

global:
  security:
    allowInsecureImages: true

primary:
  resources:
    requests:
      cpu: 250m
      memory: 256Mi
    limits:
      cpu: 500m
      memory: 512Mi

  persistence:
    size: 5Gi
    storageClass: ""

metrics:
  enabled: true

  serviceMonitor:
    enabled: false
```

Installed another release using:

```bash
helm install bankapp-mysql-v2 bitnami/mysql \
-f mysql-values.yaml
```

During deployment, the metrics sidecar attempted to pull:

```text
docker.io/bitnami/mysqld-exporter
```

This resulted in an ImagePullBackOff because the metrics container still referenced the default image repository.

This exercise demonstrated that enabling optional Helm features may introduce additional containers with their own image configuration.

---

# Task 5 – Helm Release Management

## Upgrade

Performed an upgrade.

```bash
helm upgrade bankapp-mysql bitnami/mysql \
--reuse-values \
--set metrics.enabled=true
```

Verified revision history.

```bash
helm history bankapp-mysql
```

Output:

```text
Revision 1
Install complete

Revision 2
Upgrade complete
```

Performed rollback.

```bash
helm rollback bankapp-mysql 1
```

Verified rollback history.

Helm creates a new revision instead of deleting old ones, making deployments fully traceable.

---

# Task 6 – Explore Helm Chart Structure

Downloaded the MySQL chart.

```bash
helm pull bitnami/mysql --untar
```

Directory structure:

```text
mysql/
├── Chart.yaml
├── values.yaml
├── templates/
├── charts/
├── README.md
├── values.schema.json
```

---

## Important Files

### Chart.yaml

Contains metadata about the Helm Chart.

Important fields:

- Chart Name
- Description
- Dependencies
- Version
- App Version

Example:

```yaml
version: 14.0.3
appVersion: 9.4.0
```

---

### Difference Between Version and AppVersion

| version                             | appVersion                                |
| ----------------------------------- | ----------------------------------------- |
| Version of the Helm Chart           | Version of the application being deployed |
| Changes when chart templates change | Changes when application version changes  |

Example:

```text
Chart Version
14.0.3

MySQL Version
9.4.0
```

---

### values.yaml

Stores default configuration values.

Every deployment can override these values without modifying templates.

---

### templates/

Contains Kubernetes manifests written using Go Template syntax.

Example:

```yaml
image: "{{ .Values.image.repository }}"

replicas: { { .Values.primary.replicaCount } }
```

Helm replaces these placeholders during installation.

---

### charts/

Stores dependent Helm charts.

The MySQL chart includes the Bitnami Common chart as a dependency.

---

# Comparison – Raw YAML vs Helm

| Raw Kubernetes Manifests         | Helm                   |
| -------------------------------- | ---------------------- |
| Multiple YAML files              | Single Chart           |
| Manual edits                     | Template driven        |
| No rollback                      | Built-in rollback      |
| Hardcoded values                 | Configurable values    |
| Difficult environment management | Separate values files  |
| Manual dependency management     | Automatic dependencies |

---

# Challenges Faced

### ImagePullBackOff

Issue:

```text
docker.io/bitnami/mysql
```

The required image was unavailable.

Resolution:

Configured the chart to use:

```text
bitnamilegacy/mysql
```

---

### Metrics Sidecar Issue

Enabling metrics added:

```text
mysqld-exporter
```

The exporter still referenced the default Bitnami repository, resulting in another image pull error.

This highlighted the importance of reviewing all container images used by a Helm chart when enabling optional components.

---

# Key Learnings

- Understood Helm architecture and terminology.
- Learned the difference between Charts and Releases.
- Installed applications using community Helm Charts.
- Customized deployments using values files.
- Explored Helm release lifecycle.
- Learned upgrade and rollback operations.
- Explored Helm chart structure.
- Understood Go Template syntax.
- Learned the difference between Chart Version and App Version.
- Troubleshot real-world image compatibility issues.
- Compared Helm deployments with traditional Kubernetes manifests.

---

# Conclusion

Day 78 introduced Helm as a powerful package manager for Kubernetes. By replacing multiple raw Kubernetes manifests with reusable and configurable Helm Charts, application deployment becomes simpler, more maintainable, and easier to manage across environments. The lab also provided hands-on experience with deployment, customization, troubleshooting, release management, and chart exploration, forming a solid foundation for creating custom Helm Charts in the next phase of the DevOps journey.
