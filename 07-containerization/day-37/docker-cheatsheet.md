# Docker Cheat Sheet

## Container Commands

| Command                            | Description                            |
| ---------------------------------- | -------------------------------------- |
| `docker run nginx`                 | Run a container from the `nginx` image |
| `docker run -it ubuntu bash`       | Run Ubuntu interactively with Bash     |
| `docker run -d nginx`              | Run a container in detached mode       |
| `docker run --name web nginx`      | Run a container with a custom name     |
| `docker ps`                        | List running containers                |
| `docker ps -a`                     | List all containers                    |
| `docker stop <container>`          | Stop a running container               |
| `docker start <container>`         | Start a stopped container              |
| `docker restart <container>`       | Restart a container                    |
| `docker rm <container>`            | Remove a stopped container             |
| `docker rm -f <container>`         | Force remove a running container       |
| `docker exec -it <container> bash` | Open Bash inside a running container   |
| `docker logs <container>`          | View container logs                    |
| `docker logs -f <container>`       | Follow live container logs             |
| `docker inspect <container>`       | View detailed container information    |

---

## Image Commands

| Command                                 | Description                      |
| --------------------------------------- | -------------------------------- |
| `docker images`                         | List local Docker images         |
| `docker pull nginx`                     | Pull an image from Docker Hub    |
| `docker build -t myapp:v1 .`            | Build an image from a Dockerfile |
| `docker tag myapp:v1 username/myapp:v1` | Tag an image for Docker Hub      |
| `docker push username/myapp:v1`         | Push an image to Docker Hub      |
| `docker rmi <image>`                    | Remove a local image             |
| `docker history <image>`                | View image layers                |
| `docker image inspect <image>`          | Inspect image details            |

---

## Volume Commands

| Command                              | Description                             |
| ------------------------------------ | --------------------------------------- |
| `docker volume create app_data`      | Create a named volume                   |
| `docker volume ls`                   | List Docker volumes                     |
| `docker volume inspect app_data`     | Inspect a volume                        |
| `docker volume rm app_data`          | Remove a volume                         |
| `docker run -v app_data:/data nginx` | Mount a named volume into a container   |
| `docker run -v $(pwd):/app nginx`    | Use a bind mount from host to container |

---

## Network Commands

| Command                                             | Description                           |
| --------------------------------------------------- | ------------------------------------- |
| `docker network ls`                                 | List Docker networks                  |
| `docker network create app_network`                 | Create a custom bridge network        |
| `docker network inspect app_network`                | Inspect a network                     |
| `docker network connect app_network <container>`    | Connect a container to a network      |
| `docker network disconnect app_network <container>` | Disconnect a container from a network |
| `docker run --network app_network nginx`            | Run a container on a custom network   |

---

## Docker Compose Commands

| Command                              | Description                                     |
| ------------------------------------ | ----------------------------------------------- |
| `docker compose up`                  | Start services from `docker-compose.yml`        |
| `docker compose up -d`               | Start services in detached mode                 |
| `docker compose down`                | Stop and remove Compose containers and networks |
| `docker compose down -v`             | Stop containers and remove volumes too          |
| `docker compose ps`                  | List Compose services                           |
| `docker compose logs`                | View logs from Compose services                 |
| `docker compose logs -f`             | Follow Compose logs live                        |
| `docker compose build`               | Build Compose service images                    |
| `docker compose up --build`          | Rebuild and start services                      |
| `docker compose exec <service> bash` | Open shell inside a Compose service             |
| `docker compose restart`             | Restart Compose services                        |

---

## Cleanup Commands

| Command                            | Description                                             |
| ---------------------------------- | ------------------------------------------------------- |
| `docker system df`                 | Check Docker disk usage                                 |
| `docker container prune`           | Remove stopped containers                               |
| `docker image prune`               | Remove unused images                                    |
| `docker volume prune`              | Remove unused volumes                                   |
| `docker network prune`             | Remove unused networks                                  |
| `docker system prune`              | Remove unused containers, networks, and images          |
| `docker system prune -a`           | Remove all unused images, not just dangling ones        |
| `docker system prune -a --volumes` | Remove unused images, containers, networks, and volumes |

---

## Dockerfile Instructions

| Instruction   | Description                                              |
| ------------- | -------------------------------------------------------- |
| `FROM`        | Defines the base image                                   |
| `RUN`         | Executes commands while building the image               |
| `COPY`        | Copies files from host into the image                    |
| `ADD`         | Copies files and can also extract archives or fetch URLs |
| `WORKDIR`     | Sets the working directory inside the image              |
| `EXPOSE`      | Documents the port the container uses                    |
| `ENV`         | Sets environment variables                               |
| `ARG`         | Defines build-time variables                             |
| `CMD`         | Sets the default command for the container               |
| `ENTRYPOINT`  | Defines the main executable for the container            |
| `HEALTHCHECK` | Defines how Docker checks container health               |

---

## Common Docker Run Examples

```bash
docker run -d --name web -p 8080:80 nginx
```

Runs Nginx in detached mode and maps host port `8080` to container port `80`.

```bash
docker run -it --name ubuntu-test ubuntu bash
```

Starts an interactive Ubuntu container.

```bash
docker run -d --name db -v postgres_data:/var/lib/postgresql/data postgres
```

Runs a PostgreSQL container with persistent storage.

```bash
docker run -d --name app --network app_network myapp:v1
```

Runs a container inside a custom Docker network.

---

## Useful Debugging Commands

```bash
docker logs <container>
docker exec -it <container> sh
docker inspect <container>
docker compose logs -f
docker compose ps
docker system df
```

---

## Docker Best Practices

- Use small base images like `alpine` when possible.
- Keep Dockerfiles clean and minimal.
- Use `.dockerignore` to reduce build context size.
- Use multi-stage builds for compiled applications.
- Do not store secrets directly in Dockerfiles.
- Use environment variables for configuration.
- Use named volumes for persistent data.
- Use custom networks for multi-container communication.
- Tag images properly before pushing to Docker Hub.
- Clean unused containers, images, and volumes regularly.
