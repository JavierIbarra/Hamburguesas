




//#EC2 Instance
//resource "aws_instance" "ec2-1" {
//  ami               = var.ami
//  instance_type     = var.instance_type
//  availability_zone = var.aws_availability_zone[0]
//  key_name          = "Hamburguesa-Key"
//
//  network_interface {
//    device_index         = 0
//    network_interface_id = aws_network_interface.web-server-int.id
//  }
//
//  tags = {
//    "Name" = "prod_ec2"
//  }
//
//  user_data = <<-EOF
//              #!/bin/bash
//              sudo apt update -y
//              sudo apt install apache2 -y
//              sudo systemctl start apache2
//              sudo bash -c 'echo your very first web server > /var/www/html/index.html'
//              EOF
//}
