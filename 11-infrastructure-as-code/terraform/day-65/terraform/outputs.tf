output "web_server_ip" {
  value = module.web_server.public_ip
}

output "api_server_ip" {
  value = module.api_server.public_ip
}

output "security_group_id" {
  value = module.web_sg.sg_id
}
