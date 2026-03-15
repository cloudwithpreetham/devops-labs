# Day 51 – Kubernetes Manifests and Your First Pods

## Overview

This directory contains my Day 51 Kubernetes practice from the 90 Days of DevOps journey.

The goal of this task was to understand the structure of Kubernetes YAML manifests and deploy my first Pods into a running Kubernetes cluster.

I created multiple Pod manifests by hand, applied them using `kubectl`, inspected running Pods, practiced labels and filtering, compared imperative and declarative workflows, validated manifests using dry-run, and finally cleaned up all resources.

## What I Practiced

- Writing Kubernetes Pod manifests from scratch
- Understanding the four main manifest fields:
  - `apiVersion`
  - `kind`
  - `metadata`
  - `spec`

- Creating Pods using `kubectl apply`
- Creating a Pod imperatively using `kubectl run`
- Viewing generated Kubernetes YAML
- Using dry-run to scaffold manifests
- Validating manifests before applying them
- Inspecting Pods using `kubectl describe`
- Reading container logs using `kubectl logs`
- Accessing a running container using `kubectl exec`
- Using labels to organize and filter Pods
- Understanding why standalone Pods are not used directly in production

## Project Structure

```text
2026/day-51/
├── nginx-pod.yaml
├── busybox-pod.yaml
├── app-pod.yaml
├── test-pod.yaml
├── day-51-pods.md
├── README.md
└── screenshots/
    ├── day-51-nginx-running.png
    ├── day-51-three-pods-running.png
    ├── day-51-pod-labels.png
    └── day-51-cleanup.png
```

## Files Created

| File               | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `nginx-pod.yaml`   | Pod manifest for running an Nginx container            |
| `busybox-pod.yaml` | Pod manifest for running BusyBox with a custom command |
| `app-pod.yaml`     | Third Pod manifest with multiple labels                |
| `test-pod.yaml`    | Dry-run generated Pod YAML                             |
| `day-51-pods.md`   | Detailed notes and documentation for Day 51            |
| `README.md`        | Summary of the Day 51 task                             |

## Pod Manifests

### 1. Nginx Pod

File: `nginx-pod.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```

Command used:

```bash
kubectl apply -f nginx-pod.yaml
```

Verification:

```bash
kubectl get pods
kubectl get pods -o wide
kubectl describe pod nginx-pod
kubectl logs nginx-pod
kubectl exec -it nginx-pod -- /bin/bash
```

Inside the container:

```bash
curl localhost:80
exit
```

Result:

The Nginx welcome page was displayed successfully, confirming that the Pod was running correctly.

## 2. BusyBox Pod

File: `busybox-pod.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox-pod
  labels:
    app: busybox
    environment: dev
spec:
  containers:
    - name: busybox
      image: busybox:latest
      command: ["sh", "-c", "echo Hello from BusyBox && sleep 3600"]
```

Command used:

```bash
kubectl apply -f busybox-pod.yaml
```

Verification:

```bash
kubectl logs busybox-pod
```

Output:

```text
Hello from BusyBox
```

## 3. App Pod with Labels

File: `app-pod.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
  labels:
    app: demo-app
    environment: staging
    team: devops
spec:
  containers:
    - name: demo-container
      image: nginx:stable
      ports:
        - containerPort: 80
```

Command used:

```bash
kubectl apply -f app-pod.yaml
```

Verification:

```bash
kubectl get pods --show-labels
```

## Labels and Filtering

I practiced filtering Pods using labels.

```bash
kubectl get pods --show-labels
kubectl get pods -l app=demo-app
kubectl get pods -l environment=staging
kubectl get pods -l team=devops
```

Labels used:

| Pod           | Labels                                               |
| ------------- | ---------------------------------------------------- |
| `nginx-pod`   | `app=nginx`                                          |
| `busybox-pod` | `app=busybox`, `environment=dev`                     |
| `app-pod`     | `app=demo-app`, `environment=staging`, `team=devops` |

Labels are important because they help Kubernetes and DevOps engineers organize, filter, select, monitor, and manage resources.

