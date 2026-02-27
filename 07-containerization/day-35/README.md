# Day 35 – Multi-Stage Builds & Docker Hub

## Overview

This project demonstrates how to build optimized Docker images using multi-stage builds and publish them to Docker Hub.

The main goal was to compare a large single-stage Docker image with a smaller production-ready multi-stage image.

---

## Project Structure

```text
day-35/
├── README.md
├── task.md
├── day-35-multistage-hub.md
├── go-multistage-app/
│   ├── main.go
│   ├── Dockerfile.single
│   ├── Dockerfile.multistage
│   └── Dockerfile.best-practice
└── screenshots/
```

---

## Application

The project uses a simple Go application.

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello from Day 35 - Multi-Stage Docker Build!")
}
```

---

## Dockerfiles

### `Dockerfile.single`

This Dockerfile builds and runs the Go application in a single stage.

It uses the full Go image, which makes the final image large.

### `Dockerfile.multistage`

This Dockerfile uses a builder stage and a runtime stage.

The Go compiler and build tools stay in the builder stage. Only the compiled binary is copied into the final Alpine image.

### `Dockerfile.best-practice`

This Dockerfile improves the multi-stage image by:

- Using a minimal runtime image
- Using a specific base image tag
- Running the application as a non-root user
- Copying only the compiled binary into the final image
- Reducing the binary size with Go linker flags

---

## Commands Used

### Build Single-Stage Image

```bash
cd go-multistage-app
docker build -t day35-go-single:v1 -f Dockerfile.single .
```

### Run Single-Stage Image

```bash
docker run --rm day35-go-single:v1
```

### Build Multi-Stage Image

```bash
docker build -t day35-go-multistage:v1 -f Dockerfile.multistage .
```

### Run Multi-Stage Image

```bash
docker run --rm day35-go-multistage:v1
```

### Build Best-Practice Image

```bash
docker build -t day35-go-best:v1 -f Dockerfile.best-practice .
```

### Run Best-Practice Image

```bash
docker run --rm day35-go-best:v1
```

---

## Image Size Comparison

| Image                    | Disk Usage | Content Size |
| ------------------------ | ---------: | -----------: |
| `day35-go-single:v1`     |   `1.25GB` |      `306MB` |
| `day35-go-multistage:v1` |   `15.2MB` |      `4.8MB` |
| `day35-go-best:v1`       |   `15.8MB` |     `4.78MB` |

---

## Docker Hub

The optimized multi-stage image was tagged and pushed to Docker Hub.

### Docker Hub Repository

```text
https://hub.docker.com/r/h4kops/day35-go-multistage
```

### Tags Used

| Tag      | Description            |
| -------- | ---------------------- |
| `v1`     | Versioned image tag    |
| `latest` | Latest image reference |

---

## Docker Hub Commands

### Login

```bash
docker login
```

### Tag Image

```bash
docker tag day35-go-multistage:v1 h4kops/day35-go-multistage:v1
docker tag day35-go-multistage:v1 h4kops/day35-go-multistage:latest
```

### Push Image

```bash
docker push h4kops/day35-go-multistage:v1
docker push h4kops/day35-go-multistage:latest
```

### Pull and Verify

```bash
docker pull h4kops/day35-go-multistage:v1
docker run --rm h4kops/day35-go-multistage:v1
```

Expected output:

```text
Hello from Day 35 - Multi-Stage Docker Build!
```

---

## Key Learnings

- Single-stage Docker images can become very large.
- Multi-stage builds reduce image size by separating build and runtime stages.
- The final production image should contain only what is needed to run the application.
- Smaller images are faster to push, pull, scan, and deploy.
- Docker Hub is used to publish and distribute container images.
- Specific image tags like `v1` are safer than relying only on `latest`.
- Running containers as a non-root user improves security.
- Minimal base images reduce the attack surface.

---

## Result

The Docker image size was reduced from `1.25GB` to around `15MB`.

This shows why multi-stage Docker builds are widely used in real DevOps and production environments.
