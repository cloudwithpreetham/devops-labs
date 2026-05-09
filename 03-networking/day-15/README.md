# Day 15 – Networking Concepts: DNS, IP, Subnets & Ports

## Overview

Day 15 focused on understanding the core networking concepts every DevOps engineer must know. This included learning how DNS resolves domain names, understanding IPv4 addressing, CIDR notation, subnetting basics, and identifying common network ports used by services.

This day combined both theory and hands-on validation using Linux networking commands.

---

## Topics Covered

### DNS (Domain Name System)

- How domain names resolve to IP addresses
- DNS lookup flow:
  - Local cache
  - Recursive resolver
  - Root DNS servers
  - TLD servers
  - Authoritative DNS servers

- DNS record types:
  - A
  - AAAA
  - CNAME
  - MX
  - NS

---

### IP Addressing

- IPv4 structure
- Public vs Private IPs
- Private IP ranges:
  - `10.0.0.0/8`
  - `172.16.0.0/12`
  - `192.168.0.0/16`

- Identifying local/private IP using:

```bash
ip addr show
```

---

### CIDR & Subnetting

- Understanding CIDR notation
- Network bits vs Host bits
- Host calculation examples:
  - `/24`
  - `/16`
  - `/28`

- Subnet masks and usable host ranges
- Why subnetting matters in cloud networking

---

### Ports & Services

Common service ports:

| Port  | Service |
| ----- | ------- |
| 22    | SSH     |
| 53    | DNS     |
| 80    | HTTP    |
| 443   | HTTPS   |
| 3306  | MySQL   |
| 6379  | Redis   |
| 27017 | MongoDB |

Understanding listening services using:

```bash
ss -tulpn
```

---

## Hands-on Commands Used

```bash
dig google.com
ip addr show
ss -tulpn
```

Additional useful commands:

```bash
curl -v https://google.com
ping google.com
nslookup google.com
```

---

## Files in this Directory

```text
day-15/
├── screenshots/
├── day-15-networking-concepts.md
├── referance.md
└── README.md
```

---

## Key Learnings

- DNS converts human-readable names into IP addresses.
- Private IP addressing is foundational in cloud environments like AWS VPCs.
- CIDR notation helps design scalable and efficient networks.
- Ports allow multiple services to communicate on a single machine.
- Linux networking commands are essential for troubleshooting.

---

## Outcome

This day strengthened practical networking fundamentals required for:

- Linux administration
- Cloud networking
- Kubernetes networking
- Service troubleshooting
- DevOps production debugging

---

**Day 15 complete.**
