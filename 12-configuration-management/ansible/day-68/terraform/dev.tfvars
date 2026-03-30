vpc_cidr      = "10.0.0.0/16"
subnet_cidr   = "10.0.1.0/24"
instance_type = "t3.micro"

key_name = "ansible-server-key"

ingress_ports = [
  22,
  80
]
