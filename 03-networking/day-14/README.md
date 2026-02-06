# Day 14 – Networking Fundamentals & Hands-on Checks

## Overview

Day 14 focused on understanding core networking fundamentals and practicing essential troubleshooting commands used in real-world DevOps environments.

This hands-on session covered:

- Networking models (OSI vs TCP/IP)
- Protocol mapping (IP, TCP/UDP, HTTP/HTTPS, DNS)
- Connectivity testing
- DNS resolution
- Port listening checks
- HTTP response validation
- Port probing and service reachability

---

## Topics Covered

### Networking Models

- OSI 7-layer model
- TCP/IP 4-layer model
- Practical understanding of protocol flow

### Protocol Placement

- **IP** → Internet layer
- **TCP / UDP** → Transport layer
- **HTTP / HTTPS** → Application layer
- **DNS** → Application layer

### Real-world Request Flow

```text
curl https://google.com
↓
HTTP Request
↓
TCP Connection
↓
IP Routing
↓
Remote Server Response
```

---

## Hands-on Commands Practiced

```bash
hostname -I
ping -c 4 google.com
traceroute google.com
ss -tulpn
dig google.com
curl -I https://google.com
netstat -an | head
nc -zv localhost 22
```

---

## Key Learnings

- How packets travel across networks
- Difference between connectivity issues and DNS issues
- How to inspect listening services
- How HTTP responses indicate service health
- How to validate open ports locally
- How to troubleshoot network issues step-by-step

---

## Directory Structure

```text
day-14/
├── screenshots/
├── day-14-networking.md
├── reference.md
└── README.md
```

---

## Outcome

Built practical confidence with networking commands commonly used in:

- Linux troubleshooting
- Server debugging
- Connectivity validation
- Service reachability checks
- Incident investigation

---

## DevOps Takeaway

Networking is one of the core foundations of DevOps.

If you can quickly answer:

- Is the host reachable?
- Is DNS resolving?
- Is the port open?
- Is the service responding?

You solve incidents faster.

---

**Day 14 Complete**
