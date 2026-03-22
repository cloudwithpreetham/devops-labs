# Day 60 - Kubernetes Capstone Project (WordPress + MySQL)

## Project Overview

This capstone project concludes the Kubernetes learning journey by combining all major concepts learned during Days 52–59 into a single real-world application deployment.

The project deploys a complete WordPress + MySQL stack inside Kubernetes using Deployments, StatefulSets, Services, ConfigMaps, Secrets, Persistent Volumes, Resource Management, Health Checks, and Horizontal Pod Autoscaling.

---

## Objectives

- Deploy a WordPress frontend application
- Deploy a MySQL database using StatefulSets
- Configure persistent storage for database durability
- Manage configuration using ConfigMaps and Secrets
- Implement resource requests and limits
- Configure liveness and readiness probes
- Expose the application using a Service
- Validate self-healing capabilities
- Configure Horizontal Pod Autoscaling (HPA)

---

## Architecture

```text
Browser
   │
   ▼
NodePort Service
   │
   ▼
WordPress Deployment (2 Replicas)
   │
   ├── ConfigMap
   └── Secret
   │
   ▼
MySQL StatefulSet
   │
   ▼
Persistent Volume Claim (1Gi)
```

---

## Project Structure

```text
day-60/
├── README.md
├── task.md
├── day-60-capstone.md
├── screenshots/
│   ├── 01-namespace-created.png
│   ├── 02-mysql-running.png
│   ├── 03-wordpress-pods.png
│   ├── 04-wordpress-setup-page.png
│   ├── 05-blog-created.png
│   ├── 06-wordpress-self-healing.png
│   ├── 07-mysql-self-healing.png
│   ├── 08-hpa-created.png
│   └── 09-kubectl-get-all.png
└── yaml-scripts/
    ├── mysql-secret.yaml
    ├── mysql-headless-service.yaml
    ├── mysql-statefulset.yaml
    ├── wordpress-configmap.yaml
    ├── wordpress-deployment.yaml
    ├── wordpress-service.yaml
    └── wordpress-hpa.yaml
```

---

## Kubernetes Concepts Used

| Concept          | Implementation                   |
| ---------------- | -------------------------------- |
| Namespace        | capstone                         |
| Secret           | MySQL credentials                |
| ConfigMap        | WordPress database configuration |
| Deployment       | WordPress application            |
| StatefulSet      | MySQL database                   |
| PVC              | Persistent database storage      |
| Headless Service | MySQL networking                 |
| NodePort Service | WordPress access                 |
| Resource Limits  | CPU and memory management        |
| Readiness Probe  | Application readiness            |
| Liveness Probe   | Application health               |
| HPA              | Automatic scaling                |

---

## Resources Created

### Namespace

```bash
kubectl create namespace capstone
```

### MySQL Components

- Secret
- Headless Service
- StatefulSet
- Persistent Volume Claim

### WordPress Components

- ConfigMap
- Deployment (2 Replicas)
- NodePort Service

### Autoscaling

- Horizontal Pod Autoscaler
- Minimum Replicas: 2
- Maximum Replicas: 10
- CPU Threshold: 50%

---

## Verification Results

### MySQL Verification

```bash
kubectl exec -it mysql-0 -- mysql -u wpuser -pwppass123 -e "SHOW DATABASES;"
```

Result:

```text
information_schema
performance_schema
wordpress
```

---

### WordPress Verification

- Application deployed successfully
- Connected to MySQL database
- WordPress installation completed
- Sample blog post created

Status: PASS

---

### Self-Healing Test

#### Deployment Recovery

```bash
kubectl delete pod <wordpress-pod>
```

Result:

- Pod automatically recreated
- Desired replica count maintained

Status: PASS

---

#### StatefulSet Recovery

```bash
kubectl delete pod mysql-0
```

Result:

- StatefulSet recreated Pod automatically
- Database restored successfully

Status: PASS

---

### Persistence Test

Verified that database storage remained available after MySQL Pod recreation.

Result:

- PVC remained Bound
- Database data persisted

Status: PASS

---

### HPA Verification

```bash
kubectl get hpa
```

Result:

```text
wordpress-hpa
cpu: 2%/50%
MINPODS: 2
MAXPODS: 10
```

Status: PASS

---

## Final Cluster Status

```bash
kubectl get all -n capstone
```

Resources:

- 3 Pods
- 2 Services
- 1 Deployment
- 1 StatefulSet
- 1 ReplicaSet
- 1 HPA
- 1 PVC

---

## Key Learnings

- Deploying stateful applications using StatefulSets
- Managing persistent storage using PVCs
- Separating configuration with ConfigMaps and Secrets
- Implementing self-healing workloads
- Using resource requests and limits effectively
- Monitoring application health using probes
- Configuring automatic scaling with HPA
- Understanding Kubernetes desired-state management

---

## Production Enhancements

Potential improvements for production deployments:

- Ingress Controller
- TLS Certificates
- Managed Database Service
- Automated Backup Strategy
- Prometheus Monitoring
- Grafana Dashboards
- Centralized Logging
- Network Policies
- CI/CD Pipeline
- Pod Disruption Budgets

---

## Conclusion

This capstone project successfully demonstrated the deployment and operation of a complete WordPress + MySQL application on Kubernetes while integrating all major concepts learned throughout the Kubernetes learning phase of the 90 Days of DevOps journey.

The project validated Kubernetes core capabilities including workload orchestration, service discovery, persistence, self-healing, configuration management, and autoscaling.
