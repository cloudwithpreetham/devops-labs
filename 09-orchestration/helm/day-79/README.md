# Day 79 – Creating a Custom Helm Chart for AI-BankApp

> Converted the AI-BankApp's Kubernetes manifests into a reusable Helm chart, making the complete application stack deployable with a single Helm command.

![Helm](https://img.shields.io/badge/Helm-v3-blue?logo=helm)
![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.36-326CE5?logo=kubernetes)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-Application-6DB33F?logo=springboot)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql)
![Ollama](https://img.shields.io/badge/Ollama-AI-black)

---

# Project Overview

On **Day 79** of my **#90DaysOfDevOps** journey, I transformed the AI-BankApp from a collection of raw Kubernetes manifests into a reusable, configurable Helm chart.

Instead of maintaining multiple YAML files manually, the application can now be deployed using a single Helm command while supporting configurable environments through `values.yaml`.

The application stack includes:

- Spring Boot AI-BankApp
- MySQL Database
- Ollama AI Service
- Persistent Storage
- ConfigMaps
- Secrets
- Services
- Horizontal Pod Autoscaler (HPA)

---

# Project Architecture

```text
                Helm Chart
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
    Spring Boot    MySQL      Ollama
         │           │           │
         └──────┬────┴────┬──────┘
                ▼         ▼
          Persistent Volumes
                │
          Kubernetes Cluster
```

---

# Project Structure

```text
helm-chart/
└── bankapp
    ├── Chart.yaml
    ├── values.yaml
    └── templates
        ├── _helpers.tpl
        ├── NOTES.txt
        ├── configmap.yaml
        ├── secret.yaml
        ├── storage.yaml
        ├── bankapp-deployment.yaml
        ├── mysql-deployment.yaml
        ├── ollama-deployment.yaml
        ├── services.yaml
        └── hpa.yaml
```

![Helm chart scaffold for the custom BankApp chart](screenshots/01-helm-chart-scaffold.png)

---

# Features

- Custom Helm Chart
- Dynamic configuration using `values.yaml`
- ConfigMap templating
- Secret templating
- Persistent Volume Claims
- StorageClass support
- Spring Boot Deployment
- MySQL Deployment
- Ollama Deployment
- Services
- Horizontal Pod Autoscaler
- Init Containers
- Lifecycle Hooks
- Readiness Probes
- Liveness Probes
- Conditional component deployment
- Kind Cluster deployment
- Helm validation

---

# Helm Templates Created

| Template | Description |
|-----------|-------------|
| `configmap.yaml` | Application configuration |
| `secret.yaml` | Database credentials |
| `storage.yaml` | StorageClass + PVCs |
| `bankapp-deployment.yaml` | Spring Boot application |
| `mysql-deployment.yaml` | MySQL database |
| `ollama-deployment.yaml` | Ollama AI service |
| `services.yaml` | Kubernetes Services |
| `hpa.yaml` | Horizontal Pod Autoscaler |

![Core Helm templates created for BankApp, MySQL, Ollama, services, storage, and HPA](screenshots/03-core-templates-created.png)

---

# values.yaml Configuration

The chart is fully configurable.

Example sections include:

```yaml
bankapp:
  replicaCount: 4

mysql:
  enabled: true

ollama:
  enabled: true

storageClass:
  create: true
```

Everything from Docker images to resource requests can be modified without editing templates.

![Chart metadata and values.yaml configuration for the BankApp Helm chart](screenshots/02-chart-and-values-config.png)

---

# Helm Functions Used

| Function | Purpose |
|----------|---------|
| `.Values` | Read configuration values |
| `include` | Helper templates |
| `if` | Conditional resources |
| `default` | Default values |
| `b64enc` | Secret encoding |
| `toYaml` | Convert objects to YAML |
| `nindent` | YAML indentation |

---

# Validation

## Helm Lint

```bash
helm lint bankapp/
```

Result

```text
1 chart(s) linted, 0 chart(s) failed
```

![Helm lint completed successfully for the BankApp chart](screenshots/04-helm-lint-success.png)

---

## Helm Template

```bash
helm template my-bankapp bankapp/
```

Verified rendering of:

- ConfigMap
- Secret
- StorageClass
- PVCs
- Deployments
- Services
- HPA

![Helm template rendering the generated Kubernetes manifests](screenshots/05-helm-template-render.png)

---

## Conditional Rendering

```bash
helm template my-bankapp bankapp \
--set ollama.enabled=false
```

Verified:

- Ollama Deployment removed
- Ollama Service removed
- Ollama PVC removed
- Wait-for-Ollama init container removed

![Helm dry run completed successfully before installing the chart](screenshots/07-helm-dry-run-success.png)

---

# Deployment

## Create Kind Cluster

```bash
kind create cluster --name bankapp
```

![Kind cluster created and ready for the BankApp Helm deployment](screenshots/06-kind-cluster-ready.png)

---

## Install Helm Chart

```bash
helm install my-bankapp bankapp \
-n bankapp \
--create-namespace \
--set storageClass.create=false \
--set mysql.persistence.storageClass=standard \
--set ollama.persistence.storageClass=standard
```

![Helm install completed successfully for the BankApp release](screenshots/08-helm-install-success.png)

---

## Verify Deployment

```bash
helm list -n bankapp
```

```bash
kubectl get all -n bankapp
```

![Kubernetes resources created by the BankApp Helm chart](screenshots/09-kubectl-get-all.png)

```bash
kubectl get pvc -n bankapp
```

![Persistent volume claims bound for MySQL and Ollama storage](screenshots/10-pvcs-bound.png)

```bash
kubectl get pods -n bankapp
```

![BankApp, MySQL, and Ollama pods running in the bankapp namespace](screenshots/11-pods-running.png)

---

## Application Health

```bash
curl http://localhost:8080/actuator/health
```

Output

```json
{
  "status":"UP"
}
```

---

## Access Application

```bash
kubectl port-forward \
--address 0.0.0.0 \
svc/my-bankapp-service \
-n bankapp \
8080:8080
```

Open

```
http://<EC2-PUBLIC-IP>:8080
```

![AI-BankApp login page served after port-forwarding the Helm deployment](screenshots/12-bankapp-login-page.png)

---

# Challenges Faced

### Helm Lint Error

Issue

- Default `NOTES.txt` referenced unsupported values.

Solution

- Simplified the release notes template.

---

### No Kubernetes Context

Issue

```
current-context is not set
```

Solution

Created a Kind cluster.

---

### Ollama Pending

Issue

```
Insufficient CPU
```

Solution

Reduced resource requests for local Kind deployment.

---

### Browser Connection Refused

Issue

Port forwarding was only listening on localhost.

Solution

Used:

```bash
kubectl port-forward \
--address 0.0.0.0 \
svc/my-bankapp-service \
-n bankapp \
8080:8080
```

---

# Key Learnings

- Built a custom Helm chart from raw Kubernetes manifests.
- Learned Helm chart structure and packaging.
- Parameterized deployments using `values.yaml`.
- Used Helm template functions effectively.
- Implemented reusable Kubernetes templates.
- Validated charts using `helm lint`.
- Rendered manifests using `helm template`.
- Tested deployments with `helm install --dry-run`.
- Deployed a complete application stack on Kind.
- Debugged scheduling, storage, and networking issues.

---

# Tech Stack

- Helm 3
- Kubernetes
- Kind
- Spring Boot
- MySQL
- Ollama
- Docker
- YAML
- Linux

---

# Outcome

Successfully converted the AI-BankApp from **12 static Kubernetes manifests** into a **single reusable Helm chart**.

The chart supports configurable deployments, reusable templates, conditional components, persistent storage, autoscaling, and can deploy the complete application stack with a single Helm command—closely reflecting real-world Kubernetes packaging practices.

---

**Repository:** AI-BankApp-DevOps

**Day:** 79

**Project:** Custom Helm Chart for AI-BankApp

**Challenge:** #90DaysOfDevOps
