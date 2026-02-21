# Day 29 – Introduction to Docker

## Overview

This project documents my Day 29 progress in the 90 Days of DevOps journey. The focus of this day was to understand Docker basics, install Docker, run the first container, and practice common container management commands.

Docker is a core DevOps tool used to package applications and their dependencies into lightweight containers. These containers can run consistently across local machines, servers, CI/CD pipelines, and cloud environments.

---

## What I Learned

- What Docker is and why containers are used
- Difference between containers and virtual machines
- Basic Docker architecture
- Docker client, daemon, images, containers, and registry
- How to run a test container using `hello-world`
- How to run an Nginx web server container
- How to run Ubuntu in interactive mode
- How to list, stop, remove, and inspect containers
- How to check container logs
- How to execute commands inside a running container

---

## Project Structure

```text
2026/day-29/
├── README.md
├── day-29-docker-basics.md
├── task.md
└── screenshots/
    ├── 01-docker-version.png
    ├── 02-docker-info.png
    ├── 03-hello-world-container.png
    ├── 04-nginx-container-running.png
    ├── 05-nginx-browser-page.png
    ├── 06-ubuntu-interactive-container.png
    ├── 07-running-containers.png
    ├── 08-all-containers.png
    ├── 09-stop-nginx-container.png
    ├── 10-remove-nginx-container.png
    ├── 11-detached-named-port-container.png
    ├── 12-nginx-container-logs.png
    ├── 13-exec-inside-container.png
    └── 14-cleanup-containers.png
```

---

## Docker Architecture

Docker follows a client-server architecture.

```text
User
 |
 | docker command
 v
Docker Client
 |
 | request
 v
Docker Daemon
 |
 | pulls image if needed
 v
Docker Hub / Registry
 |
 | image
 v
Docker Image
 |
 | creates
 v
Docker Container
```

### Main Components

| Component        | Description                                              |
| ---------------- | -------------------------------------------------------- |
| Docker Client    | CLI used to run Docker commands                          |
| Docker Daemon    | Background service that manages Docker objects           |
| Docker Image     | Read-only template used to create containers             |
| Docker Container | Running instance of a Docker image                       |
| Docker Registry  | Place where Docker images are stored and downloaded from |

---

## Containers vs Virtual Machines

| Feature          | Containers                               | Virtual Machines        |
| ---------------- | ---------------------------------------- | ----------------------- |
| Startup Speed    | Fast                                     | Slower                  |
| Size             | Lightweight                              | Heavy                   |
| Operating System | Shares host OS kernel                    | Runs a full guest OS    |
| Resource Usage   | Low                                      | High                    |
| Portability      | High                                     | Moderate                |
| Best Use Case    | Application deployment and microservices | Full OS-level isolation |

Containers are faster and lighter because they share the host operating system kernel. Virtual machines are heavier because each VM runs a complete operating system.

---

## Commands Practiced

### Check Docker Version

```bash
docker --version
```

### Check Docker System Information

```bash
docker info
```

### Run Hello World Container

```bash
docker run hello-world
```

### Run Nginx Container

```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

### Run Ubuntu Container Interactively

```bash
docker run -it ubuntu bash
```

### List Running Containers

```bash
docker ps
```

### List All Containers

```bash
docker ps -a
```

### Stop a Container

```bash
docker stop my-nginx
```

### Remove a Container

```bash
docker rm my-nginx
```

### Run Container in Detached Mode with Custom Name and Port Mapping

```bash
docker run -d -p 8081:80 --name nginx-explore nginx
```

### Check Container Logs

```bash
docker logs nginx-explore
```

### Execute Command Inside a Running Container

```bash
docker exec -it nginx-explore sh
```

### Clean Up Container

```bash
docker stop nginx-explore
docker rm nginx-explore
```

---

## Screenshots

| Screenshot                             | Description                                         |
| -------------------------------------- | --------------------------------------------------- |
| `01-docker-version.png`                | Verified Docker installation                        |
| `02-docker-info.png`                   | Checked Docker daemon and system details            |
| `03-hello-world-container.png`         | Ran first Docker container                          |
| `04-nginx-container-running.png`       | Started Nginx container                             |
| `05-nginx-browser-page.png`            | Accessed Nginx from browser                         |
| `06-ubuntu-interactive-container.png`  | Explored Ubuntu container interactively             |
| `07-running-containers.png`            | Listed running containers                           |
| `08-all-containers.png`                | Listed all containers                               |
| `09-stop-nginx-container.png`          | Stopped Nginx container                             |
| `10-remove-nginx-container.png`        | Removed Nginx container                             |
| `11-detached-named-port-container.png` | Tested detached mode, custom name, and port mapping |
| `12-nginx-container-logs.png`          | Checked Nginx container logs                        |
| `13-exec-inside-container.png`         | Executed commands inside running container          |
| `14-cleanup-containers.png`            | Cleaned up containers                               |

---

## Key Observation

While exploring the Nginx container using `docker exec`, the `ps` command was not available.

```text
sh: 2: ps: not found
```

This happened because official Docker images are often minimal and only include the packages required to run the application.

This is useful in real DevOps environments because minimal images are:

- Smaller in size
- Faster to pull and run
- Easier to secure
- Better for production deployments

---

## Key Takeaways

- Docker containers package applications with their dependencies.
- Containers are lightweight compared to virtual machines.
- Docker images are templates used to create containers.
- Containers are running instances of images.
- Docker Hub is used to pull public images.
- Port mapping connects host ports to container ports.
- Detached mode runs containers in the background.
- `docker logs` helps troubleshoot containers.
- `docker exec` is useful for inspecting running containers.
- Docker is a foundation for Kubernetes and cloud-native deployments.

---

## Why This Matters for DevOps

Docker is one of the most important tools in DevOps. It helps teams build, test, ship, and run applications consistently.

In real DevOps workflows, Docker is used for:

- CI/CD pipelines
- Application packaging
- Microservices deployments
- Local development environments
- Cloud deployments
- Kubernetes workloads
- Testing and debugging application environments

Learning Docker is an important step toward becoming job-ready in DevOps.

---

## Final Status

Day 29 completed successfully.

Completed tasks:

- Docker installation verified
- Docker daemon checked
- `hello-world` container executed
- Nginx container deployed
- Nginx accessed from browser
- Ubuntu container explored interactively
- Running and stopped containers listed
- Containers stopped and removed
- Detached mode practiced
- Port mapping practiced
- Container logs checked
- Commands executed inside a running container
- Cleanup completed
