# Day 55 – Kubernetes Persistent Volumes (PV) and Persistent Volume Claims (PVC)

## Objective

Containers are ephemeral by nature. When a Pod is deleted or recreated, any data stored inside the container filesystem is lost. This behavior is acceptable for stateless applications but becomes a major challenge for stateful workloads such as databases, logging systems, and applications that require persistent storage.

The objective of this lab was to understand Kubernetes persistent storage concepts using Persistent Volumes (PV), Persistent Volume Claims (PVC), and StorageClasses.

---

# Why Containers Need Persistent Storage

By default, container storage is temporary.

When a Pod is:

- Deleted
- Rescheduled
- Recreated
- Crashed and restarted

all data stored inside the container filesystem is lost.

Examples of workloads requiring persistent storage:

- MySQL
- PostgreSQL
- MongoDB
- Elasticsearch
- Jenkins
- Prometheus

To solve this problem, Kubernetes provides Persistent Volumes and Persistent Volume Claims.

---

# Understanding Persistent Volumes (PV)

A Persistent Volume (PV) is a cluster-wide storage resource managed by Kubernetes.

It abstracts the underlying storage implementation and provides storage to applications.

Characteristics:

- Cluster-scoped resource
- Created by administrators or dynamically provisioned
- Independent of Pods
- Can outlive Pod lifecycle

Example PV attributes:

- Capacity
- Access Modes
- Reclaim Policy
- Storage Backend

In this lab, a static PV was created using:

```yaml
hostPath: /tmp/k8s-pv-data
```

---

# Understanding Persistent Volume Claims (PVC)

A Persistent Volume Claim (PVC) is a request for storage made by a user or application.

A PVC specifies:

- Required storage size
- Access mode
- Storage class (optional)

Kubernetes automatically binds a suitable PV to the PVC if matching resources are available.

Relationship:

```text
Pod --> PVC --> PV --> Physical Storage
```

---

# Static Provisioning

Static provisioning requires an administrator to manually create a PV before developers create PVCs.

### Static PV Configuration

```yaml
capacity:
  storage: 1Gi

accessModes:
  - ReadWriteOnce

persistentVolumeReclaimPolicy: Retain
```

### Verification

```bash
kubectl get pv
```

Output:

```text
demo-pv   Available
```

After PVC creation:

```text
demo-pv   Bound
demo-pvc  Bound
```

---

# Demonstrating Ephemeral Storage

An `emptyDir` volume was used to demonstrate temporary storage.

### First Pod

```text
Created at Wed Jun 10 10:45:32 UTC 2026
```

### After Pod Recreation

```text
Created at Wed Jun 10 10:47:16 UTC 2026
```

Observation:

The timestamp changed because the data stored in the `emptyDir` volume was deleted when the Pod was recreated.

Conclusion:

`emptyDir` provides temporary storage only.

---

# Using PVC in a Pod

A Pod was created using the PVC and mounted at:

```text
/data
```

### First Pod Write

```text
First Pod Entry
```

Pod was deleted and recreated.

### Second Pod Write

```text
Second Pod Entry
```

### Verification

```text
First Pod Entry
Second Pod Entry
```

Result:

The file persisted across Pod deletion because the data was stored on the Persistent Volume instead of the container filesystem.

---

# Access Modes

Kubernetes supports multiple storage access modes.

## ReadWriteOnce (RWO)

```text
Read-write by a single node
```

Most commonly used access mode.

---

## ReadOnlyMany (ROX)

```text
Read-only by multiple nodes
```

Useful for shared content.

---

## ReadWriteMany (RWX)

```text
Read-write by multiple nodes
```

Used for shared storage solutions such as NFS.

---

# Reclaim Policies

Reclaim policies determine what happens to storage after a PVC is deleted.

## Retain

```text
Data is preserved.
PV moves to Released state.
Administrator cleanup required.
```

Used in this lab:

```yaml
persistentVolumeReclaimPolicy: Retain
```

Result:

```text
demo-pv -> Released
```

---

## Delete

```text
Storage and PV are automatically removed.
```

Used by the default StorageClass.

Result:

```text
Dynamic PV deleted automatically.
```

---

# StorageClass

StorageClasses automate storage provisioning.

Cluster Information:

```text
Name: standard
Provisioner: rancher.io/local-path
Reclaim Policy: Delete
Volume Binding Mode: WaitForFirstConsumer
```

Benefits:

- Developers create only PVCs
- Kubernetes automatically creates PVs
- Reduces administrative overhead
- Simplifies storage management

---

# Dynamic Provisioning

Dynamic provisioning automatically creates a PV when a PVC requests storage.

PVC Configuration:

```yaml
storageClassName: standard
```

Initially:

```text
dynamic-pvc -> Pending
```

After a Pod consumed the PVC:

```text
dynamic-pvc -> Bound
```

Automatically created PV:

```text
pvc-2911fb77-2d67-4c5d-8dd1-8169202d140d
```

Verification:

```text
Dynamic Provisioning Works
```

---

# PV Lifecycle

Persistent Volumes transition through several states.

```text
Available
    ↓
Bound
    ↓
Released
```

Observed in this lab:

```text
demo-pv
Available → Bound → Released
```

---

# Challenges Faced

### PVC Remained Pending

Problem:

```text
PVC used StorageClass "standard"
PV had no StorageClass
```

Resolution:

```yaml
storageClassName: ""
```

Result:

```text
PVC successfully bound to demo-pv
```

This highlighted the importance of matching StorageClass configuration between PVs and PVCs.

---

# Key Learnings

- Container storage is ephemeral.
- `emptyDir` data is lost when Pods are recreated.
- Persistent Volumes provide durable storage.
- PVCs abstract storage requests from applications.
- PVs and PVCs bind based on capacity and access modes.
- StorageClasses enable dynamic provisioning.
- Reclaim policies determine storage cleanup behavior.
- Dynamic provisioning simplifies storage management.
- Persistent storage is essential for stateful applications.

---

# Conclusion

In this lab, I successfully demonstrated the limitations of ephemeral container storage and implemented persistent storage using Kubernetes Persistent Volumes and Persistent Volume Claims. I explored both static and dynamic provisioning models, verified data persistence across Pod recreation, and learned how StorageClasses automate storage provisioning in Kubernetes clusters.
