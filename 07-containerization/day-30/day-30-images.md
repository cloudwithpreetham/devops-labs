# Day 30 – Docker Images & Container Lifecycle

## Goal

The goal of Day 30 was to understand how Docker images and containers work, including image layers, caching, and the complete container lifecycle.

---

## Task 1: Docker Images

### Commands Used

```bash
docker pull nginx
docker pull ubuntu
docker pull alpine

docker images

docker inspect nginx
```

### What I Did

I pulled three Docker images from Docker Hub:

- `nginx`
- `ubuntu`
- `alpine`

After pulling the images, I listed all available Docker images using:

```bash
docker images
```

### Images Pulled

| Image           | Image ID       | Disk Usage | Content Size | Status              |
| --------------- | -------------- | ---------: | -----------: | ------------------- |
| `alpine:latest` | `5b10f432ef3d` |   `13.1MB` |     `3.95MB` | Pulled successfully |
| `nginx:latest`  | `5aca99593157` |    `241MB` |       `66MB` | Already up to date  |
| `ubuntu:latest` | `f3d28607ddd7` |    `160MB` |     `45.3MB` | Already up to date  |

### Ubuntu vs Alpine Comparison

Ubuntu is larger because it includes a more complete Linux environment with package tools, libraries, and common utilities.

Alpine is much smaller because it is designed as a lightweight Linux distribution with a minimal base system. Alpine is commonly used in containers when smaller image size, faster downloads, and lower storage usage are important.

### Image Inspect Observations

Using the command below, I inspected the Nginx image:

```bash
docker inspect nginx
```

Important details observed:

- Image ID: `sha256:5aca99593157f4ae539a5dec1092a0ad8762f8e2eb1789085a13a0f5622369f6`
- Repo tag: `nginx:latest`
- Exposed port: `80/tcp`
- Nginx version: `1.31.1`
- NJS version: `0.9.1`
- Entrypoint: `/docker-entrypoint.sh`
- Default command: `nginx -g daemon off;`
- Environment variables were included in the image configuration

### Screenshot

```text
screenshots/day-30-task1-docker-images.png
screenshots/day-30-task1-nginx-inspect.png
```

---

## Task 2: Image Layers

### Command Used

```bash
docker image history nginx
```

### Observations

The `nginx` image is built using multiple layers.

Some important observations from the image history output:

- The top layer shows the default command: `CMD ["nginx" "-g" "daemon off;"]`
- Metadata instructions such as `STOPSIGNAL`, `EXPOSE`, `ENTRYPOINT`, `ENV`, and `LABEL` showed `0B` size
- Several `COPY` layers added small shell scripts such as `docker-entrypoint.sh` and Nginx entrypoint helper scripts
- One `RUN` layer added around `87.1MB`
- The base Debian layer added around `87.4MB`
- The `<missing>` values mean Docker does not show the full intermediate image IDs for those layers in the local history output

### What Are Image Layers?

Docker images are built from multiple layers. Each layer represents a filesystem change created during the image build process.

Docker uses layers because:

- Layers can be reused across images
- Builds are faster because unchanged layers are cached
- Downloads are more efficient because Docker only downloads missing layers
- Storage is optimized because shared layers are stored only once

### Why Some Layers Show `0B`

Some layers show `0B` because they only change metadata and do not add files to the filesystem.

Examples:

```text
ENV
LABEL
EXPOSE
CMD
ENTRYPOINT
STOPSIGNAL
```

These instructions configure how the image behaves, but they usually do not increase image size.

### Screenshot

```text
screenshots/day-30-task2-image-history.png
```

---

## Task 3: Container Lifecycle

### Commands Used

```bash
docker create --name lifecycle-nginx nginx
docker ps -a

docker start lifecycle-nginx
docker ps -a

docker pause lifecycle-nginx
docker ps -a

docker unpause lifecycle-nginx
docker ps -a

docker stop lifecycle-nginx
docker ps -a

docker restart lifecycle-nginx
docker ps -a

docker kill lifecycle-nginx
docker ps -a

docker rm lifecycle-nginx
docker ps -a
```

### Lifecycle Table

| Step    | Command                                      | Container State             |
| ------- | -------------------------------------------- | --------------------------- |
| Create  | `docker create --name lifecycle-nginx nginx` | `Created`                   |
| Start   | `docker start lifecycle-nginx`               | `Up`                        |
| Pause   | `docker pause lifecycle-nginx`               | `Up (Paused)`               |
| Unpause | `docker unpause lifecycle-nginx`             | `Up`                        |
| Stop    | `docker stop lifecycle-nginx`                | `Exited (0)`                |
| Restart | `docker restart lifecycle-nginx`             | `Up`                        |
| Kill    | `docker kill lifecycle-nginx`                | `Exited (137)`              |
| Remove  | `docker rm lifecycle-nginx`                  | Removed from container list |

### Observations

