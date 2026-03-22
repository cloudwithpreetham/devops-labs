# Day 58 - Metrics Server and Horizontal Pod Autoscaler (HPA)

## Overview

On Day 58 of the #90DaysOfDevOps journey, I installed the Kubernetes Metrics Server and implemented Horizontal Pod Autoscaling (HPA) to automatically scale workloads based on CPU utilization.

This lab demonstrated how Kubernetes monitors resource consumption and dynamically adjusts application replicas to handle varying workloads.

---

## Objectives

- Install and configure Metrics Server
- Monitor cluster resource usage using `kubectl top`
- Deploy an application with CPU requests
- Create an HPA using imperative commands
- Generate load and observe automatic scaling
- Configure a declarative HPA using `autoscaling/v2`
- Understand scaling behavior and stabilization windows
- Clean up resources after testing

---

## Project Structure

```text
day-58/
├── README.md
├── task.md
├── day-58-metrics-hpa.md
│
├── yaml-scripts/
│   ├── php-apache-deployment.yaml
│   └── php-apache-hpa.yaml
│
└── screenshots/
```

---

## Metrics Server Installation

Verify Metrics Server:

```bash
kubectl get pods -n kube-system | grep metrics-server
```

Install Metrics Server:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

For local lab environments, enable insecure TLS:

```yaml
- --kubelet-insecure-tls
```

Verify rollout:

```bash
kubectl rollout status deployment metrics-server -n kube-system
```

---

## Viewing Cluster Resource Usage

Node Metrics:

```bash
kubectl top nodes
```

Pod Metrics:

```bash
kubectl top pods -A
```

Sort by CPU:

```bash
kubectl top pods -A --sort-by=cpu
```

Sort by Memory:

```bash
kubectl top pods -A --sort-by=memory
```

---

## Deploying the HPA Example Application

Apply Deployment:

```bash
kubectl apply -f yaml-scripts/php-apache-deployment.yaml
```

Deployment includes CPU requests required by HPA:

```yaml
resources:
  requests:
    cpu: 200m
```

Expose the application:

```bash
kubectl expose deployment php-apache --port=80
```

Verify:

```bash
kubectl get pods
kubectl get svc
```

---

## Creating HPA Imperatively

Create the Horizontal Pod Autoscaler:

```bash
kubectl autoscale deployment php-apache \
  --cpu-percent=50 \
  --min=1 \
  --max=10
```

Verify:

```bash
kubectl get hpa
kubectl describe hpa php-apache
```

Target CPU utilization:

```text
50%
```

---

## Load Testing and Autoscaling

Generate continuous load:

```bash
kubectl run load-generator \
  --image=busybox:1.36 \
  --restart=Never \
  -- /bin/sh -c "while true; do wget -q -O- http://php-apache; done"
```

Watch HPA:

```bash
kubectl get hpa php-apache --watch
```

Watch Deployment scaling:

```bash
kubectl get deployment php-apache -w
```

Observed scaling:

```text
1 → 3 → 6 → 10 replicas
```

HPA successfully increased pod replicas when CPU utilization exceeded the configured threshold.

---

## Declarative HPA using autoscaling/v2

Apply HPA manifest:

```bash
kubectl apply -f yaml-scripts/php-apache-hpa.yaml
```

Example configuration:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  minReplicas: 1
  maxReplicas: 10
```

---

## HPA Behavior Configuration

### Scale Up

```yaml
scaleUp:
  stabilizationWindowSeconds: 0
```

- Immediate scaling response
- No stabilization delay

### Scale Down

```yaml
scaleDown:
  stabilizationWindowSeconds: 300
```

- Waits 5 minutes before reducing replicas
- Prevents unnecessary scaling fluctuations

---

## How HPA Calculates Replicas

Formula:

```text
desiredReplicas =
ceil(currentReplicas × currentUsage / targetUsage)
```

Example:

```text
Current Replicas = 3
Current CPU Usage = 100%
Target CPU Usage = 50%

Desired Replicas = 6
```

---

## autoscaling/v1 vs autoscaling/v2

| Feature                | autoscaling/v1 | autoscaling/v2 |
| ---------------------- | -------------- | -------------- |
| CPU Metrics            | Yes            | Yes            |
| Memory Metrics         | No             | Yes            |
| Custom Metrics         | No             | Yes            |
| External Metrics       | No             | Yes            |
| Scaling Policies       | No             | Yes            |
| Behavior Configuration | No             | Yes            |

---

## Cleanup

Delete created resources:

```bash
kubectl delete hpa php-apache
kubectl delete svc php-apache
kubectl delete deployment php-apache
kubectl delete pod load-generator --ignore-not-found
```

Metrics Server remains installed for future monitoring and autoscaling exercises.

---

## Screenshots

Store all screenshots in the `screenshots/` directory.

Suggested screenshots:

- Metrics Server running
- `kubectl top nodes`
- `kubectl top pods -A`
- CPU-sorted pod metrics
- HPA creation
- HPA details
- Load generator running
- Deployment scaling events
- Multiple replicas running
- Declarative HPA verification
- Cleanup verification

---

## Key Learnings

- Metrics Server provides cluster resource metrics.
- `kubectl top` displays real-time CPU and memory usage.
- HPA requires resource requests to calculate utilization percentages.
- Kubernetes can automatically scale workloads based on demand.
- Scale-up operations are fast, while scale-down operations are intentionally delayed.
- `autoscaling/v2` provides advanced scaling controls suitable for production environments.
- Autoscaling improves application availability and resource efficiency.

---

## Commands Used

```bash
kubectl top nodes
kubectl top pods -A

kubectl apply -f php-apache-deployment.yaml
kubectl expose deployment php-apache --port=80

kubectl autoscale deployment php-apache \
  --cpu-percent=50 \
  --min=1 \
  --max=10

kubectl get hpa
kubectl describe hpa php-apache

kubectl run load-generator \
  --image=busybox:1.36 \
  --restart=Never \
  -- /bin/sh -c "while true; do wget -q -O- http://php-apache; done"

kubectl delete hpa php-apache
kubectl delete svc php-apache
kubectl delete deployment php-apache
```

---

## Outcome

Successfully installed Metrics Server, monitored real-time resource consumption, implemented Horizontal Pod Autoscaling, generated workload traffic, observed automatic scaling from 1 to 10 replicas, and configured advanced scaling policies using the `autoscaling/v2` API.
