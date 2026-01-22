# Day 09 - DevOps Automation Tools with FastAPI

## Aim

Build a FastAPI-based REST API for DevOps automation tasks including log analysis and AWS EC2 monitoring.

## Features

- **Health Check Endpoint** - Monitor API service status
- **Log Analyzer** - Parse and analyze application logs (INFO, WARN counts)
- **AWS EC2 Summary** - Fetch EC2 instance details using Boto3

## Usage

### Open the project folder

```bash
cd extras/python-for-devops/day-09
```

### Set up a Python environmentz

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Run application

```bash
uvicorn main:app --reload
```

Access the API at `http://127.0.0.1:8000`

## API Endpoints

| Endpoint  | Method | Description                   |
| --------- | ------ | ----------------------------- |
| `/health` | GET    | Health check status           |
| `/logs`   | GET    | Analyze Zookeeper logs        |
| `/aws`    | GET    | Get EC2 instances summary     |
| `/docs`   | GET    | Interactive API documentation |

## Tech Stack

- Python 3.13+
- FastAPI
- Uvicorn
- Boto3
