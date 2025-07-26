provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "input_bucket" {
  bucket = "asmaa-input-bucket-demo"
}

resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}
