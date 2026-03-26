terraform {
  backend "s3" {
    bucket         = "preetham-terraform-state-2026"
    key            = "day64/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
