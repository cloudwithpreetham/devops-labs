# Day 54 – Kubernetes ConfigMaps and Secrets

## Objective

Learn how Kubernetes manages application configuration and sensitive data using ConfigMaps and Secrets. Understand different ways of consuming configuration inside Pods and observe how updates propagate in running workloads.

---

# What are ConfigMaps?

A ConfigMap is a Kubernetes object used to store non-sensitive configuration data as key-value pairs.

Common use cases:

- Application environment settings
- Feature flags
- Configuration files
- Runtime parameters
- Service endpoints

Benefits:

- Decouples configuration from container images
- Allows configuration changes without rebuilding images
- Enables environment-specific deployments

---

# What are Secrets?

A Secret is a Kubernetes object used to store sensitive information.

Common use cases:

- Database credentials
- API tokens
- Access keys
- Certificates
- SSH keys

Benefits:

- Separates sensitive data from application code
- Can be controlled through RBAC
- Mounted securely into containers
- Supports encryption at rest when enabled

---

# Task 1: Create a ConfigMap from Literals

Created a ConfigMap named `app-config` using command-line literals.

```bash
kubectl create configmap app-config \
--from-literal=APP_ENV=production \
--from-literal=APP_DEBUG=false \
--from-literal=APP_PORT=8080
```

Verified configuration:

```bash
kubectl describe configmap app-config
kubectl get configmap app-config -o yaml
```

### Observation

ConfigMap values are stored as plain text.

```yaml
data:
  APP_DEBUG: "false"
  APP_ENV: production
  APP_PORT: "8080"
```

---

# Task 2: Create a ConfigMap from a File

Created an Nginx configuration file.

File: `default.conf`

```nginx
server {
    listen 80;

    location /health {
        return 200 'healthy';
        add_header Content-Type text/plain;
    }
}
```

Created ConfigMap:

```bash
kubectl create configmap nginx-config \
--from-file=default.conf=yaml-scripts/default.conf
```

Verified:

```bash
kubectl get configmap nginx-config -o yaml
```

### Observation

The file contents are stored within the ConfigMap and can later be mounted into containers.

---

# Task 3: Using ConfigMaps in Pods

## Method 1: Environment Variables

Created a BusyBox Pod using `envFrom`.

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

Verified:

```bash
kubectl logs configmap-env-pod
```

Output:

```text
APP_ENV=production
APP_DEBUG=false
APP_PORT=8080
```

### Observation

All ConfigMap keys were automatically injected as environment variables.

---

## Method 2: Volume Mount

Mounted the Nginx ConfigMap as a volume.

```yaml
volumeMounts:
  - name: nginx-config
    mountPath: /etc/nginx/conf.d
```

Verified:

```bash
kubectl exec -it nginx-config-pod -- sh
curl localhost/health
```

Output:

```text
healthy
```

### Observation

ConfigMaps can be mounted as files and consumed directly by applications.

---

# Task 4: Create a Secret

Created a Secret named `db-credentials`.

```bash
kubectl create secret generic db-credentials \
--from-literal=DB_USER=admin \
--from-literal=DB_PASSWORD='s3cureP@ssw0rd'
```

Verified:

```bash
kubectl get secret db-credentials -o yaml
```

Output:

```yaml
data:
  DB_PASSWORD: czNjdXJlUEBzc3cwcmQ=
  DB_USER: YWRtaW4=
```

---

## Decoding Secret Values

Retrieved encoded password:

```bash
kubectl get secret db-credentials \
-o jsonpath='{.data.DB_PASSWORD}'
```

Decoded value:

```bash
echo -n "czNjdXJlUEBzc3cwcmQ=" | base64 --decode
```

Output:

```text
s3cureP@ssw0rd
```

### Observation

Secret values are Base64 encoded, not encrypted.

---

# Why Base64 Is Not Encryption

Base64 only converts data into a text-friendly format.

Characteristics:

- Easily reversible
- No encryption key required
- Does not provide confidentiality

Example:

```bash
echo -n "password" | base64
```

