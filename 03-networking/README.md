# Networking Fundamentals for DevOps (Day 14 & Day 15)

## Overview

This module documents my hands-on learning and notes on **Networking Fundamentals**, an essential skillset for DevOps and Cloud Engineers.

Over these two days, I focused on understanding:

- How networks communicate
- How devices identify each other
- How DNS resolves domain names
- How subnets work
- How ports enable application communication
- Practical troubleshooting using Linux networking commands

This foundation is critical for working with:

- Cloud Infrastructure
- Kubernetes Networking
- Load Balancers
- Reverse Proxies
- CI/CD Deployments
- DNS Management
- Security Groups / Firewalls
- Monitoring & Troubleshooting

---

## Learning Goals

By completing this module, I aimed to:

- Understand core networking concepts in simple terms
- Learn how packets move across networks
- Practice Linux networking commands used in real DevOps troubleshooting
- Build confidence in diagnosing connectivity issues
- Create reusable notes for future reference

---

# Day 14 — Networking Fundamentals & Hands-on Checks

## Topics Covered

### OSI Model

Studied the 7 layers of networking:

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

Learned how each layer contributes to communication between systems.

---

### TCP/IP Model

Understood the practical Internet communication stack:

- Network Access
- Internet
- Transport
- Application

Mapped it against the OSI model.

---

### Core Networking Commands Practiced

```bash
ip addr
ip route
ping
curl
ss -tulpn
netstat -tulpn
traceroute
dig
nslookup
```

Learned how these commands help troubleshoot:

- DNS failures
- Connection issues
- Port conflicts
- Routing problems
- Service availability

---

### Practical Checks Performed

Verified:

- Local IP address
- Default gateway
- DNS resolution
- Public internet connectivity
- Open listening ports
- Active network routes

---

## Files

```bash
day-14/
├── screenshots/
├── day-14-networking.md
├── reference.md
└── README.md
```

---

# Day 15 — Networking Concepts (DNS, IP, Subnets & Ports)

## Topics Covered

### DNS

Learned how domain names resolve into IP addresses.

Studied DNS records:

- A
- AAAA
- CNAME
- MX
- TXT
- NS

Understood the DNS lookup flow:

Browser → Resolver → Root → TLD → Authoritative DNS → IP Address

---

### IP Addressing

Covered:

- IPv4 basics
- Public IP vs Private IP
- Loopback addresses
- NAT concept
- CIDR notation

Examples:

```text
192.168.1.10/24
10.0.0.0/16
172.16.0.0/12
```

---

### Subnetting Basics

Learned:

- Network portion
- Host portion
- Subnet masks
- Available hosts calculation

Example:

```text
192.168.1.0/24 → 256 addresses
Usable hosts → 254
```

---

### Common Ports

Studied frequently used ports:

| Port | Service     |
| ---- | ----------- |
| 22   | SSH         |
| 53   | DNS         |
| 80   | HTTP        |
| 443  | HTTPS       |
| 3306 | MySQL       |
| 5432 | PostgreSQL  |
| 6379 | Redis       |
| 8080 | App Servers |

---

### DevOps Connection

Connected networking concepts to:

- Reverse Proxy setup
- Kubernetes Services
- Ingress Controllers
- Security Groups
- Nginx
- Docker networking
- Cloud VPC networking

---

# Key Takeaways

After completing Day 14 & Day 15:

- I can inspect network interfaces
- I understand DNS resolution flow
- I know how IP addressing works
- I understand CIDR and subnet basics
- I can identify common ports/services
- I can troubleshoot basic networking issues using Linux tools

---

# Repository Structure

```bash
03-networking/
├── day-14/
│   ├── screenshots/
│   ├── day-14-networking.md
│   ├── reference.md
│   └── README.md
│
├── day-15/
│   ├── screenshots/
│   ├── day-15-networking-concepts.md
│   ├── reference.md
│   └── README.md
│
└── README.md
```

---

## Progress

Networking Fundamentals Module Completed:

- Day 14: Completed
- Day 15: Completed

Continuing forward in **#90DaysOfDevOps** toward becoming job-ready in DevOps & Cloud Engineering.
