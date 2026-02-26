# Day 34 – Docker Compose: Real-World Multi-Container Apps

## Objective

The goal of Day 34 was to build a more production-like Docker Compose setup using multiple services.

For this task, I created a 3-service application stack using Docker Compose:

- Python Flask web application
- PostgreSQL database
- Redis cache

This setup also includes:

- Custom Dockerfile for the web application
- `depends_on` with healthcheck condition
- PostgreSQL healthcheck
- Restart policy testing
- Named network
- Named volume
- Service labels
- Rebuild workflow
- Scaling experiment

---

## Project Structure

```bash
.
├── app
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── docker-compose.yml

2 directories, 4 files
```

---

## Task 1: Build Your Own App Stack

I created a Docker Compose stack with three services:

| Service | Image / Build      | Purpose                  |
| ------- | ------------------ | ------------------------ |
| `web`   | Custom Flask image | Runs the web application |
| `db`    | `postgres:16`      | Provides the database    |
| `cache` | `redis:7`          | Provides the cache layer |

The web application connects to both PostgreSQL and Redis.

The browser output confirmed:

```text
Day 34 Docker Compose Advanced
Database connected successfully
Redis cache connected successfully
```

This confirms that the Flask app was able to communicate with both backend services through Docker Compose networking.

---

## Application Files

### `app/app.py`

The Flask app connects to:

- PostgreSQL using the service name `db`
- Redis using the service name `cache`

The application displays connection status for both services in the browser.

### `app/requirements.txt`

The Python dependencies used were:

```txt
flask
psycopg2-binary
redis
```

### `app/Dockerfile`

The custom Dockerfile builds the Flask application image.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

This Dockerfile performs the following steps:

1. Uses Python 3.11 slim as the base image
2. Sets `/app` as the working directory
3. Copies dependency file into the image
4. Installs Python packages
5. Copies the Flask application code
6. Exposes port `5000`
7. Starts the app using `python app.py`

---

## Task 2: `depends_on` and Healthchecks

The database service was configured with a healthcheck.

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U devops -d devopsdb"]
  interval: 10s
  timeout: 5s
  retries: 5
```

The web service waits for the database to become healthy before starting.

```yaml
depends_on:
  db:
    condition: service_healthy
  cache:
    condition: service_started
```

This is important because a container can be running before the actual database process is ready to accept connections.

### Verification

I started the stack using:

```bash
docker compose up --build
```

The output showed that the database became healthy before the web service started:

```text
Container day34-db    Healthy
Container day34-web   Started
```

This confirmed that `depends_on` with `condition: service_healthy` worked correctly.

---

## Task 3: Restart Policies

The database service was configured with:

```yaml
restart: always
```

This restart policy tells Docker to restart the database container if it stops.

### Test Attempt

I first brought the stack down using:

```bash
docker compose down
```

Then I tried to kill the database container:

```bash
docker kill day34-db
```

Since the containers were already removed, Docker returned:

```text
Error response from daemon: cannot kill container: day34-db: No such container: day34-db
```

After that, I recreated the stack using:

```bash
docker compose up -d --force-recreate
```

The output showed:

```text
Network day-34_app-network     Created
Volume day-34_postgres-data    Created
Container day34-db             Healthy
Container day34-cache          Started
Container day34-web            Started
```

This confirmed that the stack could be recreated successfully.

---

## `restart: always` vs `restart: on-failure`

### `restart: always`

Use `restart: always` for long-running services that should keep running unless intentionally stopped.

Example services:

- Database containers
- Cache containers
- Web servers
- Monitoring agents

This is useful when the service is critical and should automatically recover after a crash or host restart.

### `restart: on-failure`

Use `restart: on-failure` when a container should restart only if it exits with an error code.

Example services:

- Batch jobs
- Worker scripts
- Backup jobs
- One-time automation scripts

This policy is useful when a successful exit should not trigger a restart.

---

## Task 4: Custom Dockerfiles in Compose

Instead of using a pre-built image for the web app, the Compose file used:

```yaml
build: ./app
```

This tells Docker Compose to build the web service from the Dockerfile inside the `app/` directory.

After changing the Flask app code, I rebuilt and restarted the service using:

```bash
docker compose up --build
```

The output showed that the web image was rebuilt and the web container was recreated:

```text
web                    Built
Container day34-web    Recreated
```

This is a useful development workflow because code changes can be rebuilt and restarted with one command.

---

## Task 5: Named Networks and Volumes

### Named Network

An explicit network was created for the stack:

```yaml
networks:
  app-network:
    driver: bridge
```

All services were attached to this network.

This allowed the web app to reach other services by their Compose service names:

```text
web -> db
web -> cache
```

### Named Volume

A named volume was created for PostgreSQL data:

```yaml
volumes:
  postgres-data:
```

The database service used this volume:

```yaml
volumes:
  - postgres-data:/var/lib/postgresql/data
