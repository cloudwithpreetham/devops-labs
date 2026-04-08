# 13 - Observability

This directory contains my **Observability learning journey** from the **90 Days of DevOps Challenge**. Throughout these five days, I learned how to collect, visualize, and analyze metrics and logs using industry-standard monitoring tools.

The focus was on building a complete observability stack with **Prometheus**, **Grafana**, **Loki**, **Promtail**, **Node Exporter**, and **cAdvisor** using Docker Compose.

---

## Learning Objectives

- Understand the three pillars of observability
  - Metrics
  - Logs
  - Traces (introduction)
- Monitor Linux system metrics
- Collect Docker container metrics
- Visualize infrastructure dashboards
- Centralize application and container logs
- Learn PromQL basics
- Explore Grafana dashboards and queries
- Build a production-style monitoring stack

---

# Project Structure

```
13-observability/
├── day-73/
├── day-74/
├── day-75/
├── day-76/
├── day-77/
└── README.md
```

---

# Daily Progress

| Day | Topic | Status |
|------|-------|--------|
| Day 73 | Introduction to Observability & Prometheus | Completed |
| Day 74 | Docker Monitoring using Node Exporter & cAdvisor | Completed |
| Day 75 | Centralized Logging with Loki & Promtail | Completed |
| Day 76 | Grafana Dashboards & Prometheus Visualization | Completed |
| Day 77 | Complete Observability Stack Integration | Completed |

---

# Day 73 — Prometheus Fundamentals

## Covered

- What is Observability?
- Monitoring vs Observability
- Prometheus Architecture
- Time Series Database (TSDB)
- Targets & Scraping
- Metrics Collection
- PromQL Basics

### Learned

- Prometheus Server
- Exporters
- Pull-based monitoring
- Jobs & Targets
- Labels
- Metrics types
  - Counter
  - Gauge
  - Histogram
  - Summary

---

# Day 74 — Docker Monitoring

Built a monitoring stack using Docker Compose.

## Components

- Prometheus
- Node Exporter
- cAdvisor

### Learned

- Docker container metrics
- CPU monitoring
- Memory monitoring
- Disk metrics
- Network metrics
- Prometheus Targets

Successfully queried metrics like:

- node_cpu_seconds_total
- node_memory_MemAvailable_bytes
- container_cpu_usage_seconds_total
- container_memory_usage_bytes

---

# Day 75 — Centralized Logging

Implemented centralized log aggregation.

## Stack

- Loki
- Promtail
- Grafana

### Learned

- Log aggregation
- Log scraping
- Docker log collection
- Log labels
- LogQL basics

Collected logs from Docker containers and explored them in Grafana.

---

# Day 76 — Grafana Visualization

Connected Prometheus to Grafana.

## Built Dashboards

- CPU Usage
- Memory Usage
- Disk Usage
- Docker Containers
- Network Statistics

### Learned

- Data Sources
- Dashboards
- Panels
- Variables
- PromQL inside Grafana

---

# Day 77 — Complete Observability Stack

Integrated the complete monitoring ecosystem.

## Final Stack

- Prometheus
- Grafana
- Loki
- Promtail
- Node Exporter
- cAdvisor

### Architecture

```
Node Exporter ─────┐
                   │
cAdvisor ──────────┤
                   ▼
             Prometheus
                   │
                   ▼
               Grafana

Docker Logs
      │
      ▼
  Promtail
      │
      ▼
    Loki
      │
      ▼
   Grafana Logs
```

---

# Technologies Used

- Docker
- Docker Compose
- Prometheus
- Grafana
- Loki
- Promtail
- Node Exporter
- cAdvisor
- PromQL
- LogQL
- Linux

---

# Skills Gained

- Infrastructure Monitoring
- Metrics Collection
- Dashboard Creation
- Log Aggregation
- Docker Monitoring
- PromQL
- LogQL
- Grafana Administration
- Observability Best Practices

---

# Key Takeaways

- Monitoring helps identify system health.
- Observability enables deeper troubleshooting using metrics and logs.
- Prometheus is powerful for metrics collection.
- Grafana provides rich visualizations.
- Loki simplifies centralized logging.
- Promtail efficiently forwards logs to Loki.
- Node Exporter and cAdvisor provide valuable infrastructure and container insights.

---

# Outcome

By the end of this module, I successfully built a complete observability platform capable of:

- Monitoring Linux servers
- Monitoring Docker containers
- Visualizing infrastructure metrics
- Centralizing logs
- Troubleshooting applications using dashboards and logs
- Understanding production-ready monitoring workflows

---

## Repository Timeline

| Day | Focus |
|------|------|
| Day 73 | Prometheus Fundamentals |
| Day 74 | Docker Monitoring |
| Day 75 | Loki & Promtail |
| Day 76 | Grafana Dashboards |
| Day 77 | Complete Observability Stack |

---

## Next Module

➡️ **CI/CD Pipelines & GitHub Actions** (or your next learning module in the 90 Days of DevOps journey)

---

## Author

**Preetham**

**90 Days of DevOps Challenge**
