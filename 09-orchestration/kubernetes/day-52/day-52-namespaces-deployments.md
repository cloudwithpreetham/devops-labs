# Day 52 – Kubernetes Namespaces and Deployments

## Objective

Learn how Kubernetes Namespaces help organize cluster resources and how Deployments provide self-healing, scaling, rolling updates, and rollbacks for applications.

---

# What are Kubernetes Namespaces?

Namespaces are a way to logically separate resources within the same Kubernetes cluster.

They are commonly used to:

- Separate Development, Staging, and Production environments
- Isolate resources between teams
- Avoid naming conflicts
- Apply resource quotas and access controls

## Default Namespaces

Kubernetes provides several built-in namespaces:

| Namespace       | Purpose                             |
| --------------- | ----------------------------------- |
| default         | Default namespace for resources     |
| kube-system     | Kubernetes control plane components |
| kube-public     | Public cluster information          |
| kube-node-lease | Node heartbeat tracking             |

### Verify Default Namespaces

```bash
kubectl get namespaces
```

### Check System Components

```bash
kubectl get pods -n kube-system
```

Result:

- Total Pods running in `kube-system`: **8**

---

# Creating Custom Namespaces

Created three namespaces:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev
```

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: staging
```

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
```

Apply namespaces:

```bash
kubectl apply -f dev-namespace.yaml
kubectl apply -f staging-namespace.yaml
kubectl apply -f production-namespace.yaml
```

Verify:

```bash
kubectl get namespaces
```

---

# Running Pods in Different Namespaces

Created Nginx Pods inside custom namespaces.

```bash
kubectl run nginx-dev --image=nginx:latest -n dev
kubectl run nginx-staging --image=nginx:latest -n staging
```

Check pods in default namespace:

```bash
kubectl get pods
```

Output:

```text
No resources found in default namespace.
```

View pods across all namespaces:

```bash
kubectl get pods -A
```

This displays resources from all namespaces including:

- dev
- staging
- kube-system
- local-path-storage

---

# Kubernetes Deployment

A Deployment manages application Pods and ensures the desired number of replicas remain available.

Benefits:

- Self-healing
- Scaling
- Rolling updates
- Rollbacks

---

# Deployment Manifest

File: `nginx-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: dev
  labels:
    app: nginx

spec:
  replicas: 3

  selector:
    matchLabels:
      app: nginx

  template:
    metadata:
      labels:
        app: nginx

    spec:
      containers:
        - name: nginx
          image: nginx:1.24
          ports:
            - containerPort: 80
```

Deploy:

```bash
kubectl apply -f nginx-deployment.yaml
```

Verify:

```bash
kubectl get deployments -n dev
kubectl get pods -n dev
```

---

# Deployment Components Explained

## replicas

```yaml
replicas: 3
```

Maintains three identical Pods.

---

## selector

```yaml
selector:
  matchLabels:
    app: nginx
```

Used by the Deployment to identify Pods it manages.

---

## template

```yaml
template:
```

Acts as a blueprint for creating Pods.

---

## container image

```yaml
image: nginx:1.24
```

Specifies which container image Kubernetes should run.

---

# Understanding Deployment Status

Command:

```bash
kubectl get deployments -n dev
```

Output:

```text
READY   UP-TO-DATE   AVAILABLE
3/3     3            3
```

## READY

Number of ready Pods versus desired Pods.

## UP-TO-DATE

Pods using the latest Deployment specification.

## AVAILABLE

Pods currently available to serve traffic.

---

# Self-Healing Demonstration

List Pods:

```bash
kubectl get pods -n dev
```

Delete a Deployment-managed Pod:

```bash
kubectl delete pod nginx-deployment-68cd4c497b-v5xkn -n dev
```

Check again:

```bash
kubectl get pods -n dev
```

Observation:

- Deleted Pod was removed.
- Kubernetes automatically created a replacement Pod.
- Replacement Pod received a new name.

Example:

Deleted:

```text
nginx-deployment-68cd4c497b-v5xkn
```

Created:

```text
nginx-deployment-68cd4c497b-phcdr
```

This demonstrates Deployment self-healing.

---

# Scaling Deployments

## Scale Up

Increase replicas from 3 to 5.

```bash
kubectl scale deployment nginx-deployment --replicas=5 -n dev
```

Verify:

```bash
kubectl get pods -n dev
```

Result:

- Kubernetes created two additional Pods.

---

## Scale Down

Reduce replicas from 5 to 2.

```bash
kubectl scale deployment nginx-deployment --replicas=2 -n dev
```

Result:

- Extra Pods were automatically terminated.
- Desired state of 2 replicas maintained.

---

# Declarative Scaling

Updated Deployment manifest:

```yaml
replicas: 4
```

Apply changes:

```bash
kubectl apply -f nginx-deployment.yaml
```

Verify:

```bash
kubectl get pods -n dev
```

Result:

- Kubernetes created additional Pods to reach 4 replicas.

---

# Rolling Updates

Update container image:

```bash
kubectl set image deployment/nginx-deployment nginx=nginx:1.25 -n dev
```

Monitor rollout:

```bash
kubectl rollout status deployment/nginx-deployment -n dev
```

Result:

```text
deployment "nginx-deployment" successfully rolled out
```

Kubernetes replaced Pods gradually without downtime.

---

# Rollout History

View Deployment revisions:

```bash
kubectl rollout history deployment/nginx-deployment -n dev
```

Output:

```text
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

---

# Rollback Deployment

Rollback to previous version:

```bash
kubectl rollout undo deployment/nginx-deployment -n dev
```

Verify rollout:

```bash
kubectl rollout status deployment/nginx-deployment -n dev
```

Check image:

```bash
kubectl describe deployment nginx-deployment -n dev | grep Image
```

Output:

```text
Image: nginx:1.24
```

Rollback successfully restored the previous image version.

---

# Deployment vs Standalone Pod

| Feature          | Standalone Pod | Deployment |
| ---------------- | -------------- | ---------- |
| Self-Healing     | No             | Yes        |
| Scaling          | Manual         | Automatic  |
| Rolling Updates  | No             | Yes        |
| Rollback         | No             | Yes        |
| Production Ready | No             | Yes        |

---

# Screenshots

Included screenshots:

1. 01-namespaces-created.png
2. 02-kube-system-pods.png
3. 03-pods-all-namespaces.png
4. 04-deployment-running.png
5. 05-dev-pods-running.png
6. 06-scaled-deployment.png
7. 07-rollout-history.png

---

# Key Learnings

- Namespaces organize Kubernetes resources.
- Custom namespaces help separate environments.
- Deployments manage Pods automatically.
- Deployments provide self-healing capabilities.
- Scaling can be performed imperatively or declaratively.
- Rolling updates enable zero-downtime upgrades.
- Rollbacks allow quick recovery from failed deployments.
- Deployments are the preferred way to run applications in Kubernetes.

---

# Conclusion

Today I learned how to use Kubernetes Namespaces and Deployments to manage applications more effectively. I created isolated environments, deployed an Nginx application with multiple replicas, tested self-healing behavior, scaled workloads, performed rolling updates, and rolled back to a previous version. These are fundamental Kubernetes concepts used in real-world DevOps and production environments.
