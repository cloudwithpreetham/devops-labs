# Day 56 – Kubernetes StatefulSets

## Overview

Today I learned about Kubernetes StatefulSets, which are used for deploying stateful applications such as databases, message queues, and distributed systems. Unlike Deployments, StatefulSets provide stable network identities, ordered deployment, and persistent storage per pod.

---

## Problem with Deployments

Deployments are designed for stateless applications. They create pods with random names and do not guarantee identity or storage consistency.

### Issues:

* Pod names are random (e.g., `nginx-abc123`)
* No stable network identity
* No guaranteed storage persistence per pod
* Pods are interchangeable

This makes Deployments unsuitable for systems like:

* MySQL
* PostgreSQL
* Kafka
* Elasticsearch

---

## StatefulSet Features

| Feature          | Deployment          | StatefulSet                         |
| ---------------- | ------------------- | ----------------------------------- |
| Pod Names        | Random              | Stable (web-0, web-1, web-2)        |
| Ordering         | Parallel            | Sequential                          |
| Storage          | Shared or ephemeral | Dedicated per pod (PVC per replica) |
| Network Identity | Dynamic             | Stable DNS per pod                  |
| Use Case         | Stateless apps      | Stateful apps                       |

---

## Headless Service

A Headless Service is created with:

```yaml
clusterIP: None
```

### Purpose:

* Provides stable DNS entries for each pod
* Does not load balance traffic
* Required for StatefulSets

### Example DNS:

* web-0.nginx-headless.default.svc.cluster.local
* web-1.nginx-headless.default.svc.cluster.local
* web-2.nginx-headless.default.svc.cluster.local

---

## StatefulSet Architecture

### Key Components:

* StatefulSet controller
* Headless Service
* PersistentVolumeClaims (PVCs)

### Behavior:

* Pods are created in order (0 → 1 → 2)
* Pods are deleted in reverse order (2 → 1 → 0)
* Each pod gets its own PVC

---

## Persistent Storage

Each pod gets a dedicated volume:

* web-data-web-0
* web-data-web-1
* web-data-web-2

### Key Observation:

Even after pod deletion, data remains intact because PVC is not deleted.

---

## DNS Resolution

Each pod gets a stable DNS name:

```
<pod-name>.<service-name>.<namespace>.svc.cluster.local
```

Example:

```
web-0.nginx-headless.default.svc.cluster.local
```

This resolves to the same pod IP in the cluster.

---

## Scaling Behavior

### Scale Up:

* Pods created sequentially
* web-3 created after web-2 is ready
* web-4 created after web-3 is ready

### Scale Down:

* Pods terminated in reverse order
* web-4 deleted first
* web-3 deleted next

### Important:

PVCs are NOT deleted during scaling.

---

## Data Persistence Test

### Steps Performed:

1. Stored data inside each pod:

   * "Data from web-0"
   * "Data from web-1"
   * "Data from web-2"

2. Deleted web-0 pod

3. Kubernetes recreated the pod

4. Data was still present

### Result:

Data persisted due to PVC reattachment.

---

## Cleanup Behavior

* Deleting StatefulSet does NOT delete PVCs
* PVCs must be manually deleted
* This ensures data safety

---

## Key Learnings

* StatefulSets provide identity + storage consistency
* Headless Services enable per-pod DNS
* PVCs ensure data persistence
* Pods are not interchangeable like Deployments
* Ordered scaling ensures system stability

---

## Conclusion

StatefulSets are essential for running stateful applications in Kubernetes. They ensure that each pod has a stable identity, stable network endpoint, and persistent storage, making them suitable for production-grade databases and distributed systems.
