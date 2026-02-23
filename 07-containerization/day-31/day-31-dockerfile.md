# Day 31 – Dockerfile: Build Your Own Images

## Objective

The goal of Day 31 was to learn how to write Dockerfiles, build custom Docker images, and run containers from those images.

Dockerfiles are important in DevOps because they allow applications and environments to be packaged in a repeatable, portable, and production-ready way.

---

## Project Structure

```bash
2026/day-31/
├── day-31-dockerfile.md
├── task.md
├── screenshots
├── my-first-image/
│   └── Dockerfile
├── dockerfile-instructions/
│   ├── Dockerfile
│   └── app.txt
├── cmd-vs-entrypoint/
│   ├── Dockerfile.cmd
│   └── Dockerfile.entrypoint
├── simple-web-app/
│   ├── Dockerfile
│   ├── index.html
│   └── .dockerignore
└── optimized-build/
    ├── Dockerfile
    └── index.html
```

---

## Task 1: Your First Dockerfile

### Dockerfile Used

```Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl

CMD ["echo", "Hello from my custom image!"]
```

### Commands Used

```bash
mkdir -p ~/docker/day-31/my-first-image
cd ~/docker/day-31/my-first-image
```

```bash
docker build -t my-ubuntu:v1 .
```

```bash
docker run my-ubuntu:v1
```

### Output

```bash
Hello from my custom image!
```

### What I Learned

- `FROM` defines the base image.
- `RUN` executes commands while the image is being built.
- `CMD` defines the default command that runs when the container starts.
- Docker images can be tagged using `name:tag` format.

---

## Task 2: Dockerfile Instructions

### Files Created

```bash
dockerfile-instructions/
├── Dockerfile
└── app.txt
```

### app.txt

```text
This file was copied into the Docker image.
```

### Dockerfile Used

```Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY app.txt /app/app.txt

EXPOSE 8080

CMD ["cat", "/app/app.txt"]
```

### Commands Used

```bash
cd ~/docker/day-31/dockerfile-instructions
```

```bash
docker build -t dockerfile-instructions:v1 .
```

```bash
docker run dockerfile-instructions:v1
```

### Output

```bash
This file was copied into the Docker image.
```

### Dockerfile Instructions Explained

| Instruction | Purpose                                               |
| ----------- | ----------------------------------------------------- |
| `FROM`      | Defines the base image used to build the image        |
| `RUN`       | Runs commands during image build time                 |
| `WORKDIR`   | Sets the working directory inside the container image |
| `COPY`      | Copies files from the host machine into the image     |
| `EXPOSE`    | Documents the port the container is expected to use   |
| `CMD`       | Defines the default command for the container         |

### What I Learned

Dockerfile instructions are executed layer by layer. Each instruction creates a layer in the final image. This makes Docker images reusable and cache-friendly.

---

## Task 3: CMD vs ENTRYPOINT

## Part A: CMD

### Dockerfile.cmd

```Dockerfile
FROM ubuntu:latest

CMD ["echo", "hello"]
```

### Commands Used

```bash
cd ~/docker/day-31/cmd-vs-entrypoint
```

```bash
docker build -f Dockerfile.cmd -t cmd-demo:v1 .
```

```bash
docker run cmd-demo:v1
```

### Output

```bash
hello
```

### Custom Command Test

```bash
docker run cmd-demo:v1 echo "Hello, Preetham!"
```

### Output

```bash
Hello, Preetham!
```

### CMD Observation

When a command is passed during `docker run`, it overrides the default `CMD` instruction.

---

## Part B: ENTRYPOINT

### Dockerfile.entrypoint

```Dockerfile
FROM ubuntu:latest

ENTRYPOINT ["echo"]
```

### Commands Used

```bash
docker build -f Dockerfile.entrypoint -t entrypoint-demo:v1 .
```

```bash
docker run entrypoint-demo:v1
```

```bash
docker run entrypoint-demo:v1 "hello from entrypoint"
```

### Output

```bash
hello from entrypoint
```

### ENTRYPOINT Observation

`ENTRYPOINT` defines the main executable for the container. Any arguments passed during `docker run` are added to the `ENTRYPOINT` command.

---

## CMD vs ENTRYPOINT Summary

| Feature               | CMD                                   | ENTRYPOINT                        |
| --------------------- | ------------------------------------- | --------------------------------- |
| Purpose               | Provides default command or arguments | Defines the main executable       |
| CLI override behavior | Easily overridden                     | Arguments are appended by default |
| Best use case         | Default behavior that may change      | Fixed container behavior          |

### When to Use CMD

Use `CMD` when the command should be replaceable by the user.

Example:

```Dockerfile
CMD ["python", "app.py"]
```

### When to Use ENTRYPOINT

Use `ENTRYPOINT` when the container should always run a specific executable.

Example:

```Dockerfile
ENTRYPOINT ["echo"]
```

---

## Task 4: Build a Simple Web App Image

### Files Created

```bash
simple-web-app/
├── Dockerfile
├── index.html
└── .dockerignore
```

