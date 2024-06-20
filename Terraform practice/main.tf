#define the provider
provider "aws" {
    region = "us-west-1"
}

#create ec2 instance

resource "aws_instance" "example" {
    ami = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro" 
}

# Create s3 bucket with life cycle policy on  folder

resource "aws_s3_bucket_lifecycle_configuration" "example" {
    bucket = aws_s3_bucket.example_bucket.id
    rule{
        id = "example-rule"
        status = "Enabled"
        filter {
          prefix = "etc/"
        }
        expiration {
          days = 30
        }
    }
  
}

# VPC creation

resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"
}