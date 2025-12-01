# 12. Directory Structure & Dashy Deployment

## 📅 Date: 2025-12-01

## 📝 Summary
We established a standardized directory structure on the persistent storage drive (`/mnt/data`) and deployed our first user-facing application: **Dashy**, a personal dashboard.

## ⚙️ Technical Details

### 1. Storage Standards
To keep the server organized, we defined the following structure on the 500GB HDD:
- `/mnt/data/docker/`: Root for all container configurations and persistent volumes.
- `/mnt/data/media/`: Reserved for future media files (Movies, TV, etc.).
- `/mnt/data/downloads/`: Reserved for download clients.

### 2. Dashy Deployment
We deployed Dashy using the `docker_compose_v2` Ansible module.
- **Port:** 8080 (Mapped to container port 80).
- **Config:** A `conf.yml` file is injected from the host (`/mnt/data/docker/dashy/conf.yml`) into the container. This allows us to back up the config easily.
- **Resources:** We applied a memory limit of 1GB to prevent the Node.js process from consuming too much RAM on the laptop.

### 3. Workflow Validation
This deployment confirmed that our Ansible playbook can successfully:
1.  Create directories on the secondary drive.
2.  Copy templates from the git repository to the server.
3.  Spin up a container using those files.