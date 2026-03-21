# Day 57 - Resource Requests, Limits, and Probes

## Overview

On Day 57 of the #90DaysOfDevOps journey, I explored how Kubernetes manages resource allocation and workload health. I configured CPU and memory requests and limits, observed container termination due to memory exhaustion, investigated scheduler behavior when resources are unavailable, and implemented liveness, readiness, and startup probes for self-healing applications.

---

## Objectives

- Configure CPU and memory requests and limits
- Understand Kubernetes QoS Classes
- Observe OOMKilled behavior when memory limits are exceeded
- Analyze Pending Pods caused by insufficient cluster resources
- Implement and test liveness probes
- Implement and test readiness probes
- Implement and test startup probes
- Understand how Kubernetes automatically manages application health

---

## Project Structure

```text
day-57/
├── README.md
├── task.md
├── day-57-resources-probes.md
│
├── yaml-scripts/
│   ├── resource-limits-pod.yaml
│   ├── oomkill-pod.yaml
│   ├── high-request-pod.yaml
│   ├── liveness-pod.yaml
│   ├── readiness-pod.yaml
│   └── startup-pod.yaml
│
└── screenshots/
```

---

# Lab 1: Resource Requests and Limits

Configured resource requests and limits for a Pod.

### Requests

```yaml
requests:
  cpu: "100m"
  memory: "128Mi"
```

### Limits

```yaml
limits:
  cpu: "250m"
  memory: "256Mi"
```

### Verification

```bash
kubectl describe pod resource-demo
```

Observed:

```text
QoS Class: Burstable
```

### Learning

- Requests determine scheduling decisions.
- Limits restrict runtime resource consumption.
- Different requests and limits result in the Burstable QoS class.

![Resource demo pod running](screenshots/01-resource-pod-running.png)

![Resource demo QoS class](screenshots/02-resource-pod-describe-qos.png)

---

# Lab 2: OOMKilled Demonstration

Created a stress container that attempted to consume more memory than its configured limit.

### Memory Limit

```yaml
limits:
  memory: "100Mi"
```

### Stress Test

```yaml
args:
  - "--vm"
  - "1"
  - "--vm-bytes"
  - "200M"
```

### Verification

```bash
kubectl describe pod oom-demo
```

Observed:

```text
Reason: OOMKilled
Exit Code: 137
```

### Learning

- CPU overuse causes throttling.
- Memory overuse results in container termination.
- Exit code 137 indicates an OOMKilled container.

![OOMKilled pod status](screenshots/03-oomkilled-status.png)

![OOMKilled describe output](screenshots/04-oomkilled-describe.png)

---

# Lab 3: Pending Pod Due to Excessive Requests

Created a Pod requesting more resources than available in the cluster.

### Resource Requests

```yaml
requests:
  cpu: "100"
  memory: "128Gi"
```

### Verification

```bash
kubectl describe pod huge-request
```

Observed:

```text
FailedScheduling:
0/1 nodes are available:
1 Insufficient cpu,
1 Insufficient memory.
```

### Learning

The Kubernetes scheduler prevents Pods from running when resource requirements cannot be satisfied.

![Pending pod with excessive requests](screenshots/05-pending-pod.png)

![Scheduler insufficient resources event](screenshots/06-scheduler-insufficient-resources.png)

---

# Lab 4: Liveness Probe

Implemented a liveness probe that checks for the existence of a file.

### Probe Configuration

```yaml
livenessProbe:
  exec:
    command:
      - cat
      - /tmp/healthy
  periodSeconds: 5
  failureThreshold: 3
```

### Verification

Observed:

```text
Liveness probe failed
Container liveness failed liveness probe
Container restarted
```

### Learning

Liveness probes detect unhealthy containers and automatically restart them.

![Liveness demo pod running](screenshots/07-liveness-pod-running.png)

![Liveness probe failed event](screenshots/08-liveness-probe-failed.png)

![Liveness container restarted](screenshots/09-liveness-container-restarted.png)

---

# Lab 5: Readiness Probe

Configured an HTTP readiness probe for an NGINX Pod.

### Probe Configuration

```yaml
readinessProbe:
  httpGet:
    path: /
    port: 80
```

### Verification

Before failure:

```text
10.244.x.x:80
```

After deleting the homepage:

```text
READY: 0/1
Endpoints: <none>
Restart Count: 0
```

### Learning

Readiness probes control traffic routing but do not restart containers.

![Readiness endpoint present](screenshots/10-readiness-endpoints-present.png)

![Readiness endpoint removed](screenshots/11-readiness-endpoints-removed.png)

---

# Lab 6: Startup Probe

Configured a startup probe for a slow-starting application.

### Probe Configuration

```yaml
startupProbe:
  exec:
    command:
      - cat
      - /tmp/started
  periodSeconds: 5
  failureThreshold: 12
```

### Verification

```text
READY: 1/1
STATUS: Running
RESTARTS: 0
```

### Learning

Startup probes allow applications sufficient initialization time before health checks begin.

![Startup probe success](screenshots/12-startup-probe-success.png)

---

# Kubernetes QoS Classes

| QoS Class  | Condition             |
| ---------- | --------------------- |
| Guaranteed | Requests = Limits     |
| Burstable  | Requests < Limits     |
| BestEffort | No Requests or Limits |

### Observed

| Pod           | QoS Class  |
| ------------- | ---------- |
| resource-demo | Burstable  |
| oom-demo      | Burstable  |
| liveness-demo | BestEffort |

---

# Probe Comparison

| Probe Type | Purpose                     | Failure Action    |
| ---------- | --------------------------- | ----------------- |
| Liveness   | Detect unhealthy containers | Restart container |
| Readiness  | Control Service traffic     | Remove endpoint   |
| Startup    | Protect slow startups       | Restart container |

---

# Key Commands Used

```bash
kubectl apply -f <file>

kubectl get pods

kubectl describe pod <pod-name>

kubectl get endpoints

kubectl expose pod <pod-name> --port=80 --name=<service-name>

kubectl exec <pod-name> -- <command>

kubectl delete pod <pod-name>
```

---

# Cleanup Verification

![Cleanup verification](screenshots/13-cleanup-verification.png)

---

# Key Takeaways

- Requests help Kubernetes schedule workloads.
- Limits enforce resource consumption boundaries.
- Exceeding memory limits causes OOMKilled events.
- Excessive requests prevent scheduling.
- Liveness probes provide self-healing.
- Readiness probes manage traffic flow.
- Startup probes protect slow-starting applications.
- Proper resource management and health checks improve application reliability and cluster stability.

---

## Conclusion

Day 57 focused on resource management and application health monitoring in Kubernetes. Through practical labs, I learned how Kubernetes schedules workloads, enforces resource constraints, handles failures, and maintains application availability using liveness, readiness, and startup probes.
