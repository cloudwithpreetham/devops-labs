# Day 60 – Kubernetes Capstone Project: WordPress + MySQL

## Overview

Day 60 marks the completion of the Kubernetes learning journey by deploying a complete WordPress + MySQL application using multiple Kubernetes concepts learned throughout Days 52–59.

This project combines stateless and stateful workloads, persistent storage, configuration management, service discovery, health monitoring, and autoscaling into a single real-world deployment.

---

# Objective

Deploy a production-style WordPress + MySQL stack inside a dedicated Kubernetes namespace and validate:

- Application deployment
- Service communication
- Persistent storage
- Self-healing capabilities
- Resource management
- Horizontal Pod Autoscaling

---

# Architecture

```text
+-----------------------+
|       Browser         |
+-----------+-----------+
            |
            v
+-----------------------+
| NodePort Service      |
| wordpress             |
+-----------+-----------+
            |
            v
+-----------------------+
| WordPress Deployment  |
| Replicas: 2           |
+-----------+-----------+
            |
            v
+-----------------------+
| ConfigMap             |
| Secret                |
+-----------+-----------+
            |
            v
+-----------------------+
| MySQL StatefulSet     |
| mysql-0              |
+-----------+-----------+
            |
            v
+-----------------------+
| Persistent Volume     |
| Claim (1Gi)           |
+-----------------------+
```

---

# Kubernetes Resources Used

| Resource         | Purpose                           |
| ---------------- | --------------------------------- |
| Namespace        | Resource isolation                |
| Secret           | Database credentials              |
| ConfigMap        | Application configuration         |
| Deployment       | WordPress workload management     |
| StatefulSet      | MySQL database management         |
| PVC              | Persistent data storage           |
| Headless Service | Stable network identity for MySQL |
| NodePort Service | External application access       |
| Resource Limits  | CPU and memory control            |
| Liveness Probe   | Container health monitoring       |
| Readiness Probe  | Traffic readiness checks          |
| HPA              | Automatic scaling                 |

---

# Implementation

## 1. Namespace Creation

Created a dedicated namespace:

```bash
kubectl create namespace capstone
kubectl config set-context --current --namespace=capstone
```

---

## 2. MySQL Deployment

Created:

- Secret for database credentials
- Headless Service
- StatefulSet
- Persistent Volume Claim

Features:

- MySQL 8.0
- Persistent Storage (1Gi)
- Resource Requests and Limits
- Stable Pod Identity

Verification:

```bash
kubectl exec -it mysql-0 -- mysql -u wpuser -pwppass123 -e "SHOW DATABASES;"
```

Output:

```text
information_schema
performance_schema
wordpress
```

---

## 3. WordPress Deployment

Created:

- ConfigMap
- Deployment with 2 replicas
- Resource Requests and Limits
- Readiness Probe
- Liveness Probe

WordPress successfully connected to MySQL using:

```text
WORDPRESS_DB_HOST
WORDPRESS_DB_NAME
WORDPRESS_DB_USER
WORDPRESS_DB_PASSWORD
```

---

## 4. Service Exposure

Created a NodePort Service:

```text
Port: 80
NodePort: 30080
```

Used port-forwarding to access WordPress:

```bash
kubectl port-forward svc/wordpress 8080:80
```

Successfully completed the WordPress installation wizard and created a sample blog post.

---

# Self-Healing Validation

## WordPress Deployment Recovery

Deleted one WordPress Pod:

```bash
kubectl delete pod wordpress-6fccd79d8f-445h5
```

Result:

- Pod terminated successfully
- Deployment automatically created a replacement Pod
- Desired replica count restored

Status: PASS

---

## MySQL StatefulSet Recovery

Deleted MySQL Pod:

```bash
kubectl delete pod mysql-0
```

Result:

- StatefulSet recreated mysql-0 automatically
- Database service restored
- Pod identity remained unchanged

Status: PASS

---

# Persistence Validation

The MySQL database used a Persistent Volume Claim:

```text
mysql-storage-mysql-0
```

After deleting the MySQL Pod:

- PVC remained Bound
- Database was restored automatically
- Application data persisted

Status: PASS

---

# Horizontal Pod Autoscaler

Created HPA:

```yaml
minReplicas: 2
maxReplicas: 10
averageUtilization: 50%
```

Verification:

```bash
kubectl get hpa
```

Output:

```text
wordpress-hpa
cpu: 2%/50%
MINPODS: 2
MAXPODS: 10
```

Status: PASS

---

# Final Cluster State

```bash
kubectl get all -n capstone
```

Resources:

| Resource Type | Count |
| ------------- | ----- |
| Pods          | 3     |
| Services      | 2     |
| Deployment    | 1     |
| StatefulSet   | 1     |
| ReplicaSet    | 1     |
| HPA           | 1     |
| PVC           | 1     |

---

# Concept Mapping

| Day    | Concept                           |
| ------ | --------------------------------- |
| Day 52 | Namespaces, Deployments           |
| Day 53 | Services                          |
| Day 54 | ConfigMaps, Secrets               |
| Day 55 | Persistent Volumes, PVCs          |
| Day 56 | StatefulSets                      |
| Day 57 | Resource Requests, Limits, Probes |
| Day 58 | Horizontal Pod Autoscaler         |
| Day 59 | Helm                              |
| Day 60 | End-to-End Application Deployment |

---

# Challenges Faced

### Port Forward Interruption

While testing StatefulSet recovery, the browser temporarily became inaccessible because the active port-forward session was interrupted.

Resolution:

- Restarted port-forwarding
- Verified application accessibility again

---

# Production Improvements

If deploying this application in production, the following improvements would be added:

- Ingress Controller
- TLS Certificates
- External Managed Database
- Automated Backups
- Prometheus Monitoring
- Grafana Dashboards
- Centralized Logging
- Network Policies
- CI/CD Pipeline
- Pod Disruption Budgets

---

# Key Learnings

- StatefulSets provide stable identities for databases.
- Persistent Volume Claims protect data across Pod restarts.
- Deployments automatically maintain desired application replicas.
- ConfigMaps and Secrets separate configuration from application code.
- Probes improve workload reliability.
- HPA enables automatic scaling based on resource usage.
- Kubernetes continuously maintains the desired state of applications.

---

# Conclusion

This capstone project successfully combined all major Kubernetes concepts into a single deployment.

The project demonstrated workload orchestration, persistence, networking, configuration management, self-healing, and autoscaling capabilities of Kubernetes while deploying a real-world WordPress + MySQL application.
