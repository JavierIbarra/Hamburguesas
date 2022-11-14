
#Security Group
resource "aws_security_group" "allow-web" {
  description = "Allow web inbound traffic"
  vpc_id      = aws_vpc.vpc-1.id

  //ingress {
  //  description      = "HTTPS"
  //  from_port        = 443
  //  to_port          = 443
  //  protocol         = "tcp"
  //  cidr_blocks      = ["0.0.0.0/0"]
  //  ipv6_cidr_blocks = ["::/0"]
  //}
  //ingress {
  //  description      = "HTTP"
  //  from_port        = 80
  //  to_port          = 80
  //  protocol         = "tcp"
  //  cidr_blocks      = ["0.0.0.0/0"]
  //  ipv6_cidr_blocks = ["::/0"]
  //}
  //ingress {
  //  description      = "SSH"
  //  from_port        = 22
  //  to_port          = 22
  //  protocol         = "tcp"
  //  cidr_blocks      = ["0.0.0.0/0"]
  //  ipv6_cidr_blocks = ["::/0"]
  //}
  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = -1
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}
