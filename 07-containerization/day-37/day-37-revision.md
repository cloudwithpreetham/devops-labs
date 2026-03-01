# Day 37 – Docker Revision & Cheat Sheet

## Goal

The goal of Day 37 was to revise and consolidate Docker concepts learned from Days 29 to 36.

This revision focused on:

- Docker basics
- Containers and images
- Dockerfiles
- Volumes
- Networks
- Docker Compose
- Multi-stage builds
- Docker Hub
- Healthchecks
- Cleanup commands

---

## Self-Assessment Checklist

| Topic                                                    | Status |
| -------------------------------------------------------- | ------ |
| Run a container from Docker Hub interactive and detached | Can do |
| List, stop, remove containers and images                 | Can do |
| Explain image layers and caching                         | Can do |
| Write a Dockerfile using FROM, RUN, COPY, WORKDIR, CMD   | Can do |
| Explain CMD vs ENTRYPOINT                                | Shaky  |
| Build and tag a custom image                             | Can do |
| Create and use named volumes                             | Can do |
| Use bind mounts                                          | Can do |
| Create custom networks and connect containers            | Can do |
| Write a docker-compose.yml for a multi-container app     | Can do |
| Use environment variables and .env files in Compose      | Can do |
| Write a multi-stage Dockerfile                           | Shaky  |
| Push an image to Docker Hub                              | Can do |
| Use healthchecks and depends_on                          | Can do |

---

## Quick-Fire Questions

### 1. What is the difference between an image and a container?

An image is a read-only template used to create containers.

A container is a running instance of an image.

Example:

```bash
docker pull nginx
docker run nginx
```

Here, `nginx` is the image and the running process created from it is the container.

---

### 2. What happens to data inside a container when you remove it?

Data written inside the container filesystem is deleted when the container is removed.

To keep data permanently, we should use:

- Named volumes
- Bind mounts

Example:

```bash
docker run -v app_data:/data nginx
```

This keeps `/data` persistent even if the container is removed.

---

### 3. How do two containers on the same custom network communicate?

Containers on the same custom Docker network can communicate using container names or service names.

Example:

```bash
docker network create app_network

docker run -d --name backend --network app_network backend-image
docker run -d --name frontend --network app_network frontend-image
```

The `frontend` container can reach the backend using:

```bash
http://backend:<port>
```

In Docker Compose, services communicate using service names.

Example:

```yaml
services:
  app:
    depends_on:
      - db

  db:
    image: postgres
```

The app can connect to the database using hostname:

```bash
db
```

---

### 4. What does `docker compose down -v` do differently from `docker compose down`?

`docker compose down` stops and removes:

- Containers
- Default Compose network

`docker compose down -v` does the same thing, but also removes volumes created by Compose.

This means database data stored in Compose volumes can be deleted when using:

```bash
docker compose down -v
```

Use this command carefully.

---

### 5. Why are multi-stage builds useful?

Multi-stage builds help create smaller and cleaner Docker images.

They are useful because:

- Build tools stay in the builder stage
- Final image contains only runtime files
- Image size becomes smaller
- Security improves because fewer packages are included
- Production images become cleaner

Example:

```dockerfile
FROM node:20 AS builder
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

---

### 6. What is the difference between `COPY` and `ADD`?

`COPY` copies files and folders from the host into the image.

`ADD` can also copy files, but it has extra features:

- Can extract local compressed archives
- Can fetch files from URLs

Best practice:

Use `COPY` unless you specifically need `ADD`.

Example:

```dockerfile
COPY app.py /app/app.py
```

---

### 7. What does `-p 8080:80` mean?

`-p 8080:80` maps a port from the host machine to a port inside the container.

Format:

```bash
host_port:container_port
```

Example:

```bash
docker run -d -p 8080:80 nginx
```

This means:

- Open browser on host: `http://localhost:8080`
- Request goes to container port `80`

---

### 8. How do you check how much disk space Docker is using?

Use:

```bash
docker system df
```

This shows disk usage for:

- Images
- Containers
- Local volumes
- Build cache

For detailed output:

```bash
docker system df -v
```

---

## Weak Spots Selected

I selected these two weak areas for revision:

1. CMD vs ENTRYPOINT
2. Multi-stage Dockerfile

---

## Weak Spot 1: CMD vs ENTRYPOINT

### CMD

`CMD` provides the default command for a container.

It can be overridden from the command line.

Example:

```dockerfile
FROM ubuntu
CMD ["echo", "Hello from CMD"]
```

Run:

```bash
docker build -t cmd-demo .
docker run cmd-demo
docker run cmd-demo echo "Overridden command"
```

The second command overrides the default `CMD`.

---

### ENTRYPOINT

`ENTRYPOINT` defines the main executable for the container.

It is not easily overridden.

Example:

```dockerfile
FROM ubuntu
ENTRYPOINT ["echo"]
CMD ["Hello from ENTRYPOINT"]
```

Run:

```bash
docker build -t entrypoint-demo .
docker run entrypoint-demo
docker run entrypoint-demo "Custom message"
```

The container always runs `echo`, but the message can change.

---

### Difference Between CMD and ENTRYPOINT

| Feature              | CMD                          | ENTRYPOINT               |
| -------------------- | ---------------------------- | ------------------------ |
| Purpose              | Default command or arguments | Main executable          |
| Easy to override     | Yes                          | Not usually              |
| Common use           | Default app command          | Fixed container behavior |
| Works with arguments | Yes                          | Yes, usually with CMD    |

Best practice:

Use `ENTRYPOINT` when the container should always run a specific executable.

Use `CMD` to provide default arguments.

---

## Weak Spot 2: Multi-Stage Dockerfile

### Problem with Single-Stage Builds

A single-stage Dockerfile may include unnecessary build tools in the final image.

Example:

```dockerfile
FROM node:20
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "start"]
```

This image may be large because it contains:

- Source code
- Build dependencies
- Development tools
- Cache files

---

### Multi-Stage Build Example

```dockerfile
FROM node:20 AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

---

### Why This Is Better

The first stage builds the application.

The second stage only keeps the final output needed to run the application.

Benefits:

- Smaller image
- Cleaner production image
- Better security
- Faster deployment
- No unnecessary build tools in final image

---

## Docker Revision Commands Practiced

```bash
docker run -it ubuntu bash
docker run -d --name web -p 8080:80 nginx
docker ps
docker ps -a
docker stop web
docker rm web
docker images
docker rmi nginx
docker build -t myapp:v1 .
docker tag myapp:v1 username/myapp:v1
docker push username/myapp:v1
docker volume create app_data
docker volume ls
docker network create app_network
docker network ls
docker compose up -d
docker compose ps
docker compose logs
docker compose down
docker compose down -v
docker system df
docker system prune
```

---

## Folder Structure

```bash
2026/
└── day-37/
    ├── docker-cheatsheet.md
    └── day-37-revision.md
```

---

## Learn in Public Post

Today I completed Day 37 of my 90 Days of DevOps journey.

I revised Docker concepts from Days 29 to 36 and created a practical Docker cheat sheet covering:

- Container commands
- Image commands
- Volumes
- Networks
- Docker Compose
- Dockerfile instructions
- Cleanup commands
- Multi-stage builds

This revision helped me strengthen my Docker fundamentals and identify weak areas like CMD vs ENTRYPOINT and multi-stage builds.

#90DaysOfDevOps
#DevOpsKaJosh
#TrainWithShubham
