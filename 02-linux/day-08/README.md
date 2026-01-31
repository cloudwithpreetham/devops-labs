# Day 08 – Cloud Server Setup: Docker, Nginx & Web Deployment

## Overview

Day 08 focused on deploying and managing a real cloud server on AWS EC2, installing Docker and Nginx, configuring network access, and validating deployment through logs and browser testing.

This hands-on exercise introduced practical DevOps concepts around infrastructure provisioning, service deployment, cloud networking, and observability.

---

## Objectives

- Launch a cloud VM using AWS EC2
- Connect securely using SSH
- Install and configure Docker
- Install and manage Nginx
- Configure Security Group rules for HTTP access
- Validate service availability from the internet
- Extract and analyze Nginx access logs

---

## Project Structure

```text
day-08/
├── screenshots/
│   ├── ssh-connection.png
│   ├── system-update.png
│   ├── docker-installation.png
│   ├── nginx-running.png
│   ├── nginx-webpage.png
│   └── nginx-access-logs.png
├── day-08-cloud-deployment.md
├── nginx-logs.txt
├── reference.md
└── README.md
```

---

## Tech Stack

- AWS EC2 (Ubuntu 24.04 LTS)
- Linux
- Docker
- Nginx
- SSH
- AWS Security Groups

---

## Key Commands Used

### Connect to Server

```bash
ssh -i linux-server-key.pem ubuntu@<public-ip>
```

### Update Packages

```bash
sudo apt update && sudo apt upgrade -y
```

### Install Docker

```bash
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
docker --version
```

### Install Nginx

```bash
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

### Verify Service

```bash
curl http://localhost
```

### Check Listening Port

```bash
sudo ss -tulnp | grep 80
```

### View Logs

```bash
sudo cat /var/log/nginx/access.log
```

---

## Challenges Solved

### Network Timeout Issue

Initially, the public IP was unreachable.

**Root Cause**

- HTTP (Port 80) was not allowed in the AWS Security Group.

**Fix**

- Added inbound HTTP rule:
  - Protocol: TCP
  - Port: 80
  - Source: 0.0.0.0/0

**Result**

- Nginx became accessible publicly from browser.

---

## What I Learned

- How to provision and access cloud servers
- Installing and managing Linux services
- Docker setup on cloud VMs
- Cloud firewall / Security Group basics
- Debugging service vs network problems
- Reading and interpreting access logs

---

## DevOps Concepts Practiced

- Infrastructure provisioning
- Remote server administration
- Service deployment
- Networking & security
- Monitoring through logs
- Troubleshooting methodology

---

## Outcome

Successfully deployed a public-facing Nginx server on AWS EC2, validated access from the browser, and captured access logs for observability.

This was a practical introduction to real-world server deployment workflows used in DevOps environments.
