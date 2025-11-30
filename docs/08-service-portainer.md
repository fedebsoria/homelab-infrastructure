# 08. First Service Deployment: Portainer

## 📅 Date: 2025-11-30

## 📝 Summary
We successfully deployed our first containerized application using the "Infrastructure as Code" pipeline. We chose **Portainer** as the initial service to provide a graphical user interface (GUI) for managing the Docker runtime.

## ⚙️ Technical Strategy

### 1. Project Structure for Services
We established a standard directory pattern for future services:
- **Source (Repo):** `templates/<service_name>/docker-compose.yml`
- **Destination (Server):** `~/docker/<service_name>/docker-compose.yml`

This separation keeps the repository organized while allowing the server to have isolated directories for each stack's persistent data and configuration.

### 2. Ansible `docker_compose_v2` Module
Instead of running shell commands like `command: docker compose up`, we utilized the robust `community.docker.docker_compose_v2` Ansible module.
- **Benefits:**
    - **Idempotency:** It only restarts containers if the configuration has changed.
    - **State Management:** Explicitly defines `state: present` (running) or `absent` (stopped/removed).
    - **Pull Policy:** `pull: always` ensures we are running the latest version of the image defined in the compose file.

### 3. Service Details
- **Service:** Portainer CE (Community Edition)
- **Port:** 9000 (HTTP)
- **Volumes:** Mapped `/var/run/docker.sock` to allow Portainer to control the host Docker daemon.