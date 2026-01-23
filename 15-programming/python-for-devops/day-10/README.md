# Day 10 - DevOps Automation API Capstone Project

## Project Overview

This project is a capstone review of the FastAPI-based DevOps automation API built during **Day 09**.

The actual implementation is available here:

```bash
python-for-devops/day-09/
```

This capstone focuses on explaining the project using the **S.T.A.R method** and reviewing the DevOps concepts applied.

---

## S.T.A.R Project Explanation

### S - Situation

Manual DevOps tasks often take time and can lead to mistakes.

Common challenges included:

- Manually checking application logs
- Repeatedly opening the AWS Console to view EC2 instances
- No centralized API to access operational data
- Difficulty integrating manual checks into automation workflows

---

### T - Task

The goal was to build a simple DevOps automation API that could:

- Analyze application logs automatically
- Count important log levels such as `INFO` and `WARN`
- Fetch AWS EC2 instance details using Python
- Provide a health check endpoint for service monitoring
- Expose everything through REST API endpoints

---

### A - Action

To solve this, I built a FastAPI application with multiple DevOps-focused endpoints.

The project included:

- Creating a FastAPI application
- Building a health check endpoint
- Writing a log analyzer using Python file handling
- Using `Counter` to count log levels
- Integrating AWS Boto3 to fetch EC2 instance details
- Running the API using Uvicorn
- Testing endpoints through FastAPI Swagger UI

---

### R - Result

The final result was a working DevOps automation API.

It helped to:

- Reduce manual log analysis effort
- Access AWS EC2 instance information programmatically
- Provide structured API responses
- Create a reusable base for future automation tasks
- Build a foundation for real-world DevOps API services

---

## API Endpoints

| Endpoint  | Method | Purpose                                                |
| --------- | ------ | ------------------------------------------------------ |
| `/health` | GET    | Checks whether the API service is running              |
| `/logs`   | GET    | Analyzes application logs and returns log level counts |
| `/aws`    | GET    | Fetches AWS EC2 instance summary                       |
| `/docs`   | GET    | Opens FastAPI Swagger UI documentation                 |

---

## Tech Stack

| Tool    | Purpose                                     |
| ------- | ------------------------------------------- |
| Python  | Core programming language                   |
| FastAPI | REST API framework                          |
| Uvicorn | ASGI server to run the API                  |
| Boto3   | AWS SDK for Python                          |
| AWS EC2 | Cloud resource used for automation practice |

---

## Key DevOps Concepts Practiced

### Automation

Replaced repetitive manual tasks with API-based automation.

### Observability

Used log analysis and health checks to understand system behavior.

### Cloud Integration

Connected Python automation with AWS using Boto3.

### API-Driven Operations

Created REST endpoints that can be integrated with other tools.

### Reusability

Built a structure where more DevOps automation endpoints can be added later.

---

## What I Learned

Through this project, I learned:

- How to create REST APIs using FastAPI
- How to automate log analysis using Python
- How to use Boto3 for AWS automation
- How health check endpoints are used in real systems
- How DevOps engineers expose automation through APIs
- How to document a project using the S.T.A.R method

---

## Future Improvements

Possible improvements for this project:

- Add authentication for secure API access
- Improve exception handling
- Add structured application logging
- Add unit tests
- Add Docker support
- Add CI/CD using GitHub Actions
- Add more AWS services such as S3, Lambda, and CloudWatch
- Create a CLI tool to call the API from terminal

---

## Project Structure Reference

```bash
python-for-devops/
└── day-09/
    ├── main.py
    ├── app.log
    ├── requirements.txt
    └── README.md
```

---

## How This Helps in DevOps

This project represents a real DevOps use case where manual checks are converted into automation.

In real teams, similar APIs can be used for:

- Log monitoring
- Cloud resource checks
- Infrastructure status reports
- Internal DevOps dashboards
- CI/CD validation steps

---

## Project Location

```bash
python-for-devops/day-09/
```

---

## Conclusion

Day 10 helped me review and explain the DevOps automation API built in Day 09.

This project improved my understanding of Python automation, FastAPI, AWS integration, and real-world DevOps thinking.

---

**Built as part of Python for DevOps - Day 10**

#PythonForDevOps #TrainWithShubham #DevOpsKaJosh
