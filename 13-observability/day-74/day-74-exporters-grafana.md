# Day 74 - Prometheus Exporters & Grafana Dashboard

## Objective

The goal of Day 74 was to extend the Prometheus monitoring stack by integrating exporters and Grafana to build a complete observability solution.

By the end of this lab, I was able to:

- Monitor Linux host metrics using Node Exporter
- Monitor Docker container metrics using cAdvisor
- Query metrics using PromQL
- Visualize metrics using Grafana
- Build a production-style monitoring dashboard

---

# Architecture

```
                    +----------------------+
                    |      Grafana         |
                    |   Visualization      |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    |     Prometheus       |
                    |  Metrics Database    |
                    +-----+-----------+----+
                          |           |
               +----------v--+   +----v----------+
               |Node Exporter|   |   cAdvisor    |
               | Host Metrics|   |Container Stats|
               +-------------+   +---------------+
```

---

# Project Structure

```
day-74/
├── README.md
├── day-74-exporters-grafana.md
├── task.md
├── observability-stack/
│   ├── docker-compose.yml
│   ├── prometheus.yml
│   └── dashboards/
│       └── DevOps-dashboard.json
└── screenshots/
```

---

# Technologies Used

- Docker
- Docker Compose
- Prometheus
- Node Exporter
- cAdvisor
- Grafana
- PromQL

---

# Step 1 — Node Exporter

## Why Node Exporter?

Prometheus cannot directly collect operating system metrics.

Node Exporter exposes Linux host metrics in Prometheus format.

Examples include:

- CPU Usage
- Memory Usage
- Disk Usage
- Filesystem Metrics
- Network Statistics
- Load Average
- System Information

---

## Docker Compose Configuration

```yaml
node-exporter:
  image: prom/node-exporter:latest
  container_name: node-exporter
  ports:
    - "9100:9100"
  restart: unless-stopped
```

---

## Prometheus Scrape Configuration

```yaml
- job_name: "node-exporter"
  static_configs:
    - targets:
        - node-exporter:9100
```

---

## Verification

Node Exporter metrics endpoint:

```
http://localhost:9100/metrics
```

Verified using:

```bash
curl http://localhost:9100/metrics | head -20
```

---

# Useful PromQL Queries

## CPU

```promql
node_cpu_seconds_total{mode="idle"}
```

---

## Total Memory

```promql
node_memory_MemTotal_bytes
```

---

## Available Memory

```promql
node_memory_MemAvailable_bytes
```

---

## Memory Usage %

```promql
(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100
```

---

## Disk Usage %

```promql
100 * (
1 - node_filesystem_avail_bytes{fstype!="tmpfs"}
/
node_filesystem_size_bytes{fstype!="tmpfs"}
)
```

---

# Step 2 — cAdvisor

## Why cAdvisor?

Node Exporter only monitors the Linux host.

To monitor Docker containers, cAdvisor exports container-level metrics.

Examples:

- Container CPU
- Container Memory
- Container Filesystem
- Container Network
- Container Lifecycle

---

## Docker Compose Configuration

```yaml
cadvisor:
  image: gcr.io/cadvisor/cadvisor:latest
  container_name: cadvisor
  ports:
    - "8080:8080"
  volumes:
    - /:/rootfs:ro
    - /var/run:/var/run:ro
    - /sys:/sys:ro
    - /var/lib/docker:/var/lib/docker:ro
    - /dev/disk:/dev/disk:ro
  privileged: true
  devices:
    - /dev/kmsg
  restart: unless-stopped
```

---

## Prometheus Scrape Configuration

```yaml
- job_name: "cadvisor"
  static_configs:
    - targets:
        - cadvisor:8080
```

---

# Important Observation

During this lab I noticed that modern Ubuntu (24.04) with cgroup v2 exposes Docker container metrics using the **id** label instead of the older **name** label used in many tutorials.

For example, the following query returned no data:

```promql
rate(container_cpu_usage_seconds_total{name!=""}[5m])
```

Instead, I successfully queried metrics using:

```promql
rate(container_cpu_usage_seconds_total[5m])
```

or

```promql
sum by (id)(
rate(container_cpu_usage_seconds_total{id=~".*docker.*"}[5m])
)
```

This highlighted the importance of inspecting exporter labels before writing PromQL queries.

---

# Useful cAdvisor Queries

## CPU Usage

```promql
rate(container_cpu_usage_seconds_total[5m])
```

---

## Docker Container CPU

```promql
sum by (id)(
rate(container_cpu_usage_seconds_total{id=~".*docker.*"}[5m])
)
```

---

## Memory Usage

```promql
container_memory_usage_bytes{id=~".*docker.*"}
```

---

## Top Memory Consumers

```promql
topk(
3,
container_memory_usage_bytes{id=~".*docker.*"}
)
```

---

## Network Receive

```promql
rate(container_network_receive_bytes_total{id=~".*docker.*"}[5m])
```

---

# Step 3 — Grafana

## Why Grafana?

Prometheus stores metrics but is not intended for rich dashboards.

Grafana provides:

- Dashboards
- Panels
- Graphs
- Gauges
- Alerts
- Team Sharing

---

## Login

```
http://localhost:3000
```

Default Credentials

```
Username : admin
Password : admin
```

---

## Add Prometheus Data Source

URL

```
http://prometheus:9090
```

Successfully connected Grafana to Prometheus.

---

# Dashboard Panels

Created a custom dashboard named:

```
DevOps Observability Dashboard
```

The dashboard includes:

- Host CPU Usage
- Host Memory Usage
- Disk Usage
- Container CPU Usage
- Container Memory Usage

---

# Verification

Verified:

- Prometheus running
- Node Exporter running
- cAdvisor running
- Grafana running
- All Prometheus targets UP
- PromQL queries returning metrics
- Dashboard successfully visualizing data

---

# Screenshots

Captured the following screenshots:

- Docker Compose containers
- Prometheus Targets
- Node Exporter metrics
- cAdvisor dashboard
- Prometheus PromQL queries
- Grafana datasource
- Grafana dashboard

---

# Key Learnings

- Difference between Prometheus and Grafana
- Host monitoring using Node Exporter
- Container monitoring using cAdvisor
- Writing PromQL queries
- Building Grafana dashboards
- Understanding exporter labels
- Troubleshooting PromQL issues
- Differences between older tutorials and modern cAdvisor implementations

---

# Interview Questions

### Why is Node Exporter required?

Prometheus cannot directly collect Linux host metrics. Node Exporter exposes system metrics in Prometheus format.

---

### Why use cAdvisor?

Node Exporter monitors the host machine, whereas cAdvisor monitors Docker containers.

---

### What is PromQL?

PromQL is Prometheus Query Language used to retrieve and analyze time-series metrics.

---

### Why use Grafana if Prometheus already has graphs?

Prometheus provides basic visualization.

Grafana offers production-grade dashboards, multiple visualization types, alerting, sharing, and support for multiple data sources.

---

### What challenge did you face?

The original PromQL examples filtered metrics using the `name` label. On Ubuntu 24.04 with cgroup v2, cAdvisor exposed Docker containers using the `id` label instead. I inspected the available labels and updated the PromQL queries accordingly.

---

# Outcome

By completing this lab, I built a complete observability stack consisting of:

- Prometheus
- Node Exporter
- cAdvisor
- Grafana

This setup provides host-level and container-level monitoring with interactive dashboards, closely resembling a production monitoring environment.
