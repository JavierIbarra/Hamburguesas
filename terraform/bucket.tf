provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

resource "aws_ami" "ubuntu"{
  most_recent = true

  filter{
    name = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }

  owners = []
}

/* VPC ----------------------------------------------------------------- */

resource "aws_vpc" "prod-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "production"
  }
}

/* Subnet ----------------------------------------------------------------- */

resource "aws_subnet" "subnet-1" {
  vpc_id            = aws_vpc.prod-vpc.id
  cidr_block        = var.subnet_prefix[0].cidr_block
  availability_zone = "us-west-2"

  tags = {
    Name = var.subnet_prefix[0].name
  }
}

/* Instance ----------------------------------------------------------------- */

resource "aws_instance" "ec2" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.micro"
    subnet_id = "subnet-025e03e4152467c2d"
    security_groups = [aws_security_group.app.name]

    tags = {
      Name = "app"
    }
}

/* DNS ---------------------------------------------------------------------- */

resource "aws_route53_record" "app" {
  zone_id = var.zone_id
  name    = "app.${var.domain}"
  type    = "A"
  records = [aws_instance.app.public_ip]
  ttl     = "180"
}

/* Firewall ----------------------------------------------------------------- */

resource "aws_security_group" "app" {
  name = "allow_app"

  ingress {
    description = "https"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "http"
    from_port   = 80
    to_port     = 80
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
