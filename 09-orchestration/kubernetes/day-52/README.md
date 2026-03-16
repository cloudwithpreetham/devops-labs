# Day 52 – Kubernetes Namespaces and Deployments

## Overview

On Day 52 of my #90DaysOfDevOps journey, I explored two fundamental Kubernetes concepts:

- Namespaces
- Deployments

I learned how to organize resources within a Kubernetes cluster using namespaces and how Deployments provide self-healing, scaling, rolling updates, and rollback capabilities for applications running in Kubernetes.

---

## Objectives

- Understand Kubernetes default namespaces
- Create custom namespaces for different environments
- Deploy applications inside namespaces
- Create and manage Deployments
- Test self-healing behavior
- Scale Deployments up and down
- Perform rolling updates
- Roll back to previous application versions

---

## Project Structure

```text
day-52/
├── README.md
├── task.md
├── day-52-namespaces-deployments.md
│
├── yaml-scripts/
│   ├── dev-namespace.yaml
│   ├── staging-namespace.yaml
│   ├── production-namespace.yaml
│   └── nginx-deployment.yaml
│
└── screenshots/
    ├── 01-namespaces-created.png
    ├── 02-kube-system-pods.png
    ├── 03-pods-all-namespaces.png
    ├── 04-deployment-running.png
    ├── 05-dev-pods-running.png
    ├── 06-scaled-deployment.png
    └── 07-rollout-history.png
```

---

## Namespaces Created

| Namespace  | Purpose                 |
| ---------- | ----------------------- |
| dev        | Development environment |
| staging    | Staging environment     |
| production | Production environment  |

### Verify Namespaces

```bash
kubectl get namespaces
```

---

## Deployment Details

### Nginx Deployment

- Namespace: `dev`
- Replicas: `3`
- Container Image: `nginx:1.24`

Deployment features demonstrated:

- Replica management
- Self-healing
- Horizontal scaling
- Rolling updates
- Rollbacks

---

## Key Commands Practiced

### List Namespaces

```bash
kubectl get namespaces
```

### View Pods Across All Namespaces

```bash
kubectl get pods -A
```

### Create Deployment

```bash
kubectl apply -f nginx-deployment.yaml
```

### View Deployment

```bash
kubectl get deployments -n dev
```

### Scale Deployment

```bash
kubectl scale deployment nginx-deployment --replicas=5 -n dev
```

### Rolling Update

```bash
kubectl set image deployment/nginx-deployment nginx=nginx:1.25 -n dev
```

### Check Rollout Status

```bash
kubectl rollout status deployment/nginx-deployment -n dev
```

### Rollback Deployment

```bash
kubectl rollout undo deployment/nginx-deployment -n dev
```

---

## Self-Healing Demonstration

A Deployment-managed Pod was manually deleted.

```bash
kubectl delete pod <pod-name> -n dev
```

Kubernetes automatically created a replacement Pod to maintain the desired replica count.

This demonstrates one of the most important Kubernetes features: **self-healing**.

---

## Scaling Demonstration

### Scale Up

```bash
kubectl scale deployment nginx-deployment --replicas=5 -n dev
```

Kubernetes automatically created additional Pods.

### Scale Down

```bash
kubectl scale deployment nginx-deployment --replicas=2 -n dev
```

Kubernetes automatically terminated extra Pods while maintaining the desired state.

---

## Rolling Update and Rollback

Updated Deployment image:

```bash
kubectl set image deployment/nginx-deployment nginx=nginx:1.25 -n dev
```

Checked rollout:

```bash
kubectl rollout status deployment/nginx-deployment -n dev
```

Viewed rollout history:

```bash
kubectl rollout history deployment/nginx-deployment -n dev
```

Performed rollback:

```bash
kubectl rollout undo deployment/nginx-deployment -n dev
```

Verified image version returned to:

```text
nginx:1.24
```

---

## Screenshots

### Namespace Creation

- 01-namespaces-created.png

### Kubernetes System Pods

- 02-kube-system-pods.png

### Pods Across All Namespaces

- 03-pods-all-namespaces.png

### Deployment Status

- 04-deployment-running.png

### Deployment Pods

- 05-dev-pods-running.png

### Scaling Demonstration

- 06-scaled-deployment.png

### Rollout History

- 07-rollout-history.png

---

## Key Learnings

- Namespaces help organize and isolate Kubernetes resources.
- Deployments are the recommended way to run stateless applications.
- Deployments automatically recreate failed or deleted Pods.
- ReplicaSets work behind Deployments to maintain desired state.
- Scaling can be performed both imperatively and declaratively.
- Rolling updates provide zero-downtime application upgrades.
- Rollbacks help quickly recover from failed releases.

---

## Outcome

Successfully created multiple Kubernetes namespaces, deployed a self-healing Nginx application, scaled workloads, performed rolling updates, and rolled back to a previous version.

This exercise provided hands-on experience with core Kubernetes concepts used in real-world DevOps and Cloud environments.

---

### Tech Stack

- Linux
- Kubernetes
- kubectl
- YAML
- Nginx
- Kind Cluster

---

### Challenge

#90DaysOfDevOps Day 52 Completed Successfully.
