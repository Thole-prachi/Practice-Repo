provider "aws" {
    profile = "default"
    region = "us-east-2"
  
}
resource "aws_instance" "terraform-example" {
    ami = "ami-0652d397074720eb1"
    instance_type = "t2.micro"
  
}