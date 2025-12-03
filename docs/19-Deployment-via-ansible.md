# 15. Deployment via Ansible

## 📅 Date: 2025-12-03

## 📝 Summary
We automated the deployment of the Inventory System to the Server Node using Ansible. This transitioned the project from a local development artifact to a production workload running on the ThinkPad.

## ⚙️ Deployment Details

### 1. The Playbook (`05-deploy-inventory.yml`)
We created a specialized playbook that performs the following GitOps-style actions:
- **Directory Management:** Ensures `/mnt/data/docker/inventory-system` exists with correct permissions (`admin-lab:docker`).
- **Artifact Transfer:** Copies the source code from the Control Node (VS Code) to the Server Node.
- **Orchestration:** Uses the `community.docker.docker_compose_v2` module to build the image and start the services.
    - `build: always`: Ensures any change in Python code triggers a rebuild of the container image.
    - `pull: always`: Ensures the database base image is up to date.

### 2. Execution State
- **Container Strategy:** The application container runs with `CMD ["sleep", "infinity"]`.
- **Reasoning:** currently, the application is a "Setup Script" that terminates after execution. If placed directly in the CMD, the container would exit immediately after running, causing Docker restart loops.
- **Operation:** We execute the logic manually via `docker exec` to initialize the database schema and verify connectivity.

### 3. Validation
Verified that:
1.  Containers `inventory-system-app-1` and `inventory-system-db-1` are running.
2.  Internal DNS resolution works (Python connects to `db`).
3.  Data persistence works (Data remains on `/mnt/data` volume after restart).