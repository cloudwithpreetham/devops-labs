import boto3
import json
from datetime import datetime
from botocore.exceptions import NoCredentialsError, ClientError


def get_ec2_instances():
    """
    Fetch EC2 instance ID and current state.
    This is a read-only operation.
    """
    ec2 = boto3.client("ec2")

    instances = []

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(
                {
                    "instance_id": instance["InstanceId"],
                    "state": instance["State"]["Name"],
                }
            )

    return instances


def get_s3_buckets():
    """
    Fetch all S3 bucket names.
    This is a read-only operation.
    """
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    buckets = []

    for bucket in response["Buckets"]:
        buckets.append({"bucket_name": bucket["Name"]})

    return buckets


def generate_aws_report():
    """
    Generate AWS resource report for EC2 and S3.
    """
    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ec2_instances": get_ec2_instances(),
        "s3_buckets": get_s3_buckets(),
    }

    return report


def save_report_to_json(report, file_name="aws_report.json"):
    """
    Save AWS report into a JSON file.
    """
    with open(file_name, "w") as file:
        json.dump(report, file, indent=4)


def print_report(report):
    """
    Print AWS report in terminal.
    """
    print("\nAWS Resource Report")
    print("-" * 40)

    print("\nEC2 Instances:")
    if report["ec2_instances"]:
        for instance in report["ec2_instances"]:
            print(
                f"Instance ID: {instance['instance_id']} | State: {instance['state']}"
            )
    else:
        print("No EC2 instances found.")

    print("\nS3 Buckets:")
    if report["s3_buckets"]:
        for bucket in report["s3_buckets"]:
            print(f"Bucket Name: {bucket['bucket_name']}")
    else:
        print("No S3 buckets found.")

    print("\nReport saved to aws_report.json")


def main():
    try:
        report = generate_aws_report()
        print_report(report)
        save_report_to_json(report)

    except NoCredentialsError:
        print("AWS credentials not found. Please configure AWS CLI first.")
        print("Run: aws configure")

    except ClientError as error:
        print("AWS client error occurred:")
        print(error)

    except Exception as error:
        print("Something went wrong:")
        print(error)


if __name__ == "__main__":
    main()