Anyone can decode it:

```bash
echo -n "cGFzc3dvcmQ=" | base64 --decode
```

Therefore:

```text
Base64 = Encoding
Encryption = Security
```

---

# Task 5: Use Secrets in a Pod

Injected Secret as an environment variable.

```yaml
env:
  - name: DB_USER
    valueFrom:
      secretKeyRef:
        name: db-credentials
        key: DB_USER
```

Verified:

```bash
kubectl exec secret-pod -- printenv DB_USER
```

Output:

```text
admin
```

---

## Mount Secret as a Volume

Mounted Secret:

```yaml
volumeMounts:
  - name: secret-volume
    mountPath: /etc/db-credentials
    readOnly: true
```

Verified files:

```bash
kubectl exec secret-pod -- ls /etc/db-credentials
```

Output:

```text
DB_PASSWORD
DB_USER
```

Read Secret contents:

```bash
kubectl exec secret-pod -- cat /etc/db-credentials/DB_PASSWORD
```

Output:

```text
s3cureP@ssw0rd
```

### Observation

Mounted Secret files contain decoded plaintext values.

---

# Task 6: Update a ConfigMap and Observe Propagation

Created ConfigMap:

```bash
kubectl create configmap live-config \
--from-literal=message=hello
```

Mounted ConfigMap into a Pod.

The Pod continuously read the file every 5 seconds.

Updated ConfigMap:

```bash
kubectl patch configmap live-config \
--type merge \
-p '{"data":{"message":"world"}}'
```

### Expected Behavior

Volume-mounted ConfigMaps automatically update after a short delay.

Environment variables do not update automatically because they are loaded only when the Pod starts.

---

# Environment Variables vs Volume Mounts

| Feature              | Environment Variables     | Volume Mounts              |
| -------------------- | ------------------------- | -------------------------- |
| Best For             | Simple key-value settings | Configuration files        |
| Access Method        | Process environment       | Filesystem                 |
| Auto Update          | No                        | Yes                        |
| Requires Pod Restart | Yes                       | No                         |
| Common Usage         | APP_ENV, PORT             | Nginx configs, app configs |

---

# ConfigMaps vs Secrets

| Feature          | ConfigMap          | Secret            |
| ---------------- | ------------------ | ----------------- |
| Sensitive Data   | No                 | Yes               |
| Stored As        | Plain Text         | Base64 Encoded    |
| Use Cases        | Application Config | Passwords, Tokens |
| Mounted as Files | Yes                | Yes               |
| Used as Env Vars | Yes                | Yes               |

---

# Cleanup

Deleted all Day-54 resources.

Pods:

```bash
kubectl delete pod configmap-env-pod
kubectl delete pod nginx-config-pod
kubectl delete pod secret-pod
kubectl delete pod live-config-pod
```

ConfigMaps:

```bash
kubectl delete configmap app-config
kubectl delete configmap nginx-config
kubectl delete configmap live-config
```

Secrets:

```bash
kubectl delete secret db-credentials
```

Verified successful cleanup using:

```bash
kubectl get pods
kubectl get configmaps
kubectl get secrets
```

---

# Key Takeaways

- ConfigMaps store non-sensitive configuration.
- Secrets store sensitive application data.
- ConfigMaps can be created from literals and files.
- Secrets are Base64 encoded, not encrypted.
- Configuration can be consumed as environment variables or mounted files.
- Volume-mounted ConfigMaps and Secrets are ideal for configuration files.
- Environment variables require Pod restarts to receive updates.
- Volume-mounted ConfigMaps automatically receive updates without restarting Pods.
- Proper separation of configuration improves application portability and maintainability.

---

# Conclusion

Today I learned how Kubernetes manages application configuration using ConfigMaps and Secrets. I created ConfigMaps from literals and files, injected configuration into Pods through environment variables and volume mounts, worked with Secrets for sensitive data, decoded Base64 values, and explored how configuration updates propagate in running workloads. This is a fundamental skill for managing production Kubernetes applications securely and efficiently.
