terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  required_version = ">= 1.5.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "terraweek_bucket" {
  bucket = "terraweek-preetham-2026"
}

resource "aws_instance" "terraform_ec2" {
  ami           = "ami-02167eae61967e403"
  instance_type = "t3.micro"

  tags = {
    Name = "TerraWeek-Day1"
  }
}
