# Day 56 – Kubernetes StatefulSets

## Project Overview

This project demonstrates Kubernetes StatefulSets and how they differ from Deployments. It focuses on running stateful applications with stable pod identities, ordered deployment, persistent storage, and DNS resolution.

---

## Objectives

By completing this lab, I learned how to:

* Understand limitations of Kubernetes Deployments for stateful apps
* Create and use Headless Services
* Deploy StatefulSets with ordered pod creation
* Attach persistent storage using PVCs
* Validate stable DNS per pod
* Test data persistence across pod restarts and deletion
* Understand scaling behavior in StatefulSets

---

## Architecture

This setup includes:

* 1 StatefulSet with 3–5 replicas
* 1 Headless Service (clusterIP: None)
* PersistentVolumeClaims per pod
* BusyBox pod for DNS testing

---

## Key Components

### StatefulSet

* Provides stable pod names: `web-0`, `web-1`, `web-2`
* Ensures ordered deployment and scaling
* Maintains persistent identity for each pod

### Headless Service

* Provides stable DNS entries per pod
* Does not load balance traffic
* Required for StatefulSet networking

### Persistent Storage (PVC)

* Each pod gets its own dedicated storage
* Data persists even after pod deletion
* PVCs remain after StatefulSet deletion

---

## Kubernetes Manifests

### Deployment (Comparison Only)

Used to demonstrate random pod naming behavior.

### Headless Service

```yaml
clusterIP: None
```

### StatefulSet

* serviceName: nginx-headless
* replicas: 3
* volumeClaimTemplates used for persistent storage

---

## Key Commands Used

```bash
kubectl apply -f nginx-deployment.yaml
kubectl apply -f headless-service.yaml
kubectl apply -f statefulset.yaml

kubectl get pods -o wide
kubectl get svc
kubectl get pvc

kubectl scale statefulset web --replicas=5
kubectl delete pod web-0
```

---

## Observations

### Deployment vs StatefulSet

* Deployment pods have random names
* StatefulSet pods have stable names (web-0, web-1, web-2)

### DNS Resolution

Each pod has a stable DNS name:

```
web-0.nginx-headless.default.svc.cluster.local
```

### Storage Persistence

* Data remains intact even after pod deletion
* PVCs are not deleted automatically

### Scaling Behavior

* Scale up: ordered creation (0 → 1 → 2 → ...)
* Scale down: reverse termination (n → n-1 → ...)

---

## Results

* StatefulSet created successfully
* Headless service enabled stable DNS
* PVCs created per pod
* Data persisted after pod recreation
* Scaling behavior validated

---

## Key Learnings

* StatefulSets are required for stateful applications
* Stable identity is critical for databases and distributed systems
* Kubernetes separates compute (pods) from storage (PVCs)
* Headless Services enable direct pod addressing
* PVC lifecycle is independent of pods

---

## Conclusion

This lab demonstrated how Kubernetes handles stateful workloads using StatefulSets. It is essential for running production-grade systems like databases, message queues, and distributed storage systems where identity and persistence matter.
