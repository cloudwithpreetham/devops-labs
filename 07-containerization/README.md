# 07 - Containerization

This section documents my hands-on learning journey with Docker and containerization as part of my 90 Days of DevOps challenge.

The goal of this module is to understand how containers work, how to build Docker images, manage container storage and networking, use Docker Compose, optimize images, and finally Dockerize a complete application.

---

## Topics Covered

- Introduction to Docker
- Running and managing containers
- Docker images and containers
- Dockerfile basics
- Building custom images
- Docker volumes
- Docker networking
- Docker Compose
- Multi-container applications
- Multi-stage Docker builds
- Docker Hub image publishing
- End-to-end application Dockerization
- Docker revision and cheat sheet

---

## Folder Structure

```text
07-containerization/
├── day-29/
├── day-30/
├── day-31/
├── day-32/
├── day-33/
├── day-34/
├── day-35/
├── day-36/
└── day-37/
```

---

## Daily Progress

| Day    | Topic                           | Description                                                                        |
| ------ | ------------------------------- | ---------------------------------------------------------------------------------- |
| Day 29 | Docker Basics                   | Learned what Docker is, why containers are useful, and ran the first container     |
| Day 30 | Docker Commands                 | Practiced container lifecycle commands, image management, logs, and cleanup        |
| Day 31 | Dockerfile                      | Created custom Docker images using Dockerfiles                                     |
| Day 32 | Volumes & Networking            | Learned data persistence using volumes and container communication using networks  |
| Day 33 | Docker Compose Basics           | Used Docker Compose to run multi-container applications                            |
| Day 34 | Advanced Docker Compose         | Built production-like stacks with healthchecks, dependencies, and restart policies |
| Day 35 | Multi-Stage Builds & Docker Hub | Built optimized images and pushed images to Docker Hub                             |
| Day 36 | Docker Project                  | Dockerized a full application end-to-end                                           |
| Day 37 | Docker Revision                 | Revised Docker concepts and created a Docker cheat sheet                           |

---

## Key Docker Commands Practiced

```bash
docker --version
docker pull nginx
docker run hello-world
docker ps
docker ps -a
docker stop <container_id>
docker rm <container_id>
docker images
docker rmi <image_id>
docker build -t app-name .
docker run -d -p 8080:80 app-name
docker volume create my-volume
docker network create my-network
docker compose up -d
docker compose down
docker login
docker push username/image-name:tag
```

---

## Skills Practiced

By completing this section, I practiced:

- Running containers from Docker Hub
- Managing containers and images
- Writing Dockerfiles from scratch
- Building and tagging custom Docker images
- Understanding image layers and Docker cache
- Using named volumes and bind mounts
- Creating custom Docker networks
- Connecting multiple containers
- Writing `docker-compose.yml` files
- Managing environment variables with `.env`
- Building optimized images using multi-stage builds
- Publishing images to Docker Hub
- Dockerizing a complete application

---

## Important Concepts Learned

### Container

A container is a lightweight, isolated environment used to run an application and its dependencies consistently across different systems.

### Image

An image is a read-only template used to create containers.

### Dockerfile

A Dockerfile contains instructions to build a custom Docker image.

### Volume

A volume is used to persist data even after a container is stopped or removed.

### Network

A Docker network allows containers to communicate with each other.

### Docker Compose

Docker Compose is used to define and manage multi-container applications using a YAML file.

### Multi-Stage Build

A multi-stage build helps reduce image size by separating build-time dependencies from runtime dependencies.

---

## Real-World DevOps Relevance

Docker is widely used in DevOps because it helps teams:

- Package applications consistently
- Avoid environment mismatch issues
- Run applications locally, in CI/CD pipelines, and in production
- Build portable and repeatable deployments
- Simplify microservice-based application setups
- Improve development and deployment workflows

---

## Final Outcome

After completing Days 29 to 37, I now have a strong foundation in Docker and containerization. I can build, run, manage, optimize, and publish Docker-based applications using real-world DevOps practices.

This section prepares me for the next stage of my DevOps journey: Kubernetes and container orchestration.

---

## Status

Completed: Days 29 to 37
Module: Containerization
Focus Tool: Docker
