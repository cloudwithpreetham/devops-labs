# Day 74 - Prometheus Exporters & Grafana Dashboard

A hands-on DevOps project demonstrating how to build a complete observability stack using **Prometheus**, **Node Exporter**, **cAdvisor**, and **Grafana** to monitor both Linux host and Docker container metrics.

---

## Project Objective

The objective of this project is to build a production-style monitoring stack that provides:

- Host-level monitoring
- Container-level monitoring
- Metrics collection
- Time-series storage
- Interactive dashboards
- PromQL-based analysis

---

## Architecture

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

## Tech Stack

- Docker
- Docker Compose
- Prometheus
- Node Exporter
- cAdvisor
- Grafana
- PromQL

---

## Project Structure

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

## Components

### Prometheus

Prometheus collects and stores metrics from configured targets.

Responsibilities:

- Metric collection
- Time-series database
- PromQL query engine
- Service monitoring

---

### Node Exporter

Node Exporter exposes Linux host metrics including:

- CPU Usage
- Memory Usage
- Disk Usage
- Filesystem Statistics
- Network Metrics
- System Load

---

### cAdvisor

cAdvisor provides container-level metrics such as:

- CPU Usage
- Memory Usage
- Network Statistics
- Filesystem Usage
- Container Resource Consumption

---

### Grafana

Grafana connects to Prometheus and visualizes collected metrics through interactive dashboards.

Dashboard includes:

- Host CPU Usage
- Host Memory Usage
- Disk Usage
- Container CPU Usage
- Container Memory Usage

---

## Getting Started

### Clone Repository

```bash
git clone <repository-url>
cd day-74
```

---

### Start the Monitoring Stack

```bash
docker compose up -d
```

Verify running containers:

```bash
docker compose ps
```

---

## Access Services

| Service | URL |
|----------|-----|
| Prometheus | http://localhost:9090 |
| Node Exporter | http://localhost:9100/metrics |
| cAdvisor | http://localhost:8080 |
| Grafana | http://localhost:3000 |

---

## Grafana Login

Default credentials:

```
Username: admin
Password: admin
```

Change the password after the first login.

---

## Configure Prometheus Data Source

Inside Grafana:

```
Connections
    ↓
Data Sources
    ↓
Add Data Source
```

Choose:

```
Prometheus
```

URL:

```
http://prometheus:9090
```

Save and test the connection.

---

## Useful PromQL Queries

### Host CPU Usage

```promql
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

---

### Host Memory Usage

```promql
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
```

---

### Disk Usage

```promql
100 * (
1 - node_filesystem_avail_bytes{fstype!="tmpfs"}
/
node_filesystem_size_bytes{fstype!="tmpfs"}
)
```

---

### Container CPU Usage

```promql
sum by (id)(
rate(container_cpu_usage_seconds_total{id=~".*docker.*"}[5m])
)
```

---

### Container Memory Usage

```promql
container_memory_usage_bytes{id=~".*docker.*"}
```

---

## Key Learning

During this project, I discovered that modern Ubuntu (24.04) using **cgroup v2** exposes Docker container metrics with the `id` label instead of the older `name` label commonly found in tutorials.

For example:

Old query:

```promql
rate(container_cpu_usage_seconds_total{name!=""}[5m])
```

Updated query:

```promql
sum by (id)(
rate(container_cpu_usage_seconds_total{id=~".*docker.*"}[5m])
)
```

This reinforced the importance of inspecting available metric labels before writing PromQL queries.

---

## Skills Gained

- Prometheus fundamentals
- Prometheus scrape configuration
- Node Exporter setup
- cAdvisor integration
- PromQL basics
- Grafana dashboard creation
- Docker monitoring
- Linux host monitoring
- Metrics visualization
- Observability fundamentals
- Troubleshooting exporter metrics

---

## Screenshots

The project includes screenshots demonstrating:

- Docker Compose services
- Prometheus Targets
- Node Exporter metrics
- cAdvisor metrics
- PromQL queries
- Grafana data source configuration
- Final Grafana dashboard

---

## Outcome

By completing this project, I successfully built a complete observability stack capable of monitoring both Linux hosts and Docker containers using open-source tools.

This project provides a solid foundation for learning advanced monitoring topics such as:

- Alertmanager
- Grafana Alerting
- Loki
- Promtail
- Tempo
- Kubernetes Monitoring
- Production Observability

---

## Author

**Preetham**

**90 Days of DevOps Challenge**

Day 74 — Prometheus Exporters & Grafana Dashboard
