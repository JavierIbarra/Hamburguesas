variable "aws_access_key" {
  type = string
}

variable "aws_secret_key" {
  type = string
}

variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "aws_availability_zone" {
    description = "Availability zones"
  type = list(string)
  default = ["us-east-1a","us-east-1b"]
}

variable "public_subnet_1_cidr" {
  description = "CIDR Block for Public Subnet 1"
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr" {
  description = "CIDR Block for Public Subnet 1"
  default     = "10.0.2.0/24"
}

variable "docker_image_url_django" {
  description = "Docker image to run in the ECS cluster"
  default     = "264184798987.dkr.ecr.us-east-1.amazonaws.com/burger-api-ecs:2"
}

variable "ecs_cluster_name" {
  type = string
  default = "burger-production"
}

variable "ami" {
  type = string
  default = "ami-08c40ec9ead489470"
}

variable "instance_type" {
    type = string
    default = "t2.micro"
}

variable "container_name" {
  type = string
  default = "api"
}