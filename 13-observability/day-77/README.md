# Day 77 – End-to-End Observability Stack Validation

> **90 Days of DevOps Challenge**
> **Day 77 - Observability Project**

## Project Overview

On Day 77, I deployed and validated a complete production-style observability stack using Docker Compose. The objective was to verify that metrics, logs, and telemetry flow correctly across the monitoring ecosystem while troubleshooting compatibility issues introduced by newer versions of the observability tools.

This project demonstrates how Prometheus, Grafana, Loki, Promtail, Node Exporter, cAdvisor, and OpenTelemetry Collector work together to provide complete visibility into containerized applications.

---

# Tech Stack

- Docker Compose
- Prometheus
- Grafana Enterprise
- Loki
- Promtail
- OpenTelemetry Collector
- Node Exporter
- cAdvisor
- Python Notes Application

---

# Architecture

```text
                    +----------------------+
                    |    Notes App         |
                    +----------+-----------+
                               |
          +--------------------+--------------------+
          |                                         |
          |                                         |
   Application Logs                         Application Metrics
          |                                         |
          v                                         v
    +-------------+                     +----------------------+
    |  Promtail   |                     | OTEL Collector       |
    +------+------+                     +----------+-----------+
           |                                        |
           |                                        |
           +------------------+---------------------+
                              |
                              v
                     +------------------+
                     |      Loki        |
                     +------------------+
                              |
                              |
                     +------------------+
                     |    Grafana       |
                     +------------------+
                              ^
                              |
                     +------------------+
                     |   Prometheus     |
                     +------------------+
                      ^              ^
                      |              |
               Node Exporter     cAdvisor
```

---

# Project Structure

```text
observability-for-devops/
├── docker-compose.yml
├── prometheus.yml
├── grafana/
├── loki/
├── promtail/
├── otel-collector/
└── notes-app/
```

---

# Components Validated

- Prometheus
- Grafana
- Loki
- Promtail
- Node Exporter
- cAdvisor
- OpenTelemetry Collector
- Notes Application

---

# Deployment

Clone repository

```bash
git clone https://github.com/LondheShubham153/observability-for-devops.git
```

Navigate into project

```bash
cd observability-for-devops
```

Build the application

```bash
docker compose build notes-app
```

Deploy stack

```bash
docker compose up -d
```

Verify containers

```bash
docker compose ps
```

---

# Validation Performed

## Docker Compose

- Verified compose configuration
- Built local Notes application image
- Started all observability services
- Confirmed healthy container status

---

## Prometheus

Validated scrape targets:

- Prometheus
- Node Exporter
- cAdvisor
- OTEL Collector

Executed PromQL queries for:

- Target health
- CPU utilization
- Memory utilization
- Container metrics

---

## Grafana

Verified:

- Successful login
- Prometheus datasource
- Loki datasource
- Metrics visualization
- Log exploration

---

## Loki

Validated:

- Readiness endpoint
- Log ingestion
- WAL checkpoints
- Storage synchronization

---

## Promtail

Verified:

- Docker log discovery
- Container log tailing
- Successful log shipping to Loki

---

## Node Exporter

Collected host-level metrics including:

- CPU
- Memory
- Filesystem
- Network

---

## cAdvisor

Collected container-level metrics including:

- CPU usage
- Memory usage
- Container statistics

---

# Issues Encountered

## Issue 1

### Docker Pull Failed

The Notes application image was not available on Docker Hub because it is built locally.

### Solution

```bash
docker compose build notes-app
```

---

## Issue 2

### PromQL Query Returned No Data

Original query

```promql
rate(container_cpu_usage_seconds_total{name!=""}[5m])
```

Recent cAdvisor versions no longer expose the `name` label.

### Updated query

```promql
rate(container_cpu_usage_seconds_total[5m])
```

---

## Issue 3

### LogQL Empty Selector Error

Older Loki versions allowed:

```logql
{}
```

Loki 3.x requires a label matcher.

Updated query:

```logql
{job=~".+"}
```

---

# Validation Results

| Component         | Status |
| ----------------- | ------ |
| Docker Compose    | Passed |
| Prometheus        | Passed |
| Grafana           | Passed |
| Loki              | Passed |
| Promtail          | Passed |
| Node Exporter     | Passed |
| cAdvisor          | Passed |
| OTEL Collector    | Passed |
| Notes Application | Passed |

---

# Screenshots

## Infrastructure

- Docker Compose Services Running
- Running Containers

## Prometheus

- Targets Status
- CPU Metrics Query
- Memory Metrics Query

## Grafana

- Data Sources
- Loki Explore
- Logs Visualization

---

# Key Learnings

- Deployed an end-to-end observability stack using Docker Compose.
- Validated metrics collection using Prometheus.
- Monitored host metrics with Node Exporter.
- Collected container metrics using cAdvisor.
- Aggregated logs using Promtail and Loki.
- Explored metrics with PromQL.
- Queried centralized logs using LogQL.
- Understood Docker networking between monitoring services.
- Troubleshot compatibility differences introduced by newer versions of cAdvisor and Loki.
- Gained practical experience with production-style monitoring workflows.

---

# Version Compatibility Notes

During validation, two compatibility differences were identified:

- Recent cAdvisor versions do not expose the `name` label used in older PromQL examples.
- Loki 3.x no longer supports an empty LogQL selector (`{}`), requiring at least one label matcher such as `{job=~".+"}`.

These adjustments reflect real-world version differences and are important when working with modern observability stacks.

---

# Outcome

Successfully deployed, validated, and troubleshot a complete observability platform integrating Prometheus, Grafana, Loki, Promtail, Node Exporter, cAdvisor, OpenTelemetry Collector, and a sample application. Verified end-to-end metrics collection, centralized logging, and visualization while adapting queries to newer tool versions commonly encountered in production environments.
