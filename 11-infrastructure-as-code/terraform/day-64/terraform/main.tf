resource "aws_vpc" "main" {
  cidr_block = "10.64.0.0/16"

  tags = {
    Name = "day64-vpc"
  }
}

resource "aws_security_group" "web_sg" {
  name   = "day64-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami           = "ami-02167eae61967e403"
  instance_type = "t3.micro"

  subnet_id = aws_subnet.public.id

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "Terraform-Web-Server-v2"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.64.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "day64-public-subnet"
  }
}

resource "aws_s3_bucket" "logs_bucket" {
  bucket = "terraweek-import-test-preetham-2026"
}