```

This keeps database data persistent even if the database container is removed.

### Labels

Labels were added to services for better organization.

Example:

```yaml
labels:
  project: "90DaysOfDevOps"
  day: "34"
  service: "web-app"
```

Labels are useful in real environments because they help organize and identify containers, networks, and volumes.

---

## Task 6: Scaling Experiment

I tested scaling the web service using:

```bash
docker compose up --scale web=3
```

The output showed this warning:

```text
WARNING: The "web" service is using the custom container name "day34-web". Docker requires each container to have a unique name. Remove the custom name to scale the service
```

### What Happened?

The scaling test did not work because the `web` service used a fixed custom container name:

```yaml
container_name: day34-web
```

Docker Compose cannot create multiple replicas with the same container name because every container must have a unique name.

### Important Learning

To scale a service with Docker Compose, avoid using `container_name` for that service.

Another common scaling issue is fixed port mapping.

Example:

```yaml
ports:
  - "5000:5000"
```

If the web service is scaled to 3 replicas, all containers would try to bind to the same host port `5000`, which causes a port conflict.

### Real-World Solution

In production, multiple app replicas are usually placed behind a load balancer or reverse proxy.

Examples:

- Nginx
- Traefik
- HAProxy
- AWS Application Load Balancer
- Kubernetes Service

The load balancer receives traffic and distributes it across healthy application replicas.

---

## Commands Used

### Create Project Directory

```bash
mkdir day-34
cd day-34
mkdir app
```

### Create Application Files

```bash
cd app
touch app.py Dockerfile requirements.txt
cd ..
touch docker-compose.yml
```

### Build and Start Stack

```bash
docker compose up --build
```

### Start in Detached Mode

```bash
docker compose up --build -d
```

### Check Running Containers

```bash
docker compose ps
```

### View Logs

```bash
docker compose logs web
docker compose logs db
docker compose logs cache
```

### Stop Stack

```bash
docker compose down
```

### Stop Stack and Remove Volume

```bash
docker compose down -v
```

### Force Recreate Containers

```bash
docker compose up -d --force-recreate
```

### Rebuild After Code Change

```bash
docker compose up --build
```

### Test Scaling

```bash
docker compose up --scale web=3
```

---

## Verification Screenshots

Screenshots captured for this task:

| Screenshot                       | Description                                  |
| -------------------------------- | -------------------------------------------- |
| `01-project-structure.png`       | Project directory structure                  |
| `02-docker-compose-up-build.png` | Compose build and service startup            |
| `03-running-containers.png`      | Running containers with `docker compose ps`  |
| `04-web-app-browser-output.png`  | Flask app output in browser                  |
| `05-database-healthcheck.png`    | Database marked as healthy                   |
| `06-compose-logs-web.png`        | Docker Compose logs                          |
| `07-restart-policy-test.png`     | Stack recreated with network and volume      |
| `08-scaling-port-conflict.png`   | Scaling warning due to custom container name |

---

## Issues Faced and Fixes

### Issue 1: `tree` Command Not Found

When I first ran:

```bash
tree -L 1
```

The system showed that `tree` was not installed.

I installed it using:

```bash
sudo apt install tree
```

After installation, the project structure was displayed successfully.

### Issue 2: Database Kill Test Failed

I tried to kill the database container after running:

```bash
docker compose down
```

Because the container was already removed, Docker could not kill it.

Lesson learned:

The restart policy test should be performed while the container is running.

Correct flow:

```bash
docker compose up -d
 docker kill day34-db
 docker ps
```

### Issue 3: Scaling Failed

Scaling failed because the web service used a custom container name.

Docker Compose needs to create unique container names for multiple replicas.

Fix:

Remove this line from the `web` service before scaling:

```yaml
container_name: day34-web
```

Also avoid fixed host port mapping when scaling multiple replicas.

---

## Key Learnings

- Docker Compose can manage multi-service application stacks.
- A web app can communicate with database and cache containers using service names.
- `depends_on` controls startup order.
- `condition: service_healthy` makes startup safer than basic `depends_on`.
- Healthchecks confirm whether a service is actually ready.
- Restart policies improve container reliability.
- Named volumes are used for persistent data.
- Named networks make service communication clean and predictable.
- Custom Dockerfiles allow application images to be built directly from Compose.
- Scaling requires unique container names and proper port strategy.
- Real-world scaling usually needs a reverse proxy or load balancer.

---

## Final Outcome

I successfully created and tested a production-like Docker Compose application stack.

The final stack included:

- Python Flask web app
- PostgreSQL database
- Redis cache
- Custom Dockerfile
- Compose-based image build
- Healthcheck-based dependency
- Named network
- Named volume
- Service labels
- Restart policy testing
- Scaling experiment

This task helped me understand how Docker Compose is used in real DevOps workflows to run and manage multi-container applications.
