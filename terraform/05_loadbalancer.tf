# Production Load Balancer
resource "aws_lb" "production" {
  name               = "${var.ecs_cluster_name}-lb"
  load_balancer_type = "application"
  internal           = false
  security_groups    = [aws_security_group.allow-web.id]
  subnets            = [aws_subnet.public-subnet-1.id, aws_subnet.public-subnet-2.id]
}

# Target group
resource "aws_lb_target_group" "default-target-group" {
  name     = "${var.ecs_cluster_name}-tg"
  port     = 5000
  protocol = "HTTP"
  vpc_id   = aws_vpc.vpc-1.id

}

# Listener (redirects traffic from the load balancer to the target group)
resource "aws_lb_listener" "ecs-alb-http-listener" {
  load_balancer_arn = aws_lb.production.id
  port              = "80"
  protocol          = "HTTP"
  depends_on        = [aws_lb_target_group.default-target-group]

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.default-target-group.arn
  }
}