## Imperative vs Declarative Kubernetes

### Imperative Approach

The imperative approach means creating resources directly from the command line.

Example:

```bash
kubectl run redis-pod --image=redis:latest
```

This is fast for testing, but it is not ideal for production because the configuration is not stored as code.

### Declarative Approach

The declarative approach means writing YAML manifests and applying them.

Example:

```bash
kubectl apply -f nginx-pod.yaml
```

This is the preferred DevOps approach because the configuration can be stored in Git, reviewed, reused, and applied consistently.

## Dry Run YAML Generation

I generated a Pod manifest without creating the Pod:

```bash
kubectl run test-pod --image=nginx --dry-run=client -o yaml > test-pod.yaml
```

This created a basic YAML file that can be customized before applying.

Dry-run is useful when I want to quickly generate Kubernetes manifest templates.

## Manifest Validation

I validated manifests before applying them.

Client-side validation:

```bash
kubectl apply -f nginx-pod.yaml --dry-run=client
```

Server-side validation:

```bash
kubectl apply -f nginx-pod.yaml --dry-run=server
```

This helped me check the manifest before making actual changes in the cluster.

## Screenshots

Screenshots captured during this task:

| Screenshot                      | Purpose                                              |
| ------------------------------- | ---------------------------------------------------- |
| `day-51-nginx-running.png`      | Shows the Nginx Pod running                          |
| `day-51-three-pods-running.png` | Shows multiple Pods running with IP and node details |
| `day-51-pod-labels.png`         | Shows Pods with labels                               |
| `day-51-cleanup.png`            | Shows that all standalone Pods were deleted          |

## Cleanup

I deleted all standalone Pods after completing the task.

```bash
kubectl delete pod nginx-pod
kubectl delete pod busybox-pod
kubectl delete pod redis-pod
kubectl delete pod app-pod
```

Verification:

```bash
kubectl get pods
```

Expected result:

```text
No resources found in default namespace.
```

## Important Learning

A standalone Pod is not self-healing.

If a standalone Pod is deleted, Kubernetes does not recreate it automatically because there is no controller managing it.

This is why production workloads usually use Deployments instead of bare Pods.

Deployments provide:

- Self-healing
- Replica management
- Rolling updates
- Rollbacks
- Better production reliability

## Commands Used

```bash
kubectl apply -f nginx-pod.yaml
kubectl apply -f busybox-pod.yaml
kubectl apply -f app-pod.yaml

kubectl get pods
kubectl get pods -o wide
kubectl get pods --show-labels

kubectl describe pod nginx-pod
kubectl logs nginx-pod
kubectl logs busybox-pod

kubectl exec -it nginx-pod -- /bin/bash

kubectl get pods -l app=demo-app
kubectl get pods -l environment=staging
kubectl get pods -l team=devops

kubectl run redis-pod --image=redis:latest
kubectl get pod redis-pod -o yaml

kubectl run test-pod --image=nginx --dry-run=client -o yaml > test-pod.yaml

kubectl apply -f nginx-pod.yaml --dry-run=client
kubectl apply -f nginx-pod.yaml --dry-run=server

kubectl delete pod nginx-pod
kubectl delete pod busybox-pod
kubectl delete pod redis-pod
kubectl delete pod app-pod
```

## Key Takeaways

- Kubernetes resources are commonly defined using YAML manifests.
- A Pod is the smallest deployable unit in Kubernetes.
- The four important manifest fields are `apiVersion`, `kind`, `metadata`, and `spec`.
- `kubectl apply -f` follows the declarative approach.
- `kubectl run` follows the imperative approach.
- Labels help organize and filter resources.
- `kubectl describe` is useful for debugging.
- `kubectl logs` helps inspect container output.
- `kubectl exec` allows shell access into a running container.
- Dry-run helps validate and generate manifests.
- Standalone Pods are useful for learning but not recommended for production workloads.
- Deployments are preferred in real-world Kubernetes environments.

## Status

Day 51 completed successfully.

I created my first Kubernetes Pods from scratch and understood the foundation required before moving into Deployments.