- `docker create --name lifecycle-nginx nginx` created a container named `lifecycle-nginx` without starting it
- After creation, `docker ps -a` showed the container state as `Created`
- After starting the container, the status changed to `Up` and port `80/tcp` was visible
- `docker pause lifecycle-nginx` changed the container status to `Up (Paused)`
- `docker unpause lifecycle-nginx` resumed the container and changed the status back to `Up`
- `docker stop lifecycle-nginx` gracefully stopped the container and changed the status to `Exited (0)`
- `docker restart lifecycle-nginx` started the stopped container again and changed the status back to `Up`
- `docker kill lifecycle-nginx` forcefully stopped the container and changed the status to `Exited (137)`
- `docker rm lifecycle-nginx` removed the container from the container list
- `docker ps -a` was used after each lifecycle operation to verify the state change

### Stop vs Kill

`docker stop` sends a graceful stop signal to the container process. This allows the application to shut down properly.

`docker kill` forcefully stops the container immediately. In the output, the container exited with status code `137`, which usually means it was forcefully terminated.

### Screenshot

```text
screenshots/day-30-task3-created.png
screenshots/day-30-task3-container-lifecycle.png
screenshots/day-30-task3-pause-unpause.png
```

---

## Task 4: Working with Running Containers

### Commands Used

```bash
docker run -d --name web-nginx -p 8080:80 nginx

docker ps

docker logs web-nginx

docker logs -f web-nginx

docker exec -it web-nginx bash

pwd
ls
cat /etc/os-release
exit

docker exec web-nginx nginx -v

docker inspect web-nginx

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web-nginx

docker port web-nginx
```

### What I Did

I started an Nginx container in detached mode using:

```bash
docker run -d --name web-nginx -p 8080:80 nginx
```

The container was started with:

- Container name: `web-nginx`
- Host port: `8080`
- Container port: `80`
- Image: `nginx`

### Logs

I checked the container logs using:

```bash
docker logs web-nginx
```

The logs showed that the Nginx configuration completed successfully and the server was ready to start.

I also used follow mode:

```bash
docker logs -f web-nginx
```

This is useful for watching logs in real time.

### Exec Into Container

I entered the running container using:

```bash
docker exec -it web-nginx bash
```

Inside the container, I checked:

```bash
pwd
ls
cat /etc/os-release
```

The base OS inside the container was:

```text
Debian GNU/Linux 13 (trixie)
```

### Run a Single Command Without Entering

I ran the following command from the host without entering the container:

```bash
docker exec web-nginx nginx -v
```

Output:

```text
nginx version: nginx/1.31.1
```

### Inspect Findings

Using `docker inspect web-nginx`, I found the following details:

| Item                 | Value                          |
| -------------------- | ------------------------------ |
| Container Name       | `web-nginx`                    |
| Container ID         | `79133d02377f`                 |
| Container State      | `running`                      |
| Container IP Address | `172.17.0.2`                   |
| Network Mode         | `bridge`                       |
| Gateway              | `172.17.0.1`                   |
| Port Mapping         | `80/tcp -> 0.0.0.0:8080`       |
| IPv6 Port Mapping    | `80/tcp -> [::]:8080`          |
| Mounts               | `[]`                           |
| Nginx Version        | `1.31.1`                       |
| Base OS              | `Debian GNU/Linux 13 (trixie)` |

### Screenshot

```text
screenshots/day-30-task4-running-container.png
screenshots/day-30-task4-inspect-container.png
```

---

## Task 5: Cleanup

### Commands Used

```bash
docker stop $(docker ps -q)

docker container prune

docker image prune

docker system df
```

### Cleanup Results

- `docker stop $(docker ps -q)` stopped the running `web-nginx` container
- `docker container prune` removed all stopped containers
- Removed containers included:
  - `web-nginx`
  - stopped Ubuntu container
  - old `hello-world` container

- Total reclaimed container space: `102.4kB`
- `docker image prune` removed dangling images, but there were no dangling images to remove
- Total reclaimed image space: `0B`
- `docker system df` showed Docker disk usage after cleanup

### Docker Disk Usage After Cleanup

| Type          | Total | Active |      Size |    Reclaimable |
| ------------- | ----: | -----: | --------: | -------------: |
| Images        |     4 |      0 | `414.1MB` | `38.35kB (0%)` |
| Containers    |     0 |      0 |      `0B` |           `0B` |
| Local Volumes |     0 |      0 |      `0B` |           `0B` |
| Build Cache   |     0 |      0 |      `0B` |           `0B` |

### Screenshot

```text
screenshots/day-30-task5-cleanup.png
```

---

## Key Learnings

- Docker images are read-only templates used to create containers
- Containers are running or stopped instances of images
- Docker images are made of multiple layers
- Layers improve build speed, download efficiency, and storage usage
- `docker image history` helps us understand how an image was built
- Metadata instructions such as `ENV`, `CMD`, and `EXPOSE` may show `0B` because they do not add files
- Containers move through states such as `Created`, `Up`, `Paused`, `Exited`, and `Removed`
- `docker logs` is useful for checking application output
- `docker exec` is useful for debugging inside a running container
- `docker inspect` gives detailed information about networking, ports, mounts, image ID, and runtime state
- Cleanup commands are important to keep Docker disk usage under control

---

## Learn in Public

Today I learned how Docker images and containers work internally.

The most interesting part was understanding image layers. Docker does not store every image as one big file. Instead, it uses reusable layers. This makes builds faster, saves disk space, and avoids downloading the same data again.

I also practiced the complete container lifecycle: create, start, pause, unpause, stop, restart, kill, and remove.

```text
#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham
```
