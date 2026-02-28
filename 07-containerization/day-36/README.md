# Dockerized Flask Notes App

A simple Flask Notes application containerized with Docker and Docker Compose.
The app uses PostgreSQL as the database and allows users to add and view notes from a browser.

This project was built as part of **Day 36 of 90DaysOfDevOps**.

---

## Project Overview

This project demonstrates how to Dockerize a real application end-to-end using:

- Python Flask application
- PostgreSQL database
- Dockerfile
- Docker Compose
- Docker Hub image registry
- Environment variables
- Docker volumes
- Custom Docker network
- Database healthcheck

---

## Application Features

- Add notes from a browser
- Store notes in PostgreSQL
- Automatically create the database table on startup
- Run the complete app stack with one Docker Compose command
- Use a persistent Docker volume for database data
- Run the Flask container as a non-root user

---

## Docker Hub Image

Docker Hub Repository:

```text
https://hub.docker.com/r/h4kops/flask-notes-app
```

Pull command:

```bash
docker pull h4kops/flask-notes-app:v1
```

---

## Project Structure

```bash
day-36/
├── .dockerignore
├── .env.example
├── Dockerfile
├── README.md
├── app
│   ├── app.py
│   ├── requirements.txt
│   └── templates
│       └── index.html
├── day-36-docker-project.md
├── docker-compose.prod.yml
└── docker-compose.yml
```

---

## Environment Variables

Create a `.env` file from the example file:

```bash
cp .env.example .env
```

Example environment variables:

```env
DB_HOST=db
DB_NAME=notesdb
DB_USER=notesuser
DB_PASSWORD=notespass

POSTGRES_DB=notesdb
POSTGRES_USER=notesuser
POSTGRES_PASSWORD=notespass
```

---

## Run Locally with Docker Compose

Build and start the application:

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker compose ps
```

Open the application:

```text
http://localhost:5000
```

For an AWS EC2 instance, open:

```text
http://<EC2_PUBLIC_IP>:5000
```

Make sure port `5000` is allowed in the EC2 security group.

---

## Run Using Docker Hub Image

Use the production compose file:

```bash
docker compose -f docker-compose.prod.yml up -d
```

This pulls the image from Docker Hub:

```text
h4kops/flask-notes-app:v1
```

Check containers:

```bash
docker compose -f docker-compose.prod.yml ps
```

Stop the stack:

```bash
docker compose -f docker-compose.prod.yml down
```

---

## Useful Docker Commands

Build and run:

```bash
docker compose up --build -d
```

View containers:

```bash
docker ps
```

View Compose services:

```bash
docker compose ps
```

Check database health:

```bash
docker inspect notes-postgres-db
```

View images:

```bash
docker images
```

Tag image:

```bash
docker tag day-36-app:latest h4kops/flask-notes-app:v1
```

Push image:

```bash
docker push h4kops/flask-notes-app:v1
```

---

## Final Result

The application was successfully Dockerized, pushed to Docker Hub, and tested using a fresh pull from Docker Hub.

Final image:

```text
h4kops/flask-notes-app:v1
```
