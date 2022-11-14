#VPC
resource "aws_vpc" "vpc-1" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = {
    "Name" = "prod_vpc"
  }
}


#Gateway
resource "aws_internet_gateway" "production-igw" {
  vpc_id = aws_vpc.vpc-1.id
}

#Route Table
resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.vpc-1.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.production-igw.id
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = aws_internet_gateway.production-igw.id
  }

  tags = {
    Name = "prod_route_table"
  }
}

#Subnet
resource "aws_subnet" "public-subnet-1" {
  vpc_id            = aws_vpc.vpc-1.id
  cidr_block        = var.public_subnet_1_cidr
  availability_zone = var.aws_availability_zone[0]
  tags = {
    "Name" = "prod_subnet"
  }
}

resource "aws_subnet" "public-subnet-2" {
  vpc_id            = aws_vpc.vpc-1.id
  cidr_block        = var.public_subnet_2_cidr
  availability_zone = var.aws_availability_zone[1]
  tags = {
    "Name" = "prod_subnet"
  }
}

#Route Table Association
resource "aws_route_table_association" "RTA" {
  subnet_id      = aws_subnet.public-subnet-1.id
  route_table_id = aws_route_table.prod-route-table.id
}

#Network Interface

resource "aws_network_interface" "web-server-int" {
  subnet_id       = aws_subnet.public-subnet-1.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow-web.id]
}

#Elastic IP
resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.web-server-int.id
  associate_with_private_ip = "10.0.1.50"

  #EIP Depends on Internet Gateway to be created
  depends_on = [
    aws_internet_gateway.production-igw
  ]
}

