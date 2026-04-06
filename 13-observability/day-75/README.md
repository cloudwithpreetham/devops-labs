# Day 75 – Log Management with Loki & Promtail

> Part of my **#90DaysOfDevOps** journey

## Overview

On Day 75, I implemented the **logging pillar of observability** by integrating **Grafana Loki** and **Promtail** into the monitoring stack built on Day 74.

While Prometheus provides metrics that tell **what** is happening, Loki collects and stores logs that explain **why** it is happening. By combining metrics and logs in Grafana, troubleshooting becomes significantly faster and more efficient.

---

# Architecture

```text
                    +----------------------+
                    | Docker Containers    |
                    +----------+-----------+
                               |
                               | JSON Logs
                               |
                               v
               /var/lib/docker/containers/
                               |
                               v
                     +------------------+
                     |    Promtail      |
                     +--------+---------+
                              |
                              | Push Logs
                              |
                              v
                     +------------------+
                     |      Loki        |
                     +--------+---------+
                              |
                              | LogQL Queries
                              |
                              v
                     +------------------+
                     |    Grafana       |
                     +--------+---------+
                              |
              Metrics + Logs in One Dashboard
```

---

# Tech Stack

- Docker Compose
- Grafana
- Prometheus
- Loki
- Promtail
- Node Exporter
- cAdvisor
- LogQL

---

# Project Structure

```text
observability-stack/
│
├── docker-compose.yml
├── prometheus.yml
│
├── grafana/
│   └── provisioning/
│       └── datasources/
│           └── datasources.yml
│
├── loki/
│   └── loki-config.yml
│
├── promtail/
│   └── promtail-config.yml
│
└── README.md
```

---

# Components

## Prometheus

Collects metrics from the host and containers.

**Port:** `9090`

---

## Node Exporter

Collects Linux system metrics.

Examples:

- CPU
- Memory
- Filesystem
- Network

---

## cAdvisor

Collects Docker container metrics.

Examples:

- CPU Usage
- Memory Usage
- Network Usage
- Filesystem Usage

---

## Loki

Centralized log storage built by Grafana Labs.

Features:

- Label-based indexing
- Low storage cost
- Fast ingestion
- Native Grafana integration

---

## Promtail

Log collection agent.

Responsibilities:

- Reads Docker container logs
- Parses Docker JSON logs
- Adds labels
- Pushes logs to Loki

---

## Grafana

Provides a unified interface for:

- Metrics
- Logs
- Dashboards
- Incident Investigation

---

# Logging Pipeline

```text
Docker Containers
       │
       ▼
Docker JSON Logs
       │
       ▼
Promtail
       │
       ▼
Loki
       │
       ▼
Grafana Explore
```

---

# Configuration Files

## Loki

```text
loki/loki-config.yml
```

Configures:

- Storage
- Indexing
- HTTP API
- TSDB

---

## Promtail

```text
promtail/promtail-config.yml
```

Configures:

- Docker log scraping
- Positions tracking
- Pipeline stages
- Loki endpoint

---

# Docker Compose Services

The stack consists of:

- Prometheus
- Grafana
- Node Exporter
- cAdvisor
- Loki
- Promtail

---

# LogQL Queries

## Show all Docker logs

```logql
{job="docker"}
```

---

## Find error logs

```logql
{job="docker"} |= "error"
```

---

## Count logs

```logql
count_over_time({job="docker"}[5m])
```

---

## Log rate

```logql
rate({job="docker"}[5m])
```

---

## Search Promtail logs

```logql
{job="docker"} |= "Starting Promtail"
```

---

# Validation

Successfully verified:

- Loki readiness endpoint
- Promtail targets
- Docker log collection
- Grafana datasource
- LogQL queries
- Metrics and logs correlation

---

# Loki vs ELK

| Loki                      | ELK Stack                       |
| ------------------------- | ------------------------------- |
| Indexes labels only       | Indexes full log content        |
| Lower storage usage       | Higher storage usage            |
| Faster ingestion          | Slower ingestion                |
| Lower infrastructure cost | Higher infrastructure cost      |
| Excellent for Kubernetes  | Excellent for enterprise search |
| Native Grafana support    | Kibana support                  |

---

# Challenges Faced

- Added Loki to Docker Compose and resolved volume configuration issues.
- Configured Promtail to access Docker container log files.
- Exposed Promtail HTTP endpoint (`9080`) to verify scrape targets.
- Provisioned Grafana with both Prometheus and Loki datasources.
- Validated end-to-end log ingestion using LogQL.

---

# Key Learnings

- Metrics identify **what** happened.
- Logs explain **why** it happened.
- Loki stores logs efficiently using label-based indexing.
- Promtail automatically ships Docker logs to Loki.
- LogQL enables searching and analyzing logs.
- Combining metrics and logs in Grafana reduces Mean Time To Resolution (MTTR).

---

# Screenshots

- Loki Running
- Promtail Running
- Promtail Targets
- Grafana Datasources
- Docker Logs in Grafana Explore
- LogQL Query Results
- Count Over Time Visualization
- Metrics and Logs Side by Side
- Dashboard with Container Logs Panel

---

# Outcome

By completing Day 75, I built a complete cloud-native observability solution capable of monitoring infrastructure metrics and collecting centralized logs from Docker containers.

The stack now includes:

- Infrastructure Monitoring
- Container Monitoring
- Centralized Logging
- Log Aggregation
- Log Querying
- Unified Observability Dashboard

This setup closely resembles the observability architecture used in modern Kubernetes and cloud-native production environments.

---

## Connect With Me

If you're also learning DevOps or building cloud-native monitoring stacks, feel free to connect and share your progress.

**#90DaysOfDevOps #DevOps #Observability #Grafana #Loki #Promtail #Prometheus #Docker #CloudNative #OpenSource**
