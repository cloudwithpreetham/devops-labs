# Day 73 – Introduction to Observability with Prometheus

Learned the fundamentals of **Observability** by understanding its three pillars—**Metrics, Logs, and Traces**—and deployed **Prometheus** with **Node Exporter** using Docker Compose. Explored the Prometheus web UI, executed PromQL queries, and monitored host-level system metrics.

---

## Objectives

- Understand Observability vs Traditional Monitoring
- Learn the Three Pillars of Observability
- Deploy Prometheus using Docker
- Configure scrape targets
- Monitor host metrics using Node Exporter
- Learn PromQL fundamentals
- Explore Prometheus TSDB and data retention

---

## Project Structure

```text
day-73/
├── README.md
├── day-73-observability-prometheus.md
├── task.md
├── observability-stack/
│   ├── docker-compose.yml
│   └── prometheus.yml
└── screenshots/
```

---

## Tech Stack

- Docker
- Docker Compose
- Prometheus
- Node Exporter
- PromQL
- Linux

---

## Architecture

```text
                    +----------------+
                    |   Applications |
                    +--------+-------+
                             |
                             | Metrics
                             |
                    +--------v--------+
                    |   Prometheus    |
                    +--------+--------+
                             |
               +-------------+-------------+
               |                           |
               | PromQL Queries            |
               |                           |
        +------v------+            +-------v-------+
        | Prometheus  |            | Node Exporter |
        | Self Metrics|            | Host Metrics  |
        +-------------+            +---------------+

Future Stack

Applications
     │
     ├──────── Metrics ───────► Prometheus ─────► Grafana
     │
     ├──────── Logs ──────────► Promtail ───────► Loki ─────► Grafana
     │
     └──────── Traces ───────► OTEL Collector ─► Grafana
```

---

## Files

### docker-compose.yml

Deploys:

- Prometheus
- Node Exporter

---

### prometheus.yml

Configured scrape targets for:

- Prometheus
- Node Exporter

---

### day-73-observability-prometheus.md

Contains:

- Observability concepts
- Monitoring vs Observability
- Three pillars
- Prometheus setup
- PromQL examples
- Screenshots
- Learning summary

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd day-73
```

---

### Start Containers

```bash
docker compose up -d
```

---

### Verify Containers

```bash
docker ps
```

Expected containers:

- prometheus
- node-exporter

---

### Open Prometheus

```
http://localhost:9090
```

Navigate to:

```
Status → Targets
```

Expected:

```
prometheus      UP
node-exporter   UP
```

---

## PromQL Queries Practiced

Check target health

```promql
up
```

Count all metrics

```promql
count({__name__=~".+"})
```

Prometheus memory usage

```promql
process_resident_memory_bytes / 1024 / 1024
```

CPU metrics

```promql
node_cpu_seconds_total
```

Available memory

```promql
node_memory_MemAvailable_bytes / 1024 / 1024 / 1024
```

System load

```promql
node_load1
```

HTTP request rate

```promql
rate(prometheus_http_requests_total[5m])
```

Non-200 request rate

```promql
sum(rate(prometheus_http_requests_total{code!="200"}[5m]))
```

---

## Key Concepts Learned

### Monitoring

- Detects known issues
- Uses alerts and thresholds
- Answers **"What happened?"**

---

### Observability

- Investigates unknown issues
- Correlates telemetry data
- Answers **"Why did it happen?"**

---

### Three Pillars

### Metrics

Numerical values collected over time.

Examples:

- CPU Usage
- Memory Usage
- Request Count

---

### Logs

Timestamped records describing events.

Examples:

- Application Logs
- Error Logs
- Access Logs

---

### Traces

Track a request across multiple services.

Useful for:

- Latency analysis
- Bottleneck detection
- Distributed debugging

---

## Metric Types

### Counter

Only increases.

Examples:

- HTTP Requests
- Total Errors
- Total Logins

---

### Gauge

Can increase or decrease.

Examples:

- CPU Usage
- Memory Usage
- Active Connections

---

### Histogram

Measures value distributions using buckets.

---

### Summary

Calculates client-side quantiles and percentiles.

---

## Data Retention

Prometheus stores metrics inside its built-in Time Series Database (TSDB).

Example retention configuration:

```yaml
--storage.tsdb.retention.time=15d
--storage.tsdb.retention.size=1GB
```

Using a Docker volume ensures collected metrics persist across container restarts.

---

## Challenges Faced

The provided sample `notes-app` container responded with **HTTP 404** for the `/metrics` endpoint because it was not instrumented for Prometheus metrics.

To continue the learning objectives, monitoring was performed using:

- Prometheus self-metrics
- Node Exporter host metrics

This reinforced the understanding that Prometheus requires applications to expose a valid `/metrics` endpoint.

---

## Screenshots

- Project directory structure
- Docker Compose services running
- Prometheus Targets page
- `up` query
- `count({__name__=~".+"})`
- CPU metrics query
- Memory metrics query
- TSDB Status

---

## Key Takeaways

- Learned the difference between Monitoring and Observability.
- Understood Metrics, Logs, and Traces.
- Deployed Prometheus using Docker Compose.
- Configured scrape targets.
- Added Node Exporter for infrastructure monitoring.
- Explored Prometheus Web UI.
- Learned PromQL basics.
- Queried live infrastructure metrics.
- Understood Prometheus TSDB and retention policies.
- Built the foundation for a complete observability stack.

---

## Future Improvements

Over the next few days, this stack will be extended by adding:

- Grafana
- Loki
- Promtail
- cAdvisor
- OpenTelemetry Collector
- Application instrumentation
- Dashboards and alerts

---

## Learning Outcome

This project established the foundation of modern observability by deploying Prometheus and Node Exporter, collecting infrastructure metrics, and learning how to analyze time-series data using PromQL. These concepts form the backbone of monitoring and troubleshooting production systems in real-world DevOps environments.