### index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Day 31 Docker Web App</title>
  </head>
  <body>
    <h1>Hello from my custom Nginx Docker image!</h1>
    <p>This web page is running inside a Docker container.</p>
    <p>Day 31 - Dockerfile Practice</p>
  </body>
</html>
```

### Dockerfile Used

```Dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Commands Used

```bash
cd ~/docker/day-31/simple-web-app
```

```bash
docker build -t my-website:v1 .
```

```bash
docker run -d -p 8080:80 --name my-website-container my-website:v1
```

```bash
docker ps
```

### Browser Access

```text
http://54.200.67.162:8080
```

### Result

The custom Nginx website was successfully served from a Docker container and accessed through the browser.

### What I Learned

- `nginx:alpine` is a lightweight image useful for serving static websites.
- Nginx serves static files from `/usr/share/nginx/html/`.
- Port mapping allows access to container services from the host machine.
- `-p 8080:80` maps host port `8080` to container port `80`.

---

## Task 5: .dockerignore

### .dockerignore File

```text
node_modules
.git
*.md
.env
```

### Command Used

```bash
docker build -t my-website:v2 .
```

### Purpose of .dockerignore

The `.dockerignore` file prevents unnecessary files from being included in the Docker build context.

### Why It Matters

- Keeps Docker images clean.
- Prevents sensitive files like `.env` from being copied.
- Reduces build context size.
- Improves build speed.
- Avoids including unnecessary files such as `.git` and `node_modules`.

### What I Learned

A `.dockerignore` file works similarly to `.gitignore`, but for Docker build context. It is a best practice for real-world Docker projects.

---

## Task 6: Build Optimization

### Files Created

```bash
optimized-build/
├── Dockerfile
└── index.html
```

### Dockerfile Used

```Dockerfile
FROM nginx:alpine

WORKDIR /usr/share/nginx/html

COPY index.html index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Commands Used

```bash
cd ~/docker/day-31/optimized-build
```

```bash
docker build -t optimized-web:v1 .
```

After changing one line in `index.html`, the image was rebuilt:

```bash
docker build -t optimized-web:v2 .
```

### Observation

Docker reused cached layers where possible. Only the changed layer and the layers after it were rebuilt.

### Why Layer Order Matters

Docker builds images layer by layer. If an early layer changes, Docker must rebuild that layer and every layer after it.

For faster builds, stable instructions should be placed near the top and frequently changing instructions should be placed near the bottom.

### Good Dockerfile Layer Order

```Dockerfile
FROM base-image
RUN install dependencies
WORKDIR /app
COPY dependency files first
RUN install dependencies
COPY application source code last
CMD start command
```

### What I Learned

Docker cache improves build speed. A well-ordered Dockerfile saves time during development and CI/CD pipeline execution.

---

## Docker Images Built

| Image Name                   | Purpose                                         |
| ---------------------------- | ----------------------------------------------- |
| `my-ubuntu:v1`               | Basic Ubuntu custom image                       |
| `dockerfile-instructions:v1` | Image demonstrating Dockerfile instructions     |
| `cmd-demo:v1`                | CMD behavior demo                               |
| `entrypoint-demo:v1`         | ENTRYPOINT behavior demo                        |
| `my-website:v1`              | Static Nginx website image                      |
| `my-website:v2`              | Static Nginx website image with `.dockerignore` |
| `optimized-web:v2`           | Docker cache optimization example               |

---

## Commands Practiced

```bash
# Build image
docker build -t image-name:tag .

# Build using a specific Dockerfile
docker build -f Dockerfile.cmd -t cmd-demo:v1 .

# Run container
docker run image-name:tag

# Run container in detached mode
docker run -d image-name:tag

# Run container with port mapping
docker run -d -p 8080:80 image-name:tag

# List running containers
docker ps

# List Docker images
docker images

# Stop container
docker stop container_name

# Remove stopped containers
docker container prune
```

---

## Issues Faced

### Docker Build Warning

During the build, Docker displayed this warning:

```bash
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
Install the buildx component to build images with BuildKit.
```

### Meaning

Docker is recommending the newer BuildKit-based builder instead of the legacy builder.

### Future Improvement

Install and use Buildx for modern Docker builds:

```bash
docker buildx version
```

---

## Final Learning Summary

In this task, I learned how to:

- Write Dockerfiles from scratch.
- Build custom Docker images.
- Run containers from custom images.
- Use core Dockerfile instructions like `FROM`, `RUN`, `COPY`, `WORKDIR`, `EXPOSE`, `CMD`, and `ENTRYPOINT`.
- Understand the difference between `CMD` and `ENTRYPOINT`.
- Build a static website using `nginx:alpine`.
- Use `.dockerignore` to control the Docker build context.
- Understand Docker layer caching and build optimization.

---

## Real-World DevOps Takeaway

Dockerfiles are the foundation of containerized application delivery. In real DevOps projects, Dockerfiles are used in CI/CD pipelines, Kubernetes deployments, cloud container services, and production releases.

A good Dockerfile should be:

- Simple
- Reproducible
- Secure
- Optimized
- Easy to understand

This task helped me move from simply running Docker containers to building and shipping custom Docker images.
