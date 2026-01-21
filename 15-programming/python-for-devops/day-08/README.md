# Day 08 – AWS Automation with Python (Boto3 + CDK)

## Overview

Day 08 focuses on understanding how Python can interact with AWS services using **Boto3** and how infrastructure can be defined as code using **AWS CDK**.

The main objective of this task is to safely read AWS resource information, display it in the terminal, and save the result into a JSON report.

This project does not delete, create, or modify AWS resources using Boto3. It only performs read-only operations.

---

## Project Structure

```bash
day-08/
├── cdk-demo/
│   ├── app.py
│   ├── cdk_demo_stack.py
│   └── requirements.txt
├── node_modules/
├── screenshots/
├── aws_report.json
├── aws_resource_report.py
├── README.md
└── task.md
```

> Note: `node_modules/` should not be committed to Git. Add it to `.gitignore`.

---

## What I Worked On

### Part 1 – AWS Automation with Boto3

I created a Python script named `aws_resource_report.py` that connects to my AWS account using locally configured AWS credentials.

The script collects:

- EC2 instance ID
- EC2 instance state
- S3 bucket names

After collecting the information, the script:

- Prints the AWS resource report in the terminal
- Saves the report into `aws_report.json`

---

## Script Output

The script successfully detected one EC2 instance and confirmed that no S3 buckets were found.

```bash
AWS Resource Report
----------------------------------------

EC2 Instances:
Instance ID: i-0a9d2a462fd97ab4f | State: stopped

S3 Buckets:
No S3 buckets found.

Report saved to aws_report.json
```

---

## JSON Report

The output is also saved into `aws_report.json` in structured JSON format.

Example:

```json
{
  "generated_at": "2026-01-21 10:30:00",
  "ec2_instances": [
    {
      "instance_id": "i-0a9d2a462fd97ab4f",
      "state": "stopped"
    }
  ],
  "s3_buckets": []
}
```

---

## Files Created

### `aws_resource_report.py`

Main Python automation script.

Responsibilities:

- Connects to AWS using Boto3
- Reads EC2 information
- Reads S3 bucket information
- Prints the report in the terminal
- Saves the report as JSON

### `aws_report.json`

Generated output file containing AWS resource details in JSON format.

### `cdk-demo/`

Optional AWS CDK learning folder used to understand Infrastructure as Code with Python.

### `screenshots/`

Stores proof of execution and terminal output screenshots.

### `task.md`

Contains the original Day 08 task requirements.

---

## Tools and Technologies Used

- Python
- Boto3
- AWS CLI
- AWS CDK
- JSON
- Git
- VS Code

---

## Prerequisites

Before running the script, AWS CLI must be installed and configured.

Check AWS CLI configuration:

```bash
aws configure list
```

Verify AWS identity:

```bash
aws sts get-caller-identity
```

Install Boto3 if required:

```bash
pip install boto3
```

---

## How to Run

Move into the Day 08 folder:

```bash
cd day-08
```

Run the Python script:

```bash
python aws_resource_report.py
```

After running the script, verify that the JSON report was created:

```bash
cat aws_report.json
```

---

## AWS CDK Demo

The `cdk-demo` folder is used to understand how AWS CDK works with Python.

AWS CDK allows infrastructure to be written using a programming language. In this task, Python is used to define AWS infrastructure.

The CDK flow is:

```bash
Python CDK Code → CloudFormation Template → AWS Resources
```

### CDK Files

| File                | Purpose                              |
| ------------------- | ------------------------------------ |
| `app.py`            | Entry point of the CDK application   |
| `cdk_demo_stack.py` | Defines the AWS stack and resources  |
| `requirements.txt`  | Contains Python dependencies for CDK |

---

## CDK Commands Used for Learning

Move into the CDK folder:

```bash
cd cdk-demo
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate CloudFormation template:

```bash
cdk synth
```

Deployment is optional. I did not focus on deployment because the goal was to understand the CDK flow.

---

## Safety Notes

This project follows safe AWS learning practices.

The Boto3 script only performs read operations.

It does not:

- Create AWS resources
- Modify AWS resources
- Delete AWS resources
- Change AWS configurations

For creating or modifying infrastructure, Infrastructure as Code tools such as AWS CDK, CloudFormation, or Terraform should be used.

---

## Real-World DevOps Use Case

A similar automation script can be used by DevOps engineers to:

- Generate AWS inventory reports
- Track EC2 instance states
- List available S3 buckets
- Build audit reports
- Support monitoring and compliance workflows
- Reduce manual AWS console checks

---

## Key Learnings

- Boto3 is the AWS SDK for Python
- Python can interact with AWS services through APIs
- EC2 and S3 resource information can be collected automatically
- JSON is useful for storing structured report data
- AWS CDK helps define infrastructure using Python
- Infrastructure as Code improves repeatability and version control
- Read-only scripts are a safe way to begin AWS automation

---

## Conclusion

Day 08 helped me understand how Python and AWS work together in DevOps automation.

I learned how to use Boto3 for read-only AWS reporting and explored the basics of AWS CDK for Infrastructure as Code.

This task is an important step toward building real-world cloud automation skills.
