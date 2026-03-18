# Day 54 – Kubernetes ConfigMaps and Secrets

## Overview

On Day 54 of my #90DaysOfDevOps journey, I learned how Kubernetes manages application configuration and sensitive information using **ConfigMaps** and **Secrets**.

In real-world environments, application settings such as environment variables, feature flags, and service endpoints should not be hardcoded into container images. Kubernetes provides ConfigMaps for non-sensitive data and Secrets for sensitive information like passwords and API keys.

This lab focused on creating, consuming, and updating ConfigMaps and Secrets using environment variables and volume mounts.

---

## Objectives

- Create ConfigMaps from literals
- Create ConfigMaps from configuration files
- Inject ConfigMaps into Pods using environment variables
- Mount ConfigMaps as volumes
- Create and manage Kubernetes Secrets
- Consume Secrets using environment variables and volume mounts
- Understand Base64 encoding and its limitations
- Observe ConfigMap update propagation behavior
- Clean up Kubernetes resources

---

## Project Structure

```text
day-54/
├── README.md
├── task.md
├── day-54-configmaps-secrets.md
│
├── yaml-scripts/
│   ├── default.conf
│   ├── configmap-env-pod.yaml
│   ├── nginx-config-pod.yaml
│   ├── secret-pod.yaml
│   └── live-config-pod.yaml
│
└── screenshots/
```

---

## Tasks Completed

### Task 1 – Create ConfigMap from Literals

Created a ConfigMap named `app-config` using command-line literals.

```bash
kubectl create configmap app-config \
--from-literal=APP_ENV=production \
--from-literal=APP_DEBUG=false \
--from-literal=APP_PORT=8080
```

Verified the configuration using:

```bash
kubectl describe configmap app-config
kubectl get configmap app-config -o yaml
```

---

### Task 2 – Create ConfigMap from File

Created a custom Nginx configuration file and stored it inside a ConfigMap.

```bash
kubectl create configmap nginx-config \
--from-file=default.conf=yaml-scripts/default.conf
```

Verified the file contents were stored successfully.

---

### Task 3 – Consume ConfigMaps in Pods

#### Environment Variables

Injected all ConfigMap values into a BusyBox Pod using:

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

Verified the variables inside the container.

#### Volume Mount

Mounted the Nginx ConfigMap as a volume and confirmed the custom `/health` endpoint worked successfully.

```bash
curl localhost/health
```

Output:

```text
healthy
```

---

### Task 4 – Create a Secret

Created a Secret containing database credentials.

```bash
kubectl create secret generic db-credentials \
--from-literal=DB_USER=admin \
--from-literal=DB_PASSWORD='s3cureP@ssw0rd'
```

Verified the Secret data was Base64 encoded.

---

### Task 5 – Consume Secrets in Pods

Used:

- `secretKeyRef` for environment variables
- Secret volume mounts for file-based access

Verified:

```bash
kubectl exec secret-pod -- printenv DB_USER
```

Output:

```text
admin
```

Verified mounted Secret files contained decoded plaintext values.

---

### Task 6 – ConfigMap Update Propagation

Created a ConfigMap named `live-config`.

Mounted it into a running Pod and continuously read the configuration.

Updated the ConfigMap using:

```bash
kubectl patch configmap live-config \
--type merge \
-p '{"data":{"message":"world"}}'
```

Learned that:

- Volume-mounted ConfigMaps automatically refresh
- Environment variables do not refresh automatically
- Pod restart is required for updated environment variables

---

### Task 7 – Cleanup

Deleted all resources created during the lab.

```bash
kubectl delete pods
kubectl delete configmaps
kubectl delete secrets
```

Verified a clean cluster state after completion.

---

## Key Concepts Learned

### ConfigMaps

Used for non-sensitive configuration such as:

- Application settings
- Feature flags
- Service endpoints
- Configuration files

### Secrets

Used for sensitive information such as:

- Passwords
- API keys
- Access tokens
- Certificates

### Environment Variables vs Volume Mounts

| Feature          | Environment Variables | Volume Mounts       |
| ---------------- | --------------------- | ------------------- |
| Best For         | Simple settings       | Configuration files |
| Auto Update      | No                    | Yes                 |
| Requires Restart | Yes                   | No                  |
| Access Method    | Process Environment   | Filesystem          |

### Base64 vs Encryption

Base64 encoding:

- Converts data into text format
- Easily reversible
- Does not provide security

Encryption:

- Protects confidentiality
- Requires cryptographic keys
- Suitable for securing sensitive data

---

## Commands Practiced

```bash
kubectl create configmap
kubectl create secret
kubectl describe configmap
kubectl get configmap -o yaml
kubectl get secret -o yaml
kubectl apply -f
kubectl exec
kubectl logs
kubectl patch configmap
kubectl delete pod
kubectl delete configmap
kubectl delete secret
```

---

## Key Takeaways

- ConfigMaps separate application configuration from container images.
- Secrets store sensitive information securely within Kubernetes.
- Configuration can be consumed through environment variables or mounted files.
- Mounted ConfigMaps automatically receive updates.
- Environment variables require Pod restarts to pick up changes.
- Base64 encoding is not encryption and should not be treated as a security mechanism.

---

## Outcome

Successfully implemented Kubernetes ConfigMaps and Secrets, consumed configuration through environment variables and volume mounts, worked with encoded Secret data, and explored dynamic configuration management in Kubernetes.

---

### Connect With Me

Follow my #90DaysOfDevOps journey as I continue learning Kubernetes, Cloud, DevOps, CI/CD, and Infrastructure Automation.

**#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham #Kubernetes #ConfigMaps #Secrets #CloudNative #DevOps**
