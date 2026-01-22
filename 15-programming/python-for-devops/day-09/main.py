from fastapi import FastAPI
import boto3
from botocore.exceptions import BotoCoreError, ClientError

app = FastAPI(
    title="DevOps Automation API",
    description="FastAPI tool for DevOps automation tasks like log analysis and AWS EC2 monitoring",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "DevOps Automation API is running"}


@app.get("/logs")
def analyze_logs():
    log_file_path = "logs/zookeeper.log"

    log_summary = {"INFO": 0, "WARN": 0, "ERROR": 0}

    try:
        with open(log_file_path, "r") as file:
            for line in file:
                if "INFO" in line:
                    log_summary["INFO"] += 1
                elif "WARN" in line or "WARNING" in line:
                    log_summary["WARN"] += 1
                elif "ERROR" in line:
                    log_summary["ERROR"] += 1

        return {"status": "success", "log_file": log_file_path, "summary": log_summary}

    except FileNotFoundError:
        return {"status": "error", "message": "Log file not found"}


@app.get("/aws")
def get_ec2_summary():
    try:
        ec2_client = boto3.client("ec2")
        response = ec2_client.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append(
                    {
                        "instance_id": instance.get("InstanceId"),
                        "state": instance.get("State", {}).get("Name"),
                        "instance_type": instance.get("InstanceType"),
                        "availability_zone": instance.get("Placement", {}).get(
                            "AvailabilityZone"
                        ),
                    }
                )

        return {
            "status": "success",
            "total_instances": len(instances),
            "instances": instances,
        }

    except (BotoCoreError, ClientError) as error:
        return {"status": "error", "message": str(error)}
