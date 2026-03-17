# Day 53 – Kubernetes Services

## Overview

On Day 53 of the #90DaysOfDevOps challenge, I explored Kubernetes Services and learned how Kubernetes provides stable networking, service discovery, and load balancing for containerized applications.

Pods are ephemeral resources and their IP addresses can change whenever they are recreated. Kubernetes Services solve this problem by providing a stable network endpoint that routes traffic to healthy Pods behind the scenes.

This lab demonstrates the implementation and testing of:

* ClusterIP Service
* NodePort Service
* LoadBalancer Service
* Kubernetes DNS-based Service Discovery
* Service Endpoints and Load Balancing

---

## Project Structure

```text
day-53/
├── README.md
├── task.md
├── day-53-services.md
│
├── yaml-scripts/
│   ├── app-deployment.yaml
│   ├── clusterip-service.yaml
│   ├── nodeport-service.yaml
│   └── loadbalancer-service.yaml
│
└── screenshots/
```

---

## Objectives

* Deploy an Nginx application using Kubernetes Deployment
* Expose the application using different Service types
* Verify internal Service communication
* Test Kubernetes DNS resolution
* Understand Service Endpoints
* Compare ClusterIP, NodePort, and LoadBalancer Services

---

## Technologies Used

* Kubernetes
* Kind Cluster
* Docker
* Nginx
* BusyBox
* kubectl

---

## Deployment Architecture

```text
                    Client
                       |
                +-------------+
                |  Service    |
                +-------------+
                  /    |    \
                 /     |     \
                /      |      \
          +------+ +------+ +------+
          | Pod1 | | Pod2 | | Pod3 |
          +------+ +------+ +------+
```

The Service provides:

* Stable IP Address
* Stable DNS Name
* Load Balancing
* Service Discovery

---

## Kubernetes Services Implemented

### 1. ClusterIP Service

ClusterIP is the default Service type.

Features:

* Accessible only within the cluster
* Provides stable internal communication
* Used for microservice-to-microservice communication

Verification:

```bash
kubectl get svc
```

Example:

```text
web-app-clusterip   ClusterIP   10.96.7.92
```

---

### 2. NodePort Service

NodePort exposes an application through a port on every Kubernetes node.

Features:

* External access via NodeIP:NodePort
* Useful for testing and development
* Opens a port between 30000–32767

Example:

```text
web-app-nodeport   NodePort   80:30080/TCP
```

Traffic Flow:

```text
Client
   ↓
NodeIP:30080
   ↓
NodePort Service
   ↓
Nginx Pods
```

---

### 3. LoadBalancer Service

LoadBalancer Services expose applications externally through cloud load balancers.

Features:

* Production-ready external access
* Automatically provisions cloud load balancers
* Creates NodePort and ClusterIP internally

Example:

```text
web-app-loadbalancer   LoadBalancer   <pending>
```

Since this lab was performed on a Kind cluster, the external IP remained pending because no cloud provider is available.

---

## DNS-Based Service Discovery

Kubernetes automatically creates DNS records for every Service.

Format:

```text
<service-name>.<namespace>.svc.cluster.local
```

Example:

```text
web-app-clusterip.default.svc.cluster.local
```

Verification:

```bash
nslookup web-app-clusterip
```

Output:

```text
Name: web-app-clusterip.default.svc.cluster.local
Address: 10.96.7.92
```

---

## Service Endpoints

Endpoints represent the Pods currently receiving traffic from a Service.

Check Endpoints:

```bash
kubectl get endpoints web-app-clusterip
```

Output:

```text
10.244.0.11:80
10.244.0.12:80
10.244.0.13:80
```

This confirms that traffic is being distributed across all healthy Pods.

---

## Service Type Comparison

| Service Type | Accessible From | Common Use Case        |
| ------------ | --------------- | ---------------------- |
| ClusterIP    | Inside Cluster  | Internal communication |
| NodePort     | NodeIP:Port     | Development & Testing  |
| LoadBalancer | Public IP       | Production Workloads   |

---

## Key Learnings

* Services provide stable networking for Kubernetes Pods.
* Pod IP addresses are dynamic and should not be used directly.
* ClusterIP enables internal service communication.
* NodePort exposes applications externally through nodes.
* LoadBalancer is designed for cloud-native production environments.
* Kubernetes DNS simplifies service discovery.
* Endpoints reveal which Pods receive traffic.
* Service selectors must match Pod labels correctly.

---

## Commands Used

Deploy Application:

```bash
kubectl apply -f app-deployment.yaml
```

Create Services:

```bash
kubectl apply -f clusterip-service.yaml
kubectl apply -f nodeport-service.yaml
kubectl apply -f loadbalancer-service.yaml
```

View Services:

```bash
kubectl get svc
```

Inspect Endpoints:

```bash
kubectl get endpoints web-app-clusterip
```

DNS Verification:

```bash
nslookup web-app-clusterip
```

Service Details:

```bash
kubectl describe service web-app-loadbalancer
```

---

## Screenshots

Add the following screenshots:

* Deployment Pods Running
* ClusterIP Service Creation
* Service DNS Resolution
* NodePort Service Verification
* LoadBalancer Service Verification
* kubectl get svc Output

---

## Outcome

Successfully deployed an Nginx application and exposed it using ClusterIP, NodePort, and LoadBalancer Services. Verified service discovery through Kubernetes DNS, inspected Service Endpoints, and understood how Kubernetes Services provide stable networking and load balancing for applications running in a cluster.

---

### #90DaysOfDevOps #Kubernetes #DevOps #CloudComputing #TrainWithShubham
