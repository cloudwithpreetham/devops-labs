# Day 55 – Kubernetes Persistent Volumes (PV) and Persistent Volume Claims (PVC)

## Overview

On Day 55 of my #90DaysOfDevOps journey, I explored Kubernetes persistent storage concepts using Persistent Volumes (PV), Persistent Volume Claims (PVC), and StorageClasses.

I demonstrated the problem of ephemeral storage using `emptyDir`, implemented static and dynamic storage provisioning, verified data persistence across Pod recreation, and explored reclaim policies and volume lifecycle management.

---

# Situation

Containers are designed to be ephemeral. Any data stored inside a container is lost when the Pod is deleted or recreated.

This becomes a major challenge for stateful applications such as:

- Databases
- Monitoring systems
- Logging platforms
- CI/CD tools
- Content management systems

To solve this challenge, Kubernetes provides Persistent Volumes and Persistent Volume Claims.

---

# Task

The objectives of this lab were to:

- Demonstrate data loss using ephemeral storage
- Create a Persistent Volume (PV)
- Create a Persistent Volume Claim (PVC)
- Bind PVs and PVCs successfully
- Persist data across Pod recreation
- Explore StorageClasses
- Implement dynamic provisioning
- Understand reclaim policies and volume lifecycle

---

# Action

## 1. Demonstrated Ephemeral Storage

Created a Pod using an `emptyDir` volume and stored a timestamped message.

Verified:

```text
Created at Wed Jun 10 10:45:32 UTC 2026
```

Deleted and recreated the Pod.

Verified:

```text
Created at Wed Jun 10 10:47:16 UTC 2026
```

Observation:

The timestamp changed because `emptyDir` storage is deleted when the Pod is recreated.

---

## 2. Created a Static Persistent Volume

Created a Persistent Volume using:

```yaml
hostPath: /tmp/k8s-pv-data
```

Configuration:

```yaml
capacity:
  storage: 1Gi

accessModes:
  - ReadWriteOnce

persistentVolumeReclaimPolicy: Retain
```

Verified:

```text
demo-pv   Available
```

---

## 3. Created and Bound a PVC

Created a Persistent Volume Claim requesting:

```yaml
storage: 500Mi
```

Initially encountered a binding issue because:

```text
PVC StorageClass = standard
PV StorageClass = none
```

Resolved by disabling StorageClass matching:

```yaml
storageClassName: ""
```

Verified:

```text
demo-pvc   Bound
demo-pv    Bound
```

---

## 4. Persisted Data Across Pod Recreation

Mounted the PVC inside a Pod.

First write:

```text
First Pod Entry
```

Deleted and recreated the Pod.

Second write:

```text
Second Pod Entry
```

Verification:

```text
First Pod Entry
Second Pod Entry
```

Result:

Data remained available after Pod recreation.

---

## 5. Explored StorageClasses

Cluster StorageClass:

```text
Name: standard
Provisioner: rancher.io/local-path
Reclaim Policy: Delete
Volume Binding Mode: WaitForFirstConsumer
```

Learned how StorageClasses automate volume provisioning and simplify storage management.

---

## 6. Implemented Dynamic Provisioning

Created a PVC using:

```yaml
storageClassName: standard
```

Initially:

```text
dynamic-pvc   Pending
```

After creating a consuming Pod:

```text
dynamic-pvc   Bound
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

## 7. Verified Reclaim Policies

Deleted Pods and PVCs.

Observed:

### Static PV

```text
demo-pv   Released
```

Reason:

```text
Reclaim Policy = Retain
```

### Dynamic PV

Automatically removed.

Reason:

```text
Reclaim Policy = Delete
```

---

# Result

Successfully:

- Demonstrated ephemeral storage limitations
- Created and managed Persistent Volumes
- Created and bound Persistent Volume Claims
- Persisted application data across Pod recreation
- Explored StorageClass configuration
- Implemented dynamic provisioning
- Verified reclaim policy behavior
- Understood PV lifecycle management

---

# Verification Results

## Task 1

```text
Timestamp changed after Pod recreation
```

## Task 2

```text
PV Status = Available
```

## Task 3

```text
PVC Status = Bound
PV Status = Bound
```

## Task 4

```text
First Pod Entry
Second Pod Entry
```

## Task 5

```text
Default StorageClass = standard
```

## Task 6

```text
Dynamic PV created automatically
```

## Task 7

```text
Static PV retained
Dynamic PV deleted
```

---

# Key Concepts Learned

## Persistent Volume (PV)

A cluster-wide storage resource that exists independently of Pods.

## Persistent Volume Claim (PVC)

A request for storage made by an application.

## StorageClass

Defines how storage should be provisioned dynamically.

## Access Modes

- ReadWriteOnce (RWO)
- ReadOnlyMany (ROX)
- ReadWriteMany (RWX)

## Reclaim Policies

### Retain

```text
Keep storage after PVC deletion
```

### Delete

```text
Delete storage automatically
```

---

# Commands Used

```bash
kubectl apply -f <file>

kubectl get pv

kubectl get pvc

kubectl get storageclass

kubectl describe storageclass standard

kubectl exec -it <pod> -- sh

kubectl delete pod <pod-name>

kubectl delete pvc <pvc-name>
```

---

# Project Structure

```text
day-55/
├── README.md
├── task.md
├── day-55-persistent-volumes.md
│
├── yaml-scripts/
│   ├── emptydir-pod.yaml
│   ├── persistent-volume.yaml
│   ├── persistent-volume-claim.yaml
│   ├── pvc-demo-pod.yaml
│   ├── dynamic-pvc.yaml
│   └── dynamic-pvc-pod.yaml
│
└── screenshots/
```

---

# Key Takeaways

- Container storage is temporary by default.
- Persistent Volumes provide durable storage for stateful workloads.
- PVCs abstract storage consumption from applications.
- StorageClasses automate volume creation.
- Dynamic provisioning reduces manual storage management.
- Reclaim policies control storage cleanup behavior.
- Understanding Kubernetes storage is essential for running production-grade applications.

---

**#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham #Kubernetes #PersistentVolumes #PVC #StorageClass #CloudNative**
