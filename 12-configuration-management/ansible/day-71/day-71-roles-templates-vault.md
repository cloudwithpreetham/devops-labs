# Day 71 — Ansible Roles, Templates, Galaxy & Vault

## Overview

Today I built production-style Ansible automation using:

- Jinja2 Templates for dynamic configuration
- Custom Ansible Roles for reusable automation
- Ansible Galaxy for community roles
- Ansible Vault for secure secret management

This day focused on moving from simple playbooks to scalable, production-ready infrastructure automation.

---

# 1. Project Structure

```

ansible-practice/
├── inventory.ini
├── site.yml
├── template-demo.yml
├── docker-setup.yml
├── db-setup.yml
├── group_vars/
│   └── db/
│       └── vault.yml (encrypted)
├── roles/
│   └── webserver/
│       ├── tasks/
│       ├── handlers/
│       ├── templates/
│       ├── defaults/
│       ├── vars/
│       └── meta/
└── templates/

```

---

# 2. Jinja2 Templates

## Nginx VHost Template

File:
`templates/nginx-vhost.conf.j2`

```jinja2
server {
    listen {{ http_port | default(80) }};
    server_name {{ ansible_hostname }};

    root /var/www/{{ app_name }};
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    access_log /var/log/nginx/{{ app_name }}_access.log;
    error_log /var/log/nginx/{{ app_name }}_error.log;
}
```

## Rendered Output Example

```
server_name ip-10-0-1-26;
root /var/www/terraweek-role;
```

---

# 3. Custom Ansible Role (webserver)

## Role Structure

```
roles/webserver/
```

Includes:

- tasks
- handlers
- templates
- defaults
- vars
- meta

## Key Features

- Installs Nginx
- Configures virtual hosts
- Deploys index page
- Uses handlers for service restart
- Fully reusable across environments

---

# 4. Ansible Galaxy Role

Installed:

```
geerlingguy.docker
```

### Purpose:

Automates Docker installation using community-maintained best practices.

### Issue Faced:

- Docker CE repo mismatch on Amazon Linux 2023

### Resolution:

- Switched to OS-native `dnf install docker`

---

# 5. Docker Setup (Amazon Linux 2023)

## Installed components:

- Docker Engine
- systemd service enabled
- ec2-user added to docker group

## Verification:

```
docker --version
systemctl status docker
```

---

# 6. Ansible Vault (Secrets Management)

## Encrypted file:

```
group_vars/db/vault.yml
```

## Stored secrets:

- DB password
- Root password
- API key

## Example:

```yaml
vault_db_password: SuperSecretP@ssw0rd
vault_api_key: sk-abc123xyz789
```

---

## Execution:

```
ansible-playbook db-setup.yml --ask-vault-pass
```

## Output:

```
Password length is 19
```

---

# 7. Key Learnings

## Roles vs Playbooks

- Playbooks = execution flow
- Roles = reusable architecture

## Templates

- Enable dynamic config generation
- Use Jinja2 variables and filters

## Galaxy

- Reusable community automation
- Speeds up infrastructure setup

## Vault

- Encrypts sensitive data
- Essential for CI/CD security
- Prevents secret leakage in Git

---

# 8. DevOps Principles Applied

- Infrastructure as Code (IaC)
- Configuration as Code
- Reusability and modularity
- Secrets management
- Idempotent automation

---

# 9. Real-World Use Case

This setup mimics production environments where:

- Web servers use reusable roles
- Docker is installed via automation
- Databases are secured with Vault
- Configurations are dynamically generated
- Community roles reduce boilerplate work

---

# 10. Conclusion

Day 71 helped me transition from basic Ansible playbooks to:

- scalable automation design
- secure secret handling
- reusable role-based architecture
- real-world DevOps workflows

This is a strong foundation for CI/CD and cloud automation pipelines.
