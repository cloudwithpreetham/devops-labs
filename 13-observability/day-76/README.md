# Day 76 – OpenTelemetry and Alerting

## Overview

Day 76 focused on completing the **third pillar of observability** by integrating **OpenTelemetry (OTEL)** into the monitoring stack and implementing **alerting** using both **Prometheus** and **Grafana**.

The OpenTelemetry Collector was configured to receive OTLP metrics and traces, export metrics for Prometheus scraping, and output traces through the debug exporter. In addition, Prometheus alert rules and Grafana alerting were configured to proactively monitor infrastructure health.

This project now provides a complete observability solution with **Metrics, Logs, Traces, Dashboards, and Alerts**.

---

## Project Structure

```text
day-76/
├── README.md
├── day-76-otel-alerting.md
└── observability-stack/
    ├── docker-compose.yml
    ├── prometheus.yml
    ├── alert-rules.yml
    ├── dashboards/
    │   └── DevOps-dashboard.json
    ├── grafana/
    │   └── provisioning/
    ├── loki/
    │   └── loki-config.yml
    ├── otel-collector/
    │   └── otel-collector-config.yml
    └── promtail/
        └── promtail-config.yml
```

---

# Technologies Used

- Docker Compose
- Prometheus
- Grafana
- Loki
- Promtail
- OpenTelemetry Collector
- Node Exporter
- cAdvisor
- OTLP (OpenTelemetry Protocol)

---

# Observability Architecture

```text
                        +----------------------+
                        |      Grafana        |
                        | Dashboards          |
                        | Alerting            |
                        +----------+----------+
                                   |
             +---------------------+----------------------+
             |                     |                      |
          Metrics               Logs                  Traces
             |                     |                      |
     +-------v-------+      +------v------+      +--------v--------+
     |  Prometheus   |      |    Loki     |      | OTEL Collector  |
     +-------+-------+      +------+------+
             |                     |                     |
   +---------+----------+          |             OTLP HTTP / gRPC
   |                    |          |                     |
+--v------+      +------v-----+    |               Applications
|Node Exp.|      | cAdvisor   |    |                 / curl
+---------+      +------------+    |
                                   |
                             +-----v------+
                             | Promtail   |
                             +------------+
```

---

# Features Implemented

## OpenTelemetry Collector

- Configured OTLP Receiver
- Enabled HTTP (4318)
- Enabled gRPC (4317)
- Batch Processor
- Prometheus Exporter
- Debug Exporter

---

## Metrics Pipeline

- OTLP metrics received by Collector
- Metrics exported on port 8889
- Prometheus scraping OTEL Collector
- Custom metric verification
- PromQL validation

---

## Traces Pipeline

- OTLP traces sent using curl
- Trace successfully processed
- Span verification through Debug Exporter

---

## Prometheus Alerting

Implemented infrastructure alert rules for:

- High CPU Usage
- High Memory Usage
- Target Down
- High Disk Usage

---

## Grafana Alerting

Configured:

- Contact Point
- Evaluation Group
- Alert Rule
- Notification Policy

---

# Validation Performed

Successfully verified:

- OpenTelemetry Collector running
- Prometheus targets healthy
- OTLP traces received
- OTLP metrics exported
- Prometheus scraping collector metrics
- Custom metric available in PromQL
- Alert rules loaded
- Alert evaluation working
- Grafana notification configuration completed

---

# Screenshots

| Screenshot                         | Description                   |
| ---------------------------------- | ----------------------------- |
| 01-prometheus-targets-all-up.png   | Prometheus target status      |
| 02-otel-trace-debug-output.png     | OTEL Collector debug trace    |
| 03-prometheus-test-metric.png      | Custom metric in Prometheus   |
| 04-prometheus-alert-rules.png      | Loaded Prometheus alert rules |
| 05-prometheus-alerts.png           | Alert evaluation status       |
| 06-grafana-contact-point.png       | Grafana contact point         |
| 07-grafana-alert-rule.png          | Grafana alert rule            |
| 08-grafana-notification-policy.png | Notification policy           |

---

# Key Learnings

- OpenTelemetry standardizes telemetry collection across platforms.
- The OTEL Collector acts as a telemetry gateway using Receivers, Processors, and Exporters.
- OTLP enables consistent transport of metrics, logs, and traces.
- Prometheus can scrape metrics exposed by the OTEL Collector.
- Distributed tracing provides end-to-end request visibility across services.
- Prometheus alert rules automate infrastructure monitoring.
- Grafana Alerting enables centralized notification management through contact points and notification policies.
- Combining Prometheus, Grafana, Loki, Promtail, and OpenTelemetry delivers a production-ready observability platform.

---

# Outcome

By the end of Day 76, the observability stack was enhanced with **OpenTelemetry** for distributed tracing and telemetry collection, **Prometheus Alert Rules** for infrastructure monitoring, and **Grafana Alerting** for notification management. The project now implements all three pillars of observability—**Metrics, Logs, and Traces**—along with proactive alerting, creating a robust and production-style monitoring solution.

---

## Repository

Part of the **90 Days of DevOps** challenge.

**Day 76:** OpenTelemetry and Alerting
