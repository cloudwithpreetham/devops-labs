# Day 50 – Kubernetes Architecture and Cluster Setup

## Overview

This project documents my first hands-on step into Kubernetes.

After learning Docker and containerization, I moved into container orchestration using Kubernetes. The goal of this day was to understand Kubernetes architecture, install `kubectl`, create a local Kubernetes cluster using kind, explore cluster components, and practice basic cluster lifecycle operations.

---

## What I Built

I created a local Kubernetes cluster using **kind**.

Cluster details:

| Item               | Value                          |
| ------------------ | ------------------------------ |
| Cluster Tool       | kind                           |
| Cluster Name       | `devops-cluster`               |
| Kubernetes Version | `v1.36.1`                      |
| Node Name          | `devops-cluster-control-plane` |
| Node Status        | `Ready`                        |
| kubectl Context    | `kind-devops-cluster`          |
| Container Runtime  | `containerd`                   |

---

## Why Kubernetes?

Docker is great for building and running containers on a single machine.

But in real production environments, applications often run across multiple servers with many containers. Managing those containers manually becomes difficult.

Kubernetes solves this by providing:

- Container orchestration
- Automated scheduling
- Self-healing
- Service discovery
- Scaling
- Networking
- Desired state management

In simple words, Kubernetes helps manage containers at scale.

---

## Kubernetes Architecture

```text
                         +----------------------------+
                         |       Control Plane         |
                         |----------------------------|
                         | kube-apiserver             |
kubectl ---------------> | etcd                       |
                         | kube-scheduler             |
                         | kube-controller-manager    |
                         +-------------+--------------+
                                       |
                                       |
                         +-------------v--------------+
                         |        Worker Node          |
                         |----------------------------|
                         | kubelet                    |
                         | kube-proxy                 |
                         | container runtime          |
                         | pods                       |
                         +----------------------------+
```

---

## Main Kubernetes Components

### Control Plane

#### kube-apiserver

The API server is the main entry point into the Kubernetes cluster. Every `kubectl` command talks to the API server first.

#### etcd

etcd is the key-value database used by Kubernetes to store cluster state and configuration.

#### kube-scheduler

The scheduler decides which node should run a newly created pod.

#### kube-controller-manager

The controller manager watches the cluster and makes sure the actual state matches the desired state.

---

### Worker Node

#### kubelet

The kubelet is the node agent. It communicates with the API server and ensures pods are running correctly.

#### kube-proxy

kube-proxy manages networking rules so services and pods can communicate.

#### Container Runtime

The container runtime actually runs the containers. In my kind cluster, the runtime is `containerd`.

---

## Tools Installed

### kubectl

`kubectl` is the command-line tool used to interact with Kubernetes clusters.

Verification:

```bash
kubectl version --client
```

Output:

```text
Client Version: v1.36.1
Kustomize Version: v5.8.1
```

---

### kind

kind is a tool for running Kubernetes clusters using Docker containers.

Verification:

```bash
kind version
```

Output:

```text
kind v0.33.0-alpha+3f9ba7e259e03b go1.26.3 linux/amd64
```

---

## Cluster Creation

I created the Kubernetes cluster using:

```bash
kind create cluster --name devops-cluster
```

The cluster was created successfully and `kubectl` context was automatically set to:

```text
kind-devops-cluster
```

---

## Cluster Verification

### Check Cluster Info

```bash
kubectl cluster-info
```

Output:

```text
Kubernetes control plane is running at https://127.0.0.1:37187
CoreDNS is running at https://127.0.0.1:37187/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

---

### Check Nodes

```bash
kubectl get nodes
```

Output:

```text
NAME                           STATUS   ROLES           AGE     VERSION
devops-cluster-control-plane   Ready    control-plane   3m57s   v1.36.1
```

Screenshot:

```text
screenshots/01-kubectl-get-nodes.png
```

---

### Check kube-system Pods

```bash
kubectl get pods -n kube-system
```

Output:

```text
NAME                                                   READY   STATUS    RESTARTS   AGE
coredns-589f44dc88-b5ddd                               1/1     Running   0          9m17s
coredns-589f44dc88-sxtck                               1/1     Running   0          9m17s
etcd-devops-cluster-control-plane                      1/1     Running   0          9m25s
kindnet-rwpwb                                          1/1     Running   0          9m17s
kube-apiserver-devops-cluster-control-plane            1/1     Running   0          9m23s
kube-controller-manager-devops-cluster-control-plane   1/1     Running   0          9m23s
kube-proxy-jcmjx                                       1/1     Running   0          9m17s
kube-scheduler-devops-cluster-control-plane            1/1     Running   0          9m23s
```

Screenshot:

```text
screenshots/02-kube-system-pods.png
```

---

## kube-system Pod Explanation

| Pod                                                    | Purpose                                                        |
| ------------------------------------------------------ | -------------------------------------------------------------- |
| `coredns`                                              | Provides internal DNS resolution inside the Kubernetes cluster |
| `etcd-devops-cluster-control-plane`                    | Stores cluster state and configuration                         |
| `kindnet-rwpwb`                                        | Provides networking for the kind cluster                       |
| `kube-apiserver-devops-cluster-control-plane`          | Handles all Kubernetes API requests                            |
| `kube-controller-manager-devops-cluster-control-plane` | Reconciles desired state with actual state                     |
| `kube-proxy-jcmjx`                                     | Manages networking rules for services and pods                 |
| `kube-scheduler-devops-cluster-control-plane`          | Assigns pods to suitable nodes                                 |

---

## Node Details

I inspected the node using:

```bash
kubectl describe node devops-cluster-control-plane
```

Important details:

```text
Operating System: linux
Architecture: amd64
Container Runtime Version: containerd://2.3.1
Kubelet Version: v1.36.1
PodCIDR: 10.244.0.0/24
```

Node health conditions:

```text
MemoryPressure: False
DiskPressure: False
PIDPressure: False
Ready: True
```

---

## Cluster Lifecycle Practice

I practiced deleting and recreating the cluster.

### Delete Cluster

```bash
kind delete cluster --name devops-cluster
```

Output:

```text
Deleting cluster "devops-cluster" ...
Deleted nodes: ["devops-cluster-control-plane"]
```

---

### Recreate Cluster

```bash
kind create cluster --name devops-cluster
```

---

### Verify Again

```bash
kubectl get nodes
```

Output:

```text
NAME                           STATUS   ROLES           AGE     VERSION
devops-cluster-control-plane   Ready    control-plane   2m10s   v1.36.1
```

---

## kubeconfig

A kubeconfig file stores the configuration that `kubectl` uses to connect to a Kubernetes cluster.

It includes:

- Cluster information
- User authentication details
- Contexts
- Current active context

Default kubeconfig location:

```text
~/.kube/config
```

Current context:

```bash
kubectl config current-context
```

Output:

```text
kind-devops-cluster
```

Available contexts:

```bash
kubectl config get-contexts
```

Output:

```text
CURRENT   NAME                  CLUSTER               AUTHINFO              NAMESPACE
*         kind-devops-cluster   kind-devops-cluster   kind-devops-cluster
```

---

## What Happens When I Run `kubectl apply -f pod.yaml`?

1. `kubectl` sends the request to the API server.
2. The API server validates the request.
3. The desired state is stored in etcd.
4. The scheduler selects a suitable node.
5. The kubelet on that node receives the instruction.
6. The container runtime starts the container.
7. The pod starts running.
8. Kubernetes continuously watches and maintains the desired state.

---

## What Happens If the API Server Goes Down?

If the API server goes down, new `kubectl` commands and new resource changes cannot be processed.

Existing workloads may continue running, but the cluster cannot accept new control-plane instructions until the API server is restored.

---

## What Happens If a Worker Node Goes Down?

If a worker node goes down, pods running on that node become unavailable.

Kubernetes detects the failure and tries to reschedule the affected workloads on healthy nodes, depending on the workload type and available resources.

---

## Screenshots

| Screenshot                             | Description                              |
| -------------------------------------- | ---------------------------------------- |
| `screenshots/01-kubectl-get-nodes.png` | Shows the Kubernetes node in Ready state |
| `screenshots/02-kube-system-pods.png`  | Shows kube-system pods running           |

---

## Commands Practiced

```bash
kubectl version --client
kind version
kind create cluster --name devops-cluster
kubectl cluster-info
kubectl get nodes
kubectl get nodes -o wide
kubectl describe node devops-cluster-control-plane
kubectl get namespace
kubectl get pods -A
kubectl get pods -n kube-system
kind delete cluster --name devops-cluster
kind create cluster --name devops-cluster
kubectl config current-context
kubectl config get-contexts
kubectl config view
```

---

## Key Learnings

- Kubernetes is used to manage containers at scale.
- A Kubernetes cluster has a control plane and worker nodes.
- The API server is the main entry point into the cluster.
- etcd stores the cluster state.
- The scheduler decides where pods should run.
- The controller manager maintains the desired state.
- kubelet manages pods on a node.
- kube-proxy handles networking rules.
- kind is useful for running a local Kubernetes cluster using Docker.
- kubeconfig tells `kubectl` which cluster to connect to.
- The `kube-system` namespace contains important Kubernetes system components.

---

## Final Status

Day 50 completed successfully.

I installed Kubernetes tools, created a local kind cluster, verified the node status, checked system pods, explored the architecture, and practiced cluster lifecycle operations.
